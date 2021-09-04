import pandas as pd
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from lxml import etree

url = 'https://top.baidu.com/board?tab=realtime'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
# proxies = {
#     'http': 'http://124.232.137.37:8888',
#     'https': 'https://124.232.137.37:8888'
# }
# response = requests.get(url=url, headers=headers, proxies=proxies)
response = requests.get(url=url, headers=headers)
html = response.text

selector = etree.HTML(html)
title = selector.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[2]/a/div[1]/text()')
score = selector.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[1]/div[2]/text()')
# data = pd.Series(data=score, index=title)
# frequencies = data.astype('int')

# score = [int(i) for i in score]
score = list(map(int, score))
frequencies = dict(zip(title, score))

wordcloud = WordCloud(font_path="simkai.ttf",
                      max_words=100,
                      background_color='white',
                      scale=7)
my_wordcloud = wordcloud.fit_words(frequencies)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
