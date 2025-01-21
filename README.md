# rpg-world-engine

Builds and runs text-based Role-Playing Games, moderated by a Large Language Model.

**Project status**

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

**Contents**

- [Motivation](#motivation)
- [Goals](#goals)
- [Glossary](#glossary)
- [Annotated Bibliography](#annotated-bibliography)
- [Development environment](#development-environment)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Motivation

This is a personal side-project. I am using it as a way to explore
frameworks for building LLM applications.

## Goals

**Note**: This project is just getting started, so not much is implemented.
However, this section describes the near-term goals for the project.

The goal of this project is to provide applications that:

- Generate a hierarchical text-based RPG world model;
- Run an RPG text adventure web application that uses that model as the
  setting for an adventure.

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
  This role is responsible for:
  - telling the story;
  - responding to Playing Characters.
- Game Master : An application component that is responsible for:
  - managing the flow of interactions;
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
  RolePlayer and the Bard.
- World Model : Represents background information that defines the world and
  the adventure.
  A World Model is organized hierarchically as:<br>
  World > Regions > Locales > {PCs, NPCs}

## Annotated Bibliography

- Niki Birkner, Nick Walton. 2024-11-20. Building an AI-Powered Game.
  https://learn.deeplearning.ai/courses/building-an-ai-powered-game/
  - A short tutorial offered through DeepLearning.AI.
  - Much of the infrastructure of our project is based on the material
    in this tutorial, especially:
    - the creation of a hierarchical world model that was presented in the
      [Hierarchical Content Generation](https://learn.deeplearning.ai/courses/building-an-ai-powered-game/lesson/2/hierarchical-content-generation)
      section of that tutorial.
    - the acquisition of inventory presented in the
      [Implementing Game Mechanics](https://learn.deeplearning.ai/courses/building-an-ai-powered-game/lesson/5/implementing-game-mechanics)
      section of that tutorial.
    - the use of [Gradio](https://www.gradio.app/) for the web application.
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
    sexualized material is not returned by the storyteller.

## Development environment

We use [uv](https://github.com/astral-sh/uv) as a package manager.

### To run the web application

```shell
cd src
uv run python -m rpg_world_engine.game_master
```

This starts a web server, currently using [Gradio](https://www.gradio.app/).
When the server starts, the system log gives the URL to access the application.

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
