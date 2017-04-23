#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

MINHEIGHT = 21
MINWIDTH = 21
DEFAULTHEIGHT = 21
DEFAULTWIDTH = 70

def checkValid(arr):  # Проверка объекта на конфликт с предыдущими. Но IMHO с ошибкой в условии!?
    if len(arr) <= 1: # Если в списке всего 0 или 1 элемент - он точно без конфликтов
        return True
    Valid = True
    i = len(arr) - 1
    for n in range(i)
        if (arr[i]["top"]  + arr[i]["height"] > arr[n]["top"])    and (
            arr[i]["top"]  < arr[n]["top"]    + arr[n]["height"]) and (
            arr[i]["left"] + arr[i]["width"]  > arr[n]["left"])   and (
            arr[i]["left"] < arr[n]["left"]   + arr[n]["width"]):
            Valid = False
    return Valid


def ParserTextFile(fileName, arr):

    dir = os.path.dirname(fileName)
    name, ext = os.path.splitext(os.path.basename(fileName))
    logFileName = os.path.join(dir, name + ".log")
    logFile = open(logFileName, "w")
    logFile.write("Start parsing")
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    # arr = [{}]  # Список объектов с их свойствами. Каждый объект представлен словарем

    Errs = False

    # TODO: 1. Заменить циклы until на while
    # TODO: 2. Заменить функции Pos, Delete, Copy на аналоги


    # <Button left="10"; top="10"; bottom="100"; right="100"; Caption="Press me!">
    # <Label left="110"; top="110"; bottom="200"; right="200"; Text="Look at me!">


    i = 1  # TODO: Сделать нумерацию строк массива с 0
    with open(fileName, "r") as f:
