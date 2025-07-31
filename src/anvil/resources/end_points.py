# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import end_point_get_prompt_params, end_point_get_topics_params, end_point_get_aggregated_prompts_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.end_point_get_prompt_response import EndPointGetPromptResponse
from ..types.end_point_get_topics_response import EndPointGetTopicsResponse
from ..types.end_point_get_metadata_response import EndPointGetMetadataResponse
from ..types.end_point_get_aggregated_prompts_response import EndPointGetAggregatedPromptsResponse

__all__ = ["EndPointsResource", "AsyncEndPointsResource"]


class EndPointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return EndPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return EndPointsResourceWithStreamingResponse(self)

    def get_aggregated_prompts(
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
    ) -> EndPointGetAggregatedPromptsResponse:
        """
        Returns metrics for all prompts with frequency over time topic ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/beta/prompts",
            body=maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                },
                end_point_get_aggregated_prompts_params.EndPointGetAggregatedPromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"website_topic_id": website_topic_id},
                    end_point_get_aggregated_prompts_params.EndPointGetAggregatedPromptsParams,
                ),
            ),
            cast_to=EndPointGetAggregatedPromptsResponse,
        )

    def get_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndPointGetMetadataResponse:
        """Returns all metadata by website ID"""
        return self._get(
            "/api/beta/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndPointGetMetadataResponse,
        )

    def get_prompt(
        self,
        *,
        prompt_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndPointGetPromptResponse:
        """
        Returns all related metrics data by prompt ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/beta/prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"prompt_id": prompt_id}, end_point_get_prompt_params.EndPointGetPromptParams),
            ),
            cast_to=EndPointGetPromptResponse,
        )

    def get_topics(
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
    ) -> EndPointGetTopicsResponse:
        """
        Returns metrics for all the topics by website ID

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
                end_point_get_topics_params.EndPointGetTopicsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndPointGetTopicsResponse,
        )


class AsyncEndPointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/joinanvil/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEndPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/joinanvil/python-sdk#with_streaming_response
        """
        return AsyncEndPointsResourceWithStreamingResponse(self)

    async def get_aggregated_prompts(
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
    ) -> EndPointGetAggregatedPromptsResponse:
        """
        Returns metrics for all prompts with frequency over time topic ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/beta/prompts",
            body=await async_maybe_transform(
                {
                    "from_date": from_date,
                    "llm_provider": llm_provider,
                    "tag_ids": tag_ids,
                    "to_date": to_date,
                },
                end_point_get_aggregated_prompts_params.EndPointGetAggregatedPromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"website_topic_id": website_topic_id},
                    end_point_get_aggregated_prompts_params.EndPointGetAggregatedPromptsParams,
                ),
            ),
            cast_to=EndPointGetAggregatedPromptsResponse,
        )

    async def get_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndPointGetMetadataResponse:
        """Returns all metadata by website ID"""
        return await self._get(
            "/api/beta/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndPointGetMetadataResponse,
        )

    async def get_prompt(
        self,
        *,
        prompt_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndPointGetPromptResponse:
        """
        Returns all related metrics data by prompt ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/beta/prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prompt_id": prompt_id}, end_point_get_prompt_params.EndPointGetPromptParams
                ),
            ),
            cast_to=EndPointGetPromptResponse,
        )

    async def get_topics(
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
    ) -> EndPointGetTopicsResponse:
        """
        Returns metrics for all the topics by website ID

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
                end_point_get_topics_params.EndPointGetTopicsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndPointGetTopicsResponse,
        )


class EndPointsResourceWithRawResponse:
    def __init__(self, end_points: EndPointsResource) -> None:
        self._end_points = end_points

        self.get_aggregated_prompts = to_raw_response_wrapper(
            end_points.get_aggregated_prompts,
        )
        self.get_metadata = to_raw_response_wrapper(
            end_points.get_metadata,
        )
        self.get_prompt = to_raw_response_wrapper(
            end_points.get_prompt,
        )
        self.get_topics = to_raw_response_wrapper(
            end_points.get_topics,
        )


class AsyncEndPointsResourceWithRawResponse:
    def __init__(self, end_points: AsyncEndPointsResource) -> None:
        self._end_points = end_points

        self.get_aggregated_prompts = async_to_raw_response_wrapper(
            end_points.get_aggregated_prompts,
        )
        self.get_metadata = async_to_raw_response_wrapper(
            end_points.get_metadata,
        )
        self.get_prompt = async_to_raw_response_wrapper(
            end_points.get_prompt,
        )
        self.get_topics = async_to_raw_response_wrapper(
            end_points.get_topics,
        )


class EndPointsResourceWithStreamingResponse:
    def __init__(self, end_points: EndPointsResource) -> None:
        self._end_points = end_points

        self.get_aggregated_prompts = to_streamed_response_wrapper(
            end_points.get_aggregated_prompts,
        )
        self.get_metadata = to_streamed_response_wrapper(
            end_points.get_metadata,
        )
        self.get_prompt = to_streamed_response_wrapper(
            end_points.get_prompt,
        )
        self.get_topics = to_streamed_response_wrapper(
            end_points.get_topics,
        )


class AsyncEndPointsResourceWithStreamingResponse:
    def __init__(self, end_points: AsyncEndPointsResource) -> None:
        self._end_points = end_points

        self.get_aggregated_prompts = async_to_streamed_response_wrapper(
            end_points.get_aggregated_prompts,
        )
        self.get_metadata = async_to_streamed_response_wrapper(
            end_points.get_metadata,
        )
        self.get_prompt = async_to_streamed_response_wrapper(
            end_points.get_prompt,
        )
        self.get_topics = async_to_streamed_response_wrapper(
            end_points.get_topics,
        )
