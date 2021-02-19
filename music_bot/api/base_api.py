from abc import ABCMeta, abstractmethod
import aiohttp


class BaseApi(ABCMeta):
    """Implementation of Base Music Services API Abstract class."""

    def __init__(self, client: aiohttp.ClientSession):
        self._client = client

    @abstractmethod
    async def search(self, query: str):
        """Make asynchronous search query to API Server via aiohttp.ClientSession"""
        pass
