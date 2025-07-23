# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BetaCreateTopicParams"]


class BetaCreateTopicParams(TypedDict, total=False):
    from_date: Required[Annotated[int, PropertyInfo(alias="fromDate")]]

    llm_provider: Required[Annotated[str, PropertyInfo(alias="llmProvider")]]

    tag_ids: Required[Annotated[List[str], PropertyInfo(alias="tagIds")]]

    to_date: Required[Annotated[int, PropertyInfo(alias="toDate")]]

    archive: bool

    competitor_url: Annotated[str, PropertyInfo(alias="competitorUrl")]
