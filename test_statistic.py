import pytest
from jsonschema import validate
import uuid

from statistic_schema import SCHEMA_GET_STAT_200_SUCCESS, SCHEMA_GET_STAT_404_NOT_FOUND



class TestGetStatistic:
    @pytest.mark.parametrize(
        'existing_id_adv',
        ['34553ac8-4b07-404c-8ea3-c284c24a59a9']
    )
    def test_get_statistic_by_id_200(self, create_api, existing_id_adv):
        api = create_api
        resp = api.statistic.get_statistic_by_id(id=existing_id_adv)
        assert resp.status_code == 200
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_GET_STAT_200_SUCCESS)

    @pytest.mark.parametrize(
        'nonexisting_id_adv',
        [str(uuid.uuid4()) for _ in range(1)]
    )
    def test_get_statistic_by_id_if_id_doesnt_exist_404(self, create_api, nonexisting_id_adv):
        api = create_api
        resp = api.statistic.get_statistic_by_id(id=nonexisting_id_adv)
        assert resp.status_code == 404
        json_data = resp.json()
        validate(json_data, schema=SCHEMA_GET_STAT_404_NOT_FOUND)
