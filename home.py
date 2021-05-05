import streamlit as st 

def app(state):
	st.title('Adjust test settings')
	state.random = st.checkbox("Choose category of questions", value = True)
	state.subcategories = st.checkbox("Choose sub category of questions", value = True)
	
	

		