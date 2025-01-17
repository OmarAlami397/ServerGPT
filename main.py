#Install Discord class and setup Discord Dev App before beginning
#This is a work in progress; stay tuned for updates as we continue to enhance functionality and optimize performance.
#Make sure to use your own Dev Tokens and API keys for Discord, OpenAI, and any other integrations used in the app.

#01/17/2025 Commit Version Details: The Code written turns on the ServerGPT app in your discord server and reads all messages sent on any channel.


import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('INSERT DISCORD DEV TOKEN')
