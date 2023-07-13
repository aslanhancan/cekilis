import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from cekilis_main import Ui_MainWindow
import random

# from instagramUserinfo import username,password

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time




class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.ui.btnEkle.clicked.connect(self.ekle)
        self.ui.btnSil.clicked.connect(self.sil)
        self.ui.btnSec.clicked.connect(self.sec)
        self.ui.btnGiris.clicked.connect(self.singInClass)
        self.ui.btnList.clicked.connect(self.listeEkle)


    def singInClass(self):
        username = self.ui.lineUser.text()
        password = self.ui.linePass.text()
        ins(username,password).singIn()
        
    liste = ["ali","veli","konya"]
    def ekle(self):
        if self.ui.lineEdit.text() == "":
            self.ui.listWidget.addItems(self.liste)
        else:
            bilgi = self.ui.lineEdit.text()
            self.ui.listWidget.addItem(bilgi)
            self.ui.lineEdit.clear()

    def sil(self):
        bilgi = self.ui.listWidget.currentRow()
        secili = self.ui.listWidget.item(bilgi)
        self.ui.listWidget.takeItem(bilgi)
        del secili


    def sec(self):
        x = self.ui.listWidget.count()
        y = range(x)
        secili = (random.choice(y))

        
        self.ui.listWidget.setCurrentItem(self.ui.listWidget.item(secili))
        secili2 = self.ui.listWidget.currentItem().text()
        self.ui.lbl.setText(secili2)
    
    def listeEkle(self):
        self.ui.listWidget.addItems(ins.users_list)

class ins(Window):
    def __init__(self,username,password):
        super(ins,self).__init__()

        self.win = Window()

        self.browser = webdriver.Firefox()
        self.username=username
        self.password=password

    users_list = []

    def singIn(self):
        self.browser.get("https://instagram.com/accounts/login")
        time.sleep(4)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)
        self.takipciAl()


    def takipciAl(self):
        self.browser.get("https://instagram.com/{}".format(self.username))
        
        time.sleep(5)
        takipciSayi = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span").text
        print(takipciSayi)

        self.browser.get("https://instagram.com/{}/followers".format(self.username))
        time.sleep(6)

        modal = self.browser.find_element(By.CLASS_NAME,"_aano")
        count = len(modal.find_elements(By.XPATH, ".//div[@class='xt0psk2']"))

        # action = webdriver.ActionChains(self.browser)

        print("Takipçi Sayısı: {}".format(count))


        while count<int(takipciSayi):
            # modal.click()
            # action.key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL).perform()    
            self.browser.find_element(By.CLASS_NAME,"_aanq").click()
            time.sleep(3)
            newCount = len(modal.find_elements(By.XPATH, ".//div[@class='xt0psk2']"))
            if count < newCount:
                count=newCount
                print("Takipçi Sayısı: {}".format(count))
                time.sleep(3)
            else:
                break
        # i = 0
        followers = modal.find_elements(By.XPATH, ".//div[@class='xt0psk2']")
        time.sleep(6)
        
    
        for user in followers:
            # i+=1
            # print(i)
            link = user.find_element(By.TAG_NAME,"a").get_attribute("href").split("/")[3]
            self.users_list.append(link)
        # self.win.listeEkle(self.users_list)
        self.browser.close()
        self.win.listeEkle()







def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()


    

        