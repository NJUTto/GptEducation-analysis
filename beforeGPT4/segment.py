import pandas as pd
import re
# import jieba
import jieba.posseg as pseg
from zhon import hanzi

input_path = './clean/AI_clean.csv'
output_path = './segment/AI_segment.csv'

# 读取CSV文件
df = pd.read_csv(input_path)

# 加载停用词表
stopwords = []
with open('hit_stopwords.txt','r',encoding='utf-8') as f:
    for line in f:
        stopwords.append(line.strip())

savelist = ['答题','道德伦理','教育','考试','人工智能','人机交互','人机协作','问答技巧','原创性','作弊','作业','AI',
            '伦理道德','道德','伦理','原创','问答','技巧','人机','协作','交互','人工','智能', '论文']

# 对微博文本进行清洗
def clean_text(text):
    # 去除网址链接
    text = re.sub(r'http\S+', '', text)
    # 去除HTML标签
    text = re.sub(r'<.*?>', '', text)
    # 去除@符号和话题符号
    text = re.sub(r'@[^\s]*', '',text)
    # text = re.sub(r'#\S+#', '',text)
    # 去除中文符号
    text = re.sub(r'[{}]+'.format(hanzi.punctuation), '', text)

    # 去除英文和数字
    #text = re.sub(r'[A-Za-z0-9]', '', text)

    #jieba.load_userdict('./savelist.txt')

    # 分词并保留主要词性的词语：英语，动词，名词，形容词，副词，成语
    seg_list = pseg.lcut(text)

    # print(seg_list)

    allowed_flags = ['eng','v', 'n', 'a', 'ns', 'nt', 'vn', 'vd', 'ad', 'an', 'd','i']
    # seg_list = [word for word, flag in seg_list if flag in allowed_flags and word not in stopwords]
    seg_list = [word for word, flag in seg_list if (flag in allowed_flags  or word in savelist) and word not in stopwords]

    # print(seg_list)

    return seg_list

df['content'] = df['content'].apply(clean_text)

# 保存清洗后的结果到CSV文件
df.to_csv(output_path, index=False)