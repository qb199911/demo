from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException as no#元素抛异常
from selenium.webdriver.common.by import By as bp
import datetime



class Base:
    def __init__(self, browser="chrome"):
        """
        初始化driver
        :param browser:浏览器名称
        """
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = None
            print("请输入正确的浏览器,例如:chrome,firefox,ie")
        self.time= datetime.datetime.now().strftime('%Y-%m-%d-%T').replace(":",".")

    def open_url(self,url):
        """
        打开地址
        :param url: 被测地址
        :return:
        """
        chro=self.driver.get(url)
        sleep(2)
        return chro

        # e = self.driver.find_element()

    def find_element(self, by,locator):
        """
        定位单个元素,如果定位成功返回元素本身,如果失败,返回False
        :param locator: 定位器,例如("id","id属性值")
        :return: 元素本身
        """
        for a in range(3):
            try:
                element = self.driver.find_element(by,locator)
            except no as e:
                # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                print(f"{locator}元素没找到")
                continue
            else:
                # 没有发生异常，表示在页面中找到了该元素，返回True
                print(f"元素正常:{locator}")
                # element.send_keys("cs")
                return element

    def click(self, by,locator):
        """
        点击元素
        :return:
        """
        for a in range(1):
            try:
                element = self.find_element(by,locator)
                element.click()
            except:
                print("元素异常，无法点击")
                # self.get_jt("点击异常当前时间:{}".format(self.time))
                self.get_jt("点击异常")

                continue
    def get_jt(self,name):
        self.driver.save_screenshot(r'D:\png\%s%s.png'%(name,self.time))

    def send_keys(self, by,locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        for a in range(1):
            try:
                element = self.find_element(by,locator)
                # element.clear()
                element.send_keys(text)
            except :
                print("元素异常无法进行输入")
                self.get_jt("输入异常")
                continue


    def close(self):
        """
        关闭浏览器
        :return:
        """
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    base = Base()
    base.open_url("https://www.baidu.com/")
    base.find_element(bp.ID,"kw")
    base.send_keys(bp.ID,"kw","测试")
    base.click(bp.ID,"su")
    base.close()
