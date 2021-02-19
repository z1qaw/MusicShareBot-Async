from abc import ABCMeta, abstractmethod
import aiohttp


class BaseApi(ABCMeta):
    def __init__(self, client: aiohttp.ClientSession):
        self._client = client

    @abstractmethod
    async def search(self, query: str):
        pass
