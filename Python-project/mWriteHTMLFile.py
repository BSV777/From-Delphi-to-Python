#!/usr/bin/env python
# -*- coding: utf-8 -*-

def WriteHTMLFile(fileName, arr):
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    f = open(fileName, "w")

    # NCom, NX, NY, i, j, n, x, y, k, p, t:integer
    # s, ts, L:string
    # sp:boolean

    NCom = len(arr)
    NX = NY = NCom * 2

    Matr = []
    # Matr - двумерный массив, где
    # строка 0 - абсолютные координаты вертикальных границ объектов
    # столбец 0 - абсолютные координаты горизонтальных границ объектов
    # Возможные значения ячеек внутри:
    # None - необработанная ячейка
    # N > 0 - ячейка содержит левый верхний угол _объекта_ N
    # M < 0 - ячейка содержит левый верхний угол _пустого_блока_ M
    # '' - все остальные ячейки после обработки

    # Формирование отсортированного списка уникальных значений границ объекта по вертикали
    col = []
    for i in range(NCom):
        if arr[i]["top"] not in col:
            col.append(arr[i]["top"])
        if arr[i]["top"] + arr[i]["height"] not in col:
            col.append(arr[i]["top"] + arr[i]["height"])
    col.sort()

    # Формирование отсортированного списка уникальных значений границ объекта по горизонтали
    row = []
    for i in range(NCom):
        if arr[i]["left"] not in row:
            row.append(arr[i]["left"])
        if arr[i]["left"] + arr[i]["width"] not in row:
            row.append(arr[i]["left"] + arr[i]["width"])
    row.sort()

    # Заполнение строки 0 и столбца 0 координатами границ объектов, все остальные ячейки = None
    Matr.append([])
    Matr[0] = [None] + row
    for y in range(1, len(col) + 1):
        Matr.append([])
        Matr[y].append(col[y - 1])
        for x in range(1,len(row) + 1):
            Matr[y].append(None)

    # Расстановка объектов в блоки ячеек
    # --------------------------------------------------------------------------------
    for n in range(NCom):
        arr[n]["rowspan"] = 0
        for y in range(1, len(col) + 1):
            if (Matr[y][0] >= arr[n]["top"]) and (Matr[y][0] < (arr[n]["top"] + arr[n]["height"])):
                arr[n]["rowspan"] = arr[n]["rowspan"] + 1
                arr[n]["colspan"] = 0
                for x in range(1, len(row) + 1):
                    if (Matr[0][x] >= arr[n]["left"]) and (Matr[0][x] < (arr[n]["left"] + arr[n]["width"])):
                        arr[n]["colspan"] = arr[n]["colspan"] + 1
                        if (Matr[0][x] == arr[n]["left"]) and (Matr[y][0] == arr[n]["top"]):
                            Matr[y][x] = n
                        else:
                            Matr[y][x] = ''

    # Группировка пустых ячеек в блоки
    # --------------------------------------------------------------------------------
    Spc = []
    # Spc - двумерный массив пустых блоков, назначение столбцов:
    # 0  -  значение COLSPAN для ячейки HTML
    # 1  -  значение ROWSPAN для ячейки HTML

    # TODO: Переделать, отладить
    n = 1
    for y in range(1, len(col) + 1):
        for x in range(1, len(row) + 1):
            i = 1
            if Matr[x, y] == None:
                Matr[x, y] = -n
                while (Matr[x + i, y] == None) and (x + i < NX)
                    Matr[x + i, y] = ''
                    i += 1
                j = 1
                sp = True
                while (sp == True) and (y + j < NY)
                    sp = True
                    for k = x to x + i - 1
                        if Matr[k, y + j] <> None:
                            sp = False
                    if sp == True:
                         for k in range(x, x + i):
                            Matr[k, y + j] = ''
                         j += 1
                SetLength(Spc, 2, n + 1)
                Spc[0, n] = i
                Spc[1, n] = j
                n += 1

    for tmp in range(len(arr)): f.write(str(arr[tmp]) + "\n")  # DEBUG: Отладочный вывод
    f.write("\n\n")  # DEBUG: Отладочный вывод
    for tmp in range(len(Matr)): f.write(str(Matr[tmp]) + "\n")  # DEBUG: Отладочный вывод
    f.write("\n\n")  # DEBUG: Отладочный вывод
    for tmp in range(len(Spc)): f.write(str(Spc[tmp]) + "\n")  # DEBUG: Отладочный вывод

    # f.write('<HTML>')
    # f.write('<HEAD>')
    # f.write('<TITLE>Editor</TITLE>')
    # f.write('<META HTTP - EQUIV="Content - Type" CONTENT="text/html charset=UTF-8">')
    # f.write('</HEAD>')
    # f.write('<BODY BGCOLOR=#ffffff>')
    # f.write('<FORM>')
    # f.write('<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=' + IntToStr(Matr[NX, 0] - Matr[1, 0]) + '>')
    # f.write('   <TR>')

    # for i = 1 to NX - 1 do
    #     s = '      <TD><IMG height=1 src="spacer.gif" width=' + \
    #         IntToStr(Matr[i + 1, 0] - Matr[i, 0]) + '></TD>'
    #     f.write(s)
    #
    # f.write('   </TR>')
    # for i = 1 to NY - 1 do
    #     f.write('   <TR>')
    #     for j = 1 to NX - 1 do
    #         if Matr[j, i] > 0:  # Блок ячеек, содержащий объект
    #             if arr[Matr[j, i]]["typ"] = typ["Button"]:
    #                 ts = 'button'
    #             if arr[Matr[j, i]]["typ"] = typ["TextEdit"]:
    #                 ts = 'text'
    #             s = '      <TD'
    #             if arr[Matr[j, i]]["colspan"] > 1:
    #                 s = s + ' COLSPAN=' + IntToStr(arr[Matr[j, i]]["colspan"])
    #             if arr[Matr[j, i]]["rowspan"] > 1:
    #                 s = s + ' ROWSPAN=' + IntToStr(arr[Matr[j, i]]["rowspan"])

    # TODO: 1. Заменить case на if

    #             case arr[Matr[j, i]]["typ"] of
    #                 typ["Button"]:
    #                 s = s + '><INPUT HEIGHT="' + IntToStr(arr[Matr[j, i]]["height"]) + \
    #                     '" WIDTH="' + IntToStr(arr[Matr[j, i]]["width"]) + \
    #                     '" style="HEIGHT: ' + IntToStr(arr[Matr[j, i]]["height"]) + \
    #                     'px WIDTH: ' + IntToStr(arr[Matr[j, i]]["width"]) + \
    #                     'px" type=' + ts
    #                 f.write(s)
    #                 f.write('          value="' + arr[Matr[j, i]]["text"] + '"></TD>')
    #
    #                 typ["TextEdit"]:
    #                 s = s + '><INPUT SIZE="' + IntToStr(arr[Matr[j, i]]["width"] div 8 -1) + \
    #                     '" style="WIDTH: ' + IntToStr(arr[Matr[j, i]]["width"]) + \
    #                     'px" type=' + ts
    #                 f.write(s)
    #                 f.write('          value="' + arr[Matr[j, i]]["text"] + '"></TD>')
    #
    #                 typ["Label"]:
    #                 s = s + '>' + arr[Matr[j, i]]["text"] + '</TD>'
    #                 f.write(s)
    #
    #         if Matr[j, i] < 0:  # Пустой блок ячеек
    #             s = '      <TD'
    #             if Spc[0, - Matr[j, i]] > 1:
    #                 s = s + ' COLSPAN=' + IntToStr(Spc[0, - Matr[j, i]])
    #             if Spc[1, - Matr[j, i]] > 1:
    #                 s = s + ' ROWSPAN=' + IntToStr(Spc[1, - Matr[j, i]])
    #             s = s + '></TD>'
    #             f.write(s)
    #
    #     s = '      <TD><IMG height=' + IntToStr(Matr[0, i + 1] - Matr[0, i]) + \
    #         ' src="spacer.gif" width=1></TD>'
    #     f.write(s)
    #     f.write('   </TR>')

    # f.write('</TABLE>')
    # f.write('</FORM>')
    # f.write('</BODY>')
    # f.write('</HTML>')
    f.close()
