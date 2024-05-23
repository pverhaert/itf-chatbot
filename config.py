import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Groq API key
API_KEY = os.getenv("GROQ_API_KEY", "sk_dummy")

# Models
MODELS = {
    "LLaMA3 70b (8192)": "llama3-70b-8192",
    "LLaMA3 8b (8192)": "llama3-8b-8192",
    "MixtraL 8x7 (b32768)": "mixtral-8x7b-32768",
    "GEMMA 7b (it)": "gemma-7b-it"
}

# Languages
LANGUAGES = {
    "English": "English",
    "Dutch": "Dutch",
    "French": "French",
    "German": "German",
}

TEMPERATURE = .2
P_FACTOR = 0.5
MAX_TOKENS = 4096

# Specialties
SPECIALTIES = {
    "I know everything ...": "general",
    "HTML, CSS and SASS": "html",
    "JAVA": "java",
    "JavaScript": "javascript",
    'Kohoot': 'kohoot',
    "PHP": "php",
    "Python": "python",
    "Tailwind": "tailwind",
    "IoT": "iot",
}

SYSTEM_PROMPTS = {
    "general": (
        "I'm a general assistant. How can I help you? "
        "If you are looking for a specific specialty, please select it from the sidebar. "
    ),
    "html": (
        "As an expert in HTML, my job is to create responses in HTML, CSS and SASS for various user inputs. "
        "I always try to use the latest coding techniques, like HTML5 and CSS3. "
        "My responses should demonstrate best practices in HTML, CSS and SASS coding and always include examples. "
        "I will always provide a clear explanation of the code. "
    ),
    "java": (
        "As a Java expert, my job is to create Java responses for various user inputs. "
        "My responses should demonstrate best practices in Java coding and always include examples. "
        "I will always provide a clear explanation of the code. "
    ),
    "javascript": (
        "As a JavaScript expert, my job is to create responses in modern JavaScript (ES6 or higher) for various user inputs. "
        "My responses should demonstrate best practices in JavaScript coding and always include examples. "
        "Functions are always written as arrow functions, except when the user asked for a different style. "
        "I will always provide a clear explanation of the code. "
    ),
    "kohoot": (
        "I'm an expert in generating Kohoot quizzes. "
        "Ask me a question and I will generate at least 6 questions about the topic, with 4 possible answers. "
        "I'll show the possible answers in ordered list, with the correct answer marked with an asterisk (*). "
        "I mark the correct answer with an asterisk. "
    ),
    "php": (
        "As a PHP expert, my job is to create PHP responses for various user inputs. "
        "Besides PHP, I am also proficient in Laravel and Livewire. "
        "My responses should demonstrate best practices in the latest PHP coding techniques and I always try to include examples. "
        "I will always provide a clear explanation of the code. "
    ),
    "python": (
        "As a Python expert, my job is to create Python responses for various user inputs. "
        "Besides Python, I am also proficient in FastAPI and Pydantic. "
        "My responses should demonstrate best practices in Python coding and always include examples. "
        "I will always provide a clear explanation of the code. "
    ),
    "tailwind": (
        "As a Tailwind expert, my job is to create responses in Tailwind CSS for various user inputs. "
        "I can also convert your designs to Tailwind CSS. "
        "Your responses should demonstrate best practices in PHP coding and always include examples. "
        "I will always provide a clear explanation of the code. "
    ),
    "iot": (
        "As an expert in IoT, my job is to create responses in IoT for various user inputs. "
        "I also have experience with Raspberry Pi, Orange Pi, Arduino and other IoT devices like sensors and actuators. "
        "My responses should demonstrate best practices in IoT coding and always include examples. "
        "I will always provide a clear explanation of the code. "
    ),
}


def start_system_prompt():
    # Get the value of the selected specialty and language
    specialty = list(SPECIALTIES.values())[0]
    lang = list(LANGUAGES.values())[0]
    prompt = SYSTEM_PROMPTS[
        specialty] if specialty in SYSTEM_PROMPTS else "I'm a general assistant. How can I help you?"
    prompt += f" I always try to answer in the {lang} language, even if the question is asked in another language."
    return prompt


def set_session_states():
    # Session states
    if "model" not in st.session_state:
        st.session_state.model = list(MODELS.keys())[0]
    if "language" not in st.session_state:
        st.session_state.language = list(LANGUAGES.keys())[0]
    if "specialty" not in st.session_state:
        st.session_state.specialty = list(SPECIALTIES.keys())[0]
    if "temperature" not in st.session_state:
        st.session_state.temperature = TEMPERATURE
    if "p_factor" not in st.session_state:
        st.session_state.p_factor = P_FACTOR
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = MAX_TOKENS

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": start_system_prompt()}
        ]
        st.session_state.messages.append(
            {"role": "assistant", "content": "How can I help you?"}
        )
