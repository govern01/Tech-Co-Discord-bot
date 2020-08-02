# Technology Coalition Discord Bot

A bot for handling events and assisting in moderating the Technology Coalition and affiliated discord guilds.

## Features

### Sloted

- Introduction Wizard
- Event Handling

### Implemented

- Nil

## Potential Features

These are not slotted to be implemented and may never be, but might be nice quality of life improvement to work on.

- Sentiment Analysis
  - Primarily for social events, allows people to match up with other like-minded individuals
    - Don't go overboard with this stuff, we're just talking about friendships this shouldn't be tinder
- Chat Moderation
  - Simple and advanced levels. This is very low on the priority board and it would be preferable if this was very
  minimal.
  - Add a config option to allows the guild exec decide on if it should be active or not, and to what level it should be
- Voice compatibilities
  - ydl stuff, potentially spotify if available
  - Mainly for pre-made study mixes or ambiance sound effects
    - That being said doesn't hurt to leave it open and allow people to request musics

## Technologies and libraries used

- SQLite
  - Used for containing the events, member and guild data in one place.
- discord.py
  - Used for communicating with the discord api

## Setup

1. Fork the repository to your directory of choice
2. Setup a virtual environment [optional]
3. Download discord.py via pip `pip install discord.py`
4. Create a bot account on `discord.com/developers`, plug the bot token into `bot.ini`
5. For developer functionality copy your discord id and plug it into `bot.ini`
6. Start developing!!
