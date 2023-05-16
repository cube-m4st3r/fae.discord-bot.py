import discord
from discord.ext import commands

import os
from colorama import Back, Fore, Style
import platform
import time

from dotenv import load_dotenv

import config

load_dotenv("settings-docker.env")

MY_GUILD = discord.Object(id=config.botConfig["hub-server-guild-id"]) or discord.Object(id=os.getenv("GUILD-ID"))


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!-&%', intents=discord.Intents().all())

    async def setup_hook(self):
        for fileName in os.listdir('./Commands'):
            if fileName.endswith('.py'):
                await self.load_extension(f'Commands.{fileName[:-3]}')

        await self.tree.sync(guild=MY_GUILD)
        await self.tree.sync()


    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC",
                                                        time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(f"{prfx} Logged in as {Fore.YELLOW} {self.user.name}")
        print(f"{prfx} Bot ID {Fore.YELLOW} {self.user.id}")
        print(f"{prfx} Discord Version {Fore.YELLOW} {discord.__version__}")
        print(f"{prfx} Python Version {Fore.YELLOW} {platform.python_version()}")
        print(f"{prfx} Bot Version 0.1")
        print(f"{prfx} Slash CMDs Synced: {Fore.YELLOW + str(len(await self.tree.fetch_commands(guild=MY_GUILD)))} Commands")
        print(f"{prfx} Connected to: {Fore.YELLOW + str(len(self.guilds))} Guilds")
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="configuring home network."))

client = Client()
client.run(config.botConfig["token"])