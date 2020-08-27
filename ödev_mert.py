from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

baglanti = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='ulkeler')


class program(QDialog):
    def __init__(self,ebeveyn=None):
        #(ebeveyn(parent)bir alt sayfa açmasını engelliyor.)
        super(program,self).__init__(ebeveyn)

        izgara=QGridLayout()

        self.yazi_alani1 = QLabel("Ülke:")
        self.giris1 = QLineEdit()
        self.yazi_alani2 = QLabel("2015 Büyüme Oranı:")
        self.giris2 = QLineEdit()
        self.yazi_alani3 = QLabel("2016 Büyüme Oranı:")
        self.giris3 = QLineEdit()
        self.yazi_alani4 = QLabel("2017 Büyüme Oranı:")
        self.giris4 = QLineEdit()
        self.yazi_alani5 = QLabel("2018 Büyüme Oranı:")
        self.giris5 = QLineEdit()
        self.yazi_alani6 = QLabel("2019 Büyüme Oranı:")
        self.giris6 = QLineEdit()
        self.button = QPushButton("Kaydet")
        self.sonuc = QLabel("")
        self.yazi_alani7 = QLabel("Ülke:")
        self.giris7 = QLineEdit()
        self.button2 = QPushButton("Göster")
        self.yazi_alani8 = QLabel("Tahmini Büyüme Yüzdesi:")
        self.sonuc2 = QLabel("")
        self.bos = QLabel("")
        
        

        

        
        

        izgara.addWidget(self.yazi_alani1,1,0)
        izgara.addWidget(self.giris1,1,1)
        izgara.addWidget(self.yazi_alani2,2,0)
        izgara.addWidget(self.giris2,2,1)
        izgara.addWidget(self.yazi_alani3,3,0)
        izgara.addWidget(self.giris3,3,1)
        izgara.addWidget(self.yazi_alani4,4,0)
        izgara.addWidget(self.giris4,4,1)
        izgara.addWidget(self.yazi_alani5,5,0)
        izgara.addWidget(self.giris5,5,1)
        izgara.addWidget(self.yazi_alani6,6,0)
        izgara.addWidget(self.giris6,6,1)
        izgara.addWidget(self.button,7,0)
        izgara.addWidget(self.sonuc,7,1)
        izgara.addWidget(self.bos,8,1)
        izgara.addWidget(self.yazi_alani7,9,0)
        izgara.addWidget(self.giris7,9,1)
        izgara.addWidget(self.button2,10,1)
        izgara.addWidget(self.yazi_alani8,11,0)
        izgara.addWidget(self.sonuc2,11,1)
        

        self.setLayout(izgara)

        self.setWindowTitle("Ülke Ekleme")

        self.button.clicked.connect(self.fonksiyon)
        self.button2.clicked.connect(self.fonksiyon2)

    def fonksiyon(self):

        isaretci=baglanti.cursor()
        
        ulke = self.giris1.text()
        yil15 = float(self.giris2.text())
        yil16 = float(self.giris3.text())
        yil17 = float(self.giris4.text())
        yil18 = float(self.giris5.text())
        yil19 = float(self.giris5.text())
        

        isaretci.execute("INSERT INTO ulke (ulkee,yil15,yil16,yil17,yil18,yil19) VALUES ('%s','%s','%s','%s','%s','%s')"%(ulke,yil15,yil16,yil17,yil18,yil19))
        
        baglanti.commit()

        baglanti.close()

        self.sonuc.setText("Ülke Eklendi")
        
    def fonksiyon2(self):
        
        istenen = self.giris7.text()
        isaretci=baglanti.cursor()
        sql = "Select * From ulke where ulkee = %s"
        adr = (istenen,)
        isaretci.execute(sql,adr)
        liste = isaretci.fetchall()
        
        
        ulke = ""
        yil15 = 15
        yil16 = 16
        yil17 = 17
        yil18 = 18
        yil19 = 19
        
        
        for i in liste:
            ulke = i[0]
            yil15 = i[1]
            yil16 = i[2]
            yil17 = i[3]
            yil18 = i[4]
            yil19 = i[5]
            
        d={'yillar':[1,2,3,4,5],'degerler':
            [yil15,yil16,yil17,yil18,yil19,]}
        
        df = pd.DataFrame(data=d)
        
        yillar=df[['yillar']]
        degerler=df[['degerler']]
        
        from sklearn.model_selection import train_test_split
        
        x_train,x_test,y_train,y_test=train_test_split(yillar,degerler,test_size=0.33,random_state=0)
        
        from sklearn.linear_model import LinearRegression
        
        lr = LinearRegression()
        lr.fit(x_train,y_train)
        
        tahmin=str(lr.predict([[6]]))
        
        
            
        
            
        self.sonuc2.setText(tahmin)

uyg = QApplication([])
pencere = program()
pencere.show()
uyg.exec_()
