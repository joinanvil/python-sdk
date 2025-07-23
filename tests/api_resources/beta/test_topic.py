# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from anvil import Anvil, AsyncAnvil
from anvil._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_prompts(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        topic = client.beta.topic.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert topic.is_closed
        assert topic.json() == {"foo": "bar"}
        assert cast(Any, topic.is_closed) is True
        assert isinstance(topic, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_prompts(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        topic = client.beta.topic.with_raw_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert topic.is_closed is True
        assert topic.http_request.headers.get("X-Stainless-Lang") == "python"
        assert topic.json() == {"foo": "bar"}
        assert isinstance(topic, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_prompts(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.beta.topic.with_streaming_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as topic:
            assert not topic.is_closed
            assert topic.http_request.headers.get("X-Stainless-Lang") == "python"

            assert topic.json() == {"foo": "bar"}
            assert cast(Any, topic.is_closed) is True
            assert isinstance(topic, StreamedBinaryAPIResponse)

        assert cast(Any, topic.is_closed) is True


class TestAsyncTopic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_prompts(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        topic = await async_client.beta.topic.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert topic.is_closed
        assert await topic.json() == {"foo": "bar"}
        assert cast(Any, topic.is_closed) is True
        assert isinstance(topic, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_prompts(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        topic = await async_client.beta.topic.with_raw_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert topic.is_closed is True
        assert topic.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await topic.json() == {"foo": "bar"}
        assert isinstance(topic, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_prompts(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topic/prompts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.beta.topic.with_streaming_response.create_prompts(
            website_topic_id="websiteTopicId",
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as topic:
            assert not topic.is_closed
            assert topic.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await topic.json() == {"foo": "bar"}
            assert cast(Any, topic.is_closed) is True
            assert isinstance(topic, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, topic.is_closed) is True
