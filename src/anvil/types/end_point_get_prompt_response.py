# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndPointGetPromptResponse", "EndPointGetPromptResponseItem", "EndPointGetPromptResponseItemData"]


class EndPointGetPromptResponseItemData(BaseModel):
    important_terms: Optional[List[str]] = FieldInfo(alias="importantTerms", default=None)

    mentions: Optional[Dict[str, int]] = None

    negative_sentiment: Optional[List[Dict[str, str]]] = FieldInfo(alias="negativeSentiment", default=None)

    positive_sentiments: Optional[List[Dict[str, str]]] = FieldInfo(alias="positiveSentiments", default=None)

    ranking: Optional[Dict[str, int]] = None

    sentiment_score: Optional[Dict[str, int]] = FieldInfo(alias="sentimentScore", default=None)

    sources: Optional[List[str]] = None


class EndPointGetPromptResponseItem(BaseModel):
    id: Optional[str] = None

    answer_text: Optional[str] = FieldInfo(alias="answerText", default=None)

    bright_data_prompt_index: Optional[int] = FieldInfo(alias="brightDataPromptIndex", default=None)

    complete_post_process: Optional[bool] = FieldInfo(alias="completePostProcess", default=None)

    created: Optional[datetime] = None

    data: Optional[EndPointGetPromptResponseItemData] = None

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

    llm_provider: Optional[Literal["openai/gpt-4o", "openai/gpt-4o-search-preview", "perplexity", "gemini"]] = (
        FieldInfo(alias="llmProvider", default=None)
    )

    locale: Optional[
        Literal[
            "GLOBAL",
            "ISRAEL",
            "EU",
            "UK",
            "US",
            "IL",
            "AL",
            "AZ",
            "KG",
            "BA",
            "UZ",
            "BI",
            "XK",
            "SM",
            "DE",
            "AT",
            "CH",
            "IE",
            "IM",
            "FR",
            "ES",
            "NL",
            "IT",
            "PT",
            "BE",
            "AD",
            "MT",
            "MC",
            "MA",
            "LU",
            "TN",
            "DZ",
            "GI",
            "LI",
            "SE",
            "DK",
            "FI",
            "NO",
            "AX",
            "IS",
            "GG",
            "JE",
            "GL",
            "VA",
            "FX",
            "FO",
            "AF",
            "AM",
            "AU",
            "BH",
            "BD",
            "BT",
            "BN",
            "KH",
            "CN",
            "CY",
            "GE",
            "HK",
            "IN",
            "ID",
            "IR",
            "IQ",
            "JP",
            "JO",
            "KZ",
            "KW",
            "LA",
            "LB",
            "MY",
            "MV",
            "MN",
            "MM",
            "NP",
            "OM",
            "PK",
            "PH",
            "QA",
            "SA",
            "SG",
            "KR",
            "LK",
            "SY",
            "TW",
            "TH",
            "TR",
            "AE",
            "VN",
            "YE",
            "AR",
            "BO",
            "BR",
            "CL",
            "CO",
            "EC",
            "GY",
            "PY",
            "PE",
            "SR",
            "UY",
            "VE",
        ]
    ] = None

    owner_website_id: Optional[str] = FieldInfo(alias="ownerWebsiteId", default=None)

    owner_website_url: Optional[str] = FieldInfo(alias="ownerWebsiteUrl", default=None)

    oxy_job_id: Optional[int] = FieldInfo(alias="oxyJobId", default=None)

    prompt_id: Optional[str] = FieldInfo(alias="promptId", default=None)

    prompt_text: Optional[str] = FieldInfo(alias="promptText", default=None)

    provider: Optional[Literal["BRIGHT_DATA", "OXY"]] = None

    status: Optional[
        Literal[
            "PENDING_BRIGHTDATA",
            "BRIGHTDATA_PROCESSING",
            "OXY_PROCESSING",
            "PROCESSING_ANSWER",
            "POST_PROCESSING",
            "COMPLETED",
        ]
    ] = None

    trigger_date: Optional[datetime] = FieldInfo(alias="triggerDate", default=None)

    website_topic_id: Optional[str] = FieldInfo(alias="websiteTopicId", default=None)


EndPointGetPromptResponse: TypeAlias = List[EndPointGetPromptResponseItem]
