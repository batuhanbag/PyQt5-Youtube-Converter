from PyQt5.QtWidgets import *
import sys

import os
from PyQt5.QtGui import QIcon

from combobox_python import Ui_MainWindow

from pytube import YouTube

class Combo(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_go_mp3.clicked.connect(self.go_mp3)
        self.ui.pushButton_go_subtitle.clicked.connect(self.go_subtitle)
        self.ui.pushButton_go_mp4.clicked.connect(self.go_mp4)

        self.ui.pushButton_mp4_back.clicked.connect(self.go_homepage)
        self.ui.pushButton_mp3_back.clicked.connect(self.go_homepage)
        self.ui.pushButton_subtitle_back.clicked.connect(self.go_homepage)


        self.ui.actionHelp.triggered.connect(self.info)

        self.ui.page_homepage.index = 0
        self.ui.page_mp3.index = 1
        self.ui.page_mp4.index = 2
        self.ui.page_subtitle.index = 3

        self.ui.pushButton_browse_mp4.clicked.connect(self.browse)
        self.ui.pushButton_browse_mp3.clicked.connect(self.browse)
        self.ui.pushButton_browse_subtitle.clicked.connect(self.browse)


        self.ui.pushButton_mp4.clicked.connect(self.mp4_process)
        self.ui.pushButton_mp3.clicked.connect(self.mp3_process)
        self.ui.pushButton_subtitle.clicked.connect(self.subtitle_process)




        self.go_homepage()


    def go_homepage(self):

        self.ui.stackedWidget.setCurrentIndex(self.ui.page_homepage.index)

    def go_mp3(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.page_mp3.index)
        #self.ui.statusBar.showMessage("DOWNLOADING...")
        #self.ui.statusBar.setStyleSheet("color:rgb(0,0,255)")

    def go_mp4(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.page_mp4.index)



    def go_subtitle(self):

        self.ui.stackedWidget.setCurrentIndex(self.ui.page_subtitle.index)

    def info(self):
        QMessageBox.about(self, "Information", "This program is coded by <b>Batuhan Bağ</b>"
                                               "<br><br>"
                                               "<b>Batuhan Bağ Contact:</b>"
                                               "<br>"
                                               "<a href=\"mailto:batuhannbagg@gmail.com\">batuhannbagg@gmail.com</a>"
                                               "</font>")

    def browse(self):
        dosya_ad = QFileDialog.getOpenFileName(self, "Dosya Kaydet", os.getenv("HOME"))

        print(dosya_ad)



    def mp3_process(self):


        yt = YouTube(self.ui.lineEdit_mp3.text())

        stream = yt.streams.filter(only_audio=True).first()
        stream.download('MP3')

        QMessageBox.about(self, "Convert", "<b> Conversion Successful</b>")
        self.ui.lineEdit_mp3.clear()
    def mp4_process(self):

        yt = YouTube(self.ui.lineEdit_mp4.text())


        stream = yt.streams.filter(progressive=True).first()
        stream.download('MP4')
        QMessageBox.about(self, "Convert", "<b> Conversion Successful</b>")
        self.ui.lineEdit_mp4.clear()

    def subtitle_process(self):
        from pytube import YouTube
        yt = YouTube(self.ui.lineEdit_subtitle.text())

        caption = yt.captions['en']
        cc = caption.generate_srt_captions()
        str(cc)
        with open(yt.title+"lycris.txt", "w", encoding="utf-8") as f:
            f.write(cc)
            QMessageBox.about(self, "Convert", "<b> Conversion Successful</b>")
            self.ui.lineEdit_subtitle.clear()



import icons_rc
uygulama = QApplication([])
window = Combo()
window.show()
uygulama.exec_()
