 # 新闻段落高频词分析器
import jieba
import jieba.analyse


class ToolToMakeHighWords:
    test_str = ""

    # 初始化
    def __init__(self,test_str):
         self.test_str = str(test_str)
         pass

    def buildWithFile(self,filePath,type):
        file = open(filePath, encoding=type)
        self.test_str = file.read()

    def buildWithStr(self,test_str):
        self.test_str = test_str
        pass

     # 统计词
    def getWords(self,isSimple,isAll):
         if(isSimple):
             words = jieba.lcut_for_search(self.test_str)
             return words
         else:
             # True - 全模式 , False - 精准模式
             words = jieba.cut(self.test_str, cut_all=isAll)
             return words

    # 统计词频并排序
    def getHighWords(self,words):
        data = {}
        for charas in words:
            if len(charas) < 2:
                continue
            if charas in data:
                data[charas] += 1
            else:
                data[charas] = 1

        data = sorted(data.items(), key=lambda x: x[1], reverse=True)  # 排序

        return data

# 以频率要求数目为依据进行筛选
    def selectObjGroup(self,num):
         a = jieba.analyse.extract_tags(self.test_str, topK=num, withWeight=True, allowPOS=())
         return a

    def selectWordGroup(self,num):
         b = jieba.analyse.extract_tags(self.test_str, topK=num, allowPOS=())
         return b


def main():
    file = open('./ad.txt', encoding="utf-8")
    file_context = file.read()
    ttmhw = ToolToMakeHighWords(file_context)
    li = ttmhw.selectWordGroup(ttmhw.__sizeof__())
    print(li)

main()