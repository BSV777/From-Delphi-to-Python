#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFont

class MyWindow(QtGui.QMainWindow):  #Объявляем класс MyWindow, наследующий свойства класса QMainWindow модуля QtGui
    def __init__(self, parent=None):  #Объявляем конструктор класса MyWindow
        QtGui.QWidget.__init__(self, parent) #Сначала выполняем действия, предусмотренные конструктором родительского класса (QWidget)

        self.setFont(QFont('SansSerif', 9)) #Устанавливаем шрифт
        
# TODO: 1. Добавить скроллбары
#------------------------------------------------------------------------------
        #self.scrollLayout = QtGui.QFormLayout()

        #scrollWidget = QtGui.QWidget() # cначала создаём сам виджет
        #scrollWidget.setLayout(self.scrollLayout) # добавляем на него слой

        #scrollArea = QtGui.QScrollArea()
        #scrollArea.setWidgetResizable(True) #разрешаем проктурку
        #scrollArea.setWidget(self.scrollWidget)
#------------------------------------------------------------------------------
        
# TEST: Тестовые объекты
#------------------------------------------------------------------------------
        label1= QtGui.QLabel(u"Надпись", self) # Создали объект надпись класса QLabel                
        label1.move(120, 130)
        
        edit1 =  QtGui.QLineEdit(u"Поле", self)# Создали объект поле ввода         
        edit1.move(150, 160)
        
        button1 = QtGui.QPushButton(u"Кнопка", self) # Создали объект кнопка, экземпляр класса QPushButton
        button1.move(200, 200)
#------------------------------------------------------------------------------


        self.statusBar().showMessage(u"Готов") #Первоначальная надпись в строке статуса   
        
#Создание меню        
#------------------------------------------------------------------------------    
        menubar = self.menuBar() #Создание меню
            
        #Подменю Файл   
        a_create = QtGui.QAction(u"Созд&ать", self)
        a_create.setShortcut('Ctrl+N')
        a_create.setStatusTip(u"Создать схему размещения")    
    
        a_open = QtGui.QAction(u"&Открыть", self)
        a_open.setShortcut('Ctrl+O')
        a_open.setStatusTip(u"Открыть схему размещения объектов")    
    
        a_save = QtGui.QAction(u"&Сохранить", self)
        a_save.setShortcut('Ctrl+S')
        a_save.setStatusTip(u"Сохранить схему размещения объектов")    
    
        a_saveas = QtGui.QAction(u"Сохранить &как", self)
        a_saveas.setStatusTip(u"Сохранить схему размещения объектов как...")    
    
        a_saveasweb = QtGui.QAction(u"Сохранить как Web-страни&цу", self)        
        a_saveasweb.setStatusTip(u"Сохранить схему размещения объектов как Web-страницу")    
    
        a_openasweb = QtGui.QAction(u"Открыть как &Web-страницу", self)        
        a_openasweb.setStatusTip(u"Открыть схему размещения объектов как Web-страницу")    
        
        a_exit = QtGui.QAction(u"В&ыход", self)
        a_exit.setShortcut('Ctrl+Q')
        a_exit.setStatusTip(u"Выход из программы")
        self.connect(a_exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        m_file = menubar.addMenu(u"&Файл")
        m_file.addAction(a_create)        #Строка меню
        m_file.addAction(a_open)          #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_save)          #Строка меню
        m_file.addAction(a_saveas)        #Строка меню
        m_file.addAction(a_saveasweb)     #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_openasweb)     #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_exit)          #Строка меню
        
        #Подменю Объект        
        a_createbt = QtGui.QAction(QtGui.QIcon('icons/exit.png'), u"Создать &кнопку", self)
        a_createbt.setStatusTip(u"Создать кнопку на форме")    

        a_createed = QtGui.QAction(QtGui.QIcon('icons/exit.png'), u"Создать &поле ввода", self)
        a_createed.setStatusTip(u"Создать поле ввода на форме")    

        a_createlb = QtGui.QAction(QtGui.QIcon('icons/exit.png'), u"Создать &надпись", self)
        a_createlb.setStatusTip(u"Создать надпись на форме")    

        a_delobj = QtGui.QAction(u"У&далить объект", self)
        a_delobj.setShortcut('DEL')
        a_delobj.setStatusTip(u"Удалить выбранный объект")    
        
        m_object = menubar.addMenu(u"&Объект")        
        m_object.addAction(a_createbt)   #Строка меню
        m_object.addAction(a_createed)   #Строка меню
        m_object.addAction(a_createlb)   #Строка меню
        m_object.addSeparator()          #Разделитель меню
        m_object.addAction(a_delobj)     #Строка меню
        
        #Подменю Справка
        a_about = QtGui.QAction(u"&О программе", self)
        a_about.setShortcut('F1')
        a_about.setStatusTip(u"Сведения о программе")    
        
        m_help = menubar.addMenu(u"&Справка")
        m_help.addAction(a_about)       #Строка меню        

#Создание тулбара
#------------------------------------------------------------------------------    
#TODO: 1. Подключить правильные иконки на кнопки

        a_select = QtGui.QAction(QtGui.QIcon('icons/exit.png'), u"Выбор объекта", self)
        a_select.setStatusTip(u"Редактировать существующий объект")    

        toolbar = self.addToolBar(u"Панель инструментов")
        toolbar.addAction(a_select)     #Кнопка тулбара
        toolbar.addAction(a_createbt)   #Кнопка тулбара
        toolbar.addAction(a_createed)   #Кнопка тулбара
        toolbar.addAction(a_createlb)   #Кнопка тулбара

#------------------------------------------------------------------------------    


if __name__ == "__main__" :

    app = QtGui.QApplication(sys.argv) # Создаем объект app (приложение) - экземпляр класса QApplication

    MainForm = MyWindow() # Создаем объект MainForm - экземпляр класса MyWindow()
    
    MainForm.setWindowTitle(u"Editor -") #Заголовок окна
    MainForm.resize(450, 250)  #Установили размеры окна
    MainForm.show() # Отображаем окно


# TODO: 1. Протестировать создание объектов в Runtime
#------------------------------------------------------------------------------        
    #label2= QtGui.QLabel(u"Надпись2") # Создали объект надпись класса QLabel                
    #MainForm.add(label2)
#------------------------------------------------------------------------------        
    
    sys.exit(app.exec_()) #Запускаем цикл обработки событий объекта app (приложение)
    