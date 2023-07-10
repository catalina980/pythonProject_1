import numpy as np
import xlrd
np.set_printoptions(suppress=True)
#读取excel
wb = xlrd.open_workbook("D:\数学建模\附件1.xlsx")
#获取第一个sheet页
sheet1 = wb.sheet_by_index(0)
row1 = sheet1.nrows - 1
col1 = sheet1.ncols - 1
datamatrix = np.zeros((row1,col1))
for x in range(1,row1+1):
    for y in range(1,col1+1):
        val = sheet1.cell_value(x,y)
        if val is None or val == '':
            datamatrix[x-1,y-1] = 10000
        else:
            datamatrix[x - 1, y - 1] = val
#处理对角线元素为0
for x in range(row1):
    datamatrix[x,x] = 0
Distince = np.round(datamatrix,3)
#print(Distince)