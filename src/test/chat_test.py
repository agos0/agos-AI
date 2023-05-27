# CHAT WITH BOT THROUGH TERMINAL:

"""
import sys
from config import PATH
sys.path.append(PATH)
import openai
from config import OPENAI_API_KEY
from chat_data.conversation import MESSAGES

openai.api_key = OPENAI_API_KEY

def run_chat():
    history = MESSAGES

    while True:
        user_msg = input("me: ")
        history.append({"role": "user", "content": user_msg})
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=history,
            temperature=1,
            max_tokens=90,
        )
        chatbot_reply = response['choices'][0]['message']['content']
        print("me AI:", chatbot_reply)
        history.append({"role": "assistant", "content": chatbot_reply})

        if end(user_msg):
            break

def end(msg):
    if "bye" in msg.lower():
        return True
    return False

run_chat()
"""