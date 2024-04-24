import openpyxl


# wb = openpyxl.Workbook()
wb = openpyxl.load_workbook("transactions.xlsx")
print(wb.sheetnames)

sheet = wb["Sheet1"]

cell = sheet["a1"]
column = sheet["a"]
cells = sheet["a:c"]
print(cells)
