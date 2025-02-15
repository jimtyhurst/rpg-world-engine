# Workflow diagram

```mermaid
graph TD;
A[User submits prompt] --> B[Prompt is safe?];
B -- Yes --> C[Augment prompt with context];
B -- No --> D[Report filter violation to user];
D --> A
C --> E[LLM generates next story fragment]
E --> F[Extract content for user]
F --> I[Response is safe?]
I -- Yes --> G[Update inventory]
I -- Yes --> H[Update location]
I -- No --> K[Report warning to user]
K --> A
G --> J[Display response to user]
H --> J
J --> A
```

## Details

### Prompt is safe?

Validate the user prompt. Use a chain of classifiers as filters. These are more focused than relying on the Game Master's LLM to detect these conditions.

- is_off_topic
- is_hate_speech
- is_overtly_sexual
- is_excessively_violent
- involves_self_harm
- violates_rating

### Augment prompt with context

For example,

- system prompt
- game state
- world model
- history
- inventory
- others?

### Response is safe?

- Use the same set of filters as for user input??
- Gemini LLM provides some safety ratings in its response. For example,
  - HARM_CATEGORY_HATE_SPEECH
  - HARM_CATEGORY_DANGEROUS_CONTENT
  - See details here:
    - https://ai.google.dev/gemini-api/docs/safety-settings
    - https://ai.google.dev/gemini-api/docs/safety-settings#safety-filters
    - https://ai.google.dev/gemini-api/docs/safety-guidance

_Factors to consider_: Anthropic's
[Acceptable Use Policy](https://www.anthropic.com/legal/aup)
provides a good list of risks to consider when using LLMs.
While those risks are associated with actions in the real world,
it also makes sense to avoid some of these harms in game interactions.
