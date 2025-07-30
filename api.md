# Beta

Types:

```python
from anvil.types import (
    BetaCreatePromptMetricsResponse,
    BetaCreateTopicResponse,
    BetaRetrieveMetadataResponse,
    BetaRetrievePromptResponse,
)
```

Methods:

- <code title="post /api/beta/prompts">client.beta.<a href="./src/anvil/resources/beta.py">create_prompt_metrics</a>(\*\*<a href="src/anvil/types/beta_create_prompt_metrics_params.py">params</a>) -> <a href="./src/anvil/types/beta_create_prompt_metrics_response.py">BetaCreatePromptMetricsResponse</a></code>
- <code title="post /api/beta/topics">client.beta.<a href="./src/anvil/resources/beta.py">create_topic</a>(\*\*<a href="src/anvil/types/beta_create_topic_params.py">params</a>) -> <a href="./src/anvil/types/beta_create_topic_response.py">BetaCreateTopicResponse</a></code>
- <code title="get /api/beta/metadata">client.beta.<a href="./src/anvil/resources/beta.py">retrieve_metadata</a>() -> <a href="./src/anvil/types/beta_retrieve_metadata_response.py">BetaRetrieveMetadataResponse</a></code>
- <code title="get /api/beta/prompt">client.beta.<a href="./src/anvil/resources/beta.py">retrieve_prompt</a>(\*\*<a href="src/anvil/types/beta_retrieve_prompt_params.py">params</a>) -> <a href="./src/anvil/types/beta_retrieve_prompt_response.py">BetaRetrievePromptResponse</a></code>
