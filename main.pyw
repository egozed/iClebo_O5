# MACRO DEFINES
PYSIDE_OR_PYQT: str = 'PYQT'  # CHOOSE GUI: PYSIDE ||or|| PYQT   ???
DELAY: int = 1  # delay for showing info from 1 ms to infinity ms

if PYSIDE_OR_PYQT == 'PYQT':
    # --------- инициализашки для PyQt5 --------------------
    from PyQt5.QtCore import QThread
    from PyQt5.QtGui import QTextCursor, QPixmap
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    from GUI.pyqt.wMain_ui import Ui_MainWindow
    from GUI.pyqt.w5556_ui import Ui_Form5556
    from GUI.pyqt.w30001_ui import Ui_Form30001
    from GUI.pyqt.w30002_ui import Ui_Form30002
    from GUI.pyqt.w30003_ui import Ui_Form30003
else:  # PYSIDE_OR_PYQT == 'PYSIDE':
    # --------- инициализашки для PySide2 -------------------
    from PySide2.QtCore import QThread
    from PySide2.QtGui import QTextCursor, QPixmap
    from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
    from GUI.pyside.wMain_ui import Ui_MainWindow
    from GUI.pyside.w5556_ui import Ui_Form5556
    from GUI.pyside.w30001_ui import Ui_Form30001
    from GUI.pyside.w30002_ui import Ui_Form30002
    from GUI.pyside.w30003_ui import Ui_Form30003
# --------------------------------------------------------------------
from data import DataFrom5556, DataFrom30001, DataFrom30002, DataFrom30003  # data.py, дай человекопонятные данные из рп
from switch import switch


class MainWindowApp(QMainWindow, Ui_MainWindow):
    def __init__(self, ip: str):
        super().__init__()  # Это здесь нужно для доступа к переменным, методам QMainWindow, Ui_MainWindow
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна Ui_MainWindow
        self.ip = ip  # принимаем айпи рп и хапаем его себе
        self.lineEditEnterIP.setText(self.ip)  # показываем айпи рп юзеру
        self.setGeometry(*(save.get_from_json_data()['MAIN']))  # размещаем основное окно как оно было в прошлый раз
        self.datawindow5556 = DataWinApp5556()  # Создаём объект отдельного окна с показом данных из порта 5556
        self.datawindow30001 = DataWinApp30001()  # Создаём объект -//- 30001
        self.datawindow30002 = DataWinApp30002()  # Создаём объект -//- 30002
        self.datawindow30003 = DataWinApp30003()  # Создаём объект -//- 30003

    def __repr__(self) -> str:
        return 'MainWINDOW'

    def closeEvent(self, event):  # жамкнули на крестик в главном окне => прихлопнуть всех
        if self.isVisible():
            print(f"push X {self}")
            save.add_data_to_json({"MAIN": self.geometry().getRect()})  # сохраняем координаты размещения главного окна
            if self.datawindow5556.isVisible():
                self.datawindow5556.closeEvent(self)
            if self.datawindow30001.isVisible():
                self.datawindow30001.closeEvent(self)
            if self.datawindow30002.isVisible():
                self.datawindow30002.closeEvent(self)
            if self.datawindow30003.isVisible():
                self.datawindow30003.closeEvent(self)
            self.close()
            # del self
            print(f'{self} is DIE.')
            app.quit()
            print('The End.')

    def pushButton_30001click(self, isVisible: bool):  # обработчик жамки на кнопу "30001"
        self.datawindow30001.setWindowTitle(f"{self.ip}:30001")  # делаем заголовок этого окна типа: "ай.пи.р.п : 30001"
        self.datawindow30001.setVisible(
            isVisible)  # делаем окно с данными (видимым или невидимым) в зависимости от кнопки
        if isVisible:
            print(" 30001 is pressed")
            self.datawindow30001.show_data(
                ip=self.lineEditEnterIP.text())  # запускаем показ окна с данными из 30001 порта
        else:
            print(" 30001 is unpressed")
            self.datawindow30001.closeEvent(self)  # захлопываем это окно с данными

    def pushButton_30002click(self, isVisible: bool):
        self.datawindow30002.setWindowTitle(f"{self.ip}:30002")
        self.datawindow30002.setVisible(isVisible)
        if isVisible:
            print(" 30002 is pressed")
            self.datawindow30002.show_data(ip=self.lineEditEnterIP.text())
        else:
            print(" 30002 is unpressed")
            self.datawindow30002.closeEvent(self)

    def pushButton_30003click(self, isVisible: bool):
        self.datawindow30003.setWindowTitle(f"{self.ip}:30003")
        self.datawindow30003.setVisible(isVisible)
        if isVisible:
            print(" 30003 is pressed")
            self.datawindow30003.show_data(ip=self.lineEditEnterIP.text())
        else:
            print(" 30003 is unpressed")
            self.datawindow30003.closeEvent(self)

    def pushButton_5556click(self, isVisible: bool):
        self.datawindow5556.setWindowTitle(f"{self.ip}:5556")
        self.datawindow5556.setVisible(isVisible)
        if isVisible:
            print(" 5556 is pressed")
            self.datawindow5556.show_data(ip=self.lineEditEnterIP.text())
        else:
            print(" 5556 is unpressed")
            self.datawindow5556.closeEvent(self)


