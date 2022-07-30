import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os
import win32com.client
from comtypes.client import GetBestInterface
import time
import math
import threading as th
from AutoCad import *
import SomeWidgets as SW



class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        # ----------------------Constants------------------------------------------#
        self.replacesPlotTextFrom = ''
        self.replacesPlotTextTo = ''

        self.replacesNamesTextFrom = ''
        self.replacesNamesTextTo = ''

        self.pathPlotsFolder = ''
        # --------------------------------------------------------------------------#

        self.resize(1000, 700)
        self.setWindowTitle('Autocad Automation Application')

        self.centralWidget = SW.CentralWidget()
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.settingsWidget = SW.SettingsWidget()
        self.mainLayout.addWidget(self.settingsWidget)
        self.settingsWidget.selectFolderButton.clicked.connect(self.selectFolder)

        self.starterWidget = SW.StarterWidget(self.centralWidget)
        self.mainLayout.addWidget(self.starterWidget)
        self.starterWidget.startButton.clicked.connect(self.start)

    def start(self):

        if self.checker():
            self.starterWidget.starterButton.setEnabled(False)
            listPlots = []
            for file in os.listdir(self.pathPlotsFolder):
                if file.split('.')[-1].lower() == 'dwg':
                    listPlots.append(self.pathPlotsFolder + '\\' + file)

            self.progressPlain.setPlainText('\t\tНачата обработка файлов...\n\n')

            for i in range(len(listPlots)):


                fileName = listPlots[i].split('\\')[-1]


                thread = th.Thread(target=filesProcessing, args=(listPlots, i, self.replacePlotTextFrom,
                                                                 self.replacePlotTextTo))
                thread.run()

                while True:
                    time.sleep(0.5)
                    if th.activeCount() == 1:
                        break


                self.progressPlain.setPlainText(
                    f'{self.progressPlain.toPlainText()} Закончена обработка файла "{fileName}"\n')
                self.progressBar.setValue(math.floor(((i + 1) / len(listPlots)) * 100))


            self.progressPlain.setPlainText(
                f"{self.progressPlain.toPlainText()}\n\n\t\tПереименование файлов...\n")
            self.progressBar.setValue(0)

            for i in range(len(listPlots)):
                nameFile = lastFileName = listPlots[i].split('\\')[-1]
                nameFile = nameFile.replace(self.replaceNamesTextFrom, self.replaceNamesTextTo)
                os.rename(listPlots[i], self.pathPlotsFolder + '\\' + nameFile)
                self.progressPlain.setPlainText(
                    f'{self.progressPlain.toPlainText()}\n Файл "{lastFileName}" переименован в "{nameFile}"')
                self.progressBar.setValue(math.floor(((i + 1) / len(listPlots)) * 100))

            self.progressPlain.setPlainText(
                f"{self.progressPlain.toPlainText()}\n\n\t\tОбработка чертежей окончена!\n")

    def checker(self):

        flag = True

        self.starterWidget.errorsWidget.setPlainText('Ошибки:\n')


        if self.replacePlotTextFrom == '' or self.replacePlotTextTo == '':
            self.errorsWidget.setPlainText(
                f'{self.errorsWidget.toPlainText()} \n    Не выбрана замена в чертежах!\n')
            flag = False
        if self.replaceNamesTextFrom == '' or self.replaceNamesTextFrom == '':
            self.self.errorsWidget.setPlainText(
                f'{self.errorsWidget.toPlainText()} \n    Не выбрана замена в именах!\n')
            flag = False
        if self.pathPlotsFolder == '':
            self.errorsWidget.setPlainText(
                f'{self.errorsWidget.toPlainText()} \n    Не выбрана папка с чертежами!\n')
            flag = False

        return flag

    def selectFolder(self):

        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if file:
            self.pathPlotsFolder = file
            self.selectFolderPathLabel.setText('Путь к папке: ' + str(file))

