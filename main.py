from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

print("API key loaded:", bool(api_key))
print("Database URL loaded:", bool(database_url))