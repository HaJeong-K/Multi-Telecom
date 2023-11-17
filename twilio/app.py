# -*- coding: UTF-8 -*-
import streamlit as st

def main():
    st.title("Hello World!")

    st.text("Hello World2")

    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

if __name__ == "__main__":
    main()