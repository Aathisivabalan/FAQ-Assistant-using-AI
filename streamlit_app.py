import streamlit as st
import requests

st.title("RAG FAQ Chatbot 🤖")
st.write("Ask a question about RAG, FAISS, LLMs, etc.")

user_query = st.text_input("Your Question:")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"query": user_query},
                    timeout=10  # Add a timeout to avoid hanging
                )
                response.raise_for_status()
                answer = response.json().get("answer")
                if answer:
                    st.success(answer)
                else:
                    st.warning("No answer returned from backend.")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to backend API. Is the FastAPI server running?")
            except requests.exceptions.Timeout:
                st.error("The request to the backend timed out.")
            except requests.exceptions.RequestException as e:
                st.error(f"Backend API Error: {e}")
