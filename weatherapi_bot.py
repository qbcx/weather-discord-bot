import os
import discord
from discord import app_commands
from discord.ext import commands
import requests
from dotenv import load_dotenv
from datetime import datetime

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

def get_today_weather(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=yes"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return f"⚠️ Could not fetch today's weather for **{city}**."

        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        region = data["location"]["region"]
        localtime = data["location"]["localtime"]
        
        current = data["current"]
        temp_c = current["temp_c"]
        temp_f = current["temp_f"]
        condition = current["condition"]["text"]
        feelslike_c = current["feelslike_c"]
        feelslike_f = current["feelslike_f"]
        humidity = current["humidity"]
        wind_kph = current["wind_kph"]
        wind_dir = current["wind_dir"]
        pressure_mb = current["pressure_mb"]
        uv = current["uv"]
        vis_km = current["vis_km"]
        
        # Air quality data (if available)
        aqi_text = ""
        if "air_quality" in data:
            aqi = data["air_quality"]
            co = aqi.get("co", 0)
            no2 = aqi.get("no2", 0)
            o3 = aqi.get("o3", 0)
            pm2_5 = aqi.get("pm2_5", 0)
            pm10 = aqi.get("pm10", 0)
            aqi_text = f"\n\n**🌬️ Air Quality:**\n"
            aqi_text += f"• CO: {co:.1f} μg/m³\n• NO₂: {no2:.1f} μg/m³\n• O₃: {o3:.1f} μg/m³\n"
            aqi_text += f"• PM2.5: {pm2_5:.1f} μg/m³\n• PM10: {pm10:.1f} μg/m³"

        return (
            f"**🌤️ Today's Weather for {location}, {region}, {country}**\n"
            f"📅 Local time: {localtime}\n\n"
            f"**🌡️ Temperature:**\n"
            f"• Current: {temp_c}°C ({temp_f}°F)\n"
            f"• Feels like: {feelslike_c}°C ({feelslike_f}°F)\n\n"
            f"**☁️ Conditions:**\n"
            f"• Weather: {condition}\n"
            f"• Humidity: {humidity}%\n"
            f"• Visibility: {vis_km} km\n\n"
            f"**💨 Wind:**\n"
            f"• Speed: {wind_kph} km/h\n"
            f"• Direction: {wind_dir}\n\n"
            f"**📊 Other:**\n"
            f"• Pressure: {pressure_mb} mb\n"
            f"• UV Index: {uv}\n"
            f"{aqi_text}"
        )
    except Exception as e:
        return f"❌ Error fetching today's weather: {e}"

def get_weekly_forecast(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=7&aqi=no&alerts=no"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"⚠️ Could not fetch weekly forecast for **{city}**."

        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        region = data["location"]["region"]
        
        forecast_days = data["forecast"]["forecastday"]
        
        result = f"**📅 7-Day Forecast for {location}, {region}, {country}**\n\n"
        
        for day in forecast_days:
            date = day["date"]
            day_data = day["day"]
            
            max_temp = day_data["maxtemp_c"]
            min_temp = day_data["mintemp_c"]
            condition = day_data["condition"]["text"]
            rain_chance = day_data["daily_chance_of_rain"]
            snow_chance = day_data["daily_chance_of_snow"]
            max_wind = day_data["maxwind_kph"]
            humidity = day_data["avghumidity"]
            uv = day_data["uv"]
            
            # Convert date to more readable format
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            day_name = date_obj.strftime("%A")
            formatted_date = date_obj.strftime("%b %d")
            
            result += f"**{day_name}, {formatted_date}**\n"
            result += f"🌡️ {min_temp}°C - {max_temp}°C\n"
            result += f"☁️ {condition}\n"
            
            if rain_chance > 0:
                result += f"🌧️ Rain: {rain_chance}%\n"
            if snow_chance > 0:
                result += f"❄️ Snow: {snow_chance}%\n"
                
            result += f"💨 Wind: {max_wind} km/h | 💧 Humidity: {humidity}% | ☀️ UV: {uv}\n\n"
        
        return result
        
    except Exception as e:
        return f"❌ Error fetching weekly forecast: {e}"

# === Slash commands ===
@tree.command(name="weather", description="Get current weather for a city")
@app_commands.describe(city="Enter the city name")
async def weather(interaction: discord.Interaction, city: str):
    try:
        await interaction.response.defer(thinking=True)  # keep interaction alive
        reply = get_weather(city)
        await interaction.followup.send(reply)
    except Exception as e:
        await interaction.followup.send(f"❌ Unexpected error: {e}")

@tree.command(name="today", description="Get detailed weather for today")
@app_commands.describe(city="Enter the city name")
async def today(interaction: discord.Interaction, city: str):
    try:
        await interaction.response.defer(thinking=True)  # keep interaction alive
        reply = get_today_weather(city)
        await interaction.followup.send(reply)
    except Exception as e:
        await interaction.followup.send(f"❌ Unexpected error: {e}")

@tree.command(name="weekly", description="Get 7-day weather forecast")
@app_commands.describe(city="Enter the city name")
async def weekly(interaction: discord.Interaction, city: str):
    try:
        await interaction.response.defer(thinking=True)  # keep interaction alive
        reply = get_weekly_forecast(city)
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
