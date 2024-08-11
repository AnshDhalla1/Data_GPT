# Data_GPT

## Overview
Data_GPT is a chatbot and analytics dashboard designed to interact with your CSV, XLSX, or SQL databases. Built using LangChain and pandasai, this project eliminates the need for constructing complex SQL queries or data retrieval code, making data analysis more accessible and intuitive.

## Features
1. RAG-based Chatbot: Utilizes Retrieval-Augmented Generation (RAG) to answer user queries based on provided data.
2. Seamless Data Integration: Supports querying from CSV and Excel files.
3. LangChain and pandasai Integration: Leverages LangChain for natural language processing and pandasai for data manipulation.
4. Customizable Responses: Tailored responses based on specific user queries with a focus on financial analytics.
<img width="1440" alt="Screenshot 2024-08-11 at 10 47 50 AM" src="https://github.com/user-attachments/assets/baa2fe1c-18dd-4c9a-b900-81c958c42047">


## Installation

1. Clone the repository:
  ```bash
git clone https://github.com/YourUsername/Data_GPT.git
cd Data_GPT
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```
2. Upload your CSV file: On the application interface, upload the CSV file containing your data.
3. Interact with the chatbot: Type your queries into the chat interface, and the chatbot will respond based on the data provided.

## Project Structure

1. **app.py:** The main Streamlit application file that handles the user interface and interaction with the chatbot.
2. **chatLLM.py:** Contains the logic for interacting with OpenAI's GPT-3.5 model, including loading the question-answering chain and generating responses.
3. **knowledge.py:** Handles the loading and processing of data, including the extraction of text chunks and building the FAISS knowledge base.

<img width="802" alt="Screenshot 2024-08-11 at 10 48 14 AM" src="https://github.com/user-attachments/assets/6513ecf9-c77e-43b6-92ed-3623f577fb7a">


## License

This project is licensed under the MIT License.

## Acknowledgements

1. **LangChain** for providing a powerful framework for language model integration.
2. **pandasai** for simplifying data manipulation.
3. **Streamlit** for enabling a quick and easy deployment of ML Models.


