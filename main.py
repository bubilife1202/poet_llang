# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은 ")
# print(result)

# from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers
import streamlit as st

# chat_model = ChatOpenAI()
llm = CTransformers(
    model = "llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('AI Poet in Korean: Global Gateway to Korean Verse')
content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = llm.predict("write a poem about " + content + ":")
        st.write(result)

# st.title('_Streamlit_ is :blue[cool] :sunglasses:')