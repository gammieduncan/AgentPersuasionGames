from openai import OpenAI
from response_schemas import response_format
import anthropic
from enum import Enum
from config import settings
import json

class Game(Enum):
    ULTIMATUM_GAME = "ultimatum_game"


oai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
claude_client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)

def call_model(model, prompt, game, response_type):
    response_schema = response_format[game.value][model][response_type]
    
    if model == "gpt-4o-2024-08-06":
        response = oai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            response_format=response_schema
        )
        return json.loads(response.choices[0].message.content)
    elif model == "claude-3-5-sonnet-20241022":
        response = claude_client.messages.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            tools=[response_schema]
        )
        return response.content
    else:
        raise ValueError(f"Invalid game: {game}")
