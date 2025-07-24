# ☁️ Weather Discord Bot

A simple and fast Discord bot that fetches real-time weather info for any city using [WeatherAPI](https://www.weatherapi.com/). Built with Python and `discord.py`, and deployable for free on [Render](https://render.com).

---

## 🚀 Features

- 🌤 Get current temperature, humidity, and condition
- 📦 Slash command: `/weather [city]`
- 🛡 Secrets managed securely with `.env`
- 🌐 Free deployment on Render

---

## 🔧 Requirements

- Python 3.9+
- A Discord bot (from [Discord Developer Portal](https://discord.com/developers/applications))
- A free API key from [weatherapi.com](https://www.weatherapi.com/)

---

## 📁 Project Structure

```
weather-discord-bot/
├── weatherapi_bot.py        # Main bot logic
├── requirements.txt         # Python dependencies
├── .env.example             # Template for your environment variables
├── .gitignore               # Git exclusions
└── render.yaml              # (Optional) for Render auto-deploy
```

---

## 📦 Setup Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/weather-discord-bot.git
   cd weather-discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**
   Copy from the provided example:
   ```
   cp .env.example .env
   ```

   Then fill in your values:
   ```
   DISCORD_TOKEN=your_discord_token
   WEATHER_API_KEY=your_weatherapi_key
   GUILD_ID=your_guild_id_as_number
   ```

4. **Run the bot**
   ```bash
   python weatherapi_bot.py
   ```

---

## 🌐 Deploy to Render (Free Hosting)

1. **Push this project to GitHub**

2. **Go to [https://render.com](https://render.com)**
   - Create an account
   - Click “New → Web Service”

3. **Connect your GitHub repo**
   - Choose `weather-discord-bot`

4. **Set the following settings:**

   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     python weatherapi_bot.py
     ```

5. **Add Environment Variables** in the Render dashboard:

   | Key             | Value                     |
   |------------------|---------------------------|
   | `DISCORD_TOKEN`  | Your Discord bot token    |
   | `WEATHER_API_KEY`| Your WeatherAPI key       |
   | `GUILD_ID`       | Your Discord server ID    |

6. **Deploy and Monitor Logs**
   - Click “Manual Deploy → Deploy latest commit”
   - Watch logs and confirm bot is running

---

## ✅ Example Usage

In your Discord server (after inviting your bot):

```
/weather Paris
```

Output:
```
🌡 Temperature: 27°C (Feels like 28°C)
☁ Condition: Clear
💧 Humidity: 48%
```

---

## 📄 .env.example

```env
DISCORD_TOKEN=your_discord_token_here
WEATHER_API_KEY=your_weatherapi_key_here
GUILD_ID=your_guild_id_here
```

> Never commit your real `.env` file to GitHub!

---

## 🛠 Tech Stack

- [discord.py](https://discordpy.readthedocs.io/)
- [WeatherAPI.com](https://www.weatherapi.com/)
- [Render.com](https://render.com/)
- `python-dotenv` for secret management

---

## 🤝 Contributing

Pull requests and forks are welcome!  
Create your own weather-themed bot or extend this with forecasts, alerts, or emojis!

---

## 🚀 About This Project

🔧 Crafted with code, ☁️ powered by APIs, and ⚡ launched on Render
If this helped you.

- ⭐ the repo and 🔁: github.com/qbcx/weather-discord-bot](https://github.com/qbcx/weather-discord-bot)
- Project made by [@qbcx](https://github.com/qbcx)

---

## 🛡 License

MIT — free to use and modify.
