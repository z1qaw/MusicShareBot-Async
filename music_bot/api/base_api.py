from abc import ABCMeta, abstractmethod
from collections.abc import Awaitable
import aiohttp


class BaseApi(ABCMeta):
    """Implementation of Base Music Services API Abstract class."""

    def __init__(self, client: aiohttp.ClientSession) -> None:
        self._client = client

    @abstractmethod
    async def search(self, query: str) -> Awaitable[dict]:
        """Make asynchronous search query to API Server via aiohttp.ClientSession"""
        pass
