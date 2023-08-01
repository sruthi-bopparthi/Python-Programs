import json
from jsondiff import diff


def find_difference(file1, file2):
    data1 = json.load(file1)
    data2 = json.load(file2)
    for i in data1:
        value = data1[i]
        for j in value:
            if 'avg_price_total_in_usd' in j:
                del j["avg_price_total_in_usd"]

    for i in data2:
        value = data2[i]
        for j in value:
            if 'avg_price_total_in_usd' in j:
                del j["avg_price_total_in_usd"]

    difference_data1 = diff(data1, data2, marshal=True)
    print(difference_data1)

    first_difference_file_name = 'first_difference.json'
    with open(f'{output_file_path}/{first_difference_file_name}', 'w', encoding='utf8') as write_file:
        json.dump(difference_data1, write_file, indent=2, separators=(',', ': '))


if __name__ == '__main__':
    input_file_path = './input_data_files'
    output_file_path = './output_data_files'

    # Edit the file names based on requirements
    first_file_name = ''
    second_file_name = ''

    first_file = open(f'{input_file_path}/{first_file_name}')
    second_file = open(f'{input_file_path}/{second_file_name}')

    find_difference(first_file, second_file)
