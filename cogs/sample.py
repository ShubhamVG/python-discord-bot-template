import discord
from discord import app_commands
from discord.ext import commands


class Sample(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ping", description="sample slash command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")


async def setup(client: commands.Bot):
    await client.add_cog(Sample(client))
