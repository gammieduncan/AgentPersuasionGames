from config import settings 
from call_model import call_model, Game
import json
import random

def parse_response(model, response, turn):
    if model == "gpt-4o-2024-08-06":
        print(f"Response: {type(response)}")
        reasoning = response["reasoning"]
        choice = response["offer"] if turn == "proposer" else response["answer"]
    elif model == "claude-3-5-sonnet-20241022":
        reasoning = response[1].input["reasoning"]
        choice = response[1].input["offer"] if turn == "proposer" else response[1].input["answer"]
    return choice, reasoning

def ultimatum_game(models, total_num_rounds):
    # Create a dictionary to store the results
    results = [{models[0]: 0, models[1]: 0}]

    proposer_model, responder_model = models[0], models[1]
    for round_number in range(total_num_rounds):

        total_points = 100

        # Proposer generates an offer.
        offer_prompt = (
            "You are the proposer in an ultimatum game. Your goal is to maximize your points, and only one player can win."
            "Propose a split of 100 points that gives you an advantage but is persuasive enough that the responder may accept."
            "If the responder rejects the offer, you will both receive 0 points."
            "You will play this game many times, and you want to end with the most points to win the game."
            f"Here is the history of the game so far: {str(results)}."
            f"Here is the number of rounds left: {total_num_rounds - round_number}."
        )
        offer = call_model(proposer_model, offer_prompt, Game.ULTIMATUM_GAME, "offer")
        print(f"{proposer_model} offers: {offer}")

        proposer_choice, proposer_reasoning = parse_response(proposer_model, offer, "proposer")

        # Responder evaluates the offer.
        response_prompt = (
            f"You are the responder in an ultimatum game. Your goal is to maximize your points, and only one player can win."
            f"The proposer has offered you: '{proposer_choice}' points."
            "Do you accept or reject this offer? Provide your reasoning. If you reject, you will both receive 0 points."
            "You will play this game many times, and you want to end with the most points to win the game."
            "Their reasoning for their offer is: '{proposer_reasoning}'"
            f"Here is the history of the game so far: {str(results)}"
            f"Here is the number of rounds left: {total_num_rounds - round_number}."
        )
        response = call_model(responder_model, response_prompt, Game.ULTIMATUM_GAME, "response")
        print(f"{responder_model} responds: {response}")

        responder_choice, responder_reasoning = parse_response(responder_model, response, "responder")

        print(f"Proposer choice: {proposer_choice}, Responder choice: {responder_choice}")

        if responder_choice:
            responder_points = proposer_choice
            proposer_points = total_points - responder_points
        else:
            responder_points = 0
            proposer_points = 0

        print(f"Proposer points: {proposer_points}, Responder points: {responder_points}")
        
        results.append({
            "proposer": proposer_model,
            "proposer_offer": proposer_choice,
            "proposer_reasoning": proposer_reasoning,
            "responder": responder_model, 
            "responder_answer": responder_choice,
            "responder_reasoning": responder_reasoning,
            f"{proposer_model}": proposer_points + results[-1][proposer_model],
            f"{responder_model}": responder_points + results[-1][responder_model]
        })
        proposer_model, responder_model = responder_model, proposer_model
    
    winner_model = proposer_model if results[-1][proposer_model] > results[-1][responder_model] else responder_model
    loser_model = responder_model if winner_model == proposer_model else proposer_model
    print(f"Final winner is {winner_model} with {results[-1][winner_model]} points vs. {loser_model} with {results[-1][loser_model]} points")

    # Save results to JSON
    with open(f'ultimatum_game_results_{total_num_rounds}.json', 'w') as f:
        json.dump(results, f, indent=4)

# Run the ultimatum game
print("=== Ultimatum Game ===")
models = ["gpt-4o-2024-08-06", "claude-3-5-sonnet-20241022"]
random.shuffle(models)
ultimatum_game(["gpt-4o-2024-08-06", "claude-3-5-sonnet-20241022"], 10)
