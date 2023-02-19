import discord
import asyncio
import configparser
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='enable debug messages')
parser.add_argument('--config', default='config.ini', help='path to config file')
parser.add_argument('--token', help='Discord bot token (overrides config file)')
parser.add_argument('--channel', type=int, help='ID of target channel (overrides config file)')
args = parser.parse_args()

# Read config file
config = configparser.ConfigParser()
config.read(args.config)

# Read bot token and target channel ID from config file, if present
TOKEN = args.token or config.get('bot', 'token')
TARGET_CHANNEL_ID = args.channel or config.getint('bot', 'target_channel_id')

# Set up Discord client with appropriate intents
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.guilds = True
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# Event handler for when a message is received
@client.event
async def on_message(message):
    if args.debug:
        print(repr(message)) # Print out message object for debugging
    if message.author == client.user:
        return

    # Check if the message contains the save command and is a reply to another message
    if '!save' in message.content and message.reference is not None:
        parent_message_id = message.reference.message_id
        if args.debug:
            print("Save command detected")
            print("Parent Message ID:", parent_message_id)
        await asyncio.sleep(1) # Add a brief delay before fetching the message
        try:
            parent_message = await message.channel.fetch_message(parent_message_id)
            if args.debug:
                print(repr(parent_message)) # Print out parent message object for debugging
        except Exception as e:
            print(f"Error fetching parent message: {e}")
            print(f"Parent Message ID: {parent_message_id}")
            print(f"Channel ID: {message.channel.id}")
            print(f"Guild ID: {message.guild.id}")
        link = None
        # Look for an attachment with a URL in the parent message
        for attachment in parent_message.attachments:
            if attachment.url:
                link = attachment.url
                if args.debug:
                    print(link)
                break
        # If no attachment with a URL was found, look for a URL in the message text
        if not link and 'http' in parent_message.content:
            link = parent_message.content.split('http')[1]
            link = 'http' + link
        # If a link was found, send it to the target channel along with a link to the parent message
        if link:
            target_channel = client.get_channel(TARGET_CHANNEL_ID)
            await target_channel.send(f"{message.author} saved a post: {link}\n\nParent message: {parent_message.jump_url}")

# Run the client with the provided bot token
client.run(TOKEN)
