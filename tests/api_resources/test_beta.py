# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from anvil import Anvil, AsyncAnvil
from anvil.types import (
    BetaCreateTopicResponse,
    BetaRetrievePromptResponse,
    BetaRetrieveMetadataResponse,
    BetaCreatePromptMetricsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_prompt_metrics(self, client: Anvil) -> None:
        beta = client.beta.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_prompt_metrics(self, client: Anvil) -> None:
        response = client.beta.with_raw_response.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_prompt_metrics(self, client: Anvil) -> None:
        with client.beta.with_streaming_response.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_topic(self, client: Anvil) -> None:
        beta = client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_topic_with_all_params(self, client: Anvil) -> None:
        beta = client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_topic(self, client: Anvil) -> None:
        response = client.beta.with_raw_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_topic(self, client: Anvil) -> None:
        with client.beta.with_streaming_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_metadata(self, client: Anvil) -> None:
        beta = client.beta.retrieve_metadata()
        assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_metadata(self, client: Anvil) -> None:
        response = client.beta.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_metadata(self, client: Anvil) -> None:
        with client.beta.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_prompt(self, client: Anvil) -> None:
        beta = client.beta.retrieve_prompt(
            prompt_id="promptId",
        )
        assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_prompt(self, client: Anvil) -> None:
        response = client.beta.with_raw_response.retrieve_prompt(
            prompt_id="promptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_prompt(self, client: Anvil) -> None:
        with client.beta.with_streaming_response.retrieve_prompt(
            prompt_id="promptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_prompt_metrics(self, async_client: AsyncAnvil) -> None:
        beta = await async_client.beta.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_prompt_metrics(self, async_client: AsyncAnvil) -> None:
        response = await async_client.beta.with_raw_response.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_prompt_metrics(self, async_client: AsyncAnvil) -> None:
        async with async_client.beta.with_streaming_response.create_prompt_metrics(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaCreatePromptMetricsResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_topic(self, async_client: AsyncAnvil) -> None:
        beta = await async_client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_topic_with_all_params(self, async_client: AsyncAnvil) -> None:
        beta = await async_client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_topic(self, async_client: AsyncAnvil) -> None:
        response = await async_client.beta.with_raw_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_topic(self, async_client: AsyncAnvil) -> None:
        async with async_client.beta.with_streaming_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaCreateTopicResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_metadata(self, async_client: AsyncAnvil) -> None:
        beta = await async_client.beta.retrieve_metadata()
        assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_metadata(self, async_client: AsyncAnvil) -> None:
        response = await async_client.beta.with_raw_response.retrieve_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_metadata(self, async_client: AsyncAnvil) -> None:
        async with async_client.beta.with_streaming_response.retrieve_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaRetrieveMetadataResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_prompt(self, async_client: AsyncAnvil) -> None:
        beta = await async_client.beta.retrieve_prompt(
            prompt_id="promptId",
        )
        assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_prompt(self, async_client: AsyncAnvil) -> None:
        response = await async_client.beta.with_raw_response.retrieve_prompt(
            prompt_id="promptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_prompt(self, async_client: AsyncAnvil) -> None:
        async with async_client.beta.with_streaming_response.retrieve_prompt(
            prompt_id="promptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaRetrievePromptResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True
