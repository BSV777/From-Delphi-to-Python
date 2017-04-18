#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):   #Объявляем класс MyWindow, наследующий свойства класса QWidget модуля QtGui
 
    def __init__ (self, parent=None):  #Объявляем процедуру -конструктор класса MyWindow
        QtGui.QWidget.__init__(self, parent) #Сначала выполняем действия, предусмотренные конструктором родительского класса (QWidget)

        #self.label1= QtGui.QLabel(u"ТЕКСТ") # Создали объект надпись класса QLabel                
        #self.label1.move(15, 10)      
        
#        self.Edit1 =  QtGui.QLineEdit("3.14")# Создали объект поле ввода         
#        self.Button1 = QtGui.QPushButton(u"Кнопка") # Создали объект кнопка, экземпляр класса QPushButton
        
#        self.hbox = QtGui.QHBoxLayout()# Создали объект горизонтальный контейнер, экземпляр класса QHBoxLayout
        
#        self.vbox = QtGui.QVBoxLayout()# Создали объект вертикальный контейнер, экземпляр класса QVBoxLayout
        
#        self.vbox2 = QtGui.QVBoxLayout()# Создали объект вертикальный контейнер, экземпляр класса QVBoxLayout
        
#        self.vbox.addWidget(self.label1)# Добавили объект надпись в вертикальный контейнер
#        self.vbox.addWidget(self.Edit1)# Добавили объект поле ввода в вертикальный контейнер
        
#        self.vbox.addWidget(self.Button1)# Добавили объект кнопка в вертикальный контейнер
             
#        self.hbox.addLayout(self.vbox)# Добавили объект контейнер в вертикальный контейнер
#        self.hbox.addLayout(self.vbox2)# Добавили объект контейнер в горизонтальный контейнер
        
        
#        self.setLayout(self.hbox)# Установили горизонтальный контейнер в качестве рабочей области собственного объекта класса MyWindow
        self.label = QtGui.QLabel(u"Couldn")
        self.label.move(15, 10)

        self.label = QtGui.QLabel(u"care")
        self.label.move(35, 40)

        self.label = QtGui.QLabel('less')
        self.label.move(55, 65)

        self.label = QtGui.QLabel('And')
        self.label.move(115, 65)

        self.label = QtGui.QLabel('then')
        self.label.move(135, 45)

        self.label = QtGui.QLabel('you')
        self.label.move(115, 25)

        self.label = QtGui.QLabel('kissed')
        self.label.move(145, 10)

        self.label = QtGui.QLabel('me')
        self.label.move(215, 10)


class Absolute(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)


        label1= QtGui.QLabel(u"ТЕКСТ", self) # Создали объект надпись класса QLabel                
        label1.move(20, 10)
        
        edit1 =  QtGui.QLineEdit("3.14", self)# Создали объект поле ввода         
        edit1.move(20, 40)
        
        button1 = QtGui.QPushButton(u"Кнопка", self) # Создали объект кнопка, экземпляр класса QPushButton
        button1.move(20, 70)
    

if __name__ == "__main__" :
    import sys
    app = QtGui.QApplication(sys.argv) # Создаем объект app (приложение) - экземпляр класса QApplication

    #window = MyWindow() # Создаем объект window - экземпляр класса MyWindow()
    window = Absolute()
    
    window.setWindowTitle(u"Editor -") #Записываем атрибут WindowTitle объекта window
    window.resize(450, 250)  #Установили размеры окна
    window.show() # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки событий объекта app (приложение)
    