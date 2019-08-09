import xlrd

wb = xlrd.open_workbook(filename='test.xsxl')  # 打开文件
sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格sheet
row1 = sheet1.row_values(0) #读取第一行
print(row1)
