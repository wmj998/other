import pandas as pd
import re
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from lxml import etree

url = 'https://top.baidu.com/board'
response = requests.get(url=url)
html = response.text

selector = etree.HTML(html)
title = selector.xpath('//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a/div[1]/div[2]/div/div/text()')
number = selector.xpath('//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a/div[1]/div[2]/div/span/text()')
number = [re.findall('\d+', i)[0] for i in number]
data = pd.Series(data=number, index=title)
frequencies = data.astype('int')

wordcloud = WordCloud(font_path="FZSTK.TTF",
                      max_words=100,
                      background_color='white')
my_wordcloud = wordcloud.fit_words(frequencies)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
