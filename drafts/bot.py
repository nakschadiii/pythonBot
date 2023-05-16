from structs import *
import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="/", intents = intents)

""" @bot.event
async def on_command(ctx):
    user_id = ctx.author.id
    if user_id not in user_history:
        user_history[user_id] = history()

    command_name = ctx.message.content.split()[0]
    if command_name not in ignored_commands:
        user_history[user_id].add_command(ctx.message.content) """

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        colors = {"rouge" : discord.Color.red(), "vert" : discord.Color.green(), "jaune" : discord.Color.yellow(), "bleu" : discord.Color.blue()}
        for color in colors:
            await message.channel.send(color)
            for number in range(1, 11):
                # embed.add_field(name='Ceci est un message en rouge', value='Hello World!', inline=False)
                await message.channel.send(embed=discord.Embed(title=number, color=colors[color]))

client.run("MTA5MTMzODg5Njk2NjY4MDY2Ng.G0fbwb.nqXVunkNWO2vP_3i8gP-N6lpW7ij2SCvBV5PqY")