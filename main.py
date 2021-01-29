import streamlit as st
from States import _get_state

#paginas
import home
import bar
import line
import multi_bar
import multi_line
st.set_page_config(page_title="Graph-ly",page_icon=":fire:",layout="centered",initial_sidebar_state="auto")
state = _get_state()

PAGES = {
	"Homepage":home,
    "Line Chart": line,
    "Bar Chart": bar,
    "Multiple Bars Chart":multi_bar,
    'Multipel Lines Chart':multi_line
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app(state)
state.sync()