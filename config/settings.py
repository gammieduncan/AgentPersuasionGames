import os
from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_file)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
