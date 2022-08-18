import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

from classes import classes, class_specs, links

load_dotenv()

bot_token = os.environ['BOT_TOKEN']

# bot = disnake.Client
bot = commands.InteractionBot()

@bot.event
async def on_ready():
    print(f'MoP Jenkins, at your service, logged in as {bot.user}')

@bot.slash_command(name="talents", description="Recommended class/spec talents")
async def talents(
    interaction: disnake.ApplicationCommandInteraction, cls: str, spec: str
):
    author = interaction.author
    command_name = interaction.application_command.name

    print(f"{author.name} requested {command_name} for {spec} {cls}")
    await interaction.response.send_message(links[cls]["specs"][spec])

@bot.slash_command(name="guide", description="Everything you need to know about a class/spec")
async def guide(
  interaction: disnake.ApplicationCommandInteraction, cls: str, spec: str
):
  author = interaction.author
  command_name = interaction.application_command.name

  print(f"{author.name} requested {command_name} for {spec} {cls}")
  await interaction.response.send_message(links[cls]["guides"][spec])

@talents.autocomplete("cls")
@guide.autocomplete("cls")
async def cls_autocomplete(
    interaction: disnake.ApplicationCommandInteraction, string: str
):
    string = string.lower()

    return [c for c in classes if string in c.lower()]

@talents.autocomplete("spec")
@guide.autocomplete("spec")
async def spec_autocomplete(
    interaction: disnake.ApplicationCommandInteraction, string: str, cls: str
):
    string = string.lower()

    return [opt for opt in class_specs[cls] if string in opt.lower()]

bot.run(bot_token)