#        data = f.readlines()
#       for L in data:
#           words = L.split(";")
        # TODO: Переделать анализ строки с использованием split

        for L in f: # Проверить правильно ли так, или нужно через readlines
            if L == '': # Если строка пустая - пропускаем
                continue

            # Чистка строк по краям
            # ----------------------------------------------------------------------------------------------------
            LWork = L # Будем строку LWork модифицировать. Исходная строка L нужна для логирования.

            # Считаем, что строки без < допустимы. Добавляем < и парсим дальше.
            n = LWork.find('<') # n = Pos('<', LWork) Находим позицию символа <
            if n == -1: #if n = 0: Нет символа <
                LWork = '<' + LWork
            else:
                LWork = LWork[:n - 1] # Delete(LWork, 1, n - 1) # Удаляем возможный мусор перед <

            # Считаем, что строки без > допустимы. Добавляем > и парсим дальше.
            n = LWork.find('>') # n = Pos('>', LWork) Находим позицию символа >
            if n == -1: # if n = 0: Нет символа >
                LWork = LWork + '>'
            else:
                LWork = LWork[:n] # LWork = Copy(LWork, 1, n) Берем строку до > включительно
            # ----------------------------------------------------------------------------------------------------

            # Поиск и удаление двойных пробелов.
            # repeat # Переделать в цикл while
            #     n = Pos('  ', LWork)
            #     if n <> 0:
            #         Delete(LWork, n, 1)
            # until n = 0

            # Находит и удаляет символ <. В контексте чистки строки выше - не нужно.
            # TODO: Переделать.
            # n = Pos('< ', LWork)
            # if n <> 0:
            #     Delete(LWork, n + 1, 1)

            arr.append({})  # Создаем новый элемент списка

            # Определяем тип объекта
            # ----------------------------------------------------------------------------
            if LWork.lower().find('<button') <> -1:
                arr[i]["typ"] = typ["Button"]
            elif LWork.lower().find('<textedit') <> -1:
                arr[i]["typ"] = typ["TextEdit"]
            elif LWork.lower().find('<label') <> -1:
                arr[i]["typ"] = typ["Label"]
            else:  # Строка не содержит тип объекта - пропускаем
                arr.pop()  # Удаляем последний пустой элемент списка
                logFile.write(L + u" - строка не загружена: неверный тип объекта.")
                Errs = True
                continue
            # ----------------------------------------------------------------------------

            # Если удалось определить тип объекта - отбрасываем часть строки с названием типа
            # repeat # Переделать в цикл while
            #     n = LWork.find('')  # n = Pos(' ', LWork)
            #     if n <> -1:  # if n <> 0:
            #         LWork = LWork[n - 1:n]  # Delete(LWork, n, 1)
            # until n = 0

            # Заполнение свойств объекта
            # -----------------------------------------------------------------------------
            n = Pos('left="', LowerCase(LWork))
            if n <> 0:
                L1 = LWork
                Delete(L1, 1, Pos('left="', LowerCase(L1)) + 5)
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                try:
                    arr[i]["left"] = StrToInt(L1)
                except on E: EConvertError do
                    arr[i]["left"] = 0

            n = Pos('top="', LowerCase(LWork))
            if n <> 0:
                L1 = LWork
                Delete(L1, 1, Pos('top="', LowerCase(L1)) + 4)
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                try:
                    arr[i]["top"] = StrToInt(L1)
                except on E: EConvertError do
                    arr[i]["top"] = 0


            n = Pos('width="', LowerCase(LWork))
            if n <> 0:
                L1 = LWork
                Delete(L1, 1, Pos('width="', LowerCase(L1)) + 6)
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                try:
                    arr[i]["width"] = StrToInt(L1)
                except on E: EConvertError do
                    arr[i]["width"] = 0

            if arr[i]["typ"] <> typ["TextEdit"]:
                n = Pos('height="', LowerCase(LWork))
                if n <> 0:
                    L1 = LWork
                    Delete(L1, 1, Pos('height="', LowerCase(L1)) + 7)
                    L1 = Copy(L1, 1, Pos('"', L1) - 1)
                    try:
                        arr[i]["height"] = StrToInt(L1)
                    except on E: EConvertError do
                        arr[i]["height"] = 0

            n = Pos('caption="', LowerCase(LWork))
            if n <> 0:
                L1 = L
                Delete(L1, 1, Pos('caption', LowerCase(L1)) + 6)
                Delete(L1, 1, Pos('"', L1))
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                arr[i]["text"] = L1

            n = Pos('text="', LowerCase(LWork))
            if n <> 0:
                L1 = L
                n = Pos('textedit', LowerCase(L1))

                if n <> 0:
                    Delete(L1, 1, n + 7)

                Delete(L1, 1, Pos('text', LowerCase(L1)) + 3)
                Delete(L1, 1, Pos('"', L1))
                L1 = Copy(L1, 1, Pos('"', L1) - 1)
                arr[i]["text"] = L1
            # -----------------------------------------------------------------------------

            # Корректируем размеры и положение объектов в соответствии с константами минимально допустимых размеров
            # ------------------------------------------------------------------------
            if arr[i]["left"] < 0:
                arr[i]["left"] = 0
            if arr[i]["top"] < 0:
                arr[i]["top"] = 0
            if arr[i]["width"]  < MINWIDTH:
                arr[i]["width"] = DEFAULTWIDTH
            if arr[i]["typ"] = typ["TextEdit"]:
                arr[i]["height"] = MINHEIGHT
            elif arr[i]["height"] < MINHEIGHT:
                arr[i]["height"] = DEFAULTHEIGHT

            # Проверка объекта на конфликт с предыдущими.
            Valid = checkValid(arr)

            # Попытка коррекции объекта перемещением
            # ------------------------------------------------------------------------
            if not Valid:
                Valid = True
                n = 1

                repeat # Переделать в цикл while
                    if (arr[i]["top"] >= arr[n]["top"]) and (
                        arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
                        arr[i]["left"] >= arr[n]["left"]) and (
                        arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
                        Valid = False
                    n += 1
                until(Valid = False) or (n = i)

                if not Valid:
                    if (arr[i]["top"] >= arr[n - 1]["top"]) and (
                        arr[i]["top"] < arr[n - 1]["top"] + arr[n - 1]["height"]):
                        arr[i]["top"] = arr[n - 1]["top"] + arr[n - 1]["height"]
                Valid = True

                n = 1

                repeat # Переделать в цикл while
                    if (arr[i]["top"] >= arr[n]["top"]) and (
                        arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
                        arr[i]["left"] >= arr[n]["left"]) and (
                        arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
                        Valid = False
                    n += 1
                until(Valid = False) or (n = i)

                if not Valid:
                    if (arr[i]["left"] >= arr[n - 1]["left"]) and (
                        arr[i]["left"] < arr[n - 1]["left"] + arr[n - 1]["width"]):
                        arr[i]["left"] = arr[n - 1]["left"] + arr[n - 1]["width"]

                # Повторная проверка объекта на конфликт с предыдущими.
                Valid = checkValid(arr)

            # Попытка коррекции объекта уменьшением
            # ------------------------------------------------------------------------
            if not Valid:
                arr[i]["width"] = MINWIDTH
                arr[i]["height"] = MINHEIGHT

                # Повторная проверка объекта на конфликт с предыдущими.
                Valid = checkValid(arr)
            # ------------------------------------------------------------------------

            if Valid:
                i += 1
            else:
                arr.pop()  # Удаляем последний (конфликтующий) элемент списка
                logFile.write(L + u" - строка не загружена: значительное наложение объектов.")
                Errs = True
            # ------------------------------------------------------------------------

    logFile.write(u"End parsing")
    logFile.close()
    # if not Errs : DeleteFile(PathName + '.log')
    return Errs
