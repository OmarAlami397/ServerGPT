#Install Discord class and setup Discord Dev App
#Install OpenAI class and setup an API key on the OpenAI Development Platform
#This is a work in progress; stay tuned for updates as we continue to enhance functionality and optimize performance.
#Make sure to use your own Dev Tokens and API keys for Discord, OpenAI, and any other integrations used in the app.

#01/20/2025 Commit Version Details: First functional version of ServerGPT. Fully integrates the OpenAI Api with Discord servers through the app. 
#Currently using the gpt-3.5-turbo model.


import discord
import openai

openai.api_key = "Insert OPENAI API key"
chat_log = []

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    
    async def on_message(self, message):
        chat_log.append({"role": "user", "content": message.content})
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo", #Feel free to use different models
            messages = chat_log
        )
        assistant_response = response.choices[0].message.content
        chat_log.append({'role':'assistant', 'content': assistant_response.strip('\n').strip()})

        if client.user.mentioned_in(message):
            await message.channel.send(assistant_response)

intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('Insert Discord Dev Token')
