import discord
import random

from discord.ext import commands
from discord import app_commands
from discord.app_commands import checks

class Client(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} chegou na Angola.')

        try:
            guild = discord.Object(id = 1378036249373446254)
            synced = await self.tree.sync(guild = guild)
            print(f'synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'error: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('apaga pvf') or message.content.startswith('apaga o video pvf') or message.content.startswith('apaga o video'):
            respostas = ['nao', 'shorope', 'ratomanocu']
            await message.reply(random.choice(respostas))
        elif message.content.startswith('w'):
            respostas = ['speed', 'volecidade', 'foi L']
            await message.reply(random.choice(respostas))

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix = '+', intents = intents)

GUILD_ID = discord.Object(id = 1378036249373446254)

@client.tree.command(name = 'wcanal', description = 'mandah o w Canal', guild = GUILD_ID)
async def wCanal(interaction: discord.Interaction):
    await interaction.response.send_message('https://www.youtube.com/@CuzudoExtreme')

@client.tree.command(name = 'falar', description = 'falar.', guild = GUILD_ID)
async def falar(interaction: discord.Interaction, menssagem: str):

    if menssagem == 'sou gay' or menssagem == 'sou um lixo' or menssagem == 'sou um bosta':
        await interaction.response.send_message(f'{interaction.user.name} é um lizo orevel')
        return

    await interaction.response.send_message(menssagem)

@client.tree.command(name = 'calcular', description = 'calculadora 100% precisa que nunca erra', guild = GUILD_ID)
async def calculo(interaction: discord.Interaction, numero: float, numero2: float):
    await interaction.response.send_message(f'peros os meus galgolos angoranos deu {numero + numero2 / 69}')

@client.tree.command(name = 'doar', description = 'doar pro cuzudoExtreme e ajudar sua familia', guild = GUILD_ID)
async def doar(interaction: discord.Interaction, valor: float):
    if valor <= 10:
        await interaction.response.send_message(f'nao estou passando fomeh parah me doar {valor}, mendingoh.')
    else:
        await interaction.response.send_message(f'oberado pelos {valor} meuh abegoh.')


@client.tree.command(name='clear', guild=GUILD_ID)
@checks.has_permissions(administrator=True)
async def clear(interaction: discord.Interaction, quantidade: int):
    await interaction.response.defer(ephemeral=True)

    deleted = await interaction.channel.purge(limit=quantidade)

    await interaction.followup.send(f'pagueih {len(deleted)} menragens', ephemeral=True)


import os
client.run(os.getenv('DISCORD_TOKEN'))