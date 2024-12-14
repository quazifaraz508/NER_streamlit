import streamlit as st
from NER_logic import ner_logic
from  offensive_words import offencive_word_detect
ner_logic_op = ner_logic()

st.set_page_config(page_title="NER_prototype", layout="wide")
st.title('This is named_entity_recognition app (NER).')
st.header("from text it find STATE ,CITIES and VILLAGE but for now it has limited data so may be some of data it can't find but most of the it will.")

user_inp = st.text_input('Enter text/message: ','This is maharashtra not goa or bihar')
result = ner_logic_op.build(user_inp)
st.write(result)
result_offens = offencive_word_detect(user_inp)
st.write(result_offens)

