import streamlit as st 
import pandas as pd
import os
import base64
def app(state):
	st.title('Creating Plots')
	st.write('Click the button below to add your dataset and check if your data is correct')
	upload = st.file_uploader('',accept_multiple_files = False)
	#add option to download templates
	if st.checkbox('Download templates'):
		def get_binary_file_downloader_html(bin_file, file_label='File'):
			with open(bin_file, 'rb') as f:
				data = f.read()
			bin_str = base64.b64encode(data).decode()
			href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
			return(href)
		st.markdown(get_binary_file_downloader_html('template.xlsx', 'Excel template'), unsafe_allow_html=True)
		st.markdown(get_binary_file_downloader_html('template.csv', 'Comma separated values template'), unsafe_allow_html=True)
		st.markdown(get_binary_file_downloader_html('template.txt', 'Text file template'), unsafe_allow_html=True)
	#display data
	if upload is not None:
		state.name = upload.name
		if state.name.split('.')[1] == 'xlsx' or state.name.split('.')[1] == 'xls' :
			#state.data = pd.read_excel(upload)
			data = upload.read()
			excel = pd.ExcelFile(data)
			sheet = st.selectbox('Sheet from excel file to be used',excel.sheet_names)
			#options for excel upload
			if st.checkbox('More options', value = False):
				state.data = pd.read_excel(data, sheet_name = sheet)
				total = len(state.data)
				if st.checkbox('Select first and last row of the dataset'):
					skip = st.number_input('Beginning of the dataset', value = 1)
					last = st.number_input('End of the dataset', value = total)
				else:
					skip = 0
					last = total
				if st.checkbox('Does your data has a Header?', value = True):
					header = 0
				else:
					header = None

				state.data = pd.read_excel(data, sheet_name = sheet, skiprows = skip-1, header = header)[0:last]
				st.write(state.data)
			else:
				state.data = pd.read_excel(data, sheet_name = sheet)
				st.write(state.data)

		elif state.name.split('.')[1] == 'csv' or state.name.split('.')[1] == 'txt' :
			state.data = pd.read_csv(upload)
			st.write(state.data)
		upload.seek(0)

		