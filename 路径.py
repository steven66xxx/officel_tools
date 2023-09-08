import os  
  
# 提示用户输入要遍历的文件夹路径  
folder_path = input("请输入要遍历的文件夹路径（路径不要引号）：")  
  
# 将用户输入的相对路径转换为绝对路径  
folder_path = os.path.abspath(folder_path)  
  
# 获取文件夹中所有文件的路径  
file_paths = []  
for root, dirs, files in os.walk(folder_path):  
    for file in files:  
        file_path = os.path.join(root, file)  
        file_paths.append(file_path)  
  
# 将文件路径导出到txt  
with open("file_paths.txt", "w", encoding='utf-8') as f:  
    for file_path in file_paths:  
        f.write(file_path + "\n")