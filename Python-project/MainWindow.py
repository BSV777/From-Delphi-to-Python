#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
import mBaseWindow  # Импортируем базовую форму, нарисованную в дизайнере
import mParserTextFile
import mWriteHTMLFile

from mGUI import *

MINTOP = 65
MINLEFT = 1

# Класс MainWindow, унаследованный от QMainWindow и Ui_BaseWindow - из дизайнера
class MainWindow(QMainWindow, mBaseWindow.Ui_BaseWindow):
    _modified = False  # Схема не была модифицирована или была сохранена
    _fileName = None
    _fileNameWeb = None
    _objList = []

    # Внутренние процедуры класса
    # ------------------------------------------------------------------------------
    # TODO: Создать QScrollArea (возможно в UI)
    # ------------------------------------------------------------------------------

    def _select(self):
        print("_select")  # DEBUG: Отладочный вывод

    def _createbt(self):
        print("_createbt")  # DEBUG: Отладочный вывод
        self._modified = True
        self.button1 = QtGui.QPushButton(u"Кнопка", self)  # Создали объект кнопка, экземпляр класса QPushButton
        self.button1.move(MINLEFT, MINTOP)
        self.button1.show()


    def _createed(self):
        print("_createed")  # DEBUG: Отладочный вывод
        self._modified = True
        self.edit1 = QtGui.QLineEdit(u"Поле", self)    # Создали объект поле ввода, экземпляр класса QLineEdit
        self.edit1.move(150, 160)
        self.edit1.show()



    def _createlb(self):
        print("_createlb")  # DEBUG: Отладочный вывод
        self._modified = True
        self.label1 = QtGui.QLabel(u"Надпись2", self)   # Создали объект надпись класса QLabel
        self.label1.move(100, 150)
        self.label1.show()


    def _delobj(self):
        print("_delobj")  # DEBUG: Отладочный вывод
        self._modified = True


    def _about(self):
        print("_about")  # DEBUG: Отладочный вывод
        msgBox = QMessageBox()
        msgBox.setText(u"--------------    О программе   --------------")
        msgBox.setInformativeText(u"Редактор визуального размещения компонентов")
        ret = msgBox.exec_()

    def _create(self):
        if self._modified:
            msgBox = QMessageBox()
            msgBox.setText(u"Документ не сохранен")
            msgBox.setInformativeText(u"Сохранить изменения?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self._save()
            elif ret == QMessageBox.Discard:
                self._createFile()
        else:
            self._createFile()

    def _createFile(self):
        self._modified = False  # Схема не была модифицирована или была сохранена
        self._fileName = None
        self._fileNameWeb = None
        self.setWindowTitle(u"Editor - ")
        for i in self._objList:  # Удаляем объекты на форме
            i.deleteLater()
        self._objList = []

    def _open(self):
        if self._modified:
            msgBox = QMessageBox()
            msgBox.setText(u"Документ не сохранен")
            msgBox.setInformativeText(u"Сохранить изменения?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self._save()
            elif ret == QMessageBox.Discard:
                self._readFile()
        else:
            self._readFile()

    def _readFile(self):
        typ = {"Button": 1, "TextEdit": 2, "Label": 3}
        self._fileName = unicode(QFileDialog.getOpenFileName(self, u"Открыть файл"))
        if self._fileName is not None:  # Если пользователь указал имя файла
            dir = os.path.dirname(self._fileName)
            name, ext = os.path.splitext(os.path.basename(self._fileName))
            if os.path.exists(str(self._fileName)):  # Если входной файл существует вызываем парсер
                self._modified = False  # Схема не была модифицирована или была сохранена
                self.setWindowTitle(u"Editor - " + name)
                array = []  # Список объектов с их свойствами. Каждый объект представлен словарем
                if mParserTextFile.ParserTextFile(self._fileName, array):  # Ошибки были записаны в лог
                    msgBox = QMessageBox()
                    msgBox.setText(u"--- Input file contains errors. See log file: ---")
                    msgBox.setInformativeText(os.path.join(dir, name + ".log"))
                    ret = msgBox.exec_()
                for i in self._objList:  # Удаляем объекты на форме
                    i.deleteLater()
                self._objList = []
                for i in range(len(array)):
                    if array[i]["typ"] == typ["Button"]:  # Создали объект кнопка, экземпляр класса QPushButton
                        self._objList.append(QtGui.QPushButton(array[i]["text"], self))
                    elif array[i]["typ"] == typ["TextEdit"]:  # Создали объект поле ввода, экземпляр класса QLineEdit
                        self._objList.append(QtGui.QLineEdit(array[i]["text"], self))
                    elif array[i]["typ"] == typ["Label"]:  # Создали объект надпись, экземпляр класса QLabel
                        self._objList.append(QtGui.QLabel(array[i]["text"], self))
                    self._objList[-1].move(MINLEFT + array[i]["left"], MINTOP + array[i]["top"])
                    self._objList[-1].setFixedSize(array[i]["width"], array[i]["height"])
                    self._objList[-1].show()

    def _save(self):
        if self._fileName is None:  # Не присвоено имя файла
            self._saveas()
        else:
            with open(self._fileName, "w") as f:
                for obj in self._objList:
                    rect = obj.geometry()
                    size = u"left=\"" + str(rect.x() - MINLEFT) + "\"; top=\"" + str(rect.y() - MINTOP) + \
                           "\"; width=\"" + str(rect.width()) + "\"; height=\"" + str(rect.height()) + "\"; "
                    if type(obj) is QPushButton:  # Сохраняемый объект есть экземпляр класса QPushButton
                        s = u"<Button " + size + u"caption=\"" + str(obj.text()) + "\">"
                    elif type(obj) is QLineEdit:  # Сохраняемый объект есть экземпляр класса QLineEdit
                        s = u"<TextEdit " + size + u"text=\"" + str(obj.text()) + "\">"
                    elif type(obj) is QLabel:  # Сохраняемый объект есть экземпляр класса QLabel
                        s = u"<Label " + size + u"text=\"" + str(obj.text()) + "\">"
                    f.write(s + '\n')
            self._modified = False  # Схема не была модифицирована или была сохранена

    def _saveas(self):
        self._fileName = unicode(QFileDialog.getSaveFileName(self, u"Сохранить файл как"))
        if self._fileName is not None:  # Если пользователь указал имя файла
            self.setWindowTitle(u"Editor - " + self._fileName)
            self._save()

    def _saveasweb(self):
        self._fileNameWeb = unicode(QFileDialog.getSaveFileName(self, u"Сохранить файл как Web-страницу"))
        if self._fileName is not None:  # Если пользователь указал имя файла
            self._createWeb()

    def _createWeb(self):
        typ = {"Button": 1, "TextEdit": 2, "Label": 3}
        array = []
        i = 0
        for obj in self._objList:
            # Создаем новый элемент списка
            array.append({"text": "", "typ": 0, "left": 0, "top": 0, "width": 0, "height": 0, "colspan": 0, "rowspan": 0})
            rect = obj.geometry()
            array[i]["left"] = rect.x() - MINLEFT
            array[i]["top"] = rect.y() - MINTOP
            array[i]["width"] = rect.width()
            array[i]["height"] = rect.height()
            array[i]["text"] = obj.text()
            if type(obj) is QPushButton:  # Сохраняемый объект есть экземпляр класса QPushButton
                array[i]["typ"] = typ["Button"]
            elif type(obj) is QLineEdit:  # Сохраняемый объект есть экземпляр класса QLineEdit
                array[i]["typ"] = typ["TextEdit"]
            elif type(obj) is QLabel:  # Сохраняемый объект есть экземпляр класса QLabel
                array[i]["typ"] = typ["Label"]
            i += 1
        mWriteHTMLFile.WriteHTMLFile(self._fileNameWeb, array)


    def _openasweb(self):
        self._fileNameWeb = 'editor_py_tmp.htm'
        self._createWeb()
        # TODO: Здесь вызвать внешний браузер с открытием файла editor_py_tmp.htm



    def _exit(self):
        if not self._modified:
            exit(0)
        else:
            msgBox = QMessageBox()
            msgBox.setText(u"Документ не сохранен")
            msgBox.setInformativeText(u"Сохранить изменения?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self._save()
                exit(0)
            elif ret == QMessageBox.Discard:
                exit(0)

    # ------------------------------------------------------------------------------

    def __init__(self):  # Объявляем конструктор класса MainWindow
        super(MainWindow,
              self).__init__()  # Сначала выполняем действия, предусмотренные конструктором родительского класса
        self.setupUi(self)  # Вызов метода, унаследованного от Ui_BaseWindow для инициализации виджетов класса

        self.setFont(QFont('SansSerif', 9))  # Устанавливаем шрифт

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
