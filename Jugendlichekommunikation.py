import streamlit as st
import pandas as pd
import altair as alt

st.header("Wie Jugendliche am liebsten kommunizieren")
st.subheader("Jugendliche, die folgende Dienste täglich mehrmals pro Woche nutzen")

source = pd.DataFrame({
        'Anteil(%)': [92, 58, 46, 42, 26, 15, 13, 12, 12, 10],
        'Apps, Dienste': ['Whatsapp', 'Instagram', 'Tiktok', 'Snapschat', 'Facebook', 'Discord', 'Pinterest', 'Zoom', 'Twitch', 'Twitter']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Apps, Dienste:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=1188; 12-19 Jahre in Deutschland; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: mpfs JIM-Studie 2021")