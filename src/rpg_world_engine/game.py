import rpg_world_engine as rpg


def get_starting_game_state(world_model, inventory={}):
    return {
        "world": world_model,
        "inventory": inventory
    }
