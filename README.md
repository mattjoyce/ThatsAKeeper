# Discord Bot

This is a Discord bot that listens for the "!save" command in a message and saves the parent message's link to a specified channel. The bot is built using Python and the `discord.py` library.

## Prerequisites

- Python 3.x
- `pip`
- A Discord account with the ability to create bots

## Installation

1. Clone this repository: `git clone https://github.com/<username>/discord-bot.git`
2. Create a virtual environment for the project: `python -m venv env`
3. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate.bat` (Windows)
4. Install the `discord.py` library: `pip install discord`
5. Create a bot in the Discord Developer Portal: [https://discord.com/developers/applications](https://discord.com/developers/applications)
6. Add the bot to your Discord server using the "OAuth2" tab in the Developer Portal. Make sure to give it the necessary permissions (e.g. "Read Message History", "Send Messages", "Attach Files").
7. Copy the bot token from the "Bot" tab in the Developer Portal and paste it into the `config.ini` file.
8. Determine the ID of the channel you want to send messages to, and add it to the `config.ini` file.

## Configuration

- `config.ini`: This file contains the bot token and target channel ID. The bot token is required to authenticate the bot with Discord. The target channel ID is the ID of the channel where the bot will post messages. Both values can be obtained from the Discord Developer Portal. See the example `config.ini` file for more information.

## Usage

To start the bot, run the following command in your terminal:

