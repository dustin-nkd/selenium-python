import openpyxl

wb = openpyxl.load_workbook("credentials.xlsx")
ws = wb.active

for row in range(5, 11):
    for column in range(1, 3):
        ws.cell(row=row, column=column, value='dustin')

wb.save("credentials.xlsx")