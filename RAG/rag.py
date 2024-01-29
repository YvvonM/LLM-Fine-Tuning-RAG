import streamlit as st 
from MyFunctions import MySpecialFunctions


# create an instance of my class
special_functions_instance = MySpecialFunctions()

def get_text(fine_tuned_text):
    return special_functions_instance.get_file_text(fine_tuned_text)








def main():

    st.set_page_config(page_title="Generation of Telegram Ads in Amharic", page_icon= ":smile")
    

    with st.sidebar:
        #st.markdown("# Menu")
        pass

    st.markdown("## Ads Generation in Amharic")
    fine_tuned_text = st.file_uploader(" Upload the generative text from fune-tuning", accept_multiple_files= True)
    if st.button("Retrieval"):
        with st.spinner("Processing"):
            # get files text
            text = get_text(fine_tuned_text)
            st.write(text)

            # get_text_chunks(text)
            text_chunks = get_text_chunks(text)
            st.write(text_chunks)





if __name__ == "__main__":
    main()