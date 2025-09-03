# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ClientGetAggregatedPromptsParams"]


class ClientGetAggregatedPromptsParams(TypedDict, total=False):
    website_topic_id: Required[Annotated[str, PropertyInfo(alias="websiteTopicId")]]

    from_date: Required[Annotated[int, PropertyInfo(alias="fromDate")]]

    llm_provider: Required[Annotated[str, PropertyInfo(alias="llmProvider")]]

    tag_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="tagIds")]]

    to_date: Required[Annotated[int, PropertyInfo(alias="toDate")]]
