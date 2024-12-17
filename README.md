# rpg-world-engine
Builds and runs text-based Role-Playing Games, moderated by a Large Language Model.

**Contents**

- [Overview](#overview)
- [Glossary](#glossary)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Overview

This project provides tools to:

- Generate a hierarchical RPG world model;
- Run an RPG text adventure web application that uses that model as the setting for an adventure.

The WorldModel is constructed with the help of an LLM, based on a few brief prompts from the person building the world.

The content of the adventure is produced by an LLM, using the WorldModel and RolePlayer input as context for telling a story.

## Glossary

- Adventure : A series of interactions within a world.
- Bard : An LLM in its role as facilitator of the game is responsible for:
    - telling the story;
    - managing the flow of interactions;
    - enforcing safety policies.
- GenAI : Generative AI, e.g. an application that generates text based on a given prompt.
- jailbreak : to remove built-in limitations of an LLM, e.g. nullify the enforcement of safety policies or avoid built-in guardrails.
- LLM : Large Language Model.
- NPC : Non-Playing Character, i.e. background character defined within the World Model.
- RolePlayer : human who interacts with the game.
- RPG : Role-Playing Game.
- Safety Policy : Specifies acceptable chat behavior on the part of the RolePlayer and the Bard.
- WorldModel : Represents the state of the session, as well as the background information that defines the world and the adventure. A World Model is organized hierarchically as:
	World > Regions > Locales > {RolePlayers, NPCs}

## Code of Conduct

See the [Code of Conduct](./CODE_OF_CONDUCT.md) for project participants and contributors.

## License

Copyright (c) 2024 [Jim Tyhurst](https://jimtyhurst.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/)
as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
