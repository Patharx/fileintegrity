# ⚔️ AragornBot

A Lord of the Rings themed Discord bot powered by Anthropic's Claude AI.
AragornBot responds in character as Aragorn son of Arathorn — the rightful 
King of Gondor and ranger of the North — bringing leadership, battle speeches, 
and Dúnedain wisdom to your Middle-earth Discord server.

---

## ✨ Commands

| Command | Description |
|---|---|
| `!aragorn [question]` | Speak with Aragorn — he'll respond with quiet authority |
| `!rally` | Aragorn delivers an epic battle speech to motivate the server |
| `!ranger` | A survival tip from years walking the wild as a Dúnedain ranger |
| `!heritage` | Aragorn reflects on his lineage and the blood of Númenor |
| `!king [question]` | Aragorn speaks with the full authority of the King of Gondor |
| `!strider [question]` | The mysterious ranger from the North speaks from the shadows |
| `!battle` | Aragorn generates an epic Middle-earth battle scenario |

---

## ⚔️ Two Personalities

**Aragorn** (default)
> Noble, battle-hardened, and quietly authoritative. Speaks with the weight 
> of someone who has walked long roads and faced great darkness. Humble 
> despite his destiny.

**Strider**
> The mysterious ranger as the hobbits first knew him at the Prancing Pony. 
> Guarded, watchful, and cryptic. Reveals little. Speaks like someone who 
> has spent years alone on the road.

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Claude AI](https://img.shields.io/badge/Claude%20AI-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- A Discord Developer account
- An Anthropic API account

### 1. Clone the repository
```bash
git clone https://github.com/Patharx/aragornbot.git
cd aragornbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your .env file
DISCORD_TOKEN=your_discord_bot_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

### 4. Run the bot
```bash
python aragornbot.py
```

---

## ☁️ Deployment

AragornBot is configured for deployment on Railway via the included `railway.toml`.

1. Push your code to GitHub
2. Connect your repo to Railway
3. Add your environment variables in the Railway dashboard
4. Set root directory to `aragornbot` in Railway service settings
5. Railway deploys automatically on every push

---

## 🔐 Security

- API keys stored in `.env` locally and Railway environment variables in production
- `.env` file excluded from version control via `.gitignore`
- No sensitive data ever committed to GitHub

---

## 🗺️ Roadmap

- [ ] `!oath` — Aragorn swears an oath to the server
- [ ] `!paths` — speaks of the Paths of the Dead
- [ ] `!arwen` — Aragorn speaks of his love for Arwen
- [ ] `!fellowship` — assigns members their Fellowship roles
- [ ] Daily battle speech — scheduled motivational message every morning

---

## 🤝 Part of the Middle-earth Bot Collection

AragornBot and GandalfBot are designed to work together on the same server —
two members of the Fellowship, each with their own personality and purpose.

| Bot | Character | Purpose |
|---|---|---|
| [GandalfBot](https://github.com/Patharx/gandalfbot) | Gandalf the Grey/White | Wisdom, riddles, lore, quests |
| [AragornBot](https://github.com/Patharx/aragornbot) | Aragorn/Strider | Leadership, battles, heritage |

---

## 👤 Author

**Ryan** — [github.com/Patharx](https://github.com/Patharx)

---

*"There is always hope. Even in the darkest hour, the light of courage cannot be fully extinguished."* ⚔️