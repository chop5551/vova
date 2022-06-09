import os
import json

result = 0


def file_processing(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
        global sum_tmp
        global string_tmp
        sum_tmp = int(0)
        string_tmp = int(0)
        d = len(data['aggregations']['session']['buckets'])
        while string_tmp < d:
            b = int(data['aggregations']['session']['buckets'][string_tmp]['index']['value'])
            string_tmp += 1
            sum_tmp += b
            res = sum_tmp / string_tmp
        #print(res)
        return (res)


def calculate():
    global result
    ctn = 0
    dir = r"E:\avg_catalog\results"
    for file in os.listdir(dir):
        # print ("Файл", file)
        if file.endswith(".json"):
            full_path = os.path.join(dir, file)
            print(file)
            result += file_processing(full_path)
            ctn += 1
            print(ctn)
            pos = result / ctn
        # else:
        # print ("не могу ни чего прочить...")
    return (pos)


print(calculate())

