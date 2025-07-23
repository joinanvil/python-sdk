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


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_topic(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert beta.is_closed
        assert beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_topic_with_all_params(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert beta.is_closed
        assert beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_topic(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = client.beta.with_raw_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert beta.json() == {"foo": "bar"}
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_topic(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.beta.with_streaming_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, StreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_metadata(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = client.beta.retrieve_metadata()
        assert beta.is_closed
        assert beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_metadata(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = client.beta.with_raw_response.retrieve_metadata()

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert beta.json() == {"foo": "bar"}
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_metadata(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.beta.with_streaming_response.retrieve_metadata() as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, StreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_prompt(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = client.beta.retrieve_prompt(
            prompt_id="promptId",
        )
        assert beta.is_closed
        assert beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_prompt(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = client.beta.with_raw_response.retrieve_prompt(
            prompt_id="promptId",
        )

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert beta.json() == {"foo": "bar"}
        assert isinstance(beta, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_prompt(self, client: Anvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.beta.with_streaming_response.retrieve_prompt(
            prompt_id="promptId",
        ) as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, StreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_topic(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = await async_client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )
        assert beta.is_closed
        assert await beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_topic_with_all_params(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = await async_client.beta.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
            archive=True,
            competitor_url="competitorUrl",
        )
        assert beta.is_closed
        assert await beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_topic(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = await async_client.beta.with_raw_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        )

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await beta.json() == {"foo": "bar"}
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_topic(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.post("/api/beta/topics").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.beta.with_streaming_response.create_topic(
            from_date=0,
            llm_provider="llmProvider",
            tag_ids=["string"],
            to_date=0,
        ) as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_metadata(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = await async_client.beta.retrieve_metadata()
        assert beta.is_closed
        assert await beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_metadata(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = await async_client.beta.with_raw_response.retrieve_metadata()

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await beta.json() == {"foo": "bar"}
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_metadata(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/metadata").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.beta.with_streaming_response.retrieve_metadata() as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_prompt(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        beta = await async_client.beta.retrieve_prompt(
            prompt_id="promptId",
        )
        assert beta.is_closed
        assert await beta.json() == {"foo": "bar"}
        assert cast(Any, beta.is_closed) is True
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_prompt(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        beta = await async_client.beta.with_raw_response.retrieve_prompt(
            prompt_id="promptId",
        )

        assert beta.is_closed is True
        assert beta.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await beta.json() == {"foo": "bar"}
        assert isinstance(beta, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_prompt(self, async_client: AsyncAnvil, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/beta/prompt").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.beta.with_streaming_response.retrieve_prompt(
            prompt_id="promptId",
        ) as beta:
            assert not beta.is_closed
            assert beta.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await beta.json() == {"foo": "bar"}
            assert cast(Any, beta.is_closed) is True
            assert isinstance(beta, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, beta.is_closed) is True
