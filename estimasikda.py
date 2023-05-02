import pickle
import streamlit as st

model = pickle.load(open('estisikda.sav', 'rb'))

st.title('Estimasi KDA Pada statistik player')
Kills = st.number_input('Input Kills')
Deaths = st.number_input('Input Deats')
Assists = st.number_input('Input Assists')
killParticipation = st.number_input('Input KillPartisipation')

predict = ''

if st.button('Estimasi KDA'):
    predict = model.predict(
        [[Kills,Deaths,Assists,killParticipation]]
    )
    st.write ('Estimasi KDA: ', predict)