import os
import discord
from discord import app_commands
from discord.ext import commands
import requests
from dotenv import load_dotenv

# Load .env for local use
load_dotenv()

# === Load environment variables safely ===
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GUILD_ID_RAW = os.getenv("GUILD_ID")

if not DISCORD_TOKEN:
    raise RuntimeError("🚨 DISCORD_TOKEN is not set!")
if not WEATHER_API_KEY:
    raise RuntimeError("🚨 WEATHER_API_KEY is not set!")
if not GUILD_ID_RAW:
    raise RuntimeError("🚨 GUILD_ID is not set!")

GUILD_ID = int(GUILD_ID_RAW)

# === Discord bot setup with proper intents ===
intents = discord.Intents.default()
intents.message_content = True  # Required for message-based commands (even if unused)
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# === Weather API logic ===
def get_weather(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    try:
        response = requests.get(url, timeout=5)
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
    except Exception as e:
        return f"❌ Error fetching weather: {e}"

# === Slash command ===
@tree.command(name="weather", description="Get current weather for a city")
@app_commands.describe(city="Enter the city name")
async def weather(interaction: discord.Interaction, city: str):
    try:
        await interaction.response.defer(thinking=True)  # keep interaction alive
        reply = get_weather(city)
        await interaction.followup.send(reply)
    except Exception as e:
        await interaction.followup.send(f"❌ Unexpected error: {e}")

# === on_ready: sync slash command ===
@bot.event
async def on_ready():
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} command(s) to server {guild.id}")
        print(f"🤖 Logged in as {bot.user}")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

# === Run the bot ===
bot.run(DISCORD_TOKEN)
