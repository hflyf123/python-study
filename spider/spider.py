from urllib import request
#断点调试
class Spider:
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        #bytes
        htmls = r.read()
        htmls = str(htmls, encoding = 'utf-8')
        a = 1

#1，唯一表示符做标签
#2. 最接近数据的标签
#3. 选择可以闭合的标签
#逐渐精细化信息
    def __analysis(self,htmls):
        pass

    def go(self):
        self.__fetch_content()
        # self.__analysis(htmls)

    


spider = Spider()
spider.go()
