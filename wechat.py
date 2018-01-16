import itchat
import re

itchat.login()  # 登录微信
# 爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器
male = female = other = 0
# friends[0]是自己的信息，所以要从friend[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 计算朋友总数
total = len(friends[1:])
# 打印出自己的好友性别比例
print("男性好友： %.2f%%" % (float(male) / total * 100) + "\n" +
      "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性别好友： %.2f%%" % (float(other) / total * 100))


# 定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
from pandas import DataFrame

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
# frame.to_excel
frame.to_csv('data.txt', index=True)

# 爬签名
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
text.encode("utf-8")

file = open("signature.txt", "w", encoding='utf-8')
file.write(text)
file.close()

# 爬用户名
siglist = []
for i in friends:
    signature = i["Province"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
text.encode("utf-8")

file = open("Province.txt", "w", encoding='utf-8')
file.write(text)
file.close()
# wordlist = jieba.cut(text, cut_all=True)
# word_space_split = " ".join(wordlist)
#
# coloring = np.array(Image.open("C:/Users/zl/Desktop/wechat.jpg"))
# my_wordcloud = WordCloud(background_color="white", max_words=2000, width=1900, height=1860, margin=2,
#                          mask=coloring, max_font_size=90, random_state=42, scale=2,
#                          font_path="C:/Windows/Fonts/SimHei.ttf").generate(word_space_split)
#
# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
