#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

MINHEIGHT = 21
MINWIDTH = 21
DEFAULTHEIGHT = 21
DEFAULTWIDTH = 70

def checkValid(arr):  # Проверка объекта на конфликт с предыдущими. Но IMHO с ошибкой в условии!?
    if len(arr) <= 1:  # Если в списке всего 0 или 1 элемент - он точно без конфликтов
        return True
    Valid = True
    i = len(arr) - 1
    for n in range(i):
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
    logFile.write("Start parsing" + "\n")
    typ = {"Button": 1, "TextEdit": 2, "Label": 3}
    Errs = False
    i = 0

    with open(fileName, "r") as f:
#        data = f.readlines()
#       for L in data:
#           words = L.split(";")
        # TODO: Переделать анализ строки с использованием split

        for L in f:  # Проверить правильно ли так, или нужно через readlines
            L = L.strip()  # Удаляем пробелы по краям
            if L == '':  # Если строка пустая - пропускаем
                continue

            logFile.write("\n")  # DEBUG: Отладочный вывод
            logFile.write("LINE: " + L + "\n")  # DEBUG: Отладочный вывод

            # Чистка строк по краям, восстановление структуры строки
            # ----------------------------------------------------------------------------------------------------
            lineWork = L  # Будем строку lineWork модифицировать. Исходная строка L нужна для логирования.

            # Считаем, что строки без < допустимы. Добавляем < и парсим дальше.
            n = lineWork.find('<')  # Находим позицию символа <
            if n == -1:  # Нет символа <
                lineWork = '<' + lineWork
            else:
                lineWork = lineWork[n:]  # Удаляем возможный мусор перед <

            # Считаем, что строки без > допустимы. Добавляем > и парсим дальше.
            n = lineWork.find('>')  # Находим позицию символа >
            if n == -1:  # Нет символа >
                lineWork = lineWork + '>'
            else:
                lineWork = lineWork[:n + 1]  # lineWork = Copy(lineWork, 1, n) Берем строку до > включительно

            # Поиск и удаление лишних пробелов.
            lineWork = re.sub(r'\s+', ' ', lineWork)  # Удаление двойных пробелов используя регулярные выражения
            lineWork = re.sub(r'< ', '<', lineWork)   # Удаление пробела после символа <

            #logFile.write("Clean line " + lineWork + "\n")  # DEBUG: Отладочный вывод
            # ----------------------------------------------------------------------------------------------------
            # Создаем новый элемент списка
            arr.append({"text": "", "typ": 0, "left": 0, "top": 0, "width": 0, "height": 0, "colspan": 0, "rowspan": 0})

            # Определяем тип объекта
            # ----------------------------------------------------------------------------
            if lineWork.lower().find('<button') != -1:
                arr[i]["typ"] = typ["Button"]
            elif lineWork.lower().find('<textedit') != -1:
                arr[i]["typ"] = typ["TextEdit"]
            elif lineWork.lower().find('<label') != -1:
                arr[i]["typ"] = typ["Label"]
            else:  # Строка не содержит тип объекта - пропускаем
                arr.pop()  # Удаляем последний пустой элемент списка
                logFile.write("ERROR: " + L + " = wrong object type" + "\n")
                Errs = True
                continue
            # ----------------------------------------------------------------------------

            # Если удалось определить тип объекта - отбрасываем часть строки с названием типа
            n = lineWork.find(' ')
            if n != -1:
                lineWork = lineWork[n + 1:]

            # Заполнение свойств объекта
            # -----------------------------------------------------------------------------
            n = lineWork.lower().find('left="')
            if n != -1:
            #     L1 = lineWork
            #     Delete(L1, 1, Pos('left="', LowerCase(L1)) + 5)
            #     L1 = Copy(L1, 1, Pos('"', L1) - 1)

            L1.write(lineWork + "\n")

            #     try:
            #         arr[i]["left"] = StrToInt(L1)
            #     except on E: EConvertError do
            #         arr[i]["left"] = 0
            #
            n = lineWork.lower().find('top="')
            if n != -1:
            #     L1 = lineWork
            #     Delete(L1, 1, Pos('top="', LowerCase(L1)) + 4)
            #     L1 = Copy(L1, 1, Pos('"', L1) - 1)

            L1.write(lineWork + "\n")

            #     try:
            #         arr[i]["top"] = StrToInt(L1)
            #     except on E: EConvertError do
            #         arr[i]["top"] = 0
            #
            #
            n = lineWork.lower().find('width="')
            if n != -1:
            #     L1 = lineWork
            #     Delete(L1, 1, Pos('width="', LowerCase(L1)) + 6)
            #     L1 = Copy(L1, 1, Pos('"', L1) - 1)

            L1.write(lineWork + "\n")

            #     try:
            #         arr[i]["width"] = StrToInt(L1)
            #     except on E: EConvertError do
            #         arr[i]["width"] = 0
            #
            # if arr[i]["typ"] != typ["TextEdit"]:
            #     n = Pos('height="', LowerCase(lineWork))
            #     if n != -1:
            #         L1 = lineWork
            #         Delete(L1, 1, Pos('height="', LowerCase(L1)) + 7)
            #         L1 = Copy(L1, 1, Pos('"', L1) - 1)

            L1.write(lineWork + "\n")

            #         try:
            #             arr[i]["height"] = StrToInt(L1)
            #         except on E: EConvertError do
            #             arr[i]["height"] = 0
            #
            n = lineWork.lower().find('caption="')
            if n != -1:
            #     L1 = L
            #     Delete(L1, 1, Pos('caption', LowerCase(L1)) + 6)
            #     Delete(L1, 1, Pos('"', L1))
            #     L1 = Copy(L1, 1, Pos('"', L1) - 1)

                L1.write(lineWork + "\n")

                arr[i]["text"] = L1
            #
            n = lineWork.lower().find('text="')
            if n != -1:
                L1 = L

                L1.write(lineWork + "\n")

                n = L1.lower().find('textedit')

                if n != -1:
                    L1 = L1[:n + 7]  # Delete(L1, 1, n + 7)

                L1 = L1[:L1.lower().find('text') + 3]  # Delete(L1, 1, Pos('text', LowerCase(L1)) + 3)
                L1 = L1[:L1.lower().find('"')]  # Delete(L1, 1, Pos('"', L1))
                L1 = L1[:L1.find('"') - 1]  # L1 = Copy(L1, 1, Pos('"', L1) - 1)
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
            if arr[i]["typ"] == typ["TextEdit"]:
                arr[i]["height"] = MINHEIGHT
            elif arr[i]["height"] < MINHEIGHT:
                arr[i]["height"] = DEFAULTHEIGHT

            # Проверка объекта на конфликт с предыдущими.
