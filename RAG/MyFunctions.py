from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter



class MySpecialFunctions:
    def __init__(self):
        pass
    
    def get_file_text(self, files):
        text = ""
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                text += content
        return text
    
    
    def get_text_chunks(self, text):
        text_siplitter = RecursiveCharacterTextSplitter(
            chunk_size = 500, 
            chunk_overlaps= 100,
            separators=['\n', '\n\n'],
            length_function = len)
        chunk = text_siplitter.split_documents(text)
        return chunk
    

    def get_vectorstore():

        

    
