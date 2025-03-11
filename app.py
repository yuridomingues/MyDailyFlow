"""
MyDailyFlow - Aplicativo para gerenciar e visualizar rotinas diárias.
"""

import streamlit as st
from routine import routine  # Importe os dados da rotina

# Título do app
st.title("MyDailyFlow")

# Sidebar para selecionar o dia
day = st.sidebar.selectbox("Selecione o dia", list(routine.keys()))

# Exibir a rotina do dia selecionado
st.header(f"Rotina - {day}")
for time, activity in routine[day]:
    st.write(f"**{time}:** {activity}")
