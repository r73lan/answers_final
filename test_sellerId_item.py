import pytest
from sellerId_item_schema import SCHEMA_GET_SELLERID_ITEM_200_SUCCESS, SCHEMA_GET_SELLERID_ITEM_400_BADREQUEST
from jsonschema import validate
import random
import string

class TestGetSelleIdItem:
    @pytest.mark.parametrize("seller_id", [random.randint(10**i, 10**(i+1) - 1) for i in range(5)])
    def test_get_seller_id_item_by_seller_id_success_200(self, create_api, seller_id):
        api = create_api
        resp = api.seller_id_item.get_items_by_seller_id(seller_id)
        assert resp.status_code == 200  
        json_data = resp.json()
        print(json_data)
        validate(json_data, schema=SCHEMA_GET_SELLERID_ITEM_200_SUCCESS)

    @pytest.mark.parametrize("seller_id", [
        ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))),             
        None,            
        {}                
    ])
    def test_get_seller_id_item_by_seller_id_invalid_type_400(self, create_api, seller_id):
        api = create_api
        resp = api.seller_id_item.get_items_by_seller_id(seller_id)
        assert resp.status_code == 400  
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_GET_SELLERID_ITEM_400_BADREQUEST)