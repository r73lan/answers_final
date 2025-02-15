import furl
import requests

from constants import HOST
from baseapi import BaseAPI
from item import Item
from statistic import Statistic
from sellerId_item import sellerIdItem

from typing import TypeVar
APIType = TypeVar('APIType', bound='API')

class API(BaseAPI):
    endpoint = HOST

    def __init__(self, context: requests.Session):
        self.endpoint = str(furl.furl(self.endpoint))
        super().__init__(context)

    @property
    def item(self) -> Item:
        return self.add_child(Item)
    
    @property
    def statistic(self) -> Statistic:
        return self.add_child(Statistic)
    
    @property
    def seller_id_item(self) -> sellerIdItem:
        return self.add_child(sellerIdItem)
