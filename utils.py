from faker import Faker

class GeneratePostDataInputItem:
    faker = Faker("ru_RU")

    def generate_correct_data_with_minimum_parameters(self):
        return {
            "sellerID": self.faker.random_int(min=111111, max=999999),
            "name": self.faker.name(),
            "price": self.faker.random_int(min=100, max=100000),
        }
    
    def generate_correct_data_with_additional_parameters(self):
        return {
            "sellerID": self.faker.random_int(min=111111, max=999999),
            "name": self.faker.name(),
            "price": self.faker.random_int(min=100, max=100000),
            "testField": self.faker.random_int(min=1, max=100000)
        }
    
    def generate_incorrect_sellerID_data_type(self):
        return {
            "sellerID": self.faker.word(),  #строка вместо int
            "name": self.faker.name(),
            "price": self.faker.random_int(min=50, max=100000),
        }
    
    def generate_incorrect_name_data_type(self):
        return {
            "sellerID": self.faker.random_int(min=111111, max=999999),
            "name": self.faker.random_int(),  #int вместо string
            "price": self.faker.random_int(min=50, max=100000),
        }
    
    def generate_incorrect_price_data_type(self):
        return {
            "sellerID": self.faker.random_int(min=111111, max=999999),
            "name": self.faker.name(),
            "price": self.faker.word()   #строка вместо int
        }

