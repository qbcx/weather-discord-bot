# ☁️ Weather Discord Bot

A simple and fast Discord bot that fetches real-time weather info for any city using [WeatherAPI](https://www.weatherapi.com/).  
Built with Python and `discord.py`, and deployable for **free** on [Railway](https://railway.app).

---

## 🚀 Features

- 🌤 Slash command: `/weather [city]`
- 🌡 Current temperature, humidity, and condition
- 🔐 Secure secrets via `.env` or Railway variables
- ⚡ Hosted for free using Railway (no port required)

---

## 🧱 Requirements

- Python 3.9+
- Discord bot from [discord.com/developers](https://discord.com/developers/applications)
- WeatherAPI key from [weatherapi.com](https://www.weatherapi.com/)

---

## 🗂 Project Structure

```
weather-discord-bot/
├── weatherapi_bot.py        # Main bot logic
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
└── README.md                # Project documentation
```

---

## 💻 Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/weather-discord-bot.git
   cd weather-discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**
   ```env
   DISCORD_TOKEN=your_discord_token
   WEATHER_API_KEY=your_weatherapi_key
   GUILD_ID=your_guild_id_as_number
   ```

4. **Run the bot**
   ```bash
   python weatherapi_bot.py
   ```

---

## 🌐 Deploy to Railway (Recommended – Free)

1. Go to [https://railway.app](https://railway.app)

2. Click **“New Project” → “Deploy from GitHub Repo”**

3. Choose your `weather-discord-bot` repo

4. Under the **Variables tab**, add:

   | Key              | Value                      |
   |------------------|----------------------------|
   | `DISCORD_TOKEN`  | Your Discord bot token     |
   | `WEATHER_API_KEY`| Your WeatherAPI key        |
   | `GUILD_ID`       | Your Discord server ID     |

5. Under **Settings**, change the Start Command to:

   ```bash
   python weatherapi_bot.py
   ```

6. Click **"Deploy"** and check the logs for successful startup.

---

## 💬 Example Usage

```
/weather Tokyo
```

```
**Weather for Tokyo, Japan**
🌡 Temperature: 27°C (Feels like 29°C)
💧 Humidity: 60%
☁ Condition: Clear
```

---

## 🧪 .env.example

```env
DISCORD_TOKEN=your_discord_token_here
WEATHER_API_KEY=your_weatherapi_key_here
GUILD_ID=your_guild_id_here
```

> ⚠️ Do not commit your real `.env` file.

---

## 🛠 Tech Stack

- [`discord.py`](https://discordpy.readthedocs.io/)
- [`weatherapi.com`](https://www.weatherapi.com/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [Railway](https://railway.app) for hosting

---

## 🤝 Contributing

Forks and pull requests are welcome!

---

## 📜 License

MIT — free to use and modify

---

## 👤 Author

Created by [@qbcx](https://github.com/qbcx)
