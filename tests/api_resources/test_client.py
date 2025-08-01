# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from anvil import Anvil, AsyncAnvil
from anvil.types import (
    GetPromptResponse,
    GetTopicsResponse,
    GetMetadataResponse,
    GetAggregatedPromptsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_aggregated_prompts(self, client: Anvil) -> None:
        client_ = client.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(GetAggregatedPromptsResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_aggregated_prompts(self, client: Anvil) -> None:
        response = client.with_raw_response.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetAggregatedPromptsResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_aggregated_prompts(self, client: Anvil) -> None:
        with client.with_streaming_response.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetAggregatedPromptsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_metadata(self, client: Anvil) -> None:
        client_ = client.get_metadata()
        assert_matches_type(GetMetadataResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_metadata(self, client: Anvil) -> None:
        response = client.with_raw_response.get_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetMetadataResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_metadata(self, client: Anvil) -> None:
        with client.with_streaming_response.get_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetMetadataResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_prompt(self, client: Anvil) -> None:
        client_ = client.get_prompt(
            prompt_id="promptId",
        )
        assert_matches_type(GetPromptResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_prompt(self, client: Anvil) -> None:
        response = client.with_raw_response.get_prompt(
            prompt_id="promptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetPromptResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_prompt(self, client: Anvil) -> None:
        with client.with_streaming_response.get_prompt(
            prompt_id="promptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetPromptResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_topics(self, client: Anvil) -> None:
        client_ = client.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(GetTopicsResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_topics_with_all_params(self, client: Anvil) -> None:
        client_ = client.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert_matches_type(GetTopicsResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_topics(self, client: Anvil) -> None:
        response = client.with_raw_response.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(GetTopicsResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_topics(self, client: Anvil) -> None:
        with client.with_streaming_response.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(GetTopicsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_aggregated_prompts(self, async_client: AsyncAnvil) -> None:
        client = await async_client.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(GetAggregatedPromptsResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_aggregated_prompts(self, async_client: AsyncAnvil) -> None:
        response = await async_client.with_raw_response.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetAggregatedPromptsResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_aggregated_prompts(self, async_client: AsyncAnvil) -> None:
        async with async_client.with_streaming_response.get_aggregated_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetAggregatedPromptsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncAnvil) -> None:
        client = await async_client.get_metadata()
        assert_matches_type(GetMetadataResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncAnvil) -> None:
        response = await async_client.with_raw_response.get_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetMetadataResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncAnvil) -> None:
        async with async_client.with_streaming_response.get_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetMetadataResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_prompt(self, async_client: AsyncAnvil) -> None:
        client = await async_client.get_prompt(
            prompt_id="promptId",
        )
        assert_matches_type(GetPromptResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_prompt(self, async_client: AsyncAnvil) -> None:
        response = await async_client.with_raw_response.get_prompt(
            prompt_id="promptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetPromptResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_prompt(self, async_client: AsyncAnvil) -> None:
        async with async_client.with_streaming_response.get_prompt(
            prompt_id="promptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetPromptResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_topics(self, async_client: AsyncAnvil) -> None:
        client = await async_client.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(GetTopicsResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_topics_with_all_params(self, async_client: AsyncAnvil) -> None:
        client = await async_client.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert_matches_type(GetTopicsResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_topics(self, async_client: AsyncAnvil) -> None:
        response = await async_client.with_raw_response.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(GetTopicsResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_topics(self, async_client: AsyncAnvil) -> None:
        async with async_client.with_streaming_response.get_topics(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(GetTopicsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