class DataWinApp5556(QWidget, Ui_Form5556, DataFrom5556):
    def __init__(self):
        super().__init__()  # Это здесь нужно для доступа к переменным, методам QWidget, Ui_Form5556
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна Ui_Form5556
        self.setVisible(False)  # сразу делаем это окно невидимым
        self.setGeometry(*(save.get_from_json_data()['5556']))  # размещаем это окно как оно было в прошлый раз
        self.th5556 = Th5()  # Создаём объект отдельного потока в котором будем вынимать и показывать данные из порта 5556

    def __repr__(self) -> str:
        return f'WIN of RoboData: {self.port}'

    def show5556(self):
        alldata = self.get_info()  # получаем данные от рп
        switch(alldata['type_of_data'],
               case={
                   1: lambda: (
                       self.label_d1f1.setText(f'{alldata["f1"]:.4f}'),
                       self.label_d1f2.setText(f'{alldata["f2"]:.4f}'),
                       self.label_d1f3.setText(f'{alldata["f3"]:.4f}'),
                       self.label_d1f4.setText(f'{alldata["f4"]:.4f}'),
                       self.label_d1f5.setText(f'{alldata["f5"]:.4f}'),
                   ),
                   2: lambda: (
                       self.label_d2i1.setText(f'{alldata["i1"]}'),
                       self.label_d2i2.setText(f'{alldata["i2"]}'),
                       self.label_d2i3.setText(f'{alldata["i3"]:.2f}'),
                   ),
                   8: lambda: (
                       self.label_d8i1.setText(f'{alldata["i1"]}'),
                       self.label_d8f2.setText(f'{alldata["f2"]:.2f}'),
                       self.label_d8i7.setText(f'{alldata["bat_volt"] / 1000:.3f}V'),
                       switch(alldata["charger_status"],
                              case={
                                  0: lambda: (
                                      self.label_d8i6.setText('NO charging.'),
                                  ),
                                  6: lambda: (
                                      self.label_d8i6.setText('Dock charging...'),
                                  ),
                                  2: lambda: (
                                      self.label_d8i6.setText('FULL Charged by dock.'),
                                  ),
                                  18: lambda: (
                                      self.label_d8i6.setText('FULL Charged by DC-jack.'),
                                  ),
                                  22: lambda: (
                                      self.label_d8i6.setText('DC-jack charging...'),
                                  ),
                                  "default": lambda key: (
                                      self.label_d8i6.setText(f'{key}'),
                                  )
                              }
                              ),

                   ),
                   10: lambda: (
                       self.label_d10f1.setText(f'{alldata["f1"]:.3f}'),
                       self.label_d10f2.setText(f'{alldata["f2"]:.3f}'),
                       self.label_d10f3.setText(f'{alldata["f3"]:.3f}'),
                   ),
                   9: lambda: (
                       self.label_d9f1.setText(f'{alldata["f1"]:.2f}'),
                       self.label_d9f2.setText(f'{alldata["f2"]:.2f}'),
                       self.label_d9f3.setText(f'{alldata["f3"]:.2f}'),
                       self.label_d9f4.setText(f'{alldata["f4"]:.2f}'),
                       self.label_d9f5.setText(f'{alldata["f5"]:.2f}'),
                   ),
                   "default": lambda key: (
                       print(f'5556 type of data = {key} NOT recognized'),
                   )
               }
               )
        self.update()

    def show_data(self, ip: str):  # инициализируем показ окна с данными
        setattr(self, 'ip', ip)  # перед показом окна с данными, устанавливаем айпи рп
        self.port_connect()  # соединяемся с ip:5556
        self.th5556.start()  # запускаем в отдельном потоке бесконечный цикл show5556()

    def closeEvent(self, event):  # обработчик: прихлопнули это окно крестиком
        if self.isVisible():
            print(f"push X on {self}")
            window.pushButton_5556.toggle()
        save.add_data_to_json({"5556": self.geometry().getRect()})  # сохраняем координаты размещения этого окна
        if self.th5556:
            self.th5556.requestInterruption()  # эй поток! заканчивай!
            self.th5556.wait()  # подождем пока закончит
        self.port_disconnect()  # отсоединяемся от ip:5556
        self.close()


