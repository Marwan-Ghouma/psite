import streamlit as st

st.header("Bank check deposit")
video_file = open('bankapp2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.header("Crypto analysis and prediction")
video_file = open('cryptoapp2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.header("App mobile demo")
video_file = open('mobile2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)