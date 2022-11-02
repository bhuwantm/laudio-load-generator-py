import csv
import os

from core.config import OUTPUT_LOCATION

TEMP_ESCAPE_CHARACTER = '|'


def format_row(row):
    """
    Format row before writing to csv.
    Data is modified here based on our needs before writing to the file.
    :param row: list of values
    :return: formatted list of values
    """
    formatted_row = []
    for x in row:
        # setting None as NULL
        if x is None:
            formatted_row.append('NULL')
            continue
        if isinstance(x, str) and 'GETDATE(' in x:
            formatted_row.append(x)
            continue
        if isinstance(x, str) and 'GETDATE(' in x:
            formatted_row.append(x)
            continue
        if isinstance(x, str) and 'CAST(' in x:
            formatted_row.append(x)
            continue
        # adding quotes to string manually
        if isinstance(x, str):
            formatted_row.append(f"'{x}'")
            continue
        formatted_row.append(x)
    return formatted_row


def csv_post_processing(path):
    """
    replaces our placeholder escape character with actual comma
    :param path: file path
    :return: None
    """
    with open(path, 'r') as file:
        file_data = file.read()
        file_data = file_data.replace(TEMP_ESCAPE_CHARACTER, ',')

    with open(path, 'w') as file:
        file.write(file_data)

def write_csv(filename, headers, rows, success_msg=None):
    """
    generates a csv file at the output location with given filename
    :param filename: name of csv file
    :param headers: list of title of each comma seperated value
    :param rows: list of data that needs to be written to the file
    :param success_msg: custom message to show csv has been created
    :return: None
    """
    if headers and rows:
        path = os.path.join(OUTPUT_LOCATION, filename)
        with open(path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=TEMP_ESCAPE_CHARACTER)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(format_row(row))
        csv_post_processing(path)
        print(success_msg or 'Csv written successfully.')
    else:
        print('Nothing to write.')

