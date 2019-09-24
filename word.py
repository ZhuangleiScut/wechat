import jieba
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

file = open("NickName.txt", encoding='utf-8')
text = file.read()

wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# coloring = np.array(Image.open("C:/Users/zl/Desktop/wechat.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, width=2048, height=1536,
                         font_path="C:/Windows/Fonts/SimHei.ttf").generate(word_space_split)

# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()