class DataWinApp30001(QWidget, Ui_Form30001, DataFrom30001):
    def __init__(self):
        super().__init__()  # Это здесь нужно для доступа к переменным, методам QWidget, Ui_Form30001
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна Ui_Form30001
        self.setVisible(False)
        self.setGeometry(*(save.get_from_json_data()['30001']))
        self.th30001 = Th1()  # Создаём объект отдельного потока в котором будем вынимать и показывать данные из порта 30001

    def __repr__(self) -> str:
        return f'WIN of RoboData: {self.port}'

    def show30001(self):
        alldata = self.get_info()
        if alldata['raw_jpg'] and alldata['sizeOfJPG']:
            pix = QPixmap()
            if PYSIDE_OR_PYQT == 'PYSIDE':
                if pix.loadFromData(alldata['raw_jpg'], len=alldata['sizeOfJPG'], format='JPG'):  # for pySide
                    self.label_jpg.setPixmap(pix)
            else:
                if pix.loadFromData(alldata['raw_jpg'], format='JPG'):  # for pyQt
                    self.label_jpg.setPixmap(pix)
        # там еще дохера данных
        self.update()

    def show_data(self, ip: str):
        setattr(self, 'ip', ip)
        self.port_connect()
        self.th30001.start()

    def closeEvent(self, event):
        if self.isVisible():
            print(f"push X on {self}")
            window.pushButton_30001.toggle()
        save.add_data_to_json({"30001": self.geometry().getRect()})
        if self.th30001:
            self.th30001.requestInterruption()
            self.th30001.wait()
        self.port_disconnect()
        self.close()


class DataWinApp30002(QWidget, Ui_Form30002, DataFrom30002):
    def __init__(self):
        super().__init__()  # Это здесь нужно для доступа к переменным, методам QWidget, Ui_Form30002
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна Ui_Form30002
        self.setVisible(False)
        self.setGeometry(*(save.get_from_json_data()['30002']))
        self.th30002 = Th2()  # Создаём объект отдельного потока в котором будем вынимать и показывать данные из порта 30002

    def __repr__(self) -> str:
        return f'WIN of RoboData: {self.port}'

    def show30002(self):
        alldata = self.get_info()
        self.label_fl1.setText(f'{alldata["fl1"]:.3f}')
        self.label_t1.setText(alldata["t1"])
        self.label_t2.setText(alldata["t2"])
        self.label_t3.setText(alldata["t3"])
        self.label_t4.setText(alldata["t4"])
        self.label_t6.setText(alldata["t6"])
        # там еще дохера данных
        self.update()

    def show_data(self, ip: str):
        setattr(self, 'ip', ip)
        self.port_connect()
        self.th30002.start()

    def closeEvent(self, event):
        if self.isVisible():
            print(f"push X on {self}")
            window.pushButton_30002.toggle()
        save.add_data_to_json({"30002": self.geometry().getRect()})
        if self.th30002:
            self.th30002.requestInterruption()
            self.th30002.wait()
        self.port_disconnect()
        self.close()


