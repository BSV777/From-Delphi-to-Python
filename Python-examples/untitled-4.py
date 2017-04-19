import sys 
import numpy as np # Подключаем библиотеку numpy и даём ей псевдоним np 
import matplotlib as mpl  # Подключаем библиотеку matplotlib и даём ей псевдоним mpl
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# Импортируем из модуля backend_qt4agg библиотеки matplotlib.backends
# класс FigureCanvasQTAgg  и даём ему псевдоним FigureCanvas
from matplotlib.figure import Figure 
# Импортируем из модуля figure библиотеки matplotlib класс Figure
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Arial'
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
 
        self.hbox.addWidget(self.label1)# Добавили объект надпись в вертикальный контейнер
        self.hbox.addWidget(self.Edit1)# Добавили объект поле ввода в вертикальный контейнер
        self.hbox.addWidget(self.label2)# Добавили объект надпись в вертикальный контейнер
        self.hbox.addWidget(self.Edit2)# Добавили объект поле ввода в вертикальный контейнер
        self.hbox.addWidget(self.Button1)# Добавили объект кнопка в вертикальный контейнер
        self.vbox2.addLayout(self.hbox)# Добавили объект котнтейнер в горизонтальный контейнер
 
        self.figure = Figure()       # Создали объект figure, экземпляр класса Figure
        self.axes = self.figure.add_subplot( 111 ) # С помощью метода add_subplot класса Figure создали объект axes, экземпляр класса AxesSubplot
        ### 111 - это признак расположения на листе (для случая отображения нескольких графиков) 
        self.canvas = FigureCanvas( self.figure )# Создали объект canvas, экземпляр класса FigureCanvas
 
        self.vbox2.addWidget(self.canvas)       # Добавили объект canvas в вертикальный контейнер
        self.vbox2.addWidget(self.plainTextEdit)# Добавили объект поле многострочного ввода в вертикальный контейнер
        self.vbox2.addWidget(self.btnQuit)      # Добавили объект кнопка в вертикальный контейнер
 
        self.setLayout(self.vbox2)  # Установили горизонтальный контейнер в качестве рабочей области класса MyWindow
        self. connect (self. btnQuit, QtCore. SIGNAL ( "clicked () ") ,QtGui.qApp.quit)#Связали процедуру QtGui.qApp.quit с событием нажатия на кнопку btnQuit
        self.connect(self.Button1,QtCore.SIGNAL("clicked()"),self.calculate)#Связали процедуру calculate с событием нажатия на кнопку Button1
 
    def calculate(self):        #Объявление процедуры calculate - метода объекта класса MyWindow
        L=float(self.Edit2.text())  # Читаем значение из поля ввода в переменную λ
        k=float(self.Edit1.text())  # Читаем значение из поля ввода в переменную k
        T=1-(k-1)/(k+1)*L**2        # Вычисляем τ
        self.plainTextEdit.appendPlainText(u"λ="+str(L)+u",   τ="+str(T))# Записываем атрибут PlainText объекта PlainTextEdit
        x=np.arange(0,3,0.1)    #Массив значений аргумента
        y=1-(k-1)/(k+1)*x**2    #Создание массива значений функции как операция над массивом 
                                #обеспечивается библиотекой numpy (np) 
        self.axes.clear()       # Очищаем область построения графика
        self.axes.plot(x,y,label=u"τ(λ)") # Строим график
        self.axes.set_xbound(lower=0, upper=x.max()) # Устанавливаем диапазон оси X
        self.axes.set_ybound(lower=0, upper=1.1)     # Устанавливаем диапазон оси Y
        self.axes.set_xlabel('L')                    # Дали имя оси X
        self.axes.set_ylabel('T')                    # Дали имя оси Y
        self.axes.grid(True)                         # Добавили сетку
        self.axes.legend()                           # Добавили легенду
        self.canvas.draw()                           # Орисовываем график
 
if __name__ == '__main__':  # Основная процедура программы
    app = QtGui.QApplication(sys.argv)# Создаем объект app (приложение) - экземпляр класса QApplication
    window = MyWindow()     # Создаем объект window - экземпляр класса MyWindow()
    window.setWindowTitle(u"Газодинамическая функциия τ") #Записываем атрибут WindowTitle объекта window
    window.resize(600, 600) #Установили размеры окна
    window.show ()          # Отображаем окно
    window.calculate()      # Запускаем процедуру  calculate() чтобы отрисовать график при запуске
    sys.exit(app.exec_())   #Запускаем цикл обработки событий объекта app (приложение)
 
