# from transformers import pipeline

# model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
# sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
# res = sentiment_task("chatgpt对教育是好是坏很难说")
# print(res)

# import torch
# from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification

# # 加载预训练模型和tokenizer
# tokenizer = XLMRobertaTokenizer.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")
# model = XLMRobertaForSequenceClassification.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")

# # 待分析文本
# text = "chatgpt对教育是好是坏很难说"

# # 编码输入
# encoded_input = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

# # 进行推理
# output = model(**encoded_input)
# print(output)
# probs = output[0].softmax(1)
# print(probs)
# # 提取三个数字
# # output = probs.detach().numpy()[0]
# # num1, num2, num3 = output[0], output[1], output[2]
# prob_list = probs.tolist()[0]

# print(prob_list[0], prob_list[1], prob_list[2])
# label = torch.argmax(probs)

# # 打印结果
# print(f"情感分析结果为：{label.item()}")


import pandas as pd
import torch
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification

input_path = './gpt4/clean/gpt-4_only.csv'
output_path = './gpt4/sentiment/gpt-4_only_xmlt.csv'

# 定义情感标签
SENTIMENT_LABELS = ['negative', 'neutral', 'positive']

# 加载预训练模型和tokenizer
tokenizer = XLMRobertaTokenizer.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")
model = XLMRobertaForSequenceClassification.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")

# 读取 CSV 文件
df = pd.read_csv(input_path)

# 对每个文本进行情感分析，并将结果写入到 CSV 文件中
for i, row in df.iterrows():
    text = row['content']
    
    # 编码输入
    encoded_input = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

    # 进行推理
    output = model(**encoded_input)
    # print(output)
    probs = output[0].softmax(1)
    label = torch.argmax(probs)
    # print(probs)
    # 提取三个数字
    prob_list = probs.tolist()[0]
    # print(prob_list[0], prob_list[1], prob_list[2])
    neg_prob = prob_list[0]
    neu_prob = prob_list[1]
    pos_prob = prob_list[2]

    # 将结果写入到 CSV 文件中
    df.loc[i, 'sentiment'] = SENTIMENT_LABELS[label.item()]
    df.loc[i, 'neg_prob'] = prob_list[0]
    df.loc[i, 'neu_prob'] = prob_list[1]
    df.loc[i, 'pos_prob'] = prob_list[2]

# 将结果保存到新的 CSV 文件中
df.to_csv(output_path, index=False)