# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from anvil import Anvil, AsyncAnvil
from tests.utils import assert_matches_type
from anvil.types.beta import TopicCreatePromptsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_prompts(self, client: Anvil) -> None:
        topic = client.beta.topic.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_prompts(self, client: Anvil) -> None:
        response = client.beta.topic.with_raw_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_prompts(self, client: Anvil) -> None:
        with client.beta.topic.with_streaming_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_prompts(self, async_client: AsyncAnvil) -> None:
        topic = await async_client.beta.topic.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_prompts(self, async_client: AsyncAnvil) -> None:
        response = await async_client.beta.topic.with_raw_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_prompts(self, async_client: AsyncAnvil) -> None:
        async with async_client.beta.topic.with_streaming_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(TopicCreatePromptsResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True
