#!/usr/bin/env python3.6
#-*- coding: UTF-8 -*-
#
# Servidor: Servidores | Acid Games
# Programador: Troy#1935
#

#━[ Módulos ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import discord
import secreto
from random import *
import asyncio

from pyfiglet import Figlet
from datetime import datetime

#━[ Variáveis ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Importantes:

client = discord.Client()
prefix = secreto.Prefix()
token = secreto.Token()
now = datetime.now()

# Cores:

Fuchsia=0xD900FF
Red=0xFF0000

#━[ Online ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@client.event
async def on_ready():
    print(f'━━━━━━━━━━━━ {client.user.name} ━━━━━━━━━━━━')
    print(f'Nome: {client.user.name}')
    print(f'  ID: {client.user.id}')
    print(f'━━━━━━━━━━━━ {client.user.name} ━━━━━━━━━━━━')

    # Status:

    while True:
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=f'❤ Olá! Você quer brincar?', type=1))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=f'❤ Meu prefixo é {prefix}', type=1))

#━[ Comandos ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@client.event
async def on_message(message):

    #━[ Comando: Help ]━━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}help'):

        embed = discord.Embed(
            title='👾 Meus Comandos',
            color=Fuchsia
	    )
        
        # Comandos - Públicos:

        embed.add_field(
            name="Público",
            value=f"`{prefix}ascii`\n"
                  f"`{prefix}emoji`\n"
                  f"`{prefix}avatar`\n"
                  f"`{prefix}dado`",
            inline=True
        )

        # Comandos - Privados:

        embed.add_field(
            name="Privado",
            value=f"`{prefix}aviso`\n"
                  f"`{prefix}votar`",
            inline=True
        )

        # Footer - Desenvolvedor:

        embed.set_footer(text=f"Criador: Troy#1935")

        await client.send_message(message.channel, embed=embed)



    #━[ Comando: Ascii ]━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}ascii'):

        # Fonte do Figlet:

        fonte = Figlet(font='standard')

        # Mensagem que irá imprimir:

        mensagem = message.content.replace(f'{prefix}ascii', ' ').strip()

        await client.send_message(message.channel, "```\n{}\n```".format(fonte.renderText(mensagem)))



    #━[ Comando: Emoji ]━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}emoji'):
        try:

            # Nome do Emoji:

            nome = message.content.replace(f'{prefix}emoji', ' ')

            # Retirar espaçamentos que contém ':' na string:

            retirar = nome.split(':')

            embed = discord.Embed(
                title=retirar[1],
                color=Red
            )

            # Setar o Emoji:

            embed.set_image(
                url="https://cdn.discordapp.com/emojis/{}.png".format(retirar[2].strip('>'))
            )

            await client.send_message(message.channel, embed=embed)

        except IndexError:

            embed = discord.Embed(
                title='Inválido!',
                color=Red,
                description=f'<@{message.author.id}>, Não será possível utilizá-lo! O emoji não é definitivo do servidor.'
            )

            await client.send_message(message.channel, embed=embed)



    #━[ Comando: Avatar ]━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}avatar'):
        try:

            # Menção do Usuário:

            mencao = message.mentions[0]

            embed = discord.Embed(
                title=f'{mencao}',
                description='[Download]('+mencao.avatar_url+')',
                color=Red
            )

            # Setar avatar do usuário:

            embed.set_image(url=mencao.avatar_url)

            # Footer - Nome » Usuário & Hora » Utilizou o comando:

            embed.set_footer(text=f"Comando utilizado por {message.author} às {now.hour}:{now.minute}")

            await client.send_message(message.channel, embed=embed)

        except:

            # Autor do Comando:

            autor = message.author

            embed = discord.Embed(
                title=f"{autor}",
                color=Red,
                description='[Download]('+autor.avatar_url+')'
            )

            # Setar avatar do autor:

            embed.set_image(url=autor.avatar_url)

            # Footer - Nome » Autor & Hora » Utilizou o comando:

            embed.set_footer(text=f"Comando utilizado por {autor} às {now.hour}:{now.minute}")

            await client.send_message(message.channel, embed=embed)




    #━[ Comando: Votar ]━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}votar'):
        try:

            mensagem = message.content.replace(f'{prefix}votar', ' ')

            embed = discord.Embed(
                    title="📌 Votação",
                    color=0xda00ff,
                    description=f'{mensagem}'
            )

            # Avatar do Autor:
            embed.set_thumbnail(url=message.author.avatar_url)

            # Nome do Autor:
            embed.set_footer(text=f"Por: {message.author.name}")

            # Excluir Mensagem:
            await client.delete_message(message)

            await client.send_typing(message.channel)

            embedSet = await client.send_message(message.channel, embed=embed)

            await client.add_reaction(embedSet, "✅")
            await client.add_reaction(embedSet, "❌")

        except IndexError:
            await client.send_message(message.channel, ":shrug: **|** Insira um texto para iniciar à votação.")



    #━[ Comando: Dado ]━━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}dado'):

        choice = randint(1, 6)

        embed = discord.Embed(
            title='🎲 Dado',
            color=0x1CF9FF,
            description=f'Joguei o dado, o resultado foi **{choice}**.'
        )

        await client.send_message(message.channel, embed=embed)




    #━[ Comando: Aviso ]━━━━━━━━━━━━━━━━━━━━━━━━━━

    if message.content.lower().startswith(f'{prefix}aviso'):

        if not message.author.server_permissions.administrator:
            embed = discord.Embed(
                    title='Inválido',
                    description='Você não tem permissão.',
                    color=0xff0000
            )

            embed.set_thumbnail(url="https://i.imgur.com/KC2Sq0g.png")

            embed.set_footer(
                    text=f'Comando solicitado por {message.author}',
                    icon_url=f'{message.author.avatar_url}'
            )

            return await client.send_message(message.channel, embed=embed)

        msg = message.content.replace(f'{prefix}aviso', ' ').strip()

        embed = discord.Embed(
            title='Mensagem',
            description=f'{msg}',
            color=0x00ff3b
        )

        embed.set_thumbnail(url="https://i.imgur.com/LfeLKTs.png")

        embed.set_footer(
            text=f'Comando solicitado por {message.author}',
            icon_url=f'{message.author.avatar_url}'
        )

        await client.send_message(message.channel, embed=embed)

        x = list(message.server.members)
        s = 0

        for member in x:
            embed = discord.Embed(
                    color=0x1aff00,
                    description=f'{msg}'
            )

            embed.set_image(url="https://cdn.discordapp.com/icons/486673336525520912/8a1828a322f6bc921ac9538c38e833c8.png?size=2048")

            embed.set_footer(
                    text=f'{client.user.name}',
                    icon_url=f'{client.user.avatar_url}'
            )

            try:
                await client.send_message(member, embed=embed)
                print(member.name)
                s += 1

            except:
                pass

        print('\n---- FIM ----\n')


        embed = discord.Embed(
            title='Mensagem Enviada',
            description='Mensagem enviada com sucesso!',
            color=0x1aff00
        )

        embed.set_footer(
            text=f'Comando solicitado por {message.author}',
            icon_url=f'{message.author.avatar_url}'
        )

        embed.set_thumbnail(url="https://i.imgur.com/qEmnerT.png")

        await client.send_message(message.channel, embed=embed)

client.run(token)
