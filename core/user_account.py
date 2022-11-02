from collections import OrderedDict

from core.config import GLOBAL_INITIAL_ID
from core.helpers import csv_helper


class UserAccount:
    INITIAL_ID = GLOBAL_INITIAL_ID
    DEFAULT_PASSWORD = '$2a$11$nTv1VqTF7Yx40gjpjG00L.00vRe0ZB/SgxKbGtAr15lRnXmLt0nj6'

    def __init__(self, employee_list, count: int):
        # creating user accounts for managers only
        self.employee_list_for_user = employee_list[:count]

    def get_data(self):
        data_list = []

        for i, employee_dict in enumerate(self.employee_list_for_user):
            data_list.append(OrderedDict({
                'id': self.INITIAL_ID + i,
                'employee_id': employee_dict.get('id'),
                'username': f"{employee_dict.get('first_name')}{employee_dict.get('last_name')}",
                'email': employee_dict.get('email_work'),
                'password': self.DEFAULT_PASSWORD,
                'last_password_changed_date': 'GETDATE()',
                'is_active': 1,
                'is_account_activated': 1,
                'is_activation_email_sent': 1,
                'created_at': 'GETDATE()',
                'updated_at': 'GETDATE()',
                'is_onboarding_complete': 1,
                'saml_sso_user_identifier': f"manager+{employee_dict.get('id')}",
                'is_locked': 0,
                'display_name': employee_dict.get('first_name'),
                'should_notify_team_changes': 0
            }))

        return data_list

    def generate_csv(self):
        """
        gets data, generates csv from the data and returns the same data
        :return: return a list of user dict having length as count
        """
        data_list = self.get_data()
        if data_list:
            headers = list(data_list[0].keys())
            rows = [list(user_account.values()) for user_account in data_list]
            csv_helper.write_csv('user_accounts.csv', headers, rows, 'User accounts csv successfully generated.')
        return data_list
