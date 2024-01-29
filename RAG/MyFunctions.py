from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from PyPDF2 import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.embeddings import HuggingFaceInstructEmbeddings
#from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)



# It will store the embedding on disk
persist_directory = "db"


class MySpecialFunctions:
    def __init__(self):
        pass
    
    def get_file_text(self, files):
        text = ""
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    text += content
            except Exception as e:
                print(f"Error reading file {file}: {e}")

        return text
    
    
    def get_pdf_text(self, pdf):
        text = ""
        for doc in pdf:
            reader = PdfReader(doc)
            for page in reader.pages:
                text += page.extract_text()

        return text


    
    
    def get_text_chunks(self, text):
        text_siplitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000, 
            chunk_overlap = 200,
            separators=['\n', '\n\n'],
            length_function = len)
        chunk = text_siplitter.split_text(text)
        return chunk
    

    def get_vectorstore(self, chunks):
        # embed with OpenAI
        #embedding = OpenAIEmbeddings()
        hf_embedding = HuggingFaceEmbeddings()

        # embed with HuggingFace. You replace cpu by cuda
        # hf_embedding = HuggingFaceInstructEmbeddings(
        #     model_name="hkunlp/instructor-xl", 
        #     model_kwargs={"device": "cpu"})

        # create the open-source embedding function
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # create vectorstore
        vector_db = Chroma.from_documents(
            documents = chunks,
            embedding = hf_embedding,
            #persist_directory = persist_directory
        )

        return vector_db #, persist_directory





        

    
