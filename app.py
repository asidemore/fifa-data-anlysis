import os
from apikey import apikey

from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = apikey

st.title('三水十草月')
prompt = st.text_input('put your question')

llm = OpenAI(temperature=0.9)
text = prompt
st.write(llm(text))