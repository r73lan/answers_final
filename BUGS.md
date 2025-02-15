# Баг репорт

1. Метод ```GET \item``` при запросе с id несуществующего объявления не соответствует json-схеме <br>

Тест-кейс: <br>

    1. Отправить запрос https://qa-internship.avito.com/api/1/item/b861296a-e6fc-475e-8bac-67628bc1cb58 <br>

    Ожидаемое поведение: <br>
    'messages': { }, т.к. ('messages': {'type': 'object'} из swagger.yaml) <br> 

    Фактический результат: <br> 
    'messages': null <br>

    Исследование: <br>

    ```FAILED test_item.py::TestGetItem::test_get_item_by_id_if_id_doesnt_exist_code_404[b861296a-e6fc-475e-8bac-67628bc1cb58] - jsonschema.exceptions.ValidationError: None is not of type 'object'``` <br> 

2. Метод ```GET \item``` при запросе с id несуществующего объявления не соответствует json-схеме <br>

Тест-кейс: <br>

    Отправить запрос https://qa-internship.avito.com/api/1/statistic/2ae39465-fec1-48b8-97c8-81e6f931c661 <br>
    
    Ожидаемое поведение: <br>
    'messages': { }, т.к. ('messages': {'type': 'object'} из swagger.yaml) <br> 
    
    Фактический результат: <br> 
    'messages': null <br> 
    
    Исследование: <br>
    ```FAILED test_statistic.py::TestGetStatistic::test_get_statistic_by_id_if_id_doesnt_exist_404[165a6e61-af07-4514-936b-5baee70a0a79] - jsonschema.exceptions.ValidationError: None is not of type 'object'``` <br> 


3. Метод ```POST \item``` неверно создает объявления<br>

Тест-кейс: <br>
    1. Создать объявление у любого продавца <br>
    2. Из responce запроса узнать id_adv обхявления
    3. Сделать ```GET \item\{id_adv}``` запрос <br>
    
    Ожидаемое поведение: <br>
    ```GET \item\{id_adv}``` будет создержать поля с такими же значениями, как при создании запроса <br> 
    
    Фактический результат: <br> 
    поле "name" у ```GET \item\{id_adv}``` не совпадает со значением при создании объявления ```POST \item```
    
    Исследование: <br>
    ```FAILED test_item.py::TestPostItem::test_post_creates_item_and_get_by_adv_id_returns_it[data_10] - AssertionError: names error: created name in adv: "dsdsd" doesnt equal with POST\item data: "Савина Ангелина Даниловна"``` <br> 

3. Метод ```POST \item``` неверно создает объявления<br>
Тест-кейс: <br>
    1. Создать объявление у любого продавца <br>
    2. Из responce запроса узнать id_adv объявления
    3. Сделать ```GET \{selleID}\item\``` запрос <br>
    
    Ожидаемое поведение: <br>
    ответ ```GET \{selleID}\item\``` будет создержать товар с такими же значениями полей ```name```, ```price```, ```id_adv```, как при создании запроса <br> 
    
    Фактический результат: <br> 
    поле "name" у ```GET \item\{id_adv}``` не совпадает со значением при создании объявления ```POST \item``` <br>
    
    Исследование: <br>
    ```FAILED test_item.py::TestPostItem::test_post_creates_item_and_get_by_seller_id_returns_it[data_20] - AssertionError: created adv isnt in seller's advs list```



