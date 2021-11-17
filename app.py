# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

publication_d = {0:"Towards Data Science",1:"UX Collective",2:"The Startup",3:"The Writing Cooperative publication",4:"Data Driven Investor",5:"Better Marketing",6:"Better Humans"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="Aplikacja do predykcji liczby oklasków")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://miro.medium.com/max/500/1*ZhYNqU2y96_f3QkWq9oiWQ.jpeg")

	with overview:
		st.title("Aplikacja do predykcji liczby oklasków")

	with left:
		publication_radio = st.radio("Kategoria", list(publication_d.keys()), format_func=lambda x : publication_d[x] )

	with right:
		responses_slider = st.slider("Komentarze", value=1, min_value=0, max_value=173)
		reading_time_slider = st.slider("Czas czytania w minutach", min_value=0, max_value=55)

	data = [[responses_slider, reading_time_slider, publication_radio]]
	claps = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Ile oklasków otrzyma artykuł?")
		st.subheader(claps)
		st.write("Dziękuję. W takim razie napiszę!")

if __name__ == "__main__":
    main()