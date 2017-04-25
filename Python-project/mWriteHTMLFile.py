#!/usr/bin/env python
# -*- coding: utf-8 -*-

def WriteHTMLFile(fileName, arr):
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    f = open(fileName, "w")

    NCom = len(arr)

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
    NY = len(col)

    # Формирование отсортированного списка уникальных значений границ объекта по горизонтали
    row = []
    for i in range(NCom):
        if arr[i]["left"] not in row:
            row.append(arr[i]["left"])
        if arr[i]["left"] + arr[i]["width"] not in row:
            row.append(arr[i]["left"] + arr[i]["width"])
    row.sort()
    NX = len(row)

    # Заполнение строки 0 и столбца 0 координатами границ объектов, все остальные ячейки = None
    Matr.append([])
    Matr[0] = [None] + row
    for y in range(1, NY + 1):
        Matr.append([])
        Matr[y].append(col[y - 1])
        for x in range(1, NX + 1):
            Matr[y].append(None)

    # Расстановка объектов в блоки ячеек
    # --------------------------------------------------------------------------------
    for n in range(NCom):
        arr[n]["rowspan"] = 0
        for y in range(1, NY + 1):
            if (Matr[y][0] >= arr[n]["top"]) and (Matr[y][0] < (arr[n]["top"] + arr[n]["height"])):
                arr[n]["rowspan"] = arr[n]["rowspan"] + 1
                arr[n]["colspan"] = 0
                for x in range(1, NX + 1):
                    if (Matr[0][x] >= arr[n]["left"]) and (Matr[0][x] < (arr[n]["left"] + arr[n]["width"])):
                        arr[n]["colspan"] = arr[n]["colspan"] + 1
                        if (Matr[0][x] == arr[n]["left"]) and (Matr[y][0] == arr[n]["top"]):
                            Matr[y][x] = n
                        else:
                            Matr[y][x] = ''  # Отмечаем ячейки как обработанные

    # Группировка пустых ячеек в блоки
    # --------------------------------------------------------------------------------
    # Spc - двумерный массив пустых блоков, назначение столбцов:
    # 0  -  значение COLSPAN для ячейки HTML
    # 1  -  значение ROWSPAN для ячейки HTML

    # TODO: Отладить!

    Spc = [[],[]]
    n = 1
    for y in range(1, NY + 1):
        for x in range(1, NX + 1):
            i = 1
            if Matr[y][x] == None:
                Matr[y][x] = -n
                while (x + i < NX) and (Matr[y][x + i] == None):  # Считаем количество необработанных ячеек справа
                    Matr[y][x + i] = ''  # Отмечаем ячейки как обработанные
                    i += 1
                j = 1
                sp = True
                while (sp == True) and (y + j < NY):
                    sp = True
                    for k in range(x, x + i):
                        if Matr[y + j][k] <> None:
                            sp = False
                    if sp == True:
                         for k in range(x, x + i):
                            Matr[y + j][k] = ''
                         j += 1
                # Spc.append([])
                Spc[0].append(i)  # Spc[0][n] = i
                Spc[1].append(j)  # Spc[1][n] = j
                n += 1

    f.write('<HTML>\n')
    f.write('<HEAD>\n')
    f.write('<TITLE>Editor</TITLE>\n')
    f.write('<META HTTP - EQUIV="Content - Type" CONTENT="text/html charset=UTF-8">\n')
    f.write('</HEAD>\n')
    f.write('<BODY BGCOLOR=#ffffff>\n')
    f.write('<FORM>\n')
    f.write('<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=' + str(Matr[0][NX] - Matr[0][1]) + '>\n')
    f.write('   <TR>\n')

    for i in range(1, NX):
        s = '      <TD><IMG height=1 src="spacer.gif" width=' + str(Matr[0][i + 1] - Matr[0][i]) + '></TD>\n'
        f.write(s)

    f.write('   </TR>\n')
    for i in range(1, NY):
        f.write('   <TR>\n')
        for j in range(1, NX):
            if Matr[i][j] != '' and Matr[i][j] > 0:  # Блок ячеек, содержащий объект
                if arr[Matr[i][j]]["typ"] == typ["Button"]:
                    ts = 'button'
                if arr[Matr[i][j]]["typ"] == typ["TextEdit"]:
                    ts = 'text'
                s = '      <TD'
                if arr[Matr[i][j]]["colspan"] > 1:
                    s = s + ' COLSPAN=' + str(arr[Matr[i][j]]["colspan"])
                if arr[Matr[i][j]]["rowspan"] > 1:
                    s = s + ' ROWSPAN=' + str(arr[Matr[i][j]]["rowspan"])

                if arr[Matr[i][j]]["typ"] == typ["Button"]:
                    s = s + '><INPUT HEIGHT="' + str(arr[Matr[i][j]]["height"]) + '" WIDTH="' + \
                        str(arr[Matr[i][j]]["width"]) + '" style="HEIGHT: ' + str(arr[Matr[i][j]]["height"]) + \
                        'px WIDTH: ' + str(arr[Matr[i][j]]["width"]) + 'px" type=' + ts
                    f.write(s)
                    f.write(' value="' + arr[Matr[i][j]]["text"] + '"></TD>\n')

                elif arr[Matr[i][j]]["typ"] == typ["TextEdit"]:
                    s = s + '><INPUT SIZE="' + str(arr[Matr[i][j]]["width"] // 8 - 1) + '" style="WIDTH: ' + \
                        str(arr[Matr[i][j]]["width"]) + 'px" type=' + ts
                    f.write(s)
                    f.write(' value="' + arr[Matr[i][j]]["text"] + '"></TD>\n')

                elif arr[Matr[i][j]]["typ"] == typ["Label"]:
                    s = s + '>' + arr[Matr[i][j]]["text"] + '</TD>\n'
                    f.write(s)

            if Matr[i][j] != '' and Matr[i][j] < 0:  # Пустой блок ячеек
                s = '      <TD'
                if Spc[0][- Matr[i][j]] > 1:
                    s = s + ' COLSPAN=' + str(Spc[0][- Matr[i][j]])
                if Spc[1][- Matr[i][j]] > 1:
                    s = s + ' ROWSPAN=' + str(Spc[1][- Matr[i][j]])
                s = s + '></TD>\n'
                f.write(s)

        s = '      <TD><IMG height=' + str(Matr[i + 1][0] - Matr[i][0]) + \
            ' src="spacer.gif" width=1></TD>\n'
        f.write(s)
        f.write('   </TR>\n')

    f.write('</TABLE>\n')
    f.write('</FORM>\n')
    f.write('</BODY>\n')
    f.write('</HTML>\n')

    for tmp in range(len(arr)): f.write(str(arr[tmp]) + "\n")  # DEBUG: Отладочный вывод
    f.write("\n\n")  # DEBUG: Отладочный вывод
    for tmp in range(len(Matr)):
        tmp2 = '%5s' % str(Matr[tmp])
        f.write(tmp2 + "\n")  # DEBUG: Отладочный вывод
    f.write("\n\n")  # DEBUG: Отладочный вывод
    for tmp in range(len(Spc)): f.write(str(Spc[tmp]) + "\n")  # DEBUG: Отладочный вывод

    f.close()
