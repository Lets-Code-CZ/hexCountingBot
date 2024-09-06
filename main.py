from os import environ, getenv

from discord import Client, Intents, Message
from dotenv import load_dotenv

# Enviromental values
load_dotenv()
ALLOWED_CHANNEL_ID = int(getenv("ALLOWED_CHANNEL_ID") or 0)

client = Client(intents=Intents.all())  # Client instance


@client.event
async def on_message(message: Message) -> None:
    """Message processing"""
    if message.author == client.user:
        return None

    # Checking channel
    if message.channel.id != ALLOWED_CHANNEL_ID:
        return None

    # Checking duplicity
    last_messages = await message.channel.history(limit=10).flatten()
    last_author_id = [x for x in last_messages if not x.author.bot][1].author.id
    if message.author.id == last_author_id:
        await message.channel.send("Dej prostor taky ostatním!", delete_after=10)
        return None

    # Invalid next message
    awaited_message = hex(int(environ["DISCORD_COUNTER"], 16))[2:]
    if not message.content.lower().startswith(awaited_message):
        await message.channel.send(
            f"Ajéje, chyba! Očekáválo se `{awaited_message}`", delete_after=10
        )
        return None

    # Valid input
    await message.add_reaction("\U0001f44d")
    next_val = hex(int(environ["DISCORD_COUNTER"], 16) + 1)
    environ["DISCORD_COUNTER"] = next_val
    with open("./save.txt", "w", encoding="UTF-8") as save_file:
        save_file.write(next_val)
    return None


if __name__ == "__main__":
    try:
        with open("./save.txt", "r", encoding="UTF-8") as save_file:
            environ["DISCORD_COUNTER"] = save_file.read()
    except FileNotFoundError:
        environ["DISCORD_COUNTER"] = "0"
    client.run(getenv("TOKEN"))