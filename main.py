from urllib import request
import discord
import asyncio
import os
import random
import json
import requests
import aiohttp
from discord.utils import get
from keep_alive import keep_alive
from discord.ext import commands, tasks
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix="&", intents=intents)


@client.event
async def on_ready():
    print("we are logged in")


@client.command()
async def advice(ctx):
    r = requests.get("https://api.adviceslip.com/advice")
    res = r.json()
    await ctx.send(res)


# https://nekos.life/api/v2/endpoints
# Genshin Impact


@client.command()
async def kiss(ctx):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def lewd(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/hentai")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command()
async def cringe(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/cringe")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def ngif(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def ass(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/ass")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def manga(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/manga")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="Random meme")
async def meme(ctx):
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def cuckold(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/cuckold")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(help="nsfw section")
async def ahegao(ctx):
    r = requests.get("https://hmtai.herokuapp.com/v2/ahegao")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command()
async def slap(ctx):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command()
async def spank(ctx):
    r = requests.get("https://nekos.life/api/v2/img/spank")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command(aliases=["8ball"], help="Enter Your Question")
async def eightball(ctx, *, question):
    response = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    await ctx.send(f"**Question: ** {question}\n**Answers:** {random.choice(response)}")


@client.command()
async def cuddle(ctx):
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res["url"])
    await ctx.send(embed=em)


@client.command()
async def hello(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/741236889394085954/1013625088228196463/yeah_Bounce_1.webm"
    )


@client.command()
async def jojo(ctx):
    await ctx.send("https://c.tenor.com/xEqrBmCJjPoAAAAC/jojo-u-got-that.gif")


@client.command()
async def hmm(ctx):
    await ctx.message.author.send("Zaby F Tezk ya 5awal")


@client.command()
async def bestie(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/848138223498428416/1014603064377872504/unknown.png"
    )


@client.command()
async def simp(ctx):
    num = [
        "https://cdn.discordapp.com/attachments/1005660277284556840/1010902562171531344/unknown.png",
        "https://cdn.discordapp.com/attachments/1005660277284556840/1011333473191067728/unknown.png",
        "https://cdn.discordapp.com/attachments/697977423991668846/1008370099645841438/unknown.png",
        "https://cdn.discordapp.com/attachments/684380643941154839/1014612991003602964/unknown.png",
        "https://cdn.discordapp.com/attachments/684380643941154839/1014613234583621762/unknown.png",
        "https://cdn.discordapp.com/attachments/707709742658617356/953470513009815593/unknown.png",
        "https://cdn.discordapp.com/attachments/684380643941154839/1014626477305769985/unknown.png",
    ]

    await ctx.send(f"{random.choice(num)}")


@client.command()
async def avatar(ctx, *, avamember: discord.Member):
    userAvatarUrl = avamember.avatar.url
    await ctx.send(userAvatarUrl)


@client.command()
async def basel(ctx):
    x = 0
    while x < 5:
        await ctx.message.author.send("ابو الاطفال")
        x += 1


# @client.event
# async def on_message(message):
# if message.author in black_list: # craete a black_list for **bot** (must be Iterator)
# await message.author.kick()
load_dotenv()

keep_alive()

client.run(os.getenv("TOKEN"))
