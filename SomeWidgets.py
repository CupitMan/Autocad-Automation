from PyQt5.QtWidgets import *
from PyQt5 import QtCore


def ProgressBar():
    bar = QProgressBar()
    bar.setStyleSheet("""
    QProgressBar {
        height: 25px;
        background: #555;
        box-shadow: inset 0 -1px 1px rgba(255,255,255,0.3);
        color: #fafafa;
        font-size: 20px;

    }
    """)
    return bar

class CustomButton(QPushButton):

    def __init__(self, text, parent=None):

        QWidget.__init__(self, parent=parent)

        self.setStyleSheet("""
            QPushButton {
                background-color: #2ea44f;
                color: rgb(255, 255, 255);
                max-width: 500px;
                max-height: 60px;
                min-height: 50px;
                min-width: 250px;
                border-radius: 5px;
                font-size: 15px;
                font-family: Segoe UI bold;
                border: none;
            }

            QPushButton:hover {
                background-color: #24853f;
            }

            QPushButton:pressed {
                background-color: #2bb351;
            }
        """)
        self.setText(text)

class CentralWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setStyleSheet("""
        QWidget {
            background-color: #363861;
        }
        """)

class InformationLabel(QLabel):

    def __init__(self, text, size=20, parent=None):

        QLabel.__init__(self, parent=parent)

        self.setStyleSheet(f"""
        QLabel {{
            color: #FFF;
            font-size: {size}px;
            border: none;
        }}
        """)
        self.setText(text)

class ReplacesEdits(QLineEdit):

    def __init__(self, type, parent=None):

        QLineEdit.__init__(self, parent=parent)

        self.setStyleSheet("""
        QLineEdit {
            color: #2f2f36;
            min-height: 30px;
            font-size: 20px;
            background-color: #FAFAFA;
            max-width: 300px;
        }
        """)

        if type == 'from':
            self.setPlaceholderText('Введите что заменить')
        else:
            self.setPlaceholderText('Введите на что заменить')

class ErrorsPlain(QPlainTextEdit):

    def __init__(self, parent=None):

        QPlainTextEdit.__init__(self, parent=parent)

        self.setStyleSheet("""
        QPlainTextEdit {
            background-color: #fafafa;
            font-size: 15px;
            color: #87210c;
            
        }
        """)
        self.setReadOnly(True)

    def addError(self):

        currentText = self.toPlainText()

        if "Ошибки" in currentText:
            
        else:



class ProcessPlain(QPlainTextEdit):

    def __init__(self, parent=None):

        QPlainTextEdit.__init__(self, parent=parent)

        self.setStyleSheet("""
        QPlainTextEdit {
            background-color: #fafafa;
            font-size: 15px;
            color: #333;
        }
        """)
        self.setReadOnly(True)

class SettingsWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.settingsLayout = QVBoxLayout()
        self.setLayout(self.settingsLayout)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.settingsLayout.setSpacing(0)
        self.settingsLayout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("border-right: 3px solid grey;")
        self.settingsLayout.setSpacing(10)

        #-------------------------------Выбрать папку-------------------------------#
        self.selectFolderLabel = InformationLabel(text="Выберите папку с чертежами")
        self.selectFolderButton = CustomButton(text="ВЫБЕРИТЕ ПАПКУ")
        self.selectFolderPath = InformationLabel(text="Путь к папке не выбран")
        #---------------------------------------------------------------------------#

        #------------------------------Замена в чертежах----------------------------#
        self.replacesPlotsLabel = InformationLabel(text="Замена в чертежах")
        self.replacePlotsEditFrom = ReplacesEdits(type="from")
        self.replacePlotsEditTo = ReplacesEdits(type="to")
        #---------------------------------------------------------------------------#

        #-----------------------------Замена в именах-------------------------------#
        self.replacesNamesLabel = InformationLabel(text="Замена в именах файлов")
        self.replaceNamesEditFrom = ReplacesEdits(type="from")
        self.replaceNamesEditTo = ReplacesEdits(type="to")
        #---------------------------------------------------------------------------#

        #----------------------------Формирование Layout----------------------------#
        self.selectFolderWidget, self.replacePlotsWidget, self.replaceNamesWidget = (QWidget(self),
                                                                                     QWidget(self), QWidget(self))
        self.selectFolderLayout, self.replacePlotsLayout, self.replaceNamesLayout = (StandartVLayout(),
                                                                                     StandartVLayout(), StandartVLayout())
        self.selectFolderWidget.setLayout(self.selectFolderLayout)
        self.replacePlotsWidget.setLayout(self.replacePlotsLayout)
        self.replaceNamesWidget.setLayout(self.replaceNamesLayout)
        #---------------------------------------------------------------------------#

        #----------------------------Заполнение Layout------------------------------#

        #-------------Выбор папки------------------------------#
        self.selectFolderLayout.addWidget(self.selectFolderLabel)
        self.selectFolderLayout.addWidget(self.selectFolderButton)
        self.selectFolderLayout.addWidget(self.selectFolderPath)
        #------------------------------------------------------#

        #------------Замена в чертежах-------------------------#
        self.replacePlotsLayout.addWidget(self.replacesPlotsLabel)
        self.replacePlotsLayout.addWidget(self.replacePlotsEditFrom)
        self.replacePlotsLayout.addWidget(self.replacePlotsEditTo)
        #------------------------------------------------------#

        #-----------Замена в именах----------------------------#
        self.replaceNamesLayout.addWidget(self.replacesNamesLabel)
        self.replaceNamesLayout.addWidget(self.replaceNamesEditFrom)
        self.replaceNamesLayout.addWidget(self.replaceNamesEditTo)
        #------------------------------------------------------#

        #--------Добавление в основной Layout------------------#
        self.settingsLayout.addWidget(self.selectFolderWidget)
        self.settingsLayout.addWidget(self.replacePlotsWidget)
        self.settingsLayout.addWidget(self.replaceNamesWidget)
        #------------------------------------------------------#

        #---------------------------------------------------------------------------#

    def GetReplaces(self):

        dictionaryReplaces = {
            "PlotsFrom": self.replacePlotsEditFrom,
            "PlotsTo": self.replacePlotsEditTo,
            "NamesFrom": self.replaceNamesEditFrom,
            "NamesTo": self.replaceNamesEditTo
        }

        return dictionaryReplaces



class StandartVLayout(QVBoxLayout):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setAlignment(QtCore.Qt.AlignVCenter)
        self.setContentsMargins(10, 10, 10, 10)

class StarterWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.starterLayout = QVBoxLayout()
        self.setLayout(self.starterLayout)
        self.starterLayout.setSpacing(5)
        self.starterLayout.setContentsMargins(10, 10, 10, 10)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        #--------------------------Виджеты------------------------------------------#
        self.errorsWidget = ErrorsPlain()

        self.processLabel = InformationLabel('ОКНО ПРОЦЕССОВ')
        self.processLabel.setAlignment(QtCore.Qt.AlignVCenter)

        self.processWidget = ProcessPlain()

        self.progressBar = ProgressBar()
        self.progressBar.setValue(0)

        self.startButton = CustomButton("НАЧАТЬ ОБРАБОТКУ")
        #---------------------------------------------------------------------------#

        #----------------------Заполнение Layout------------------------------------#
        self.starterLayout.addWidget(self.errorsWidget)
        self.starterLayout.addWidget(self.processLabel)
        self.starterLayout.addWidget(self.processWidget)
        self.starterLayout.addWidget(self.progressBar)
        self.starterLayout.addWidget(self.startButton)
        #---------------------------------------------------------------------------#