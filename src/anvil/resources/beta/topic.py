# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

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
from ...types.beta import topic_create_prompts_params
from ..._base_client import make_request_options
from ...types.beta.topic_create_prompts_response import TopicCreatePromptsResponse

__all__ = ["TopicResource", "AsyncTopicResource"]


class TopicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TopicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return TopicResourceWithStreamingResponse(self)

    def create_prompts(
        self,
        *,
        website_topic_id: str,
        from_date: int,
        llm_provider: str,
        tag_ids: List[str],
        to_date: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicCreatePromptsResponse:
        """
        Returns analysis and metrics for all prompts with frequency over time by website
        and topic ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/beta/topic/prompts",
            body=maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                },
                topic_create_prompts_params.TopicCreatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"website_topic_id": website_topic_id}, topic_create_prompts_params.TopicCreatePromptsParams
                ),
            ),
            cast_to=TopicCreatePromptsResponse,
        )


class AsyncTopicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTopicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return AsyncTopicResourceWithStreamingResponse(self)

    async def create_prompts(
        self,
        *,
        website_topic_id: str,
        from_date: int,
        llm_provider: str,
        tag_ids: List[str],
        to_date: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicCreatePromptsResponse:
        """
        Returns analysis and metrics for all prompts with frequency over time by website
        and topic ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/beta/topic/prompts",
            body=await async_maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                },
                topic_create_prompts_params.TopicCreatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"website_topic_id": website_topic_id}, topic_create_prompts_params.TopicCreatePromptsParams
                ),
            ),
            cast_to=TopicCreatePromptsResponse,
        )


class TopicResourceWithRawResponse:
    def __init__(self, topic: TopicResource) -> None:
        self._topic = topic

        self.create_prompts = to_raw_response_wrapper(
            topic.create_prompts,
        )


class AsyncTopicResourceWithRawResponse:
    def __init__(self, topic: AsyncTopicResource) -> None:
        self._topic = topic

        self.create_prompts = async_to_raw_response_wrapper(
            topic.create_prompts,
        )


class TopicResourceWithStreamingResponse:
    def __init__(self, topic: TopicResource) -> None:
        self._topic = topic

        self.create_prompts = to_streamed_response_wrapper(
            topic.create_prompts,
        )


class AsyncTopicResourceWithStreamingResponse:
    def __init__(self, topic: AsyncTopicResource) -> None:
        self._topic = topic

        self.create_prompts = async_to_streamed_response_wrapper(
            topic.create_prompts,
        )