class DataWinApp30003(QWidget, Ui_Form30003, DataFrom30003):
    def __init__(self):
        super().__init__()  # Это здесь нужно для доступа к переменным, методам QWidget, Ui_Form30003
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна Ui_Form30003
        self.setVisible(False)
        self.setGeometry(*(save.get_from_json_data()['30003']))
        self.th30003 = Th3()  # Создаём объект отдельного потока в котором будем вынимать и показывать данные из порта 30003

    def __repr__(self) -> str:
        return f'WIN of RoboData: {self.port}'

    def show30003(self):
        raw_data = self.get_info()
        if raw_data['sizeOfJPG'] < 0:  # => text
            if 'text' in raw_data.keys():
                self.textBrowser.append(raw_data['text'])
                self.textBrowser.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                # self.textBrowser.insertPlainText(raw_data['text'])
        else:  # => data+jpg
            if '1000' in raw_data.keys():
                x, y, ang = raw_data['1000']
                self.label_coord_x.setText(f'{x:.3f}')
                self.label_coord_y.setText(f'{y:.3f}')
                self.label_coord_ang.setText(f'{ang:.3f}')
            if '1004' in raw_data.keys():
                date, fval1, fval2 = raw_data['1004']
                self.label_date.setText(date)
                self.label_fVal1.setText(f'{fval1:.3f}')
                self.label_fVal2.setText(f'{fval2:.3f}')
            if 'jpg' in raw_data.keys():
                pix = QPixmap()
                if PYSIDE_OR_PYQT == 'PYSIDE':
                    if pix.loadFromData(raw_data['jpg'], len=raw_data['sizeOfJPG'], format='JPG'):  # for pySide
                        self.label_jpg.setPixmap(pix)
                else:
                    if pix.loadFromData(raw_data['jpg'], format='JPG'):  # for pyQt
                        self.label_jpg.setPixmap(pix)
        self.update()

    def show_data(self, ip: str):
        setattr(self, 'ip', ip)
        self.port_connect()
        self.th30003.start()

    def closeEvent(self, event):
        if self.isVisible():
            print(f"push X on {self}")
            window.pushButton_30003.toggle()
        self.textBrowser.clear()
        save.add_data_to_json({"30003": self.geometry().getRect()})
        if self.th30003:
            self.th30003.requestInterruption()
            self.th30003.wait()
        self.port_disconnect()
        self.close()


class Th1(QThread):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return 'Thread for 30001'

    def run(self):
        print(f"{self} is started")
        while not self.isInterruptionRequested():  # пока не придет прерывание "эй,заканчивай!", крутимся бесконечно
            window.datawindow30001.show30001()  # показываем данные с порта в окне
            self.msleep(DELAY)  # спим 1 мСек
        print(f"{self} is finished")


class Th2(QThread):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return 'Thread for 30002'

    def run(self):
        print(f"{self} is started")
        while not self.isInterruptionRequested():
            window.datawindow30002.show30002()
            self.msleep(DELAY)
        print(f"{self} is finished")


class Th3(QThread):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return 'Thread for 30003'

    def run(self):
        print(f"{self} is started")
        while not self.isInterruptionRequested():
            window.datawindow30003.show30003()
            self.msleep(DELAY)
        print(f"{self} is finished")


class Th5(QThread):
    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return 'Thread for 5556'

    def run(self):
        print(f"{self} is started")
        while not self.isInterruptionRequested():
            window.datawindow5556.show5556()
            self.msleep(DELAY)
        print(f"{self} is finished")


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    import sys  # sys нужен для передачи argv в QApplication
    from iCleboIP4finder import get_ip
    from GUI.settings_saver import SettingsSaver

    app = QApplication(sys.argv)  # Новый экземпляр
    save = SettingsSaver('GUI/settings.json')  # Создаём объект сохраняшки расположения окон
    window = MainWindowApp(get_ip())  # Создаём объект основного окна и закидываем в него айпи4 робота

    window.show()  # Показываем основное окно
    sys.exit(app.exec_())  # app.exec_()    и запускаем приложение
