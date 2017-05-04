#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import webbrowser

import mBaseWindow  # Импортируем базовую форму, нарисованную в дизайнере
import mParserTextFile
import mWriteHTMLFile

MINHEIGHT = 21
MINWIDTH = 21
DEFAULTHEIGHT = 21
DEFAULTWIDTH = 70

TYP = {"Button": 1, "TextEdit": 2, "Label": 3}

MINTOP = 65
MINLEFT = 1

# TODO: Осталось реализовать перемещение, масштабирование и удаление объектов

# Класс MainWindow, унаследованный от QMainWindow и Ui_BaseWindow - из дизайнера
class MainWindow(QMainWindow, mBaseWindow.Ui_BaseWindow):
    _modified = False  # Схема не была модифицирована или была сохранена
    _fileName = None
    _fileNameWeb = None
    _objList = []
    _newOperation = None  # Указание на требуемую операцию с объектом:
    # None - не требуется, 0 - редактирование/удаление, 1, 2, 3 - создание в соответствии с TYP
    _canPlaceObject = False
    _currentObj = None
    _toMove = False
    _currX = 0
    _currY = 0
    _currDX = 0
    _currDY = 0

    # Внутренние процедуры класса
    # ------------------------------------------------------------------------------
    # TODO: Создать QScrollArea (возможно в UI)
    # ------------------------------------------------------------------------------

    # Использовать типы курсора
    # PointingHandCursor  # Курсор указывающий на объект
    # OpenHandCursor      # Курсор перед перемещением
    # ClosedHandCursor    # Курсор при перемещении
    # SizeVerCursor       # Курсор при изменении высоты
    # SizeHorCursor       # Курсор при изменении ширины
    # SizeBDiagCursor     # Курсор при изменении высоты и ширины - вторичная диагональ
    # SizeFDiagCursor     # Курсор при изменении - главная диагональ
    # ForbiddenCursor     # Курсор при невозможности помещения объекта в текущую позицию

    def _select(self):
        self.statusBar().showMessage(u"Выберите объект для редактирования")
        self._newOperation = 0
        self.unsetCursor()

    def _createbt(self):
        self.statusBar().showMessage(u"Кликните на поле, чтобы создать PushButton")
        self._newOperation = TYP["Button"]
        self.setMouseTracking(True)
        self.setCursor(QtCore.Qt.CrossCursor)

    def _createed(self):
        self.statusBar().showMessage(u"Кликните на поле, чтобы создать LineEdit")
        self._newOperation = TYP["TextEdit"]
        self.setMouseTracking(True)
        self.setCursor(QtCore.Qt.CrossCursor)

    def _createlb(self):
        self.statusBar().showMessage(u"Кликните на поле, чтобы создать Label")
        self._newOperation = TYP["Label"]
        self.setMouseTracking(True)
        self.setCursor(QtCore.Qt.CrossCursor)

    # TODO: Устранить рекурсивный вызов: QWidget::repaint: Recursive repaint detected
    # Перехватываем события
    def eventFilter(self, obj, event):
        if (event.type() == QtCore.QEvent.HoverMove) and (type(obj) is MainWindow):
            self._currX = event.pos().x()
            self._currY = event.pos().y()
        if not self._toMove and event.type() == QtCore.QEvent.MouseButtonPress and type(obj) is not MainWindow:
            self._currDX = event.pos().x()
            self._currDY = event.pos().y()
            self._currentObj = obj
            self._toMove = True
            self.setCursor(QtCore.Qt.ClosedHandCursor)
            self._newOperation = 0
            #self._currentObj.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        if event.type() == QtCore.QEvent.MouseButtonRelease and (type(obj) is not MainWindow):
            self._currentObj = None
            self._toMove = False
            self.unsetCursor()
            self._newOperation = 0
            #obj.setStyleSheet('border-style: none; border-width: 0px; border-color: black;')
        if self._toMove and type(obj) is not MainWindow:
            x = self._currX - self._currDX
            y = self._currY - self._currDY
            # Проверяем, возможно ли переместить объект в текущую позицию.
            self._canPlaceObject = True
            for obj in self._objList:
                if obj is not self._currentObj:
                    rect = obj.geometry()
                    if x < MINLEFT or y < MINTOP:
                        self._canPlaceObject = False
                    if (y + DEFAULTHEIGHT > rect.y()) and (y < rect.y() + rect.height()) \
                        and (x + DEFAULTWIDTH > rect.x()) and (x < rect.x() + rect.width()):
                        self._canPlaceObject = False
            if self._canPlaceObject:
                #self._currentObj.move(x, y)
                self.statusBar().showMessage("[" + str(x) + ", " + str(y) + "]")
        return False


    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        # Проверяем, возможно ли поместить создаваемый объект в текущую позицию.
        self._canPlaceObject = True
        for obj in self._objList:
            rect = obj.geometry()
            if x < MINLEFT or y < MINTOP:
                self._canPlaceObject = False
            if (y + DEFAULTHEIGHT > rect.y()) and (y < rect.y() + rect.height()) \
                and (x + DEFAULTWIDTH > rect.x()) and (x < rect.x() + rect.width()):
                self._canPlaceObject = False
        if self._canPlaceObject:
            if self._newOperation == TYP["Button"]:  # Создали объект кнопка, экземпляр класса QPushButton
                self._objList.append(QtGui.QPushButton(u"Button", self))
                self._objList[-1].installEventFilter(self)
                self._objList[-1].move(event.x(), event.y())
                self._objList[-1].setFixedSize(DEFAULTWIDTH, DEFAULTHEIGHT)
                self._objList[-1].show()
                self._modified = True
            elif self._newOperation == TYP["TextEdit"]:  # Создали объект поле ввода, экземпляр класса QLineEdit
                self._objList.append(QtGui.QLineEdit(u"Edit", self))
                self._objList[-1].installEventFilter(self)
                self._objList[-1].move(event.x(), event.y())
                self._objList[-1].setFixedSize(DEFAULTWIDTH, DEFAULTHEIGHT)
                self._objList[-1].show()
                self._modified = True
            elif self._newOperation == TYP["Label"]:  # Создали объект надпись, экземпляр класса QLabel
                self._objList.append(QtGui.QLabel(u"Label", self))
                self._objList[-1].installEventFilter(self)
                self._objList[-1].move(event.x(), event.y())
                self._objList[-1].setFixedSize(DEFAULTWIDTH, DEFAULTHEIGHT)
                self._objList[-1].show()
                self._modified = True
        return QMainWindow.mousePressEvent(self, event)

    def closeEvent(self, event):
        self._exit()
        return QMainWindow.closeEvent(self, event)

    def _delobj(self):
        self._newOperation = 0
        self.unsetCursor()

    def _about(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
        msgBox = QMessageBox()
        msgBox.setText(u"--------------    О программе   --------------")
        msgBox.setInformativeText(u"Редактор визуального размещения компонентов")
        ret = msgBox.exec_()

    def _create(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
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
        self.statusBar().showMessage(u"Готов")  # Первоначальная надпись в строке статуса

    def _open(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
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
                    if array[i]["typ"] == TYP["Button"]:  # Создали объект кнопка, экземпляр класса QPushButton
                        self._objList.append(QtGui.QPushButton(array[i]["text"], self))
                    elif array[i]["typ"] == TYP["TextEdit"]:  # Создали объект поле ввода, экземпляр класса QLineEdit
                        self._objList.append(QtGui.QLineEdit(array[i]["text"], self))
                    elif array[i]["typ"] == TYP["Label"]:  # Создали объект надпись, экземпляр класса QLabel
                        self._objList.append(QtGui.QLabel(array[i]["text"], self))
                    self._objList[-1].move(MINLEFT + array[i]["left"], MINTOP + array[i]["top"])
                    self._objList[-1].setFixedSize(array[i]["width"], array[i]["height"])
                    self._objList[-1].show()

    def _save(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
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
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
        self._fileName = unicode(QFileDialog.getSaveFileName(self, u"Сохранить файл как"))
        if self._fileName is not None:  # Если пользователь указал имя файла
            self.setWindowTitle(u"Editor - " + self._fileName)
            self._save()

    def _saveasweb(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
        self._fileNameWeb = unicode(QFileDialog.getSaveFileName(self, u"Сохранить файл как Web-страницу"))
        if self._fileName is not None:  # Если пользователь указал имя файла
            self._createWeb()

    def _createWeb(self):
        array = []
        for obj in self._objList:
            # Создаем новый элемент списка
            array.append({"text": "", "typ": 0, "left": 0, "top": 0, "width": 0, "height": 0, "colspan": 0, "rowspan": 0})
            rect = obj.geometry()
            array[-1]["left"] = rect.x() - MINLEFT
            array[-1]["top"] = rect.y() - MINTOP
            array[-1]["width"] = rect.width()
            array[-1]["height"] = rect.height()
            array[-1]["text"] = obj.text()
            if type(obj) is QPushButton:  # Сохраняемый объект есть экземпляр класса QPushButton
                array[-1]["typ"] = TYP["Button"]
            elif type(obj) is QLineEdit:  # Сохраняемый объект есть экземпляр класса QLineEdit
                array[-1]["typ"] = TYP["TextEdit"]
            elif type(obj) is QLabel:  # Сохраняемый объект есть экземпляр класса QLabel
                array[-1]["typ"] = TYP["Label"]
        mWriteHTMLFile.WriteHTMLFile(self._fileNameWeb, array)


    def _openasweb(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
        dir = os.path.abspath(os.curdir)
        self._fileNameWeb = os.path.join(dir, "editor_py_tmp.htm")
        self._createWeb()
        webbrowser.open(self._fileNameWeb)

    def _exit(self):
        self._newOperation = None  # Отмена требуемой операции с объектом
        self.unsetCursor()    # Возврат курсора по умолчанию
        if self._modified:
            msgBox = QMessageBox()
            msgBox.setText(u"Документ не сохранен")
            msgBox.setInformativeText(u"Сохранить изменения?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self._save()
        # TODO: Проверить существование файла editor_py_tmp.htm и удалить
        exit(0)

    # ------------------------------------------------------------------------------
    def __init__(self):  # Конструктор класса MainWindow
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
        a_select.triggered.connect(self._select)

        toolbar = self.addToolBar(u"Панель инструментов")
        toolbar.addAction(a_select)  # Кнопка тулбара
        toolbar.addAction(self.a_createbt)  # Кнопка тулбара
        toolbar.addAction(self.a_createed)  # Кнопка тулбара
        toolbar.addAction(self.a_createlb)  # Кнопка тулбара
        # ------------------------------------------------------------------------------
        self.installEventFilter(self)
        self.statusBar().showMessage(u"Готов")  # Первоначальная надпись в строке статуса


# Тестирование интерфейса
if __name__ == "__main__":
    app = QApplication([])  # Создаем объект app (приложение) - экземпляр класса QApplication
    test = MainWindow()  # Создаем объект MainForm - экземпляр класса MainWindow()
    test.setWindowTitle(u"test")  # Заголовок окна
    test.resize(450, 250)  # Установили размеры окна
    test.show()  # Отображаем окно
    app.exec_()  # Запускаем цикл обработки событий объекта app (приложение)
