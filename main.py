import streamlit as st
from States import _get_state
from PIL import Image
img = Image.open('pharmacy.png').convert('RGB')
#paginas
import home
import test
st.set_page_config(page_title="Interntrial",page_icon=img,layout="centered",initial_sidebar_state="auto")
state = _get_state()

PAGES = {
	"Settings":home,
	"Test":test
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app(state)
state.sync()
