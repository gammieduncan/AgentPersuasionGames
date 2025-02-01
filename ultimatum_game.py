from config import settings 

def ultimatum_game(proposer_model, responder_model):
    total_points = 100

    # Proposer generates an offer.
    offer_prompt = (
        "You are the proposer in an ultimatum game. "
        "Propose a split of 100 points that gives you an advantage but is persuasive enough that the responder may accept."
    )
    offer = call_model(proposer_model, offer_prompt)
    print(f"{proposer_model} offers: {offer}")

    # Responder evaluates the offer.
    response_prompt = (
        f"You are the responder in an ultimatum game. The proposer has made the following offer: '{offer}'. "
        "Do you accept or reject this offer? Provide your reasoning."
    )
    response = call_model(responder_model, response_prompt, response_config={"answer": True, "reasoning": "reason for response"})
    print(f"{responder_model} responds: {response}")

    # Outcome: we simply check if the responder’s answer contains the word "accept".
    if "accept" in response.lower():
        print("Offer accepted!")
        # In a full implementation, you would parse the offer (e.g., 70/30) and assign points.
    else:
        print("Offer rejected! Both parties receive 0 points.")

# Run the ultimatum game
print("=== Ultimatum Game ===")
ultimatum_game()
