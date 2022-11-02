import random
from collections import OrderedDict
from enum import Enum

from core.config import GLOBAL_INITIAL_ID
from core.helpers import utils, csv_helper
from core.helpers.global_faker import GlobalFakerComposer


class EmployeeType(Enum):
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'


class Employee:
    INITIAL_ID = GLOBAL_INITIAL_ID
    MANAGER_ID = 53  # manager id for all manager

    MANAGER_COUNT = 10
    US_TIME_ZONE = 8
    PROFILE_PIC_ID = 67
    CLIENT_EMPLOYEE_ID_START = 10000
    ZIP = [27616, 27610, 27610, 27520]
    JOB_CODE = [
        309630, 324530, 504830, 505430, 505539, 506450, 506821, 506921, 507021, 507130, 508230, 508730, 509730, 5435
    ]
    EMPLOYEE_JOB_TITLE = (
        "Associate Director, Ambulatory",
        "Associate Director, Cancer Center",
        "Associate Director, Emergency",
        "Associate Director, Medical / Surgical Nursing",
        "Associate Director, Perioperative",
        "Care Associate",
        "CNA",
        "Director",
        "Manager",
        "Office Manager",
        "Patient Services Coordinator",
        "RN",
        "Team Lead",
        "Technician",
        "Unit Secretary"
    )

    # foreign key range based on reference from xwalk
    FTE_STATUS_IDS = [1, 3]
    EMPLOYEE_ROLES_IDS = [1, 14]
    DEGREE_LEVEL_IDS = [1, 6]
    STATES = [1, 204]
    COUNTRIES = [1, 252]
    SHIFTS = [1, 2]
    FACILITIES = [1, 2]

    # random range
    COST_CENTER = [8, 41]
    JOIN_DAY_REDUCTION_RANGE = [0, 2000]
    CREATED_AT_RANGE = [20, 1000]
    UPDATED_AT_RANGE = [0, 19]
    CURRENTLY_HOUR_RATE = [20, 40]
    YEARS_OF_EXP = [0, 20]
    DOB_MONTH = [1, 12]
    DOB_DAY = [1, 28]
    DOB_YEAR = [1970, 2000]

    def __init__(self, count: int):
        if count % 2 != 0 or count < 0:
            raise AttributeError(f'Count must be an even positive number. Wrong value {count} supplied.')

        self.count = count
        self.male_count = int(count / 2)
        self.female_count = int(count / 2)
        self.global_faker_composer = GlobalFakerComposer()
        self.male_names = self.global_faker_composer.get_unique_male_names(self.male_count)
        self.female_names = self.global_faker_composer.get_unique_female_names(self.female_count)
        self.names = self.male_names + self.female_names
        self.address_streets = self.global_faker_composer.get_street_address(count)
        self.cities = self.global_faker_composer.get_cities(count)

    def get_join_date(self):
        return f'DATEADD(DAY, -{utils.get_random_from_range(self.JOIN_DAY_REDUCTION_RANGE)}, GETDATE())'

    def get_work_email(self, employee_id):
        return f'nurse+{employee_id}@laudio.com'

    def get_personal_email(self, employee_id):
        return f'nurse+{employee_id}@gmail.com'

    def get_gender(self, i):
        return 'M' if i < self.male_count else 'F'

    def get_client_employee_id(self, i):
        return self.CLIENT_EMPLOYEE_ID_START + i

    def get_create_at(self):
        return f'DATEADD(DAY, -{utils.get_random_from_range(self.CREATED_AT_RANGE)}, GETDATE())'

    def get_updated_at(self):
        return f'DATEADD(DAY, -{utils.get_random_from_range(self.UPDATED_AT_RANGE)}, GETDATE())'

    def get_manager_employee_id(self, i):
        if i < self.MANAGER_COUNT:
            return self.MANAGER_ID
        return utils.get_random_from_range([self.INITIAL_ID, self.INITIAL_ID + self.MANAGER_COUNT])

    def get_data(self):
        """
        :return: return a list of employee dict having length as count
        """
        data_list = []

        for i, name in enumerate(self.names):
            first_name, last_name = name.split(" ", 1)
            employee_type = EmployeeType.MANAGER.value if i < self.MANAGER_COUNT else EmployeeType.EMPLOYEE.value

            data_list.append(OrderedDict({
                'id': i + self.INITIAL_ID,
                'join_date': self.get_join_date(),
                'most_recent_hire_date': None,
                'type': employee_type,
                'termination_date': None,
                'termination_reason': None,
                'is_active': 1,
                'first_name': first_name,
                'middle_name': None,
                'last_name': last_name,
                'cost_center_id': utils.get_random_from_range(self.COST_CENTER),
                'fte_status_id': utils.get_random_from_range(self.FTE_STATUS_IDS),
                'primary_employee_role_id': utils.get_random_from_range(self.EMPLOYEE_ROLES_IDS),
                'pay_level': None,
                'current_hourly_rate': utils.get_random_from_range(self.CURRENTLY_HOUR_RATE),
                'degree_level_id': utils.get_random_from_range(self.DEGREE_LEVEL_IDS),
                'generation_id': None,
                'years_of_experience': utils.get_random_from_range(self.YEARS_OF_EXP),
                'dob_month': utils.get_random_from_range(self.DOB_MONTH),
                'dob_day': utils.get_random_from_range(self.DOB_DAY),
                'dob_year': utils.get_random_from_range(self.DOB_YEAR),
                'email_work': self.get_work_email(i),
                'email_personal': self.get_personal_email(i),
                'address_street': self.address_streets[i],
                'address_street2': None,
                'address_city': self.cities[i],
                'address_state_id': utils.get_random_from_range(self.STATES),
                'address_zip': random.choice(self.ZIP),
                'address_country_id': utils.get_random_from_range(self.COUNTRIES),
                'timezone_id': self.US_TIME_ZONE,
                'phone_work': None,
                'phone_cell': None,
                'phone_home': None,
                'profile_pic_link': None,
                'profile_pic_file_id': self.PROFILE_PIC_ID,
                'gender': self.get_gender(i),
                'shift_id': utils.get_random_from_range(self.SHIFTS),
                'client_employee_id': self.get_client_employee_id(i),
                'created_at': self.get_create_at(),
                'updated_at': self.get_updated_at(),
                'is_terminated': 0,
                'manager_employee_id': self.get_manager_employee_id(i),
                'available_pto_hours': None,
                'preferred_name': random.choice([None, first_name]),
                'sso_username': None,
                'anniversary_date': None,
                'job_code_start_date': None,
                'job_title': random.choice(self.EMPLOYEE_JOB_TITLE),
                'facility_id': utils.get_random_from_range(self.FACILITIES),
                'is_dropped': 0,
                'union_name': None,
                'job_code': random.choice(self.JOB_CODE),
                'state_seniority_date': None
            }))

        return data_list

    def generate_csv(self):
        """
        gets data, generates csv from the data and returns the same data
        :return: return a list of employee dict having length as count
        """
        data_list = self.get_data()
        if data_list:
            headers = list(data_list[0].keys())
            rows = [list(employee_dict.values()) for employee_dict in data_list]
            csv_helper.write_csv('employees.csv', headers, rows, 'Employee csv successfully generated.')
        return data_list
