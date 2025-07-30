# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BetaRetrieveMetadataResponse", "BetaRetrieveMetadataResponseItem", "BetaRetrieveMetadataResponseItemPrompt"]


class BetaRetrieveMetadataResponseItemPrompt(BaseModel):
    id: Optional[str] = None

    language: Optional[
        Literal[
            "ENGLISH",
            "SPANISH",
            "PORTUGUESE",
            "HEBREW",
            "GERMAN",
            "ITALIAN",
            "FRENCH",
            "MANDARIN",
            "HINDI",
            "ARABIC",
            "JAPANESE",
            "RUSSIAN",
        ]
    ] = None

    text: Optional[str] = None


class BetaRetrieveMetadataResponseItem(BaseModel):
    id: Optional[str] = None

    llm_provider: Optional[str] = FieldInfo(alias="llmProvider", default=None)

    prompts: Optional[List[BetaRetrieveMetadataResponseItemPrompt]] = None

    text: Optional[str] = None


BetaRetrieveMetadataResponse: TypeAlias = List[BetaRetrieveMetadataResponseItem]
