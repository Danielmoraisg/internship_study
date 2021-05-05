import streamlit as st 
import requests
import pandas as pd
import streamlit.components.v1 as components

def app(state):
	r = requests.get('https://docs.google.com/spreadsheets/d/1IDSpGH-kQMOzUWdZEpSkvFTBesC7OU9gvduYiWY5Xsw/edit?usp=sharing')
	data = r.content
	df = pd.read_html(data, skiprows = 1)[0].iloc[:,1:].dropna(how = 'all', axis = 1).dropna(how = 'all', axis = 0).fillna('empty')
	df['Categories'] = list(map(lambda x : x.split(','),df.Categories))
	df['sub categories'] = list(map(lambda x : x.split(','),df['sub categories']))
	if state.random:
		df = df.explode('Categories')
		if state.subcategories:
			df = df.explode('sub categories')
			subcategory = st.selectbox('Select the subcategory you want to train',sorted(list(set(df['sub categories']))))
			subdf = df[df['sub categories'] == subcategory]
		else:
			category = st.selectbox('Select the category you want to train',sorted(list(set(df.Categories))))
			subdf = df[df['Categories'] == category]
		if st.button('Next question'):
			samp = subdf.sample()
			q = samp['Question'].values[0]
			st.write(q)
			st.write('Your answer')
			components.html(
				"""<html>
<body>

<form action="/action_page.php">
<textarea id="w3review" name="w3review" rows="8" cols="90">

  </textarea>
  <br><br>
</form>

</body>
</html>"""
)
			with st.beta_expander('See hint'):
				st.write(samp['hint'].values[0])
			with st.beta_expander('See answer & Categories'):
				st.write(samp['Answer'].values[0])
				st.write("Categories: " + "".join(samp.Categories.values[0]))
				st.write("Subcategories: " + "".join(samp['sub categories'].values[0]))
		else:
			st.write('Click the button to get a question')
	else:
		if st.button('Next question'):
			samp = df.sample()
			q = samp['Question'].values[0]
			st.write(q)
			st.write('Your answer')
			components.html(
				"""<html>
<body>

<form action="/action_page.php">
<textarea id="w3review" name="w3review" rows="8" cols="90">

  </textarea>
  <br><br>
</form>

</body>
</html>"""
				)
			with st.beta_expander('See hint'):
				st.write(samp['hint'].values[0])
			with st.beta_expander('See answer & Categories'):
				st.write(samp['Answer'].values[0])
				st.write("Categories: " + ", ".join(samp.Categories.values[0]))
				st.write("Subcategories: " + ", ".join(samp['sub categories'].values[0]))
		else:
			st.write('Click the button to get a question')