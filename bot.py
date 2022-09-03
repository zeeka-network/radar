import discord
import os

GUILD_ID = 923604493378154496

TOKEN = os.getenv("ZEEKABOT")


class MyClient(discord.Client):
    async def on_ready(self):
        guild = self.get_guild(GUILD_ID)
        print(guild.members)
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.messages = True
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
