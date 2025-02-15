from typing import Optional, Type, TypeVar

import furl
import requests

BaseAPIType = TypeVar('BaseAPIType', bound='BaseAPI')

class BaseAPI:
    endpoint: str = ''

    def __init__(self, context: requests.Session, parent: Optional[BaseAPIType] = None):
        self.context = context
        self.parent = parent

    def add_child(self, api_class: Type['BaseAPI']) -> BaseAPIType:
        return api_class(context=self.context, parent=self)

    def get(self, *args, **kwargs):
        response = self.context.get(
            url=self.url,
            *args,
            **kwargs,
        )
        return response

    def post(self, data: dict, *args, **kwargs):
        response = self.context.post(
            url=self.url,
            json=data,
            *args,
            **kwargs
        )
        return response
    
    @property
    def url(self) -> str:
        if self.parent:
            url = furl.furl(self.parent.url)
            url.add(path=self.endpoint)
        else:
            url = furl.furl(self.endpoint)
        return url.url
