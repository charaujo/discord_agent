from dotenv import load_dotenv
from openai import OpenAI

import discord
import os

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API client
OPENAI_KEY = os.getenv('OPENAI_KEY')
oa_client = OpenAI(api_key=OPENAI_KEY)

#ask openai - respond with a simple message
def ask_openai(question):
    completion = oa_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
             "content": f"Respond friendly to the following question: {question}"}
        ]
    )

    #print the response
    response = completion.choices[0].message.content
    print(response)
    return response

# Set up intents
intents = discord.Intents.default()
intents.message_content = True # Ensure that your bot can read message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hey Friend! How can I assist you today?')
    
    if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question ")[1]
        print(f"Message: {message.content}")
        response = ask_openai(message_content)
        print(f"Teacher: {response}")
        print("---")
        await message.channel.send(response)

client.run(os.getenv('DISCORD_TOKEN'))
