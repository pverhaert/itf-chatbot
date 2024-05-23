import streamlit as st
from groq import Groq
from config import *

st.set_page_config(page_title="ITF Chatbot", page_icon="assets/logo-tm.svg", layout="wide")

with open('./assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def display_chat_history():
    for message in st.session_state.messages:
        if message["role"] == "system":
            continue
        with st.chat_message(message["assistant"]):
            st.markdown(message["content"])


def stream_response(completion):
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


def update_system_prompt():
    specialty = SPECIALTIES.get(st.session_state.specialty)
    # lang = st.session_state.language
    lang = LANGUAGES.get(st.session_state.language)
    prompt = SYSTEM_PROMPTS[
        specialty] if specialty in SYSTEM_PROMPTS else "I'm a general assistant. How can I help you?"
    prompt += f" I always try to answer in the {lang} language, even if the question is asked in another language."
    st.session_state.messages[0]["content"] = prompt


def main():
    set_session_states()

    # Sidebar
    with st.sidebar:
        col1, col2 = st.columns([9, 6])
        with col1:
            st.selectbox("Model:", list(MODELS.keys()), key='model')
        with col2:
            st.selectbox("Language:", list(LANGUAGES.keys()), key='language', on_change=update_system_prompt())
        st.selectbox("Specialty:", list(SPECIALTIES.keys()), key='specialty', on_change=update_system_prompt())
        with st.expander("Advanced Settings", expanded=False):
            st.slider("Temperature:", min_value=0.0, max_value=2.0, step=0.1, key='temperature')
            st.slider("P Factor:", min_value=0.0, max_value=1.0, step=0.01, key='p_factor')
            st.slider("Max Tokens:", min_value=1024, max_value=8192, step=512, key='max_tokens')
        st.button("Clear Chat", on_click=lambda: st.session_state.pop("messages", None))

    # Main
    with open('assets/logo-tm.svg') as f:
        st.markdown(f'<div id="main_header">{f.read()}<p>ITF Chatbot</p></div>', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if not API_KEY:
        st.info("Please add your GROQ_API_KEY in .env")
        st.stop()
    client = Groq(api_key=API_KEY)

    if prompt := st.chat_input():
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )
        st.chat_message("user").write(prompt)
        completion = client.chat.completions.create(
            model=MODELS[st.session_state.model],
            temperature=st.session_state.temperature,
            top_p=st.session_state.p_factor,
            max_tokens=st.session_state.max_tokens,
            stream=True,
            stop='stop',
            messages=st.session_state.messages
        )
        # Stream completion
        with st.chat_message("assistant"):
            response = st.write_stream(stream_response(completion))
        # Add completion to messages
        st.session_state.messages.append({"role": "assistant", "content": response})
        # st.session_state


if __name__ == "__main__":
    main()
