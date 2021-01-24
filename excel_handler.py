from openpyxl import Workbook

def itemListToExcel(item_list):
    wb = Workbook()
    ws = wb.active

    ws.column_dimensions['A'].width = 35
    ws["A1"] = "Item"
    for i in range(len(item_list)):
        ws["A" + str(i+2)] = item_list[i]

    wb.save(filename="result.xlsx")