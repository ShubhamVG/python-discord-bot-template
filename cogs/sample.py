import discord
from discord import app_commands
from discord.ext import commands


class Sample(commands.Cog):  # Cog Defintion
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ping", description="sample slash command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @commands.Cog.listener()  # Sample Event Listener
    async def on_guild_join(guild: discord.Guild):
        print(f"Client has just joined the guild {guild.name}")


async def setup(client: commands.Bot):  # Function to add the cog to the client
    await client.add_cog(Sample(client))
