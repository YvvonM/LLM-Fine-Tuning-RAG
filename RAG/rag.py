import streamlit as st 
from MyFunctions import MySpecialFunctions
from dotenv import load_dotenv


# create an instance of my class
special_functions_instance = MySpecialFunctions()

def get_text(external_data ):
    return special_functions_instance.get_file_text(external_data )

def get_pdf_text(external_data ):
    return special_functions_instance.get_pdf_text(external_data )

def get_chunks(text):
    return special_functions_instance.get_text_chunks(text)

def get_vectorstore(text_chunks):
    return special_functions_instance.get_vectorstore(text_chunks) 





def main():
    load_dotenv()
    st.set_page_config(page_title="Generation of Telegram Ads in Amharic", page_icon= ":smile")
    

    with st.sidebar:
        #st.markdown("# Menu")
        pass

    st.markdown("## Ads Generation in Amharic")
    external_data = st.file_uploader(" Upload the generative text from fune-tuning", accept_multiple_files= True)
    if st.button("Retrieval"):
        with st.spinner("Processing"):
            # get files text
            #text = get_text(external_data )
            text = get_pdf_text(external_data )
            #st.write(text)

            # get_text_chunks(text)
            text_chunks = get_chunks(text)
            st.write(text_chunks)


            # get_vectorstore 
            vectorstore_db = get_vectorstore(text_chunks)
            #st.write(vectorstore_db)
            #st.write("--------------")
            #st.write(persist_directory)





if __name__ == "__main__":
    main()