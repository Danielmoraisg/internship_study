import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objects import Layout

from pathlib import Path
import os
import base64

def app(state):
	#configs basicas
    st.title('Bar Plot')
    Y = st.selectbox('Column to be mapped on the Y axis',state.data.columns)
    X = st.selectbox('Column to be mapped on the X axis',state.data.columns)
    color = st.selectbox('Specify columns to differ bar color',state.data.columns)
    modes = {'Groups':'group', 'Stacked':'stack','Overlay':'overlay','Relative positioning':'relative'}
    mode = st.selectbox('How to display different groups', list(modes.keys()))
    title = st.text_input("Title",state.name[0:-4])    
    #advanced configs
    xtitle = X
    ytitle = Y
    
    if st.checkbox('Advanced'):
    	st.write('Configs avançadas:')
    	ytitle = st.text_input('Y Title', Y)
    	xtitle = st.text_input('X Title', X)

    fig = px.bar(state.data, x=X, y=Y, title=title,template = 'plotly_white', color = color, barmode = modes[mode])

    fig.update_xaxes(showgrid = True,showline=True, linewidth=2, linecolor='black', title_text = xtitle)
    fig.update_yaxes(showgrid = True,showline=True, linewidth=2, linecolor='black', title_text = ytitle)
    fig.update_layout(title_x=0.5, bargap = 0.2, bargroupgap=0.1)

    st.plotly_chart(fig, use_container_width=True)
    def img_to_bytes(img_path):
    	img_bytes = Path(img_path).read_bytes()
    	encoded = base64.b64encode(img_bytes).decode()
    	return encoded
    fig_html = "To download the plot click the camera icon <img src='data:image/png;base64,{}' width='18' height='15' class='img-fluid'>".format(img_to_bytes(r'images/download_icon.png'))
    st.markdown(fig_html, unsafe_allow_html=True,)
