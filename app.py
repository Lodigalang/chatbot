import streamlit as st
from Inference import chat_bot

# Judul aplikasi
st.title("Bot Chat Sederhana dengan Gemini 2.0 Flash")

# Inisialisasi session state untuk menyimpan pesan chat
# session_state adalah cara streamlit untuk menyimpan data antar interaksi user
# Ini penting agar chat bot kita bisa mengingat percakapan sebelumnya
if "message" not in st.session_state:
    st.session_state.message = []

# Menampilkan pesan-pesan yang sudah ada dari session state
# Kode ini melooping semua pesan yang tersimpan di st.session_state.message
# dan menampilkannya di UI menggunakan st.chat_message
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Membuat input chat untuk user
# st.chat_input membuat sebuah input text box di mana user bisa mengetik pesannya
prompt = st.chat_input("Ketik Pesan")

# Memproses input dari user
# Kode ini dijalankan ketika user mengetik pesan dan menekan Enter
if prompt:
    # Memanggil fungsi chat_bot untuk mendapatkan respon dari model
    # chat_bot(prompt) adalah fungsi dari module Inference.py yang melakukan inferensi
    # menggunakan model Gemini dan mengembalikan responnya
    response = chat_bot(prompt)

    # Menampilkan pesan user di chat
    with st.chat_message("user"):
        st.markdown(prompt)
    # Menyimpan pesan user ke session state
    st.session_state.message.append({
        "role": "user", "content": prompt
    })

    # Menampilkan pesan dari bot di chat
    with st.chat_message("assistant"):
        st.markdown(response)
    # Menyimpan pesan bot ke session state
    st.session_state.message.append({
        "role": "assistant", "content": response
    })