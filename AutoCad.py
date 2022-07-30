import os
import win32com.client
from comtypes.client import GetBestInterface
import time
import math
import sys

def filesProcessing(listPlots, i, from_, to):

    fileName = listPlots[i]

    document = win32com.client.Dispatch("AutoCAD.Application")
    document.Documents.Open(fileName)

    try:
        acad = document.ActiveDocument
    except:
        time.sleep(2)
        acad = document.ActiveDocument
    print(acad)
    time.sleep(1)
    for j in range(acad.ModelSpace.Count):
        try:
            item = acad.ModelSpace.Item(j)
            objname = item.ObjectName.lower()
        except:
            item = acad.ModelSpace.Item(j)
            objname = item.ObjectName.lower()
        if 'text' in objname:
            text = win32com.client.CastTo(item, "IAcadText")
            if from_ in text.TextString:
                text.TextString = text.TextString.replace(from_,
                                                          to)
                text.Update()
    acad.Save()
    acad.Close(True)


    #window.progressPlain.setPlainText(
    #    f'{window.progressPlain.toPlainText()} \nВ файле "{currentFile}" сделано {replaces} замен\n')
    #window.progressBar.setValue(math.ceil(((i + 1) / len(listPlots)) * 100))

def filesInfo(window, fileName, i, listPlots):
    window.progressPlain.setPlainText(
        f'{window.progressPlain.toPlainText()} Закончена обработка файла "{fileName}"\n')
    window.progressBar.setValue(math.floor(((i + 1) / len(listPlots)) * 100))
