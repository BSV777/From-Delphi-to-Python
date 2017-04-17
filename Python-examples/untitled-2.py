from PyQt4 import QtCore, QtGui
class MyWindow(QtGui.QWidget):   #Объявляем класс MyWindow, наследующий свойства класса QWidget модуля QtGui
 
    def __init__ (self, parent=None):  #Объявляем процедуру -конструктор класса MyWindow
        QtGui.QWidget.__init__ (self, parent) #Сначала выполняем действия, предусмотренные конструктором родительского класса (QWidget)
        self.label1= QtGui.QLabel(u"Показатель адиабаты") # Создали объект надпись класса QLabel
        self.label2= QtGui.QLabel(u"Коэффициент скорости") # Создали объект надпись класса QLabel
        self.Edit1 =  QtGui.QLineEdit("1.4")# Создали объект поле ввода
        self.Edit2 =  QtGui.QLineEdit("1")# Создали объект поле ввода
        self.btnQuit = QtGui.QPushButton("Close") # Создали объект кнопка, экземпляр класса QPushButton
        self.Button1 = QtGui.QPushButton(u"Вычислить") # Создали объект кнопка, экземпляр класса QPushButton
        self.plainTextEdit=QtGui.QPlainTextEdit()# Создали объект поле многострочного ввода, экземпляр класса QPlainTextEdit
        self.hbox = QtGui.QHBoxLayout()# Создали объект горизонтальный контейнер, экземпляр класса QHBoxLayout
        self.vbox = QtGui.QVBoxLayout()# Создали объект вертикальный контейнер, экземпляр класса QVBoxLayout
        self.vbox2 = QtGui.QVBoxLayout()# Создали объект вертикальный контейнер, экземпляр класса QVBoxLayout
        self.vbox.addWidget(self.label1)# Добавили объект надпись в вертикальный контейнер
        self.vbox.addWidget(self.Edit1)# Добавили объект поле ввода в вертикальный контейнер
        self.vbox.addWidget(self.label2)# Добавили объект надпись в вертикальный контейнер
        self.vbox.addWidget(self.Edit2)# Добавили объект поле ввода в вертикальный контейнер
        self.vbox.addWidget(self.Button1)# Добавили объект кнопка в вертикальный контейнер
        self.vbox.addWidget(self.btnQuit)# Добавили объект кнопка в вертикальный контейнер
        self.hbox.addLayout(self.vbox)# Добавили объект котнтейнер в вертикальный контейнер
        self.hbox.addLayout(self.vbox2)# Добавили объект котнтейнер в горизонтальный контейнер
        self.vbox2.addWidget(self.plainTextEdit)# Добавили объект поле многострочного ввода в вертикальный контейнер
        self.setLayout(self.hbox)# Установили горизонтальный контейнер в качестве рабочей области собственного объекта  класса MyWindow(
        self. connect (self. btnQuit, QtCore. SIGNAL ( "clicked () ") ,QtGui.qApp.quit)#Связали процедуру QtGui.qApp.quit с событием нажатия на кнопку btnQuit
        self.connect(self.Button1,QtCore.SIGNAL("clicked()"),self.calculate)#Связали процедуру calculate с событием нажатия на кнопку Button1
 
 
    def calculate(self): #Объявление процедуры calculate - метода объекта класса MyWindow
        L=float(self.Edit2.text())  # Читаем значение из поля ввода в переменную λ
        k=float(self.Edit1.text())  # Читаем значение из поля ввода в переменную k
        T=1-(k-1)/(k+1)*L**2        # Вычисляем
        self.plainTextEdit.setPlainText("T="+str(T))# Записываем атрибут PlainText объекта PlainTextEdit
 
 
 
if __name__ == '__main__':# Основная процедура программы
    import sys
    app = QtGui.QApplication(sys.argv)# Создаем объект app (приложение) - экземпляр класса QApplication
    window = MyWindow() # Создаем объект window - экземпляр класса MyWindow()
    window.setWindowTitle(u"Газодинамическая функциия τ") #Записываем атрибут WindowTitle объекта window
    window.resize(300, 50)  #Установили размеры окна
    window. show () # Отображаем окно
    sys.exit(app.exec_()) #Запускаем цикл обработки событий объекта app (приложение)
