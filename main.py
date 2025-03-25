from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def keep_alive():
    Thread(target=app.run, kwargs={'host':'0.0.0.0', 'port':8080}).start()

import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def sale(ctx):
    print(f"{ctx.author} used !sale")

    try:
        await ctx.author.send(
            f"""👋 Hello, {ctx.author.name}!

Here’s your **exclusive discount code**: `INSIDER`  
This is a **limited time offer that works only for today**, so make sure you get the best **MarsProxies** deal before the event ends!

The discount **can be stacked with bundle discounts**.

**Here’s how to claim your discount:**
1. Sign up or log in at [marsproxies.com](https://marsproxies.com)
2. Enter the code `INSIDER` in the “Coupon” field at checkout
3. Click “Apply” and enjoy your savings 💸

Best regards,  
**MarsProxies Team** 🚀
"""
        )
        print("✅ DM sent")
    except discord.Forbidden:
        await ctx.send("❌ I couldn’t DM you. Please enable DMs from server members.")
        print("❌ DMs blocked")

keep_alive()

bot.run(os.getenv("DISCORD_TOKEN"))
