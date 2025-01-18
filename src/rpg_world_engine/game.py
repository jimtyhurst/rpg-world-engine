import rpg_world_engine as rpg


def get_starting_game_state(world_model, inventory={}):
    return {
        "world": world_model,
        "player": world_model["player"],
        "challenge": world_model["challenge"],
        "inventory": inventory
    }
