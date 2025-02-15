from baseapi import BaseAPI
from typing import Optional

class Item(BaseAPI):
    endpoint = 'item'

    def get_item_by_id(self, id: Optional[str], url: Optional[str] = None, *args, **kwargs):
        url = f"{self.url}/{id}"
        response = self.context.get(
            url=url,
            *args,
            **kwargs,
        )
        return response

    @property
    def item(self):
        return self.add_child(Item)
