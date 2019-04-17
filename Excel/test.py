# -*- conding:utf-8 -*-
#Author:wzf

import xlrd
import os
workbook = xlrd.open_workbook('z.xlsx');

print(workbook.sheet_names())

Data_sheet = workbook.sheets()[1];
print(Data_sheet.name,Data_sheet.nrows,Data_sheet.ncols)
rows = Data_sheet.row_values(17) #获取第一行内容
cols = Data_sheet.col_values(1) #获取第二列内容
cell_A1 = Data_sheet.cell(15,4)

hebing = workbook.sheet_by_index(1)
for hb in hebing.merged_cells:
    rs,re,cs,ce = hb
    print(hb)

