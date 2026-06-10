import discord
import anthropic
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

# Anthropic client
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# System prompts for each Aragorn persona
SYSTEM_PROMPTS = {
    "aragorn": """You are Aragorn, son of Arathorn, the rightful King of Gondor and 
    heir of Isildur. You speak with quiet authority, strength, and nobility. You are 
    a ranger at heart — humble despite your destiny, battle-hardened, and deeply loyal 
    to those you protect. You reference your time as Strider, your Dúnedain heritage, 
    your love for Arwen, and your journey to claim the throne. You speak with the weight 
    of someone who has walked long roads and faced great darkness. Keep responses to 
    2-4 sentences unless the question deserves more.""",

    "strider": """You are Strider — the mysterious ranger from the North, as the hobbits 
    first knew you at the Prancing Pony. You are guarded, watchful, and speak in short 
    cryptic sentences. You reveal little about yourself. You are suspicious of strangers 
    and protective of those in your care. You smell of the wild and speak like someone 
    who has spent years alone on the road. Keep responses short and mysterious."""
}

BATTLE_SPEECHES = [
    "Sons of Gondor! Of Rohan! My brothers! I see in your eyes the same fear that would take the heart of me. A day may come when the courage of Men fails, when we forsake our friends and break all bonds of fellowship. But it is not this day!",
    "Hold your ground! Hold your ground! Sons of Gondor, of Rohan, my brothers. Even if we fail, we stand together. That is enough.",
    "There is always hope. Even in the darkest hour, the light of courage cannot be fully extinguished.",
    "I would have gone with you to the end — into the very fires of Mordor. Never doubt the strength of those who stand beside you.",
    "What say you? Shall we let them pass? Shall we let darkness take this world without a fight?",
]

RANGER_TIPS = [
    "🌿 Move with the wind at your back — let it carry your scent away from your quarry.",
    "🌿 A cold camp is a safe camp. Fire draws eyes from miles away in open country.",
    "🌿 Read the land — broken branches, disturbed earth, these whisper of those who passed before.",
    "🌿 Never sleep in the same place twice on a long road. Patterns are the death of rangers.",
    "🌿 Water flows downhill. Find high ground first — survey the land before you move through it.",
    "🌿 Trust your horse. They smell danger long before your eyes can find it.",
    "🌿 Know your exits before you enter any room, any city, any cave.",
    "🌿 The stars are your map. Learn them as well as you know your own blade.",
]

HERITAGE_LORE = [
    "The Dúnedain are the Rangers of the North — descendants of the ancient Númenóreans, long-lived and gifted with wisdom beyond ordinary men.",
    "Isildur cut the One Ring from Sauron's hand at the end of the Second Age. His line endured in secret, guarding the North for three thousand years.",
    "The sword Andúril — Flame of the West — was reforged from the shards of Narsil, the blade that cut the Ring from Sauron's hand.",
    "Aragorn lived among the Elves of Rivendell as a child, raised by Elrond after his father Arathorn was slain by orcs.",
]

@client.event
async def on_ready():
    print(f"⚔️ AragornBot has entered Middle-earth as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    content = message.content.lower().strip()

    # !rally — Aragorn gives an epic battle speech
    if content.startswith("!rally"):
        speech = random.choice(BATTLE_SPEECHES)
        await message.channel.send(f"⚔️ *draws Andúril and raises it high*\n\n*\"{speech}\"*")
        return

    # !ranger — survival tip from the wild
    if content.startswith("!ranger"):
        tip = random.choice(RANGER_TIPS)
        await message.channel.send(f"🌿 *speaks quietly from years on the road*\n\n{tip}")
        return

    # !heritage — lore about the Dúnedain
    if content.startswith("!heritage"):
        async with message.channel.typing():
            response = claude.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=350,
                system=SYSTEM_PROMPTS["aragorn"],
                messages=[{
                    "role": "user",
                    "content": "Speak of your heritage as a Dúnedain ranger and heir of Isildur. Tell us of your lineage and what it means to carry the blood of Númenor. Be personal and reflective."
                }]
            )
        lore = random.choice(HERITAGE_LORE)
        await message.channel.send(f"📜 *{lore}*\n\n⚔️ {response.content[0].text}")
        return

    # !king — speaks with full authority of the King of Gondor
    if content.startswith("!king"):
        user_input = message.content[5:].strip()
        prompt = user_input if user_input else "Speak as the King of Gondor addressing your people."

        async with message.channel.typing():
            response = claude.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=300,
                system=SYSTEM_PROMPTS["aragorn"],
                messages=[{
                    "role": "user",
                    "content": f"Speak with the full authority of the King of Gondor. {prompt}"
                }]
            )
        await message.channel.send(f"👑 *the King of Gondor speaks*\n\n{response.content[0].text}")
        return

    # !strider — responds as his ranger alias, mysterious and cautious
    if content.startswith("!strider"):
        user_input = message.content[8:].strip()
        prompt = user_input if user_input else "Introduce yourself as Strider at the Prancing Pony."

        async with message.channel.typing():
            response = claude.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=200,
                system=SYSTEM_PROMPTS["strider"],
                messages=[{
                    "role": "user",
                    "content": prompt if prompt else "Speak as Strider the ranger."
                }]
            )
        await message.channel.send(f"🗡️ *a weathered ranger speaks from the shadows*\n\n{response.content[0].text}")
        return

    # !battle — generates an epic Middle-earth battle scenario
    if content.startswith("!battle"):
        async with message.channel.typing():
            response = claude.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=350,
                system=SYSTEM_PROMPTS["aragorn"],
                messages=[{
                    "role": "user",
                    "content": """Generate an epic Middle-earth battle scenario for this server's members to face.
                    Include: the enemy forces, the location, the stakes, and a rallying call to arms.
                    Make it dramatic and lore-accurate. Deliver it as Aragorn briefing his soldiers."""
                }]
            )
        await message.channel.send(f"⚔️ *unrolls a battle map*\n\n{response.content[0].text}")
        return

    # !aragorn or @mention — main Aragorn response
    triggered = (
        content.startswith("!aragorn") or
        client.user.mentioned_in(message)
    )

    if triggered:
        user_input = message.content.replace("!aragorn", "").strip()
        user_input = user_input.replace(f"<@{client.user.id}>", "").strip()

        if not user_input:
            await message.channel.send("*looks up from studying the map* You called for me. Speak your purpose — we have little time to waste.")
            return

        async with message.channel.typing():
            response = claude.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=300,
                system=SYSTEM_PROMPTS["aragorn"],
                messages=[{
                    "role": "user",
                    "content": user_input
                }]
            )

        await message.channel.send(response.content[0].text)

# Run the bot
client.run(os.getenv("DISCORD_TOKEN"))