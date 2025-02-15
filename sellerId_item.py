from baseapi import BaseAPI

class sellerIdItem(BaseAPI):
    endpoint = r'sellerId/item'

    def get_items_by_seller_id(self, seller_id: int):
        url = self.url.replace('sellerId', str(seller_id))
        responce = self.context.get(url=url)
        return responce
