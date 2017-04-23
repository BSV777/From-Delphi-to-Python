#!/usr/bin/env python
# -*- coding: utf-8 -*-

def WriteHTMLFile(fileName, arr):
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    array = []  # Список объектов с их свойствами. Каждый объект представлен словарем
    f = open(fileName, "w")

    MinHeight = 21
    MinWidth = 21
    DefaultHeight = 21
    DefaultWidth = 70

    # TODO: 1. Заменить case на if

    # NCom, NX, NY, i, j, n, x, y, k, p, t:integer
    # s, ts, L:string
    # sp:boolean
    # Matr: array of array of integer  # Рабочая матрица парсера, где
    # строка 0  -  абсолютные координаты вертикальных границ объектов
    # столбец 0  -  абсолютные координаты горизонтальных границ объектов
    # Возможные значения ячеек внутри:
    # 32767  -  необработанная ячейка
    # N > 0  -  ячейка содержит левый верхний угол объекта N
    # M < 0  -  ячейка содержит левый верхний угол пустого блока M
    # 0  -  все остальные ячейки после обработки

    #Spc: array of array of integer  # Матрица пустых блоков, назначение столбцов:
    # 0  -  значение COLSPAN для ячейки HTML
    # 1  -  значение ROWSPAN для ячейки HTML

    NCom = High(Prop_s) # Заменить на размер массива
    NX = NCom * 2
    NY = NCom * 2
    SetLength(Matr, NX + 1, NY + 1)
    for x = 0 to NX do
        for y = 0 to NY do
            Matr[x, y] = 32767
    for i = 1 to NCom do  # Заполнение строки 0 и столбца 0 координатами границ объектов  
        Matr[0, i * 2 - 1] = array[i]["top"]
        Matr[0, i * 2] = array[i]["top"] + array[i]["height"]
        Matr[i * 2 - 1, 0] = array[i]["left"]
        Matr[i * 2, 0] = array[i]["left"] + array[i]["width"]

    repeat  # Сортировка значений столбца 0
        p = 0
        for k = 1 to NY - 1 do
            if Matr[0, k] > Matr[0, k + 1]:
                t = Matr[0, k]
                Matr[0, k] = Matr[0, k + 1]
                Matr[0, k + 1] = t
                p += 1
    until p = 0

    repeat  # Удаление дублей в столбце 0
        for k = 1 to NY - 1 do
            p = 0
            if (Matr[0, k]=Matr[0, k + 1]):
                for i = k + 1 to NY - 1 do 
                    Matr[0, i] = Matr[0, i + 1]
                p += 1
        NY = NY - p
    until p = 0

    repeat  # Сортировка значений строки 0
        p = 0
        for k = 1 to NX - 1 do
            if Matr[k, 0] > Matr[k + 1, 0]:
                t = Matr[k, 0]
                Matr[k, 0] = Matr[k + 1, 0]
                Matr[k + 1, 0] = t
                p += 1
    until p = 0

    repeat  # Удаление дублей в строке 0
        for k = 1 to NX - 1 do
            p = 0
            if Matr[k, 0] = Matr[k + 1, 0]:
                for i = k + 1 to NX - 1 do 
                    Matr[i, 0] = Matr[i + 1, 0]
                p += 1
        NX = NX - p
    until p = 0

    for n = 1 to NCom do  # Расстановка объектов в блоки ячеек
        array[n]["colspan"] = 0
        for x = 1 to NX do
            if (Matr[x, 0] >= array[n]["left"]) and (
                Matr[x, 0] < array[n]["left"] + array[n]["width"]):
                array[n]["colspan"] = array[n]["colspan"] + 1
                array[n]["rowspan"] = 0
                for y = 1 to NY do
                    if (Matr[0, y] >= array[n]["top"]) and (
                        Matr[0, y] < array[n]["top"] + array[n]["height"]):
                        array[n]["rowspan"] = array[n]["rowspan"] + 1
                        if (Matr[x, 0] = array[n]["left"]) and (
                            Matr[0, y] = array[n]["top"]):
                            Matr[x, y] = n
                        else:
                            Matr[x, y] = 0

    n = 1  # Группировка пустых ячеек в блоки
    for y = 1 to NY - 1 do  
        for x = 1 to NX - 1 do
            i = 1
            if Matr[x, y] = 32767:
                Matr[x, y] = -n
                while (Matr[x + i, y] = 32767) and (x + i < NX) do
                    Matr[x + i, y] = 0
                    i += 1
                j = 1
                sp = True
                while (sp = True) and (y + j < NY) do
                    sp = True
                    for k = x to x + i - 1 do
                        if Matr[k, y + j] <> 32767:
                            sp = False
                    if sp = True:
                         for k = x to x + i - 1 do
                            Matr[k, y + j] = 0
                         j += 1
                SetLength(Spc, 2, n + 1)
                Spc[0, n] = i
                Spc[1, n] = j
                n += 1

    f.write('<HTML>')
    f.write('<HEAD>')
    f.write('<TITLE>Конкурсное задание</TITLE>')
    f.write('<META HTTP - EQUIV="Content - Type" CONTENT="text/html charset=windows - 1251">')
    f.write('</HEAD>')
    f.write('<BODY BGCOLOR=#ffffff>')
    f.write('<FORM>')
    f.write('<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=' + IntToStr(Matr[NX, 0] - Matr[1, 0]) + '>')
    f.write('   <TR>')
    for i = 1 to NX - 1 do  
        s = '      <TD><IMG height=1 src="spacer.gif" width=' + \
            IntToStr(Matr[i + 1, 0] - Matr[i, 0]) + '></TD>'
        f.write(s)
    
    f.write('   </TR>')
    for i = 1 to NY - 1 do  
        f.write('   <TR>')
        for j = 1 to NX - 1 do
            if Matr[j, i] > 0:  # Блок ячеек, содержащий объект
                if array[Matr[j, i]]["typ"] = typ["Button"]:
                    ts = 'button'
                if array[Matr[j, i]]["typ"] = typ["TextEdit"]:
                    ts = 'text'
                s = '      <TD'
                if array[Matr[j, i]]["colspan"] > 1:
                    s = s + ' COLSPAN=' + IntToStr(array[Matr[j, i]]["colspan"])
                if array[Matr[j, i]]["rowspan"] > 1:
                    s = s + ' ROWSPAN=' + IntToStr(array[Matr[j, i]]["rowspan"])
                case array[Matr[j, i]]["typ"] of
                    typ["Button"]:
                    s = s + '><INPUT HEIGHT="' + IntToStr(array[Matr[j, i]]["height"]) + \
                        '" WIDTH="' + IntToStr(array[Matr[j, i]]["width"]) + \
                        '" style="HEIGHT: ' + IntToStr(array[Matr[j, i]]["height"]) + \
                        'px WIDTH: ' + IntToStr(array[Matr[j, i]]["width"]) + \
                        'px" type=' + ts
                    f.write(s)
                    f.write('          value="' + array[Matr[j, i]]["text"] + '"></TD>')

                    typ["TextEdit"]:
                    s = s + '><INPUT SIZE="' + IntToStr(array[Matr[j, i]]["width"] div 8 -1) + \
                        '" style="WIDTH: ' + IntToStr(array[Matr[j, i]]["width"]) + \
                        'px" type=' + ts
                    f.write(s)
                    f.write('          value="' + array[Matr[j, i]]["text"] + '"></TD>')

                    typ["Label"]:
                    s = s + '>' + array[Matr[j, i]]["text"] + '</TD>'
                    f.write(s)
    
            if Matr[j, i] < 0:  # Пустой блок ячеек
                s = '      <TD'
                if Spc[0, - Matr[j, i]] > 1:
                    s = s + ' COLSPAN=' + IntToStr(Spc[0, - Matr[j, i]])
                if Spc[1, - Matr[j, i]] > 1:
                    s = s + ' ROWSPAN=' + IntToStr(Spc[1, - Matr[j, i]])
                s = s + '></TD>'
                f.write(s)

        s = '      <TD><IMG height=' + IntToStr(Matr[0, i + 1] - Matr[0, i]) + \
            ' src="spacer.gif" width=1></TD>'
        f.write(s)
        f.write('   </TR>')

    f.write('</TABLE>')
    f.write('</FORM>')
    f.write('</BODY>')
    f.write('</HTML>')
    f.close()
