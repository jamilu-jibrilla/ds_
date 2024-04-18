from flask import Flask, request, jsonify
from langchain.llms import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import PyPDF2
import os

from numpy import dtype

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = ""
def extract_text_from_pdf(filename):
    with open(filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


documents = SimpleDirectoryReader("extract/Data_Files").load_data()


openai = OpenAI(temperature=0.7) 
index = VectorStoreIndex.from_documents(documents) 


@app.route('/ask', methods=['POST'])
def answer_query():
    query = request.json.get('question')
    if not query:
        return "Please provide a question!", 400

    query_engine = index.as_query_engine()

    response = query_engine.query(query)
    
    return jsonify(str(response))

if __name__ == '__main__':
    app.run()
