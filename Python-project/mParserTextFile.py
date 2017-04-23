#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def ParserTextFile(fileName, arr):
    dir = os.path.dirname(fileName)
    name, ext = os.path.splitext(os.path.basename(fileName))
    logFileName = os.path.join(dir, name + ".log")
    logFile = open(logFileName, "w")
    logFile.write("Start parsing")
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    array = [{}]  # Список объектов с их свойствами. Каждый объект представлен словарем

    MinHeight = 21
    MinWidth = 21
    DefaultHeight = 21
    DefaultWidth = 70
    Errs = False

    # TODO: 1. Заменить циклы until на while
    # TODO: 2. Заменить функции Pos, Delete, Copy на аналоги

    i = 1
    with open(fileName) as f:
        for L in f:
            if L <> '':
                LWork = L
                n = Pos('<', LWork)

                if n = 0:
                    LWork = '<' + LWork
                else:
                    Delete(LWork, 1, n - 1)

                n = Pos('>', LWork)

                if n = 0:
                    LWork = LWork + '>'
                else:
                    LWork = Copy(LWork, 1, n)

                repeat # Переделать в цикл while
                    n = Pos('  ', LWork)
                    if n <> 0:
                        Delete(LWork, n, 1)
                until n = 0

                n = Pos('< ', LWork)

                if n <> 0:
                    Delete(LWork, n + 1, 1)

                array.append({})  # Создаем новый элемент списка

                if Pos('<button', LowerCase(LWork)) <> 0:
                    array[i]["typ"] = typ["Button"]

                if Pos('<textedit', LowerCase(LWork)) <> 0:
                    array[i]["typ"] = typ["TextEdit"]

                if Pos('<label', LowerCase(LWork)) <> 0:
                    array[i]["typ"] = typ["Label"]

                if array[i]["typ"] <> 0: # Здесь наверное нужно заменить на none или на in typ
                    repeat # Переделать в цикл while
                        n = Pos(' ', LWork)
                        if n <> 0:
                            Delete(LWork, n, 1)
                    until n = 0

                    n = Pos('left="', LowerCase(LWork))
                    if n <> 0:
                        L1 = LWork
                        Delete(L1, 1, Pos('left="', LowerCase(L1)) + 5)
                        L1 = Copy(L1, 1, Pos('"', L1) - 1)
                        try:
                            array[i]["left"] = StrToInt(L1)
                        except on E: EConvertError do
                            array[i]["left"] = 0

                    n = Pos('top="', LowerCase(LWork))
                    if n <> 0:
                        L1 = LWork
                        Delete(L1, 1, Pos('top="', LowerCase(L1)) + 4)
                        L1 = Copy(L1, 1, Pos('"', L1) - 1)
                        try:
                            array[i]["top"] = StrToInt(L1)
                        except on E: EConvertError do
                            array[i]["top"] = 0


                    n = Pos('width="', LowerCase(LWork))
                    if n <> 0:
                        L1 = LWork
                        Delete(L1, 1, Pos('width="', LowerCase(L1)) + 6)
                        L1 = Copy(L1, 1, Pos('"', L1) - 1)
                        try:
                            array[i]["width"] = StrToInt(L1)
                        except on E: EConvertError do
                            array[i]["width"] = 0

                    if array[i]["typ"] <> typ["TextEdit"]:
                        n = Pos('height="', LowerCase(LWork))
                        if n <> 0:
                            L1 = LWork
                            Delete(L1, 1, Pos('height="', LowerCase(L1)) + 7)
                            L1 = Copy(L1, 1, Pos('"', L1) - 1)
                            try:
                                array[i]["height"] = StrToInt(L1)
                            except on E: EConvertError do
                                array[i]["height"] = 0

                    n = Pos('caption="', LowerCase(LWork))
                    if n <> 0:
                        L1 = L
                        Delete(L1, 1, Pos('caption', LowerCase(L1)) + 6)
                        Delete(L1, 1, Pos('"', L1))
                        L1 = Copy(L1, 1, Pos('"', L1) - 1)
                        array[i]["text"] = L1

                    n = Pos('text="', LowerCase(LWork))
                    if n <> 0:
                        L1 = L
                        n = Pos('textedit', LowerCase(L1))

                        if n <> 0:
                            Delete(L1, 1, n + 7)

                        Delete(L1, 1, Pos('text', LowerCase(L1)) + 3)
                        Delete(L1, 1, Pos('"', L1))
                        L1 = Copy(L1, 1, Pos('"', L1) - 1)
                        array[i]["text"] = L1

                    if array[i]["left"] < 0:
                        array[i]["left"] = 0

                    if array[i]["top"] < 0:
                        array[i]["top"] = 0

                    if array[i]["width"] < MinWidth:
                        array[i]["width"] = DefaultWidth

                    if array[i]["height"] < MinHeight:
                        array[i]["height"] = DefaultHeight

                    if array[i]["typ"] = typ["TextEdit"]:
                        array[i]["height"] = MinHeight

                    Valid = True

                    if i > 1:
                        n = 1
                        repeat # Переделать в цикл while
                            if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
                                array[i]["top"] < array[n]["top"] + array[n]["height"]) and (
                                array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
                                array[i]["left"] < array[n]["left"] + array[n]["width"]):
                                Valid = False
                            n += 1
                        until(Valid = False) or (n = i)

                    if not Valid:  # Попытка коррекции объекта перемещением
                        Valid = True
                        n = 1

                        repeat # Переделать в цикл while
                            if (array[i]["top"] >= array[n]["top"]) and (
                                array[i]["top"] < array[n]["top"] + array[n]["height"]) and (
                                array[i]["left"] >= array[n]["left"]) and (
                                array[i]["left"] < array[n]["left"] + array[n]["width"]):
                                Valid = False
                            n += 1
                        until(Valid = False) or (n = i)

                        if not Valid:
                            if (array[i]["top"] >= array[n - 1]["top"]) and (
                                array[i]["top"] < array[n - 1]["top"] + array[n - 1]["height"]):
                                array[i]["top"] = array[n - 1]["top"] + array[n - 1]["height"]
                        Valid = True

                        n = 1

                        repeat # Переделать в цикл while
                            if (array[i]["top"] >= array[n]["top"]) and (
                                array[i]["top"] < array[n]["top"] + array[n]["height"]) and (
                                array[i]["left"] >= array[n]["left"]) and (
                                array[i]["left"] < array[n]["left"] + array[n]["width"]):
                                Valid = False
                            n += 1
                        until(Valid = False) or (n = i)

                        if not Valid:
                            if (array[i]["left"] >= array[n - 1]["left"]) and (
                                array[i]["left"] < array[n - 1]["left"] + array[n - 1]["width"]):
                                array[i]["left"] = array[n - 1]["left"] + array[n - 1]["width"]
                        Valid = True

                        n = 1

                        repeat # Переделать в цикл while
                            if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
                                array[i]["top"] < array[n]["top"] + array[n]["height"]) and (
                                array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
                                array[i]["left"] < array[n]["left"] + array[n]["width"]):
                                Valid = False
                            n += 1
                        until(Valid = False) or (n = i)

                    if not Valid:  # Попытка коррекции объекта уменьшением
                        array[i]["width"] = MinWidth
                        array[i]["height"] = MinHeight
                        Valid = True
                        n = 1

                        repeat # Переделать в цикл while
                            if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
                                array[i]["top"] < array[n]["top"] + array[n]["height"]) and (
                                array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
                                array[i]["left"] < array[n]["left"] + array[n]["width"]):
                                Valid = False
                            n += 1
                        until(Valid = False) or (n = i)

                    if Valid:
                        i += 1
                    else:
                        array.append({})  # Создаем новый элемент списка
                        logFile.write(L + u" - строка не загружена: значительное наложение объектов.")
                        Errs = True
                else:
                    array.append({})  # Создаем новый элемент списка
                    logFile.write(L + u" - строка не загружена: неверный тип объекта.")
                    Errs = True

    logFile.write(u"End parsing")
    logFile.close()
    # if not Errs : DeleteFile(PathName + '.log')
    return Errs
