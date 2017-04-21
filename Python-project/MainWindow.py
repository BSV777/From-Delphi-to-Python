#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from PyQt4.QtGui import *

import mBaseWindow  # Импортируем базовую форму, нарисованную в дизайнере


# Класс MainWindow, унаследованный от QMainWindow и Ui_BaseWindow - из дизайнера
class MainWindow(QMainWindow, mBaseWindow.Ui_BaseWindow):

    # Внутренние процедуры класса
    # ------------------------------------------------------------------------------
    # TODO: Работать здесь!
    # ------------------------------------------------------------------------------

    def _select(self):
        print("_select")  # DEBUG: Отладочный вывод

        # scrollArea = QtGui.QScrollArea(self)
        # self.label2 = QtGui.QLabel(u"Надпись2", self)  # Создали объект надпись класса QLabel
        # self.label2.move(80, 80)

        # self.items_ly.addWidget(label2)
        # self.add
        # addWidget(label2)
        # self.label2.setParent =


        # scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # scrollArea.setParent(self)
        # label2.setParent(scrollArea)
        # scrollArea.show()
        # scrollArea.setVisible(True)
        # print(scrollArea.sizes())

        # if scrollArea.isVisible():
        #    print('visible') 
        # else:
        #    print('not')

    def _createbt(self):
        print("_createbt")  # DEBUG: Отладочный вывод
        self.verticalLayout.addWidget(QtGui.QPushButton(u"Кнопка", self))


    def _createed(self):
        print("_createed")  # DEBUG: Отладочный вывод
        self.verticalLayout.addWidget(QtGui.QLineEdit(u"Поле", self))


    def _createlb(self):
        print("_createlb")  # DEBUG: Отладочный вывод
        self.verticalLayout.addWidget(QtGui.QLabel(u"Надпись", self))


    def _delobj(self):
        print("_delobj")  # DEBUG: Отладочный вывод

    def _about(self):
        print("_about")  # DEBUG: Отладочный вывод
        msgBox = QMessageBox()
        msgBox.setText(u"--------------    О программе   --------------")
        msgBox.setInformativeText(u"Редактор визуального размещения компонентов")
        ret = msgBox.exec_()

    def _create(self):
        print("_create")  # DEBUG: Отладочный вывод

    def _open(self):
        fileName = QFileDialog.getOpenFileName(self, u"Открыть файл")

    def _save(self):
        fileIsNew = True  # Сделать проверку, что файл не был сохранен
        if fileIsNew:
            self._saveas()
        else:
            pass  # Здесь сделать сохранение в файл

    def _saveas(self):
        fileName = QFileDialog.getOpenFileName(self, u"Сохранить файл как")

    def _saveasweb(self):
        fileName = QFileDialog.getOpenFileName(self, u"Сохранить файл как Web-страницу")

    def _openasweb(self):
        print("_openasweb")  # DEBUG: Отладочный вывод

    def _exit(self):
        msgBox = QMessageBox()
        msgBox.setText(u"Документ не сохранен")
        msgBox.setInformativeText(u"Сохранить изменения?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            print("need to save")
        elif ret == QMessageBox.Discard:
            exit(0)

    # ------------------------------------------------------------------------------

    def __init__(self):  # Объявляем конструктор класса MyWindow
        super(MainWindow,
              self).__init__()  # Сначала выполняем действия, предусмотренные конструктором родительского класса
        self.setupUi(self)  # Вызов метода, унаследованного от Ui_BaseWindow для инициализации виджетов класса

        self.setFont(QFont('SansSerif', 9))  # Устанавливаем шрифт


        # TODO: 1. Добавить скроллбары
        # ------------------------------------------------------------------------------
        # scrollArea.setWidget(label2)
        # self.setWidget(self.scrollArea)

        # self.scrollLayout = QtGui.QFormLayout()

        # scrollWidget = QtGui.QWidget() # cначала создаём сам виджет
        # scrollWidget.setLayout(self.scrollLayout) # добавляем на него слой

        # scrollArea = QtGui.QScrollArea()
        # scrollArea.setWidgetResizable(True) #разрешаем проктурку
        # scrollArea.setWidget(self.scrollWidget)

        # -----------------------------------------
        # self.gridLayout = QGridLayout(self)
        # self.scrollArea = QScrollView(self)
        # self.scrollArea.setGeometry(0, 0, 369, 286)
        # self.Form1Layout = QGridLayout(self.scrollArea.viewport())
        # self.gridLayout.addWidget(self.scrollArea, 0, 0)
        # ------------------------------------------------------------------------------

        # TEST: Тестовые объекты
        # ------------------------------------------------------------------------------
        # label1 = QtGui.QLabel(u"Надпись", self)         # Создали объект надпись класса QLabel
        # label1.move(120, 200)
        #
        # edit1 = QtGui.QLineEdit(u"Поле", self)          # Создали объект поле ввода
        # edit1.move(150, 160)
        #
        # button1 = QtGui.QPushButton(u"Кнопка", self)    # Создали объект кнопка, экземпляр класса QPushButton
        # button1.move(200, 200)


        # # ==============================================================================
        # # Создание меню - код рабочий, но не используется - перенесено в дизайнер
        # # ------------------------------------------------------------------------------
        # menubar = self.menuBar()  # Создание меню
        #
        # # Меню Файл
        # a_create = QtGui.QAction(u"Созд&ать", self)
        # a_create.setShortcut('Ctrl+N')
        # a_create.setStatusTip(u"Создать схему размещения")
        #
        # a_open = QtGui.QAction(u"&Открыть", self)
        # a_open.setShortcut('Ctrl+O')
        # a_open.setStatusTip(u"Открыть схему размещения объектов")
        #
        # a_save = QtGui.QAction(u"&Сохранить", self)
        # a_save.setShortcut('Ctrl+S')
        # a_save.setStatusTip(u"Сохранить схему размещения объектов")
        #
        # a_saveas = QtGui.QAction(u"Сохранить &как", self)
        # a_saveas.setStatusTip(u"Сохранить схему размещения объектов как...")
        #
        # a_saveasweb = QtGui.QAction(u"Сохранить как Web-страни&цу", self)
        # a_saveasweb.setStatusTip(u"Сохранить схему размещения объектов как Web-страницу")
        #
        # a_openasweb = QtGui.QAction(u"Открыть как &Web-страницу", self)
        # a_openasweb.setStatusTip(u"Открыть схему размещения объектов как Web-страницу")
        #
        # a_exit = QtGui.QAction(u"В&ыход", self)
        # a_exit.setShortcut('Ctrl+Q')
        # a_exit.setStatusTip(u"Выход из программы")
        #
        # m_file = menubar.addMenu(u"&Файл")
        # m_file.addAction(a_create)              # Строка меню
        # m_file.addAction(a_open)                # Строка меню
        # m_file.addSeparator()                   # Разделитель меню
        # m_file.addAction(a_save)                # Строка меню
        # m_file.addAction(a_saveas)              # Строка меню
        # m_file.addAction(a_saveasweb)           # Строка меню
        # m_file.addSeparator()                   # Разделитель меню
        # m_file.addAction(a_openasweb)           # Строка меню
        # m_file.addSeparator()                   # Разделитель меню
        # m_file.addAction(a_exit)                # Строка меню
        #
        # # Меню Объект
        # a_createbt = QtGui.QAction(QtGui.QIcon('icons/bt.png'), u"Создать &кнопку", self)
        # a_createbt.setStatusTip(u"Создать кнопку на форме")
        #
        # a_createed = QtGui.QAction(QtGui.QIcon('icons/ed.png'), u"Создать &поле ввода", self)
        # a_createed.setStatusTip(u"Создать поле ввода на форме")
        #
        # a_createlb = QtGui.QAction(QtGui.QIcon('icons/lb.png'), u"Создать &надпись", self)
        # a_createlb.setStatusTip(u"Создать надпись на форме")
        #
        # a_delobj = QtGui.QAction(u"У&далить объект", self)
        # a_delobj.setShortcut('DEL')
        # a_delobj.setStatusTip(u"Удалить выбранный объект")
        #
        # m_object = menubar.addMenu(u"&Объект")
        # m_object.addAction(a_createbt)          # Строка меню
        # m_object.addAction(a_createed)          # Строка меню
        # m_object.addAction(a_createlb)          # Строка меню
        # m_object.addSeparator()                 # Разделитель меню
        # m_object.addAction(a_delobj)            # Строка меню
        #
        # # Меню Справка
        # a_about = QtGui.QAction(u"&О программе", self)
        # a_about.setShortcut('F1')
        # a_about.setStatusTip(u"Сведения о программе")
        #
        # m_help = menubar.addMenu(u"&Справка")
        # m_help.addAction(a_about)  # Строка меню
        # # ==============================================================================

        # Меню - связь сигналы-слоты
        self.a_create.triggered.connect(self._create)
        self.a_open.triggered.connect(self._open)
        self.a_save.triggered.connect(self._save)
        self.a_saveas.triggered.connect(self._saveas)
        self.a_saveasweb.triggered.connect(self._saveasweb)
        self.a_openasweb.triggered.connect(self._openasweb)
        self.a_exit.triggered.connect(self._exit)
        self.a_createbt.triggered.connect(self._createbt)
        self.a_createed.triggered.connect(self._createed)
        self.a_createlb.triggered.connect(self._createlb)
        self.a_delobj.triggered.connect(self._delobj)
        self.a_about.triggered.connect(self._about)

        # Создание тулбара
        # ------------------------------------------------------------------------------
        a_select = QtGui.QAction(QtGui.QIcon('icons/obj.png'), u"Выбор объекта", self)
        a_select.setStatusTip(u"Редактировать существующий объект")
        a_select.triggered.connect(self._select)

        toolbar = self.addToolBar(u"Панель инструментов")
        toolbar.addAction(a_select)  # Кнопка тулбара
        toolbar.addAction(self.a_createbt)  # Кнопка тулбара
        toolbar.addAction(self.a_createed)  # Кнопка тулбара
        toolbar.addAction(self.a_createlb)  # Кнопка тулбара

        # ------------------------------------------------------------------------------

        self.statusBar().showMessage(u"Готов")  # Первоначальная надпись в строке статуса


# Тестирование интерфейса
if __name__ == "__main__":
    app = QApplication([])  # Создаем объект app (приложение) - экземпляр класса QApplication
    test = MainWindow()  # Создаем объект MainForm - экземпляр класса MainWindow()
    test.setWindowTitle(u"test")  # Заголовок окна
    test.resize(450, 250)  # Установили размеры окна
    test.show()  # Отображаем окно
    app.exec_()  # Запускаем цикл обработки событий объекта app (приложение)
