#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def ParserTextFile(fileName, arr):
    typeOfObj = {"Button": 1, "TextEdit": 2, "Label": 3}
    dir = os.path.dirname(fileName)
    name, ext = os.path.splitext(os.path.basename(fileName))
    logFileName = os.path.join(dir, name + ".log")
    logFile = open(logFileName, "w")
    logFile.write("Start parsing")
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    array = [{}]  # Список объектов с их свойствами. Каждый объект представлен словарем

    # Пример:
    # array.append({"text" : u"Текст", "typ" : typ["TextEdit"], "left" : 0, "top" : 0,
    #              "width" : 0, "height" : 0, "colspan" : 0, "rowspan" : 0})
    # array[3]["colspan"] = 7

    # В проекте на Delphi это было так:
    #   Prop_s:A_s # Вектор строковых свойств объектов
    #   Prop_i:A_i # Матрица числовых свойств объектов, назначение столбцов:
    #               # 0  -  тип объекта: Button  -  1, TextEdit  -  2, Label  -  3
    #               # 1  -  свойство left
    #               # 2  -  свойство top
    #               # 3  -  свойство width
    #               # 4  -  свойство height
    #               # 5  -  значение COLSPAN для ячейки HTML
    #               # 6  -  значение ROWSPAN для ячейки HTML

    MinHeight = 21
    MinWidth = 21
    DefaultHeight = 21
    DefaultWidth = 70
    Errs = False

    #   L,L1,LWork:string
    #   i,n:integer
    #   Valid:boolean

    # TODO: 1. Сделать корректную замену: Prop_i[0, i] на array[i]["typ"]
    #          используя в условиях соответственно typ["Button"] typ["TextEdit"] typ["Label"]

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
                repeat
                n = Pos('  ', LWork)
                if n <> 0:
                    Delete(LWork, n, 1)
            until
            n = 0
            n = Pos('< ', LWork)
            if n <> 0:
                Delete(LWork, n + 1, 1)
                array.append({})  # Создаем новый элемент списка
            if Pos('<button', LowerCase(LWork)) <> 0:
                Prop_i[0, i] = 1
            if Pos('<textedit', LowerCase(LWork)) <> 0:
                Prop_i[0, i] = 2
            if Pos('<label', LowerCase(LWork)) <> 0:
                Prop_i[0, i] = 3
            if Prop_i[0, i] <> 0:
                repeat
                n = Pos(' ', LWork)
                if n <> 0:
                    Delete(LWork, n, 1)
            until
            n = 0
            n = Pos('left="', LowerCase(LWork))
            if n <> 0:
                L1 = LWork
                Delete(L1, 1, Pos('left="', LowerCase(L1)) + 5)
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                try
                    array[i]["left"] = StrToInt(L1)
                except on E: EConvertError
                do
                array[i]["left"] = 0
    n = Pos('top="', LowerCase(LWork))
    if n <> 0:
        L1 = LWork
        Delete(L1, 1, Pos('top="', LowerCase(L1)) + 4)
        L1 = Copy(L1, 1, Pos('"', L1) - 1)
        try
            array[i]["top"] = StrToInt(L1)
        except on E: EConvertError
        do
        array[i]["top"] = 0


n = Pos('width="', LowerCase(LWork))
if n <> 0:
    L1 = LWork
    Delete(L1, 1, Pos('width="', LowerCase(L1)) + 6)
    L1 = Copy(L1, 1, Pos('"', L1) - 1)
    try
        array[i]["width"] = StrToInt(L1)
    except on E: EConvertError
    do
    array[i]["width"] = 0
if Prop_i[0, i] <> 2:
    n = Pos('height="', LowerCase(LWork))
    if n <> 0:
        L1 = LWork
        Delete(L1, 1, Pos('height="', LowerCase(L1)) + 7)
        L1 = Copy(L1, 1, Pos('"', L1) - 1)
        try
            array[i]["height"] = StrToInt(L1)
        except on E: EConvertError
        do
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
if Prop_i[0, i] = 2:
    array[i]["height"] = MinHeight
Valid = True
if i > 1:
    n = 1
    repeat
    if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
        array[i]["top"] < array[n]["top"] + array[n]["height"]) and \
            (array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
        array[i]["left"] < array[n]["left"] + array[n]["width"]):
        Valid = False
    n = n + 1
    until(Valid=False) or (n = i)
if not Valid:  # Попытка коррекции объекта перемещением
    Valid = True
    n = 1
    repeat
    if (array[i]["top"] >= array[n]["top"]) and (array[i]["top"] < array[n]["top"] + array[n]["height"]) and \
            (array[i]["left"] >= array[n]["left"]) and (array[i]["left"] < array[n]["left"] + array[n]["width"]):
        Valid = False
    n = n + 1
    until(Valid=False) or (n = i)
    if not Valid:
        if (array[i]["top"] >= Prop_i[2, n - 1]) and (array[i]["top"] < Prop_i[2, n - 1] + Prop_i[4, n - 1]):
            array[i]["top"] = Prop_i[2, n - 1] + Prop_i[4, n - 1]
    Valid = True
    n = 1
    repeat
    if (array[i]["top"] >= array[n]["top"]) and (array[i]["top"] < array[n]["top"] + array[n]["height"]) and \
            (array[i]["left"] >= array[n]["left"]) and (array[i]["left"] < array[n]["left"] + array[n]["width"]):
        Valid = False
    n = n + 1
    until(Valid=False) or (n = i)
    if not Valid:
        if (array[i]["left"] >= Prop_i[1, n - 1]) and (array[i]["left"] < Prop_i[1, n - 1] + Prop_i[3, n - 1]):
            array[i]["left"] = Prop_i[1, n - 1] + Prop_i[3, n - 1]
    Valid = True
    n = 1
    repeat
    if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
        array[i]["top"] < array[n]["top"] + array[n]["height"]) and \
            (array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
        array[i]["left"] < array[n]["left"] + array[n]["width"]):
        Valid = False
    n = n + 1
    until(Valid=False) or (n = i)
if not Valid:  # Попытка коррекции объекта уменьшением
    array[i]["width"] = MinWidth
    array[i]["height"] = MinHeight
    Valid = True
    n = 1
    repeat
    if (array[i]["top"] + array[i]["height"] > array[n]["top"]) and (
        array[i]["top"] < array[n]["top"] + array[n]["height"]) and \
            (array[i]["left"] + array[i]["width"] > array[n]["left"]) and (
        array[i]["left"] < array[n]["left"] + array[n]["width"]):
        Valid = False
    n = n + 1
    until(Valid=False) or (n = i)
if Valid:
    i = i + 1
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
