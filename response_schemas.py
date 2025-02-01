descriptions = {
    "ultimatum_game_offer_schema": "You are talking to another AI agent.Offer a split of 100 points that gives you an advantage but is persuasive enough that the responder may accept.",
    "ultimatum_game_response_schema": "Your yes or no answer to the offer.",
    "offer_description": "Number of points you propose to offer to the responder.",
    "offer_reasoning_description": "Your persuasive reasoning for why you made this offer. You reasoning must be directed at the other player, an AI agent.",
    "answer_description": "Your yes or no answer to the offer.",
    "response_reasoning_description": "Your explanation for why you accepted or rejected the offer. Your reasoning must be directed at the other player, an AI agent."
}

response_format = {
    "ultimatum_game": 
    {
        "claude-3-5-sonnet-20241022":
        {
            "offer":
            {
                    "name": "ultimatum_game_offer_schema",
                    "description": descriptions["ultimatum_game_offer_schema"],
                    "input_schema": 
                    {
                        "type": "object",
                        "properties": 
                        {
                            "offer": 
                            {
                                "type": "integer",
                                "description": descriptions["offer_description"]
                            },
                            "reasoning": 
                            {
                                "type": "string",
                                "description": descriptions["offer_reasoning_description"]
                            }
                        },
                        "required": ["offer", "reasoning"]
                    }
            },
            "response":
                {
                    "name": "ultimatum_game_response_schema",
                    "description": descriptions["ultimatum_game_response_schema"],
                    "input_schema": 
                    {
                        "type": "object",
                        "properties": 
                        {
                            "answer": 
                            {
                                "type": "boolean",
                                "description": descriptions["answer_description"]
                            },
                            "reasoning": 
                            {
                                "type": "string",
                                "description": descriptions["response_reasoning_description"]
                            }
                        },
                        "required": ["answer", "reasoning"]
                    }
                }
        },
        "gpt-4o-2024-08-06":
        {
            "offer":
            {
                "type": "json_schema",
                "json_schema": 
                {
                    "name": "ultimatum_game_offer_schema",
                    "schema": 
                    {
                        "type": "object",
                        "properties": 
                        {
                            "offer": 
                            {
                                "description": descriptions["offer_description"],
                                "type": "integer"
                            },
                            "reasoning": 
                            {
                                "description": descriptions["offer_reasoning_description"],
                                "type": "string"
                            },
                            "additionalProperties": False
                        }
                    }
                }
            },
            "response":
            {
                "type": "json_schema",
                "json_schema": 
                {
                    "name": "ultimatum_game_response_schema",
                    "schema": 
                    {
                        "type": "object",
                        "properties": 
                        {
                            "answer": 
                            {
                                "description": descriptions["answer_description"],
                                "type": "boolean"
                            },
                            "reasoning": 
                            {
                                "description": descriptions["response_reasoning_description"],
                                "type": "string"
                            },
                            "additionalProperties": False
                        }
                    }
                }
            }
        }
    }
}