from environs import Env
env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
file_id_1 = 'AgACAgIAAxkBAAO3ZE9AiSa2aj-2nAh2PU8llsiY48QAAgfJMRsCknhK5XaK8njsm6cBAAMCAANtAAMvBA'