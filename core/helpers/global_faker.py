from faker import Faker
from faker.providers import person, address


class GlobalFakerComposer:
    def __init__(self):
        Faker.seed(0)
        self.fake = Faker()
        self.fake.add_provider(person)
        self.fake.add_provider(address)

    def get_list(self, count: int, fn):
        """
        :param count: desired number of items in the list
        :param fn: function that generates fake data
        :return: list with length of count
        """
        return [fn() for _ in range(count)]

    def get_unique_list(self, count: int, fn):
        """
        :param count: required number of unique valued items
        :param fn: function that generates fake data
        :return: unique item list with length of count
        """
        generated_list = []
        iteration_count = 0
        while len(set(generated_list)) < count:
            iteration_count += 1
            print(f"Iteration for unique list: {iteration_count}")
            generated_list = [fn() for _ in range(count * 2)]
        return generated_list[:count]

    def _get_name_without_prefix_suffix(self):
        """
        :return: string with first_name and last_name without any prefix and suffix like Dr. Mr.
        """
        return f'{self.fake.first_name()} {self.fake.last_name()}'

    def _get_male_name_without_prefix_suffix(self):
        """
        :return: string with male_first_name and last_name without any prefix and suffix like Dr. Mr.
        """
        return f'{self.fake.first_name_male()} {self.fake.last_name()}'

    def _get_female_name_without_prefix_suffix(self):
        """
        :return: string with female_first_name and last_name without any prefix and suffix like Dr. Mr.
        """
        return f'{self.fake.first_name_female()} {self.fake.last_name()}'

    def get_unique_male_names(self, count: int):
        """
        :return: string with unique male first and last name
        """
        return self.get_unique_list(count, self._get_male_name_without_prefix_suffix)

    def get_unique_female_names(self, count: int):
        """
        :return: string with unique female first and last name
        """
        return self.get_unique_list(count, self._get_female_name_without_prefix_suffix)

    def get_unique_names(self, count: int):
        """
        :return: string with unique first and last name
        """
        return self.get_unique_list(count, self._get_name_without_prefix_suffix)

    def get_street_address(self, count: int):
        """
        :return: random street address as string
        """
        return self.get_list(count, self.fake.street_address)

    def get_cities(self, count: int):
        """
        :return: random city of the world as string
        """
        return self.get_list(count, self.fake.city)
