# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mBaseWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BaseWindow(object):
    def setupUi(self, BaseWindow):
        BaseWindow.setObjectName(_fromUtf8("BaseWindow"))
        BaseWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(BaseWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        BaseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BaseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.m_file = QtGui.QMenu(self.menubar)
        self.m_file.setObjectName(_fromUtf8("m_file"))
        self.m_object = QtGui.QMenu(self.menubar)
        self.m_object.setObjectName(_fromUtf8("m_object"))
        self.m_help = QtGui.QMenu(self.menubar)
        self.m_help.setObjectName(_fromUtf8("m_help"))
        BaseWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BaseWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BaseWindow.setStatusBar(self.statusbar)
        self.a_create = QtGui.QAction(BaseWindow)
        self.a_create.setObjectName(_fromUtf8("a_create"))
        self.a_open = QtGui.QAction(BaseWindow)
        self.a_open.setObjectName(_fromUtf8("a_open"))
        self.a_save = QtGui.QAction(BaseWindow)
        self.a_save.setObjectName(_fromUtf8("a_save"))
        self.a_saveas = QtGui.QAction(BaseWindow)
        self.a_saveas.setObjectName(_fromUtf8("a_saveas"))
        self.a_saveasweb = QtGui.QAction(BaseWindow)
        self.a_saveasweb.setObjectName(_fromUtf8("a_saveasweb"))
        self.a_openasweb = QtGui.QAction(BaseWindow)
        self.a_openasweb.setObjectName(_fromUtf8("a_openasweb"))
        self.a_exit = QtGui.QAction(BaseWindow)
        self.a_exit.setObjectName(_fromUtf8("a_exit"))
        self.a_createbt = QtGui.QAction(BaseWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_createbt.setIcon(icon)
        self.a_createbt.setObjectName(_fromUtf8("a_createbt"))
        self.a_createed = QtGui.QAction(BaseWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/ed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_createed.setIcon(icon1)
        self.a_createed.setObjectName(_fromUtf8("a_createed"))
        self.a_createlb = QtGui.QAction(BaseWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/lb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_createlb.setIcon(icon2)
        self.a_createlb.setObjectName(_fromUtf8("a_createlb"))
        self.a_delobj = QtGui.QAction(BaseWindow)
        self.a_delobj.setObjectName(_fromUtf8("a_delobj"))
        self.a_about = QtGui.QAction(BaseWindow)
        self.a_about.setObjectName(_fromUtf8("a_about"))
        self.actionErerere = QtGui.QAction(BaseWindow)
        self.actionErerere.setObjectName(_fromUtf8("actionErerere"))
        self.a_prop = QtGui.QAction(BaseWindow)
        self.a_prop.setObjectName(_fromUtf8("a_prop"))
        self.m_file.addAction(self.a_create)
        self.m_file.addAction(self.a_open)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_save)
        self.m_file.addAction(self.a_saveas)
        self.m_file.addAction(self.a_saveasweb)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_openasweb)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_exit)
        self.m_object.addAction(self.a_createbt)
        self.m_object.addAction(self.a_createed)
        self.m_object.addAction(self.a_createlb)
        self.m_object.addSeparator()
        self.m_object.addAction(self.a_delobj)
        self.m_object.addSeparator()
        self.m_object.addAction(self.a_prop)
        self.m_help.addAction(self.a_about)
        self.menubar.addAction(self.m_file.menuAction())
        self.menubar.addAction(self.m_object.menuAction())
        self.menubar.addAction(self.m_help.menuAction())

        self.retranslateUi(BaseWindow)
        QtCore.QMetaObject.connectSlotsByName(BaseWindow)

    def retranslateUi(self, BaseWindow):
        BaseWindow.setWindowTitle(_translate("BaseWindow", "MainWindow", None))
        self.m_file.setTitle(_translate("BaseWindow", "&Файл", None))
        self.m_object.setTitle(_translate("BaseWindow", "&Объект", None))
        self.m_help.setTitle(_translate("BaseWindow", "&Справка", None))
        self.a_create.setText(_translate("BaseWindow", "Созд&ать", None))
        self.a_create.setStatusTip(_translate("BaseWindow", "Создать схему размещения", None))
        self.a_create.setShortcut(_translate("BaseWindow", "Ctrl+N", None))
        self.a_open.setText(_translate("BaseWindow", "&Открыть", None))
        self.a_open.setStatusTip(_translate("BaseWindow", "Открыть схему размещения объектов", None))
        self.a_open.setShortcut(_translate("BaseWindow", "Ctrl+O", None))
        self.a_save.setText(_translate("BaseWindow", "&Сохранить", None))
        self.a_save.setStatusTip(_translate("BaseWindow", "Сохранить схему размещения объектов", None))
        self.a_save.setShortcut(_translate("BaseWindow", "Ctrl+S", None))
        self.a_saveas.setText(_translate("BaseWindow", "Сохранить &как", None))
        self.a_saveas.setStatusTip(_translate("BaseWindow", "Сохранить схему размещения объектов как...", None))
        self.a_saveasweb.setText(_translate("BaseWindow", "Сохранить как Web-страни&цу", None))
        self.a_saveasweb.setStatusTip(_translate("BaseWindow", "Сохранить схему размещения объектов как Web-страницу", None))
        self.a_openasweb.setText(_translate("BaseWindow", "Открыть как &Web-страницу", None))
        self.a_openasweb.setStatusTip(_translate("BaseWindow", "Открыть схему размещения объектов как Web-страницу", None))
        self.a_exit.setText(_translate("BaseWindow", "В&ыход", None))
        self.a_exit.setStatusTip(_translate("BaseWindow", "Выход из программы", None))
        self.a_exit.setShortcut(_translate("BaseWindow", "Ctrl+Q", None))
        self.a_createbt.setText(_translate("BaseWindow", "Создать &кнопку", None))
        self.a_createed.setText(_translate("BaseWindow", "Создать &поле ввода", None))
        self.a_createlb.setText(_translate("BaseWindow", "Создать &надпись", None))
        self.a_delobj.setText(_translate("BaseWindow", "У&далить объект", None))
        self.a_delobj.setShortcut(_translate("BaseWindow", "Del", None))
        self.a_about.setText(_translate("BaseWindow", "&О программе", None))
        self.a_about.setStatusTip(_translate("BaseWindow", "Сведения о программе", None))
        self.a_about.setShortcut(_translate("BaseWindow", "F1", None))
        self.actionErerere.setText(_translate("BaseWindow", "ererere", None))
        self.a_prop.setText(_translate("BaseWindow", "Свойства", None))

