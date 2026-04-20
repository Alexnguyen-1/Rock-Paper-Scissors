import random
import streamlit as st
st.title("✊ Rock Paper Scissors ✋✌️")
Options=['Rock','Paper','Scissors']
User_choice=st.radio('Enter you choice: ', ['Rock','Paper','Scissors'])
if st.button("Play"):
    Bot_choice=random.choice(Options)
    if User_choice==Bot_choice:
        st.write('Bot chose ' + Bot_choice)
        st.write('Tie')
    elif (User_choice=='Rock' and Bot_choice=='Scissors') or \
            (User_choice=='Paper' and Bot_choice=='Rock') or \
            (User_choice=='Scissors' and Bot_choice=='Paper'):
        st.write('Bot chose ' + Bot_choice)
        st.write('🎉 You win!')
    else:
        st.write('Bot chose ' + Bot_choice)
        st.write('💻 Bot wins :(')
