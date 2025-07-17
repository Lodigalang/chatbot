import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Konfigurasi API key
genai.configure(api_key=api_key)

# Inisialisasi model (bisa ganti dengan gemini-1.5-pro atau lainnya)
model = genai.GenerativeModel("gemini-2.0-flash")  # atau "gemini-pro", "gemini-1.5-pro"

# Fungsi untuk mengirim pesan
def chat_bot(prompt):
    response = model.generate_content(prompt)
    return response.text
