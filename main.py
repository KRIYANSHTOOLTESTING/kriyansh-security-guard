import os
import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Bot टोकन (Render.com के Environment Variables से लेगा)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB = os.getenv("MONGO_DB")  # MongoDB यूआरएल

# Pyrogram क्लाइंट इनिशियलाइज़ करें
app = Client("KriyanshBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ---------------------- मॉडरेशन कमांड्स ----------------------
@app.on_message(filters.command("ban"))
async def ban_user(_, msg: Message):
    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        await msg.chat.ban_member(user_id)
        await msg.reply(f"🚫 {user_id} को बैन कर दिया गया!")

@app.on_message(filters.command("unban"))
async def unban_user(_, msg: Message):
    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        await msg.chat.unban_member(user_id)
        await msg.reply(f"✅ {user_id} को अनबैन कर दिया गया!")

# ---------------------- एंटरटेनमेंट फीचर्स ----------------------
@app.on_message(filters.command("meme"))
async def send_meme(_, msg: Message):
    memes = [
        "https://telegra.ph/file/meme1.jpg",
        "https://telegra.ph/file/meme2.jpg",
    ]
    await msg.reply_photo(random.choice(memes))

@app.on_message(filters.command("love"))
async def love_calc(_, msg: Message):
    if msg.reply_to_message:
        user = msg.reply_to_message.from_user
        love_percent = random.randint(0, 100)
        await msg.reply(f"💖 {user.mention} के साथ प्यार {love_percent}% है!")

# ---------------------- AI चैट (ChatGPT स्टाइल) ----------------------
@app.on_message(filters.command("ai"))
async def ai_chat(_, msg: Message):
    query = msg.text.split(" ", 1)[1]
    response = f"🤖 AI: {query} का जवाब यहाँ आएगा..."
    await msg.reply(response)

# ---------------------- स्टार्ट कमांड ----------------------
@app.on_message(filters.command("start"))
async def start(_, msg: Message):
    await msg.reply(
        "✨ **बवाल बॉट** में आपका स्वागत है!\n"
        "मालिक: @KRIYANSH_CHOUDHARY\n\n"
        "कमांड्स:\n"
        "/ban - यूजर को बैन करे\n"
        "/meme - मजेदार मेमे भेजे\n"
        "/ai [सवाल] - AI से बात करें",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("मालिक", url="https://t.me/KRIYANSH_CHOUDHARY")]
        ])
    )

# ---------------------- बॉट रन करें ----------------------
print("बॉट स्टार्ट हो रहा है...")
app.run()
