#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

MINHEIGHT = 21
MINWIDTH = 21
DEFAULTHEIGHT = 21
DEFAULTWIDTH = 70

def correctLine(line):  # Чистка строк по краям, восстановление структуры строки
    # Поиск и удаление лишних пробелов.
    tempLine = line.strip()  # Удаляем пробелы по краям
    if tempLine != "":
        tempLine = re.sub(r'\s+', ' ', tempLine)  # Удаление двойных пробелов используя регулярные выражения
        tempLine = re.sub(r'< ', '<', tempLine)  # Удаление пробела после символа <
        tempLine = re.sub(r'= ', '=', tempLine)  # Удаление пробела после символа =
        tempLine = re.sub(r' =', '=', tempLine)  # Удаление пробела перед символом =

        # Считаем, что строки без < допустимы. Добавляем < и парсим дальше
        n = tempLine.find('<')  # Находим позицию символа <
        if n == -1:  # Нет символа <
            tempLine = '<' + tempLine
        else:
            tempLine = tempLine[n:]  # Удаляем возможный мусор перед <

        # Считаем, что строки без > допустимы. Добавляем > и парсим дальше
        n = tempLine.find('>')  # Находим позицию символа >
        if n == -1:  # Нет символа >
            tempLine = tempLine + '>'
        else:
            tempLine = tempLine[:n + 1]  # Берем строку до > включительно
    return tempLine


def checkValid(arr):  # Проверка объекта на конфликт с предыдущими.
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
        for L in f:
            lineWork = correctLine(L)  # Чистка строк по краям, восстановление структуры строки
            if lineWork == '':  # Если строка пустая - пропускаем
                continue

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
                logFile.write("ERROR  (wrong object type) : " + L)
                Errs = True
                continue
            # ----------------------------------------------------------------------------

            # Если удалось определить тип объекта - отбрасываем часть строки с названием типа
            n = lineWork.find(' ')
            if n != -1:
                lineWork = lineWork[n + 1:]

            # Заполнение свойств объекта
            # -----------------------------------------------------------------------------
            n = lineWork.lower().find('left="')  # Заполнение свойства left, если указано
            if n != -1:
                L1 = lineWork[lineWork.lower().find('left="') + 6:]
                L1 = L1[:L1.find('"')]
                try:
                    arr[i]["left"] = int(L1)
                except ValueError:
                    arr[i]["left"] = 0

            n = lineWork.lower().find('top="')  # Заполнение свойства top, если указано
            if n != -1:
                L1 = lineWork[lineWork.lower().find('top="') + 5:]
                L1 = L1[:L1.find('"')]
                try:
                    arr[i]["top"] = int(L1)
                except ValueError:
                    arr[i]["top"] = 0

            n = lineWork.lower().find('width="')  # Заполнение свойства width, если указано
            if n != -1:
                L1 = lineWork[lineWork.lower().find('width="') + 7:]
                L1 = L1[:L1.find('"')]
                try:
                    arr[i]["width"] = int(L1)
                except ValueError:
                    arr[i]["width"] = 0

            if arr[i]["typ"] != typ["TextEdit"]:  # Заполнение свойства height, если указано и если это не TextEdit
                n = lineWork.lower().find('height="')
                if n != -1:
                    L1 = lineWork[lineWork.lower().find('height="') + 8:]
                    L1 = L1[:L1.find('"')]
                    try:
                        arr[i]["height"] = int(L1)
                    except ValueError:
                        arr[i]["height"] = 0

            n = lineWork.lower().find('caption="')  # Заполнение свойства caption, если указано
            if n != -1:
                L1 = lineWork[lineWork.lower().find('caption="') + 9:]
                L1 = L1[:L1.find('"')]
                arr[i]["text"] = L1

            n = lineWork.lower().find('text="')  # Заполнение свойства text, если указано
            if n != -1:
                L1 = lineWork[lineWork.lower().find('text="') + 6:]
                L1 = L1[:L1.find('"')]
                arr[i]["text"] = L1

            # Корректируем размеры и положение объектов в соответствии с константами минимально допустимых размеров
            # ------------------------------------------------------------------------
            if arr[i]["left"] < 0:
                arr[i]["left"] = 0
            if arr[i]["top"] < 0:
                arr[i]["top"] = 0
            if arr[i]["width"] < MINWIDTH:
                arr[i]["width"] = DEFAULTWIDTH
            if arr[i]["typ"] == typ["TextEdit"]:
                arr[i]["height"] = MINHEIGHT
            elif arr[i]["height"] < MINHEIGHT:
                arr[i]["height"] = DEFAULTHEIGHT

            Valid = checkValid(arr)  # Проверка объекта на конфликт с предыдущими

            # Попытка коррекции объекта перемещением
            # TODO: Проверить корректность работы, отладить
            # ------------------------------------------------------------------------
            if not Valid:
                Valid = True
                for n in range(len(arr) - 1):
                    if (arr[i]["top"] >= arr[n]["top"]) and (arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
                    arr[i]["left"] >= arr[n]["left"]) and (arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
                        Valid = False
                        break

                if not Valid:
                    if (arr[i]["top"] >= arr[n - 1]["top"]) and (arr[i]["top"] < arr[n - 1]["top"] + arr[n - 1]["height"]):
                        arr[i]["top"] = arr[n - 1]["top"] + arr[n - 1]["height"]

                Valid = True
                for n in range(len(arr) - 1):
                    if (arr[i]["top"] >= arr[n]["top"]) and (arr[i]["top"] < arr[n]["top"] + arr[n]["height"]) and (
                    arr[i]["left"] >= arr[n]["left"]) and (arr[i]["left"] < arr[n]["left"] + arr[n]["width"]):
                        Valid = False
                        break

                if not Valid:
                    if (arr[i]["left"] >= arr[n - 1]["left"]) and (arr[i]["left"] < arr[n - 1]["left"] + arr[n - 1]["width"]):
                        arr[i]["left"] = arr[n - 1]["left"] + arr[n - 1]["width"]

                Valid = checkValid(arr)  # Повторная проверка объекта на конфликт с предыдущими

            #  Попытка коррекции объекта уменьшением
            # TODO: Можно уменьшать не сразу до минимума, а до устранения конфликта
            # ------------------------------------------------------------------------
            if not Valid:
                arr[i]["width"] = MINWIDTH
                arr[i]["height"] = MINHEIGHT

                Valid = checkValid(arr)  # Повторная проверка объекта на конфликт с предыдущими
            # ------------------------------------------------------------------------
            if Valid:
                i += 1
            else:
                arr.pop()  # Удаляем последний (конфликтующий) элемент списка
                logFile.write("ERROR (conflict of objects): " + L)
                Errs = True

    logFile.write("End of parsing" + "\n")
    logFile.close()
    return Errs
