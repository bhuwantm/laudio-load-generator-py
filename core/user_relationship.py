from collections import OrderedDict

from core.config import GLOBAL_INITIAL_ID
from core.helpers import csv_helper


class UserRelationships:
    """
    Currently creating relationship with maggie only
    """
    INITIAL_ID = GLOBAL_INITIAL_ID
    MANAGER_ID = 8

    def __init__(self, employee_list):
        # creating user accounts for managers only
        self.employee_list = employee_list

    def get_data(self):
        data_list = []

        for i, employee_dict in enumerate(self.employee_list):
            data_list.append(OrderedDict({
                'id': self.INITIAL_ID + i,
                'user_account_id': self.MANAGER_ID,
                'employee_id': employee_dict.get('id'),
                'type': 'PRIMARY_MANAGER',
                'inverse_type ': 'PRIMARY_EMPLOYEE',
                'is_hr_relationship': 1,
                'relationship_type': 'PRIMARY',
                'created_at': 'GETDATE()',
                'updated_at': 'GETDATE()',
                'user_team_configuration_ids': '[10]'
            }))

        return data_list

    def generate_csv(self):
        """
        gets data, generates csv from the data and returns the same data
        :return: return a list of user relationship dict
        """
        data_list = self.get_data()
        if data_list:
            headers = list(data_list[0].keys())
            rows = [list(user_relationship.values()) for user_relationship in data_list]
            csv_helper.write_csv('user_relationships.csv', headers, rows,
                                 'User relationships csv successfully generated.')
        return data_list
