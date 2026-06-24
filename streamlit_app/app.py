import streamlit as st

st.title('Agentic Travel Assistant')
query = st.chat_input('Plan my trip')
if query:
    st.write(f'Planning trip for: {query}')
