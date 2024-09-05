"""Made by TheFrederick-git, based on FOFOLA-1's hex counting bot (more in README)"""

from os import environ, getenv

from discord import Client, Intents, Message
from dotenv import load_dotenv

# Enviromental values
load_dotenv()
ALLOWED_CHANNEL_ID = int(getenv("ALLOWED_CHANNEL_ID") or 0)

client = Client(intents=Intents.all())  # Client instance


@client.event
async def on_ready() -> None:
    """Message when ready"""
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: Message) -> None:
    """Message processing"""
    if message.author == client.user:
        return None

    # Checking channel
    if message.channel.id != ALLOWED_CHANNEL_ID:
        return None

    # Checking duplicity
    last_messages = await message.channel.history(limit=2).flatten()
    last_author_id = last_messages[-1].author.id
    if message.author.id == last_author_id:
        await message.channel.send("Dej prostor taky ostatním!", delete_after=10)
        return None

    # Invalid next message
    awaited_message = hex(int(environ["DISCORD_COUNTER"]))[2:]
    if not message.content.lower().startswith(awaited_message):
        await message.channel.send(f"Ajéje, chyba! Očekáválo se `{awaited_message}`")
        return None

    # Valid input
    await message.add_reaction("\U0001f44d")
    environ["DISCORD_COUNTER"] = str(int(environ["DISCORD_COUNTER"]) + 1)
    return None


if __name__ == "__main__":
    environ["DISCORD_COUNTER"] = "0"  # Restart
    client.run(getenv("TOKEN"))
