import csv
import re

# 定义需要删除的特殊符号和词语列表
# special_chars = ['【', '】',]
special_words = ['收起d','O网页链接','收起全文d','收起O','更多详情请点击>>','详情戳>>>','详见>>','>>','>>>','详见↓','详情↓','↓']

# 去除@对象
pattern1 = re.compile(r'@[^\s]*')
pattern2 = re.compile(r'▲[^\s]*')
pattern3 = re.compile(r'★[^\s]*')
# pattern4 = re.compile(r"(?i)\#[^\#]*(?<!chat)gpt[^\#]*?\#")

# 定义读取和写入csv文件的路径
input_path = './deleterow/AI.csv'
output_path = './clean/AI_clean.csv'

# 读取csv文件并打开输出文件
with open(input_path, 'r', encoding='utf-8') as input_file, open(output_path, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.DictReader(input_file)
    headers = reader.fieldnames

    # 写入csv文件头
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()

    # 处理每一行数据
    for row in reader:
        content = row['content']

        # content = re.sub(r"#([^#]*chatgpt[^#]*)#", lambda x: x.group(0) if re.search(r"chatgpt", x.group(0), re.IGNORECASE) else "", content)

        # 删除特殊符号和词语
        # for char in special_chars:
        #     content = content.replace(char, '')
        for word in special_words:
            content = content.replace(word, '')

        content = pattern1.sub('', content)
        content = pattern2.sub('', content)
        content = pattern3.sub('', content)
        # content = pattern4.sub('', content)

        # content = re.sub(r'#\S+#', '',content)
        

        # 保留其他列数据
        row['content'] = content

        # 将处理后的行写入输出文件
        writer.writerow(row)