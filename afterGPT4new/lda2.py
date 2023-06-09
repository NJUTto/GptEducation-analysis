import pandas as pd
import re
import jieba.posseg as pseg
from zhon import hanzi
from gensim import corpora, models
import pyLDAvis.gensim_models

# 读取csv文件
input1 = pd.read_csv('./clean/AI_clean.csv')
input2 = pd.read_csv('./clean/人工智能_clean.csv')
input3 = pd.read_csv('./clean/人机交互_clean.csv')
input4 = pd.read_csv('./clean/人机协作_clean.csv')

# 加载停用词表
stopwords = []
with open('hit_stopwords.txt','r',encoding='utf-8') as f:
    for line in f:
        stopwords.append(line.strip())

savelist = ['答题','道德伦理','教育','考试','人工智能','人机交互','人机协作','问答技巧','原创性','作弊','作业','AI',
            '伦理道德','道德','伦理','原创','问答','技巧','人机','协作','交互','人工','智能', '论文','GPT-4','gpt-4','gpt4','GPT4']


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

    # 分词并保留主要词性的词语
    seg_list = pseg.lcut(text)

    allowed_flags = ['eng', 'n','a','v','an','vn']
    seg_list = [word for word, flag in seg_list if (flag in allowed_flags  or word in savelist) and word not in stopwords and len(word)>1]

    return seg_list

# df['content'] = df['content'].apply(clean_text)
contents = pd.concat([input1['content'],input2['content'],input3['content'],input4['content']]).apply(clean_text)

# 将文本转化为列表
texts = []
for list in contents:
    words = list
    texts.append(words)

# 建立词典
dictionary = corpora.Dictionary(texts)

# 建立语料库
corpus = [dictionary.doc2bow(text) for text in texts]

# 建立LDA模型
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1, passes=100)

# Get top 30 words for topic 0
top_words = lda.show_topic(0, 30)

# Save to CSV
df = pd.DataFrame(top_words, columns=['word', 'probability'])
df.to_csv('./topic/AI+人工智能+人机协作/交互.csv', index=False)

# 输出主题
# for topic in lda.print_topics(num_topics=1, num_words=30):
#     print(topic)

# data = pyLDAvis.gensim_models.prepare(lda, corpus, dictionary)

# pyLDAvis.show(data,local=False)  # 可视化主题模型