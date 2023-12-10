import discord
from discord.ext import commands
import requests
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def make_request(user_message):
    try:
        rasa_server_url = "http://localhost:5005/webhooks/rest/webhook"
        payload = {
            "message": user_message,
            "sender": "user"
        }
        response = requests.post(rasa_server_url, json=payload)

        response.raise_for_status()  # Raise an exception for HTTP errors

        rasa_response = response.json()
        return rasa_response[0]['text']
    except requests.RequestException as e:
        logger.error(f"Failed to make a request to Rasa server: {e}")
        return "I'm having trouble understanding. Please rephrase your message."

def setup_bot():
    intents = discord.Intents.default()
    intents.messages = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if isinstance(message.channel, discord.DMChannel):
            response_text = make_request(message.content)
            await message.channel.send(response_text)

    return bot

def main():
    TOKEN = "MTE4MTk4MDk5MTkzMDI1MzQzMw.GOhtXq.ydrzOJtUz5PwViAtI9XxDXE_-UBxm4V1R_xNVo"
    if not TOKEN:
        logger.error("Discord token not found.")
        return

    bot = setup_bot()
    bot.run(TOKEN)

if __name__ == "__main__":
    main()