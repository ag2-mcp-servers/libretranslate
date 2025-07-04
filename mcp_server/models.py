# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T04:15:54+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field, RootModel, confloat


class Detection(BaseModel):
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Confidence value', examples=[0.6]
    )
    language: Optional[str] = Field(None, description='Language code', examples=['en'])


class Detections(RootModel[List[Detection]]):
    root: List[Detection]


class ErrorResponse(BaseModel):
    error: Optional[str] = Field(None, description='Error message')


class ErrorSlowDown(BaseModel):
    error: Optional[str] = Field(None, description='Reason for slow down')


class Source(BaseModel):
    code: Optional[str] = Field(None, description='Language code')
    name: Optional[str] = Field(
        None, description='Human-readable language name (in English)'
    )


class Target(BaseModel):
    code: Optional[str] = Field(None, description='Language code')
    name: Optional[str] = Field(
        None, description='Human-readable language name (in English)'
    )


class Language(BaseModel):
    source: Optional[Source] = None
    target: Optional[Target] = None


class FrontendSettings(BaseModel):
    apiKeys: Optional[bool] = Field(
        None, description='Whether the API key database is enabled.'
    )
    charLimit: Optional[int] = Field(
        None,
        description='Character input limit for this language (-1 indicates no limit)',
    )
    frontendTimeout: Optional[int] = Field(
        None, description='Frontend translation timeout'
    )
    keyRequired: Optional[bool] = Field(
        None, description='Whether an API key is required.'
    )
    language: Optional[Language] = None
    suggestions: Optional[bool] = Field(
        None, description='Whether submitting suggestions is enabled.'
    )
    supportedFilesFormat: Optional[List[str]] = Field(
        None, description='Supported files format'
    )


class Language1(BaseModel):
    code: Optional[str] = Field(None, description='Language code')
    name: Optional[str] = Field(
        None, description='Human-readable language name (in English)'
    )
    targets: Optional[List[str]] = Field(
        None, description='Supported target language codes'
    )


class Languages(RootModel[List[Language1]]):
    root: List[Language1]


class SuggestResponse(BaseModel):
    success: Optional[bool] = Field(
        None, description='Whether submission was successful'
    )


class Translate(BaseModel):
    translatedText: Optional[Union[str, List]] = Field(
        None, description='Translated text(s)'
    )


class TranslateFile(BaseModel):
    translatedFileUrl: Optional[str] = Field(None, description='Translated file url')
