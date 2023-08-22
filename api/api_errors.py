import django
django.setup()
from sefaria.model import *
from typing import List
from enum import Enum

class APIWarningCode(Enum):
    APINoVersion = 101
    APINoLanguageVersion = 102
    APINoSourceText = 103

"""
classes for data errors in API calls.
used when part of the data that was requested exists and returned, and part is missing.  
"""

class APIDataError():
    """
    general class
    """

    def __init__(self):
        pass


class TextsAPIResponseMessage(APIDataError):
    """
    class for returning a message and an error code
    """

    def get_message(self) -> dict:
        return {'error_code': self.error_code,
                'message': self.message}


class APINoVersion(TextsAPIResponseMessage):

    def __init__(self, oref: Ref, vtitle: str, lang: str):
        self.error_code = APIWarningCode.APINoVersion.value
        self.message = f'We do not have version named {vtitle} with language code {lang} for {oref}'


class APINoLanguageVersion(TextsAPIResponseMessage):

    def __init__(self, oref: Ref, langs: List[str]):
        self.error_code = APIWarningCode.APINoLanguageVersion.value
        self.message = f'We do not have the code language you asked for {oref}. Available codes are {langs}'


class APINoSourceText(TextsAPIResponseMessage):

    def __init__(self, oref: Ref):
        self.error_code = APIWarningCode.APINoSourceText.value
        self.message = f'We do not have the source text for {oref}'
