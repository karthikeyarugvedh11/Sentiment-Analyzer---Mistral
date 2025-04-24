import streamlit as st
import requests
st.title("Sentiment Analyzer")
text_input=st.text_area("Write the sentence:")
if st.button("Analyze"):
 response=requests.post(url="http://localhost:8000/analyze/",data={"text":text_input})
 sentiment = response.json().get("sentiment", "Error")
 st.subheader("Predicted Sentiment:")
 st.write(sentiment)