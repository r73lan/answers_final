import pytest
from jsonschema import validate
import uuid
import re

from utils import GeneratePostDataInputItem

from item_schema import SCHEMA_GET_ITEMS_200_SUCCESS, SCHEMA_GET_ITEMS_404_NOT_FOUND, SCHEMA_POST_ITEMS_200_SUCCESS, SCHEMA_POST_ITEMS_400_BADREQUEST  
from sellerId_item_schema import SCHEMA_GET_SELLERID_ITEM_200_SUCCESS

class TestGetItem:
    @pytest.mark.parametrize(
        'existing_id_adv',
        ['34553ac8-4b07-404c-8ea3-c284c24a59a9']
    )
    def test_get_item_by_id_code_200(self, create_api, existing_id_adv):
        api = create_api
        resp = api.item.get_item_by_id(id=existing_id_adv)
        assert resp.status_code == 200
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_GET_ITEMS_200_SUCCESS)

    @pytest.mark.parametrize(
        'nonexisting_id_adv',
        [str(uuid.uuid4()) for _ in range(1)]
    )
    def test_get_item_by_id_if_id_doesnt_exist_code_404(self, create_api, nonexisting_id_adv):
        api = create_api
        resp = api.item.get_item_by_id(id=nonexisting_id_adv)
        assert resp.status_code == 404
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_GET_ITEMS_404_NOT_FOUND)

class TestPostItem:
    generate_data = GeneratePostDataInputItem()
    uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

    @pytest.mark.parametrize("data_1", [generate_data.generate_correct_data_with_minimum_parameters()])
    def test_post_creates_item_and_get_by_adv_id_returns_it(self, create_api, data_1):
        api = create_api
        resp = api.item.post(data=data_1)
        assert resp.status_code == 200
        json_post_data = resp.json()
        validate(json_post_data, schema=SCHEMA_POST_ITEMS_200_SUCCESS)

        uuid_match = re.search(self.uuid_pattern, resp.text)
        assert uuid_match
        uuid_adv = uuid_match.group(0) 
        

        responce_get_item_by_id = api.item.get_item_by_id(id=uuid_adv)
        assert responce_get_item_by_id.status_code == 200
        json_get_data = responce_get_item_by_id.json()
        validate(json_get_data, schema=SCHEMA_GET_ITEMS_200_SUCCESS)

        created_adv_data = json_get_data[0]
        assert created_adv_data["sellerId"] == data_1["sellerID"], f'sellerIds error: created sellerID in adv: "{created_adv_data["sellerId"]}" doesnt equal with POST\item data"{data_1["sellerID"] }"'
        assert created_adv_data["name"] == data_1["name"], f'names error: created name in adv: "{created_adv_data["name"]}" doesnt equal with POST\item data: "{data_1["name"]}"'
        assert created_adv_data["price"] == data_1["price"], f'prices error: created price in adv: "{created_adv_data["price"]}" doesnt equal with POST\item data: "{data_1["price"]}"'


        
    @pytest.mark.parametrize("data_2", [generate_data.generate_correct_data_with_minimum_parameters()])
    def test_post_creates_item_and_get_by_seller_id_returns_it(self, create_api, data_2):
        api = create_api
        resp = api.item.post(data=data_2)
        assert resp.status_code == 200
        json_post_data = resp.json()
        validate(json_post_data, schema=SCHEMA_POST_ITEMS_200_SUCCESS)

        uuid_match = re.search(self.uuid_pattern, resp.text)
        assert uuid_match
        uuid_adv = uuid_match.group(0) 
        
        responce_get_item_by_seller_id = api.seller_id_item.get_items_by_seller_id(data_2["sellerID"])
        assert responce_get_item_by_seller_id.status_code == 200
        json_get_data = responce_get_item_by_seller_id.json()
        validate(json_get_data, schema=SCHEMA_GET_SELLERID_ITEM_200_SUCCESS)

        is_adv_in_seller_list = any((item["id"] == uuid_adv and item["name"] == data_2["name"] and item["price"] == data_2["price"]) for item in json_get_data)
        assert is_adv_in_seller_list, "created adv isnt in seller's advs list"


    @pytest.mark.parametrize("data_3", [generate_data.generate_correct_data_with_additional_parameters()])
    def test_post_correct_data_with_additional_parameters(self, create_api, data_3):
        api = create_api
        resp = api.item.post(data=data_3)
        assert resp.status_code == 200
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_POST_ITEMS_200_SUCCESS)

    @pytest.mark.parametrize("data_4", [generate_data.generate_correct_data_with_minimum_parameters()])
    def test_post_correct_data_with_minimum_parameters(self, create_api, data_4):
        api = create_api
        resp = api.item.post(data=data_4)
        assert resp.status_code == 200
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_POST_ITEMS_200_SUCCESS)

    @pytest.mark.parametrize("data_5", [generate_data.generate_incorrect_sellerID_data_type()])
    def test_post_incorrect_data_seller_id(self, create_api, data_5):
        api = create_api
        resp = api.item.post(data=data_5)
        assert resp.status_code == 400
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_POST_ITEMS_400_BADREQUEST)

    @pytest.mark.parametrize("data_6", [generate_data.generate_incorrect_name_data_type()])
    def test_post_incorrect_data_name(self, create_api, data_6):
        api = create_api
        resp = api.item.post(data=data_6)
        assert resp.status_code == 400
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_POST_ITEMS_400_BADREQUEST)

    @pytest.mark.parametrize("data_7", [generate_data.generate_incorrect_price_data_type()])
    def test_post_incorrect_data_price(self, create_api, data_7):
        api = create_api
        resp = api.item.post(data=data_7)
        assert resp.status_code == 400
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_POST_ITEMS_400_BADREQUEST)
