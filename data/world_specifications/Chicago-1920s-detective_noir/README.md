README

These prompts were created manually as I was experimenting with prompt
styles.

The ultimate goal is to parameterize the prompts, so that anyone can create
a new world easily by supplying a small amount of information about the world.
Then the series of prompts will be used with the LLM API to create a world,
regions, and locales hierarchically. So we start at the level of the _world_,
then generate _regions_ in that world, then for each region, generate some
_locales_.