#            Valid = checkValid(arr)

            # Попытка коррекции объекта перемещением
            # ------------------------------------------------------------------------
            # if not Valid:
            #     Valid = True
            #     n = 1
            #
            #     repeat # Переделать в цикл while
            #         if (arr[i]["top"] >= arr[n]["top"]) and (
            #             arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
            #             arr[i]["left"] >= arr[n]["left"]) and (
            #             arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
            #             Valid = False
            #         n += 1
            #     until(Valid = False) or (n = i)
            #
            #     if not Valid:
            #         if (arr[i]["top"] >= arr[n - 1]["top"]) and (
            #             arr[i]["top"] < arr[n - 1]["top"] + arr[n - 1]["height"]):
            #             arr[i]["top"] = arr[n - 1]["top"] + arr[n - 1]["height"]
            #     Valid = True
            #
            #     n = 1
            #
            #     repeat # Переделать в цикл while
            #         if (arr[i]["top"] >= arr[n]["top"]) and (
            #             arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
            #             arr[i]["left"] >= arr[n]["left"]) and (
            #             arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
            #             Valid = False
            #         n += 1
            #     until(Valid = False) or (n = i)
            #
            #     if not Valid:
            #         if (arr[i]["left"] >= arr[n - 1]["left"]) and (
            #             arr[i]["left"] < arr[n - 1]["left"] + arr[n - 1]["width"]):
            #             arr[i]["left"] = arr[n - 1]["left"] + arr[n - 1]["width"]
            #
            #     # Повторная проверка объекта на конфликт с предыдущими.
            #     Valid = checkValid(arr)
            #
            # # Попытка коррекции объекта уменьшением
            # # ------------------------------------------------------------------------
            # if not Valid:
            #     arr[i]["width"] = MINWIDTH
            #     arr[i]["height"] = MINHEIGHT
            #
            #     # Повторная проверка объекта на конфликт с предыдущими.
            #     Valid = checkValid(arr)
            # # ------------------------------------------------------------------------
            #
            # if Valid:
            #     i += 1
            # else:
            #     arr.pop()  # Удаляем последний (конфликтующий) элемент списка
            #     logFile.write(L + " ERROR - conflict of objects")
            #     Errs = True
            # # ------------------------------------------------------------------------
            logFile.write("OBJECT: " + str(arr[i]) + "\n")  # DEBUG: Отладочный вывод

    logFile.write("\n")  # DEBUG: Отладочный вывод
    logFile.write("End parsing" + "\n")
    logFile.close()
    # if not Errs : DeleteFile(PathName + '.log')
    return Errs
