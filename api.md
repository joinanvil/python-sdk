# Beta

Types:

```python
from anvil.types import (
    BetaCreateTopicResponse,
    BetaRetrieveMetadataResponse,
    BetaRetrievePromptResponse,
)
```

Methods:

- <code title="post /api/beta/topics">client.beta.<a href="./src/anvil/resources/beta/beta.py">create_topic</a>(\*\*<a href="src/anvil/types/beta_create_topic_params.py">params</a>) -> <a href="./src/anvil/types/beta_create_topic_response.py">BetaCreateTopicResponse</a></code>
- <code title="get /api/beta/metadata">client.beta.<a href="./src/anvil/resources/beta/beta.py">retrieve_metadata</a>() -> <a href="./src/anvil/types/beta_retrieve_metadata_response.py">BetaRetrieveMetadataResponse</a></code>
- <code title="get /api/beta/prompt">client.beta.<a href="./src/anvil/resources/beta/beta.py">retrieve_prompt</a>(\*\*<a href="src/anvil/types/beta_retrieve_prompt_params.py">params</a>) -> <a href="./src/anvil/types/beta_retrieve_prompt_response.py">BetaRetrievePromptResponse</a></code>

## Topic

Types:

```python
from anvil.types.beta import TopicCreatePromptsResponse
```

Methods:

- <code title="post /api/beta/topic/prompts">client.beta.topic.<a href="./src/anvil/resources/beta/topic.py">create_prompts</a>(\*\*<a href="src/anvil/types/beta/topic_create_prompts_params.py">params</a>) -> <a href="./src/anvil/types/beta/topic_create_prompts_response.py">TopicCreatePromptsResponse</a></code>
