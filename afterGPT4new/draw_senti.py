import pandas as pd
import matplotlib.pyplot as plt

# Load data
data1 = pd.read_csv('./sentiment/copilot_office.csv')
# data2 = pd.read_csv('./sentiment/chatgpt_道德伦理.csv')
# data3 = pd.read_csv('./sentiment/chatgpt_问答技巧.csv')
# data4 = pd.read_csv('./sentiment/道德伦理_xmlt.csv')
# data5 = pd.read_csv('./gpt4/sentiment/道德伦理_xmlt_new.csv')

# Count sentiment values
# data = pd.concat([data1['sentiment'],data2['sentiment']])
# sentiment_counts = data.value_counts()

sentiment_counts = data1['sentiment'].value_counts()

sentiment_counts.name = ''

# Plot pie chart
# sentiment_counts.plot(kind='pie', autopct='%1.1f%%',labeldistance=0.8)

# plt.title('After the release of GPT-4', fontsize=15)
sentiment_counts.plot(kind='pie', autopct='%1.1f%%', fontsize=16)

# plt.savefig('./pic/作业+答题问答+原创性.png', dpi=300)
# plt.savefig('./gpt4/pic_gpt4/作业+答题问答+原创性.png', dpi=300)

plt.savefig('./pic_afterGpt4/copilot.png', dpi=300)