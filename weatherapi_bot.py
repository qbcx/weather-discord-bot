import os
import discord
from discord import app_commands
from discord.ext import commands
import requests
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

# === Secure environment variables ===
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

# === Discord bot setup ===
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# === Weather command logic ===
def get_weather(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code != 200:
        return f"⚠️ Could not fetch weather for **{city}**."

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    feelslike_c = data["current"]["feelslike_c"]
    humidity = data["current"]["humidity"]
    icon = data["current"]["condition"]["icon"]

    return (
        f"**Weather for {location}, {country}**\n"
        f"🌡 Temperature: {temp_c}°C (Feels like {feelslike_c}°C)\n"
        f"💧 Humidity: {humidity}%\n"
        f"☁ Condition: {condition}\n"
        f"[Icon](https:{icon})"
    )

@tree.command(name="weather", description="Get current weather for a city")
@app_commands.describe(city="Enter the city name")
async def weather(interaction: discord.Interaction, city: str):
    await interaction.response.defer()
    reply = get_weather(city)
    await interaction.followup.send(reply)

@bot.event
async def on_ready():
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} slash command(s) to server {guild.id}")
        print(f"🤖 Bot is ready as {bot.user}")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

bot.run(DISCORD_TOKEN)