import json
from jsondiff import diff
import deepdiff

file1= open("/Users/shrutiboparti/Downloads/file1.json")
file2= open("/Users/shrutiboparti/Downloads/file2.json")
def findDifference(file1,file2):
    data1=json.load(file1)
    data2=json.load(file2)
    for i in data1:
        value=data1[i]
        for j in value:
            if 'avg_price_total_in_usd' in j:
                del j["avg_price_total_in_usd"]

    for i in data2:
        value=data2[i]
        for j in value:
            if 'avg_price_total_in_usd' in j:
                del j["avg_price_total_in_usd"]

    difference_data1=diff(data1,data2, marshal=True)
    print(difference_data1)

    with open("/Users/shrutiboparti/Downloads/diff1.json", "w", encoding="utf8") as write_file:
        json.dump(difference_data1, write_file, indent=2, separators=(',', ': '))

    #difference_data2=diff(data2,data1)
    #print(difference_data2)

findDifference(file1,file2)