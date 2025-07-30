# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TopicCreatePromptsResponse",
    "TopicCreatePromptsResponseItem",
    "TopicCreatePromptsResponseItemMentionFrequency",
    "TopicCreatePromptsResponseItemMentionFrequencySery",
    "TopicCreatePromptsResponseItemSeoMetrics",
]


class TopicCreatePromptsResponseItemMentionFrequencySery(BaseModel):
    date: datetime

    value: float


class TopicCreatePromptsResponseItemMentionFrequency(BaseModel):
    average: Optional[float] = None

    data_format: Optional[Literal["NUMBER", "PERCENTAGE", "CURRENCY", "TEXT", "SCORE"]] = FieldInfo(
        alias="dataFormat", default=None
    )

    dates: Optional[List[datetime]] = None

    days_span: Optional[int] = FieldInfo(alias="daysSpan", default=None)

    delta: Optional[float] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    from_date: Optional[datetime] = FieldInfo(alias="fromDate", default=None)

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

    median: Optional[float] = None

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)

    series: Optional[List[TopicCreatePromptsResponseItemMentionFrequencySery]] = None

    to_date: Optional[datetime] = FieldInfo(alias="toDate", default=None)

    value: Optional[float] = None


class TopicCreatePromptsResponseItemSeoMetrics(BaseModel):
    cpc: Optional[float] = None

    search_volume: Optional[int] = FieldInfo(alias="searchVolume", default=None)


class TopicCreatePromptsResponseItem(BaseModel):
    answer_text: Optional[str] = FieldInfo(alias="answerText", default=None)

    important_terms: Optional[List[str]] = FieldInfo(alias="importantTerms", default=None)

    invocations: Optional[int] = None

    latest_run_data: Optional[datetime] = FieldInfo(alias="latestRunData", default=None)

    mention_frequency: Optional[TopicCreatePromptsResponseItemMentionFrequency] = FieldInfo(
        alias="mentionFrequency", default=None
    )

    negative_sentiments: Optional[List[Dict[str, str]]] = FieldInfo(alias="negativeSentiments", default=None)

    positive_sentiments: Optional[List[Dict[str, str]]] = FieldInfo(alias="positiveSentiments", default=None)

    prompt: Optional[str] = None

    prompt_analysis_id: Optional[str] = FieldInfo(alias="promptAnalysisId", default=None)

    prompt_id: Optional[str] = FieldInfo(alias="promptId", default=None)

    prompts_count: Optional[int] = FieldInfo(alias="promptsCount", default=None)

    ranking: Optional[float] = None

    seo_metrics: Optional[TopicCreatePromptsResponseItemSeoMetrics] = FieldInfo(alias="seoMetrics", default=None)

    share_of_voice: Optional[float] = FieldInfo(alias="shareOfVoice", default=None)

    sources: Optional[List[str]] = None


TopicCreatePromptsResponse: TypeAlias = List[TopicCreatePromptsResponseItem]
