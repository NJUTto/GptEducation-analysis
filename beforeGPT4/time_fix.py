import csv
from datetime import datetime, timedelta

with open("./论文.csv", 'r', encoding='utf-8', errors='ignore') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    fieldnames = reader.fieldnames + ['time_sec']  # 新增一个名为"时间(加秒)"的列
    with open('论文_sec.csv', 'w', newline='') as output_file:  # 将结果写入到一个新的csv文件中
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            # 将时间列的值转换为datetime对象
            time_str = row['publish_time']
            time = datetime.strptime(time_str, '%Y-%m-%d %H:%M')
            # 添加30秒
            time += timedelta(seconds=30)
            # 将新的时间值写入到新列中
            row['publish_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
            # 将整行写入到新文件中
            writer.writerow(row)

