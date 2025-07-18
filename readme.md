# LLM-Powered Q&A Chatbot

A simple, end-to-end GenAI project that functions as a Question & Answer chatbot. Users can ask queries and get responses from various supported Large Language Models (LLMs).

## 🚀 Features

- **Q&A Interface**: Simple and intuitive interface to ask questions.
- **Multi-Model Support**: Flexibility to switch between different LLMs.
- **OpenAI Integration**: Supports various models from OpenAI.
- **Open Source LLMs**: Includes support for open-source models via Ollama.
- **Easy Setup**: Get started quickly by providing your API keys in a `.env` file.



## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip
- An OpenAI API Key 
- [Ollama](https://ollama.com/) installed and running (if you wish to use open-source models)

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Irfan140/Chat-bot.git](https://github.com/Irfan140/Chat-bot.git)
    cd Chat-bot
    ```

2.  **Create a virtual environment :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a new file named `.env` in the root directory of the project.


    > **Note**: The project  requires LangSmith for tracing and monitoring. You will need to add your LangSmith credentials to the `.env` file as well.
    > ```env
    > # .env file for LangSmith
    > LANGSMITH_TRACING="true"
    > LANGSMITH_ENDPOINT="[https://api.smith.langchain.com](https://api.smith.langchain.com)"
    > LANGSMITH_API_KEY="your-langsmith-api-key"
    > LANGSMITH_PROJECT="your-project-name"
    > ```

## ▶️ How to Run

1.  Ensure your virtual environment is activated.
2.  Run the main application file:
    ```bash
    streamlit run app_openai.py
    ```
3.  Open your browser and navigate to the local URL provided in the terminal (e.g., `http://127.0.0.1:8501`).

---

Happy coding! 😁
