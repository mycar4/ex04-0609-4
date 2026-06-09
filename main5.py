from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title("디지털 글쓰기")
subject = st.text_input("글 쓸 주제를 입력하세요")

# '작성하기' 버튼을 누른 경우에만 아래 코드가 실행됨
if st.button("작성하기"):
    with st.spinner("Wait for it...", show_time=True):
        response = chat_model.invoke(subject + "에 대해 설명해줘") 
        st.write(response.content)