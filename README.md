# rpg-world-engine
Builds and runs text-based Role-Playing Games, moderated by a Large Language Model.

**Contents**

- [Overview](#overview)
- [Glossary](#glossary)
- [Annotated Bibliography](#annotated-bibliography)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Overview

This project provides tools to:

- Generate a hierarchical text-based RPG world model;
- Run an RPG text adventure web application that uses that model as the
    setting for an adventure.

The WorldModel is constructed with the help of an LLM, based on a few
brief prompts from the person building the world.

The content of the adventure is produced by an LLM, using the WorldModel
and Playing Character input as context for telling a story and for
facilitating an adventure.

## Glossary

- Adventure : A series of interactions within a world.
- Bard : An application component as storyteller for the game. This is a
    subset of what most RPGs refer to as the Gamemaster. In this project, we
    want the Bard to be implemented with an LLM.
    This role is responsible for:
    - telling the story;
    - responding to Playing Characters.
- Gamemaster : An application component that is responsible for:
    - managing the flow of interactions;
    - enforcing safety policies.
- GenAI : Generative AI, e.g. an application that generates text based on a
    given prompt.
- jailbreak : to remove built-in limitations of an LLM, e.g. nullify the
    enforcement of safety policies or avoid built-in guardrails.
- LLM : Large Language Model.
- NPC : Non-Playing Character, i.e. background character defined within the
    World Model.
- PC : Playing Character, i.e. human who interacts with the game.
- RPG : Role-Playing Game.
- Safety Policy : Specifies acceptable chat behavior on the part of the
    RolePlayer and the Bard.
- WorldModel : Represents the state of the session, as well as the
    background information that defines the world and the adventure.
    A World Model is organized hierarchically as:<br>
	World > Regions > Locales > {PCs, NPCs}

## Annotated Bibliography
- Niki Birkner, Nick Walton. 2024-11-20. Building an AI-Powered Game.
    https://learn.deeplearning.ai/courses/building-an-ai-powered-game/
    - A short tutorial offered through DeepLearning.AI.
    - Much of the infrastructure of our project is based on the material
        in this tutorial, especially the creation of a hierarchical world
        model that was presented in the
        [Hierarchical Content Generation](https://learn.deeplearning.ai/courses/building-an-ai-powered-game/lesson/2/hierarchical-content-generation)
        section of that tutorial.
- Hidden Door.
    https://www.hiddendoor.co/
    - Playing a game in this hosted "online social roleplaying game"
        platform started me thinking about what it would take to build
        such a system.
- EvidentlyAI. LLM evaluations for AI product teams.
    - About the course: https://www.evidentlyai.com/llm-evaluations-course
    - Recordings: https://www.youtube.com/playlist?list=PL9omX6impEuMgDFCK_NleIB0sMzKs2boI
    - This excellent tutorial of 13 short videos provides a concise,
        practical discussion of evaluating application components that
        rely on an LLM.
    - We want to explore the notion of safety and risks within the context
        of this project, such as assuring that hate speech and overly
        sexualized material is not returned by the storyteller.
- Jack Parker-Holder, et al. 2024-12-04. Genie 2: A large-scale foundation world model.
    https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/
    - We do not use
        [Genie 1](https://deepmind.google/research/publications/60474/)
        or
        [Genie 2](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)
        in our project, as they are primarily for video interaction.
        However, they are additional examples of using a large foundational
        generative model for creating an interactive game world.

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
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
