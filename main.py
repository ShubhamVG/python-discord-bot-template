import os

import discord
from discord.ext import commands

with open("token.txt", "r") as f:
    TOKEN = f.read()  # Reading the discord bot token from the file

client = commands.Bot(
    intents=discord.Intents.all(),  # Intents Levels
    command_prefix="!",  # Your basic command prefix goes here
    help_command=None,  # You can set a help command, but I prefer None
    description="This is a discord bot template. You should change this.",
    # ^^ Change this to whatever your bot is meant to do
)


async def load_cogs(client: commands.Bot) -> None:
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):  # Loading all the supplemental cog files
            # For better organization of commands and files
            await client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def setup_hook() -> None:
    await load_cogs(client)  # This runs when the bot is ready


@client.command(name="sync")
async def sync(context: commands.Context):
    await client.tree.sync()  # This will sync your application commands
    await context.reply("Syncing...")


def main():
    client.run(TOKEN)  # Running the bot


if __name__ == "__main__":
    main()  # If this is the file being run, run the main function
