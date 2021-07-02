import pandas as pd
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from lxml import etree

url = 'https://top.baidu.com/board?tab=realtime&sa=search_31065'
response = requests.get(url=url)
html = response.text

selector = etree.HTML(html)
title = selector.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[2]/a/text()')
number = selector.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[1]/div[2]/text()')

data = pd.Series(data=number, index=title[0:-1:2])
frequencies = data.astype('int')

wordcloud = WordCloud(font_path="FZSTK.TTF",
                      max_words=100,
                      background_color='white')
my_wordcloud = wordcloud.fit_words(frequencies)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
