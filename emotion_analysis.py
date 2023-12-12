from snownlp import SnowNLP

text = u"我爱你,tmd,什么意思"
s = SnowNLP(text)

for sentence in s.sentences:
    s1 = SnowNLP(sentence)
    print(s1.sentiments)
