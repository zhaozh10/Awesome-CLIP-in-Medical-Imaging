import re

def process_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        if line.strip():
            # 在第一个 \ 后面添加回车
            line = re.sub(r'\\ ', '\\\n', line, count=1)
            # 在第二个 \ 后面添加回车
            line = re.sub(r'\\ ', '\\\n', line, count=1)
            # 在行末添加回车和空行
            line = line.rstrip() + '\n\n'
            processed_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)

# 输入文件和输出文件路径
input_file = 'preTraining.txt'
output_file = 'new.txt'

# 处理文件
process_text_file(input_file, output_file)
