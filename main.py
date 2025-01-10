import os
import discord
from discord.ext import commands

with open("token.txt", "r") as f:
    TOKEN = f.read()

client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix="!",
    help_command=None,
    description="This is a discord bot template. You should change this.",
)

async def load_cogs(client: commands.Bot) -> None:
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def setup_hook() -> None:
    await load_cogs(client)

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()