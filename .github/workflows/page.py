from demo.zdh_lx.base import Base
from selenium.webdriver.common.by import By as bp
from time import sleep
import yaml
class Login_page(Base):
    fs = open("C:\\Users\\v_bingbqi\\PycharmProjects\\untitled\\demo\\zdh_lx\\pass_word.yaml", "r")
    data = yaml.full_load(fs.read())
    url=data["data"]["url"]
    id=data["data"]["id"]
    name=data["data"]["name"]
    def dl(self):
        self.open_url(self.url)
        # self.click(bp.ID,"s-top-loginbtn")
        # sleep(2)
        # self.send_keys(bp.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]',self.id)
        # self.send_keys(bp.XPATH,'//*[@id="TANGRAM__PSP_11__password1"]',self.name)
        # self.click(bp.ID,"TANGRAM__PSP_11__submit1")
        sleep(5)
    def set_stop(self):
        self.driver.close()

if __name__ == '__main__':
    l=Login_page()
    l.dl()
    l.set_stop()

