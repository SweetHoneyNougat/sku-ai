import os
import pandas as pd

def to_data_list(dir_path):
    in_list = []
    out_list = []
    file_names = set()

    for i in os.listdir(dir_path):
        file_names.add(os.path.splitext(i)[0])

    for i in file_names:
        with open(dir_path+'\\'+i+'.in', 'r', encoding='utf-8') as in_file:
            with open(dir_path+'\\'+i+'.out', 'r', encoding='utf-8') as out_file:
                for j in in_file.readlines():
                    in_list.append(j.strip())
                for j in out_file.readlines():
                    out_list.append(int(j))

    return [in_list, out_list]

data_dict = {
    'password': [],
    'label': []
}

# data1, data2에 있는 데이터를 데이터 프레임으로 모은 후 csv 파일로 내보내기

passwords, labels = to_data_list("data\\data1")
data_dict['password'] = passwords
data_dict['label'] = labels

passwords, labels = to_data_list("data\\data2")
data_dict['password'].extend(passwords)
data_dict['label'].extend(labels)

df = pd.DataFrame(data_dict)
df.to_csv("data\\csv\\original.csv", index=False)

print(df)
