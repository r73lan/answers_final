from baseapi import BaseAPI
from typing import Optional

class Statistic(BaseAPI):
    endpoint = 'statistic'

    def get_statistic_by_id(self, id: Optional[str]):
        url = f"{self.url}/{id}"
        response = self.context.get(
            url=url,
        )
        return response

    @property
    def statistic(self):
        return self.add_child(Statistic)