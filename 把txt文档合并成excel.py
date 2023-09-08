import os
import csv

def txt_to_csv(folder_path):
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 判断是否为txt文件
            if file.endswith('.txt'):
                txt_file = os.path.join(root, file)
                csv_file = os.path.splitext(txt_file)[0] + '.csv'
                # 读取txt文件，转换成csv格式
                with open(txt_file, 'r') as f_txt, open(csv_file, 'w', newline='') as f_csv:
                    reader = csv.reader(f_txt, delimiter='\t')
                    writer = csv.writer(f_csv)
                    for row in reader:
                        writer.writerow(row)
    # 合并所有csv文件
    csv_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_list.append(os.path.join(root, file))
    with open('result.csv', 'w',encoding='GBK', newline='') as f:
        writer = csv.writer(f)
        for csv_file in csv_list:
            with open(csv_file, 'r') as f_csv:
                reader = csv.reader(f_csv)
                for row in reader:
                    writer.writerow(row)

if __name__ == '__main__':
    folder_path = input('请输入路径:（举例：C:/xxx/xxx）')
    txt_to_csv(folder_path)