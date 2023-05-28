import sys
from path import PATH
sys.path.append(PATH)

import os
from dotenv import load_dotenv
load_dotenv()

import openai
import discord
from training_data.conversation import MESSAGES

import traceback

openai.api_key = os.getenv('OPENAI_API_KEY')
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

history = MESSAGES

def is_stop_command(message):
    return '!stop' in message.content and message.author != client.user

@client.event
async def on_message(message):
    print(message.content)
    try:
        if message.author == client.user:
            return
        if is_stop_command(message):
            await message.channel.send("Stopping the bot...")
            await client.close()
            return
        if client.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
            user_message = {
                "role": "user",
                "content": message.content
            }
            history.append(user_message)
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=history,
                temperature=1,
                max_tokens=90,
            )
            reply = response['choices'][0]['message']['content']
            assistant_message = {
                "role": "assistant",
                "content": reply
            }
            history.append(assistant_message)
            await message.channel.send(reply)
    except Exception as e:
        print(traceback.format_exc())

client.run(TOKEN)