import re
import urllib2
class Grawlpage:
    def __init__(self):
        self.page=1
        self.controller=True
    def urlpage(self):
        url="https://www.qiushibaike.com/8hr/page/"
        url=url+str(self.page)
        headers={"Host":"www.qiushibaike.com",
                  "Connection":"keep-alive",
                  "Cache-Control":"max-age=0",
                  "Upgrade-Insecure-Requests":1,
                  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
                }
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        response=response.read()
        rule=re.compile(r'<div class="content">(.*?)</div>',re.S)
        content=rule.findall(response)
        print "正在下载"
        self.extract(content)
    def extract(self,content):
        for item in content:
            item=item.replace("<br>","").replace("<br/>","").replace("<span>","").replace("</span>","")
            self.download(item)
    def download(self,item):
            with open("G:/"+str(self.page)+".txt","a") as f:
                f.write(item)
                print"成功保存"
    def control(self):
        while self.controller:
            self.urlpage()
            command=raw_input("若继续下载请按回车（退出请输入quit）")
            if command=="quit":
                self.controller = False
                print "谢谢使用"
            self.page+=1
if __name__ == '__main__':
    qiushi=Grawlpage()
    qiushi.urlpage()
    qiushi.control()
