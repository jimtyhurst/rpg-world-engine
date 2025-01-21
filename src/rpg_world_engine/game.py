from rpg_world_engine import policy


def get_starting_game_state(world_model, game_scenario, inventory=None):
    if inventory is None:
        inventory = {}
    return {
        "title": game_scenario["title"],
        "world": world_model,
        "player": world_model["player"],
        "challenge": game_scenario["challenge"],
        "age_appropriate_rating": policy.AgeAppropriateRating(game_scenario["age_appropriate_rating"]),
        "inventory": inventory,
    }
