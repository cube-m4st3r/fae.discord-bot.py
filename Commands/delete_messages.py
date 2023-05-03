import discord
from discord import app_commands
from discord.ext import commands

import config


class delete_messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="delete_messages", description="Delete Messages")
    async def deletemessages(self, interaction: discord.Interaction, number: int, member: discord.Member=None):
        if interaction.user.id in config.botConfig["user-access-ids"]:
            delete_counter = 0
            await interaction.response.send_message(content="Wird gemacht!", delete_after=3, ephemeral=True)
            async for message in interaction.channel.history():
                if message.author == member or member == None:
                    await message.delete()
                    delete_counter += 1
                if delete_counter == number:
                    break
        else:
            await interaction.send_message(content="You don't have access to my commands!", ephemeral=True, delete_after=5)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(delete_messages(bot), guild=discord.Object(id=config.botConfig["hub-server-guild-id"]))