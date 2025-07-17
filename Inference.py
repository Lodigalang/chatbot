from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")

def chat_bot(prompt) :
    response = chat.send_message(prompt)
    return response.text


#if __name__== "__main__":
    #input_text = input("Chat: ")
    #chat_bot(input_text)
    #reply=chat_bot(input_text)
    #print(reply)