# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .topic import (
    TopicResource,
    AsyncTopicResource,
    TopicResourceWithRawResponse,
    AsyncTopicResourceWithRawResponse,
    TopicResourceWithStreamingResponse,
    AsyncTopicResourceWithStreamingResponse,
)
from ...types import beta_create_topic_params, beta_retrieve_prompt_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.beta_create_topic_response import BetaCreateTopicResponse
from ...types.beta_retrieve_prompt_response import BetaRetrievePromptResponse
from ...types.beta_retrieve_metadata_response import BetaRetrieveMetadataResponse

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def topic(self) -> TopicResource:
        return TopicResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)

    def create_topic(
        self,
        *,
        from_date: int,
        llm_provider: str,
        tag_ids: List[str],
        to_date: int,
        archive: bool | NotGiven = NOT_GIVEN,
        competitor_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaCreateTopicResponse:
        """
        Returns analysis and metrics for all the topics by website ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/beta/topics",
            body=maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                    "archive": archive,
                    "competitor_url": competitor_url,
                },
                beta_create_topic_params.BetaCreateTopicParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaCreateTopicResponse,
        )

    def retrieve_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaRetrieveMetadataResponse:
        """Returns all metadata by website ID"""
        return self._get(
            "/api/beta/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaRetrieveMetadataResponse,
        )

    def retrieve_prompt(
        self,
        *,
        prompt_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaRetrievePromptResponse:
        """
        Returns all related metrics data by prompt ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/beta/prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"prompt_id": prompt_id}, beta_retrieve_prompt_params.BetaRetrievePromptParams),
            ),
            cast_to=BetaRetrievePromptResponse,
        )


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def topic(self) -> AsyncTopicResource:
        return AsyncTopicResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)

    async def create_topic(
        self,
        *,
        from_date: int,
        llm_provider: str,
        tag_ids: List[str],
        to_date: int,
        archive: bool | NotGiven = NOT_GIVEN,
        competitor_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaCreateTopicResponse:
        """
        Returns analysis and metrics for all the topics by website ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/beta/topics",
            body=await async_maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                    "archive": archive,
                    "competitor_url": competitor_url,
                },
                beta_create_topic_params.BetaCreateTopicParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaCreateTopicResponse,
        )

    async def retrieve_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaRetrieveMetadataResponse:
        """Returns all metadata by website ID"""
        return await self._get(
            "/api/beta/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaRetrieveMetadataResponse,
        )

    async def retrieve_prompt(
        self,
        *,
        prompt_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BetaRetrievePromptResponse:
        """
        Returns all related metrics data by prompt ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/beta/prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prompt_id": prompt_id}, beta_retrieve_prompt_params.BetaRetrievePromptParams
                ),
            ),
            cast_to=BetaRetrievePromptResponse,
        )


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.create_topic = to_raw_response_wrapper(
            beta.create_topic,
        )
        self.retrieve_metadata = to_raw_response_wrapper(
            beta.retrieve_metadata,
        )
        self.retrieve_prompt = to_raw_response_wrapper(
            beta.retrieve_prompt,
        )

    @cached_property
    def topic(self) -> TopicResourceWithRawResponse:
        return TopicResourceWithRawResponse(self._beta.topic)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.create_topic = async_to_raw_response_wrapper(
            beta.create_topic,
        )
        self.retrieve_metadata = async_to_raw_response_wrapper(
            beta.retrieve_metadata,
        )
        self.retrieve_prompt = async_to_raw_response_wrapper(
            beta.retrieve_prompt,
        )

    @cached_property
    def topic(self) -> AsyncTopicResourceWithRawResponse:
        return AsyncTopicResourceWithRawResponse(self._beta.topic)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.create_topic = to_streamed_response_wrapper(
            beta.create_topic,
        )
        self.retrieve_metadata = to_streamed_response_wrapper(
            beta.retrieve_metadata,
        )
        self.retrieve_prompt = to_streamed_response_wrapper(
            beta.retrieve_prompt,
        )

    @cached_property
    def topic(self) -> TopicResourceWithStreamingResponse:
        return TopicResourceWithStreamingResponse(self._beta.topic)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.create_topic = async_to_streamed_response_wrapper(
            beta.create_topic,
        )
        self.retrieve_metadata = async_to_streamed_response_wrapper(
            beta.retrieve_metadata,
        )
        self.retrieve_prompt = async_to_streamed_response_wrapper(
            beta.retrieve_prompt,
        )

    @cached_property
    def topic(self) -> AsyncTopicResourceWithStreamingResponse:
        return AsyncTopicResourceWithStreamingResponse(self._beta.topic)
