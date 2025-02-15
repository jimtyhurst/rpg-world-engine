# rpg-world-engine

_Build and run a text-based Role-Playing Games, moderated by a Large Language
Model._

**Contents**

- [Motivation](#motivation)
- [Project status](#project-status)
- [Goals](#goals)
- [Design](#design)
- [Glossary](#glossary)
- [Run the web application](#run-the-web-application)
- [Development environment](#development-environment)
- [Annotated Bibliography](#annotated-bibliography)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Motivation

This is a personal side-project. I am using it as a way to explore
frameworks for building LLM applications.

## Project status

- The project is just getting started.
- Basic aspects of the interaction loop are implemented, so the human player
  can have a dialog with the Game Master.
- The world model was generated through a set of manual interactions with an
  LLM chat interface. A goal is to develop a World Builder application
  to make it easy to create new worlds.
- _Not Implemented Yet_
  - The Game Master should provide more descriptions as the Player moves
    to a new location or meets a new Non-Playing Character (NPC).
  - Enable the Main Character to acquire things. The Game Master
    should maintain an inventory of those objects.
  - Verify that the Player's dialog satisfies the age appropriate rating
    for the game. Some of this functionality is already provided by
    the LLM playing the role of a Game Master. The LLM will already refuse to
    respond to some user-submitted prompts. But this should be
    implemented more completely with specific classifiers
    as judges.
  - The Game Master should maintain a representation of progress towards
    meeting the story's "challenge" or "adventure" goals.
  - The Game Master should provide help to the Player to move them along
    towards the adventure's completion.

## Goals

- Generate a hierarchical text-based RPG world model;
- Run an RPG text adventure web application that uses that model as the
  setting for an adventure.

## Design

The World Model is constructed with the help of an LLM, based on a few
brief prompts from the person building the world.

The content of the adventure is produced by an LLM, using the World Model
and Playing Character input as context for telling a story and for
facilitating an adventure.

## Glossary

- Adventure : A series of interactions within a world.
- Bard : An application component as storyteller for the game. This is a
  subset of what most RPGs refer to as the Game Master. In this project, we
  want the Bard to be implemented with an LLM.
  This role is responsible for telling the story.
- Game Master (GM) : An application component that is responsible for:
  - managing the flow of interactions;
  - responding to Playing Characters.
  - enforcing safety policies.
- game scenario : A particular challenge or adventure goal within the
  context of the given World Model.
- game state : Represents the state of a game session.
- GenAI : Generative AI, e.g. an application that generates text based on a
  given prompt.
- jailbreak : to remove built-in limitations of an LLM, e.g. nullify the
  enforcement of safety policies or avoid built-in guardrails.
- LLM : Large Language Model.
- NPC : Non-Playing Character, i.e. background character defined within the
  World Model.
- PC : Playing Character, i.e. a main character in the story, played
  by a human who interacts with the game.
- RPG : Role-Playing Game.
- Safety Policy : Specifies acceptable chat behavior on the part of the
  RolePlayer and the Game Master.
- World Model : Represents background information that defines the world and
  the adventure.
  A World Model is organized hierarchically as:<br>
  World > Regions > Locales > {PCs, NPCs}

## Run the web application

We use [uv](https://github.com/astral-sh/uv) as a package manager,
but you can use any other package manager that you prefer.

```shell
# Install dependencies in a virtual environment.
uv venv --python 3.13
source .venv/bin/activate
uv sync

# Start the app server.
cd src
uv run python -m rpg_world_engine.game_master
```

This starts a web server, currently using [Gradio](https://www.gradio.app/).
When the server starts, the server log contains the URL to access the application.

## Development environment

We use [uv](https://github.com/astral-sh/uv) as a package manager.

### Install dependencies in a virtual environment.

```shell
uv venv --python 3.13
source .venv/bin/activate
uv sync
```

### Initialize pre-commit for tests, linter, and formatter

```shell
pre-commit install
```

### To display logging during `pytest`

```shell
uv run pytest --log-cli-level=DEBUG
```

### Run the `ruff` linter

```shell
uv run ruff check .
```

### Run the `ruff` formatter

```shell
uv run ruff format .
```

## Annotated Bibliography

- Niki Birkner ([together.ai](https://www.together.ai/))
  and Nick Walton ([AI Dungeon](https://aidungeon.com/)).
  2024-11-20.
  Building an AI-Powered Game.<br>
  https://learn.deeplearning.ai/courses/building-an-ai-powered-game/
  - A short tutorial offered through [DeepLearning.AI](https://www.deeplearning.ai/).
  - Much of the infrastructure of our project is based on the material
    in this tutorial, especially:
    - The creation of a hierarchical world model that was presented in the
      [Hierarchical Content Generation](https://learn.deeplearning.ai/courses/building-an-ai-powered-game/lesson/2/hierarchical-content-generation)
      section of that tutorial.
    - The acquisition of inventory presented in the
      [Implementing Game Mechanics](https://learn.deeplearning.ai/courses/building-an-ai-powered-game/lesson/5/implementing-game-mechanics)
      section of that tutorial.
    - The use of [Gradio](https://www.gradio.app/) for the web application.
- Hidden Door.
  https://www.hiddendoor.co/
  - Playing a game in this hosted "online social roleplaying game"
    platform started me thinking about what it would take to build
    such a system.
  - According to their website, their system uses many types of AI components.
    However for this project, I am experimenting with how much can be done
    with just an LLM.
- EvidentlyAI. LLM evaluations for AI product teams.
  - About the course: https://www.evidentlyai.com/llm-evaluations-course
  - Recordings: https://www.youtube.com/playlist?list=PL9omX6impEuMgDFCK_NleIB0sMzKs2boI
  - This excellent tutorial of 13 short videos provides a concise,
    practical discussion of evaluating application components that
    rely on an LLM.
  - We want to explore the notion of safety and risks within the context
    of this project, such as assuring that hate speech and overly
    sexualized material is not submitted by the human Player and not returned by the LLM-based storyteller.

## Code of Conduct

See the [Code of Conduct](./CODE_OF_CONDUCT.md) for project participants and
contributors.

## License

Copyright (c) 2024-2025 [Jim Tyhurst](https://jimtyhurst.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/)
as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
