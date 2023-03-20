from demo.zdh_lx.page import Login_page
import unittest
import HTMLReport
from selenium.webdriver.common.by import By as bp
from time import sleep
class Test_case01(unittest.TestCase):
    def setUp(self):
        self.driver=Login_page()
        self.driver.dl()

    def tearDown(self):
        self.driver.set_stop()
    def test001(self):
        '''是否可以登录'''
        self.driver.click(bp.ID, "s-top-loginbtn")
        self.driver.send_keys(bp.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]', self.driver.id)
        self.driver.send_keys(bp.XPATH, '//*[@id="TANGRAM__PSP_11__password"]', self.driver.name)
        self.driver.click(bp.ID, "TANGRAM__PSP_11__submit")
    def test002(self):
        """贴吧搜索"""
        self.driver.click(bp.LINK_TEXT,"贴吧")
        ck=self.driver.driver.window_handles
        self.driver.driver.switch_to.window(ck[1])  # 切换窗口
        self.driver.send_keys(bp.NAME,"kw1","测试")
        self.driver.click(bp.LINK_TEXT,"全吧搜索")
        sleep(1)
        jg=self.driver.find_element(bp.XPATH,'//*[@id="head"]/div/p/label[1]').text
        self.assertEqual(jg,"搜贴1")
if __name__ == '__main__':
    suite = unittest.TestSuite()  # 测试套件
    loader = unittest.TestLoader()  # 测试加载
    suite.addTest(loader.loadTestsFromTestCase(Test_case01))
    runner = HTMLReport.TestRunner(report_file_name='baidu_test',  # 文件名
                                   output_path='baidu_report',  # 文件夹名
                                   title='百度-自动化测试报告{}'.format(Login_page().time),  # 标题
                                   description='登录',  # 描述用例
                                   lang='cn'  # 语言
                                   )
    runner.run(suite)  # 执行上面的