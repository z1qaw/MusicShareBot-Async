from typing import Set
from collections.abc import Awaitable
from .types import ApiObjectNamesPlural, ApiObjectName
from aiohttp import ClientSession

from ..base_api import BaseApi
from .exceptions import NoAuthCredsError


class AppleMusicApi(BaseApi):
    api_host = 'https://amp-api.music.apple.com'

    def __init__(self, client: ClientSession, auth_key: str) -> None:
        super().__init__(client)

        if not auth_key:
            raise NoAuthCredsError('You must specify auth_key')

        self._auth_key = auth_key

    async def _make_api_request(self, api_method_path: str, params: dict) -> Awaitable[dict]:
        api_method_uri = self.api_host + api_method_path
        headers = {
            'authorization': self._auth_key
        }
        response = await self._client.get(api_method_uri, params=params, headers=headers)
        return response.json()

    async def search(self, query: str, limit: int = 25,
                     object_types: Set[ApiObjectName] = ApiObjectNamesPlural
                     ) -> Awaitable[dict]:
        api_method_path = '/v1/catalog/ru/search'
        params = {
            'term': query,
            'types': ','.join([obj.value for obj in list(object_types)]),
            'limit': limit,
            'with': 'serverBubbles'
        }
        return await self._make_api_request(api_method_path, params)
