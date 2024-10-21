
import nextcord
import requests
from nextcord.ext import commands

# Set the bot intents
intents = nextcord.Intents.default()
intents.message_content = True

# Initialize the bot with slash command support
bot = commands.Bot(intents=intents)

@bot.slash_command(name="autolog", description="Upload a new blog post to the website")
async def autolog(ctx: nextcord.Interaction, message: str):
    # Send the message to your backend API (use an actual web server URL)
    api_url = "https://yourwebsite.com/autolog.php"  # Replace with your actual API URL
    data = {"message": message}
    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            await ctx.response.send_message("Blog post has been uploaded!")
        else:
            await ctx.response.send_message("Failed to upload the blog post.")
    except Exception as e:
        await ctx.response.send_message(f"Error: {e}")

# Start the bot
bot.run("MTI5Nzk2OTI5NTA4NjU4Mzk3MA.GA8Gfq.HaRA4L7s1tmO53IeeuENmGulbP-z6Je3C-w3v8")
