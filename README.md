# ITF Chatbot with Groq API
This project is a Streamlit application that interacts with the Groq API to provide information about the ITF Chatbot.

## Technologies Used
- Python 3.x
- Streamlit
- Groq API
- dotenv for environment management

## Getting Started

### Prerequisites
Ensure you have Python 3.11 or higher installed on your system. Streamlit and other required packages will be installed via the requirements file.

### Installation
1. Clone the repository: `git clone https://github.com/pverhaert/itf-groq-chatbot.git`
2. Navigate to the project directory: `cd itf-groq-chatbot`
3. Set up a virtual environment (optional but recommended)
4. Install the required Python packages: `pip install -r requirements.txt`

## Configuration
### Obtaining a Groq API Key
To use this application, you'll need an API key from Groq. Visit the [Groq API documentation](https://console.groq.com/docs/quickstart) to learn how to obtain one.

### Setting Up Your Environment
Once you have your API key, you need to set it in your environment:
- Rename `.env.example` to `.env`.
- Open the `.env` file and replace `YOUR_API_KEY_HERE` with your Groq API key

This step is crucial for the application to interact with Groq's services securely.

## Running the Application
To run the application, use the following command: `streamlit run main.py`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
