import pandas as pd

# 读取A.csv文件
a_file_path = 'Pre-training Papers.csv'
a_df = pd.read_csv(a_file_path)

# 读取B.md文件
b_file_path = 'README.md'
with open(b_file_path, 'r', encoding='utf-8') as file:
    b_content = file.read()

# 初始化未处理的数据列表
unprocessed = []

# 遍历A.csv的每一行，检查B.md中是否包含相应的article字符串
for index, row in a_df.iterrows():
    article = row['Name']
    if article not in b_content:
        unprocessed.append(row)

# 将未处理的数据写入新的CSV文件
if unprocessed:
    unprocessed_df = pd.DataFrame(unprocessed)
    unprocessed_df.to_csv('Pre-training-unpro.csv', index=False)
else:
    print("所有数据都在B.md中找到了对应的字符串。")

print("处理完成。")
