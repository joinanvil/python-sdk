# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BetaCreateTopicResponse",
    "BetaCreateTopicResponseItem",
    "BetaCreateTopicResponseItemAverageRanking",
    "BetaCreateTopicResponseItemAverageRankingSery",
    "BetaCreateTopicResponseItemMentionRate",
    "BetaCreateTopicResponseItemMentionRateSery",
    "BetaCreateTopicResponseItemShareOfVoice",
    "BetaCreateTopicResponseItemShareOfVoiceSery",
    "BetaCreateTopicResponseItemTopic",
    "BetaCreateTopicResponseItemTopicPrompt",
    "BetaCreateTopicResponseItemTopicTag",
]


class BetaCreateTopicResponseItemAverageRankingSery(BaseModel):
    date: datetime

    value: float


class BetaCreateTopicResponseItemAverageRanking(BaseModel):
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

    series: Optional[List[BetaCreateTopicResponseItemAverageRankingSery]] = None

    to_date: Optional[datetime] = FieldInfo(alias="toDate", default=None)

    value: Optional[float] = None


class BetaCreateTopicResponseItemMentionRateSery(BaseModel):
    date: datetime

    value: float


class BetaCreateTopicResponseItemMentionRate(BaseModel):
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

    series: Optional[List[BetaCreateTopicResponseItemMentionRateSery]] = None

    to_date: Optional[datetime] = FieldInfo(alias="toDate", default=None)

    value: Optional[float] = None


class BetaCreateTopicResponseItemShareOfVoiceSery(BaseModel):
    date: datetime

    value: float


class BetaCreateTopicResponseItemShareOfVoice(BaseModel):
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

    series: Optional[List[BetaCreateTopicResponseItemShareOfVoiceSery]] = None

    to_date: Optional[datetime] = FieldInfo(alias="toDate", default=None)

    value: Optional[float] = None


class BetaCreateTopicResponseItemTopicPrompt(BaseModel):
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


class BetaCreateTopicResponseItemTopicTag(BaseModel):
    color_hex: str = FieldInfo(alias="colorHex")

    name: str

    website_topic_id: str = FieldInfo(alias="websiteTopicId")

    id: Optional[str] = None

    topic_ids: Optional[List[str]] = FieldInfo(alias="topicIds", default=None)


class BetaCreateTopicResponseItemTopic(BaseModel):
    id: Optional[str] = None

    archived: Optional[bool] = None

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

    last_run: Optional[datetime] = FieldInfo(alias="lastRun", default=None)

    llm_provider: Optional[str] = FieldInfo(alias="llmProvider", default=None)

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

    prompts: Optional[List[BetaCreateTopicResponseItemTopicPrompt]] = None

    seo_keyword_index: Optional[int] = FieldInfo(alias="seoKeywordIndex", default=None)

    tags: Optional[List[BetaCreateTopicResponseItemTopicTag]] = None

    text: Optional[str] = None

    website_id: Optional[str] = FieldInfo(alias="websiteId", default=None)


class BetaCreateTopicResponseItem(BaseModel):
    archived: Optional[bool] = None

    average_ranking: Optional[BetaCreateTopicResponseItemAverageRanking] = FieldInfo(
        alias="averageRanking", default=None
    )

    mention_rate: Optional[BetaCreateTopicResponseItemMentionRate] = FieldInfo(alias="mentionRate", default=None)

    prompts_count: Optional[int] = FieldInfo(alias="promptsCount", default=None)

    roi: Optional[float] = None

    search_volume: Optional[int] = FieldInfo(alias="searchVolume", default=None)

    share_of_voice: Optional[BetaCreateTopicResponseItemShareOfVoice] = FieldInfo(alias="shareOfVoice", default=None)

    started: Optional[bool] = None

    topic: Optional[BetaCreateTopicResponseItemTopic] = None


BetaCreateTopicResponse: TypeAlias = List[BetaCreateTopicResponseItem]
