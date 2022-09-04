import discord
import os
import io,json

GUILD_ID = 923604493378154496
TOKEN = os.getenv("ZEEKABOT")


class MyClient(discord.Client):
    async def on_ready(self):
        guild = self.get_guild(GUILD_ID)
        users = {}
        for m in guild.members:
            name = m.name + '#' + m.discriminator
            id = m.id
            users[name.lower()] = id
        with io.open("users.json", "w") as f:
            json.dump(users, f, indent=3)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
