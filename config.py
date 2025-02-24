from os import getenv


API_ID = int(getenv("API_ID", "21567814"))
API_HASH = getenv("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = getenv("BOT_TOKEN", "7333052013:AAGPIHa-bKWgvK0XlvkMbIzIjsSjt5fJ9jk")
OWNER_ID = int(getenv("OWNER_ID", "6126688051"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002288634593"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


