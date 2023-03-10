import discord
import youtube_dl

#insert your discord bot token here
TOKEN = "YOUR_DISCORD_BOT_TOKEN"

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    if message.content.startswith("!play"):
        query = message.content[6:]
        voice_channel = message.author.voice.channel
        await voice_channel.connect()
        await play_music(query, voice_channel)

async def play_music(query, voice_channel):
    ydl_opts = {"format": "bestaudio"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        url = info["url"]
        source = await discord.FFmpegOpusAudio.from_probe(url)
        voice_client = await voice_channel.connect()
        voice_client.play(source)

client.run(TOKEN)