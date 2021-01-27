from openpyxl import Workbook
import warframe_market_script

def itemListToExcel(item_list):
    wb = Workbook()
    ws = wb.active

    ws.column_dimensions['A'].width = 35
    ws["A1"] = "Item"
    for i in range(len(item_list)):
        ws["A" + str(i+2)] = item_list[i]
    
    ws["B1"] = "Plat"
    for i in range(len(item_list)):
        ws["B" + str(i+2)] = str(warframe_market_script.getAveragePlatPrice(ws["A"+ str(i+2)].value))

    ws["C1"] = "Ducat"
    for i in range(len(item_list)):
        ws["C" + str(i+2)] = str(warframe_market_script.getDucatPrice(ws["A"+ str(i+2)].value))
    
    ws.column_dimensions['D'].width = 10
    ws["D1"] = "Plat:Ducat"
    for i in range(len(item_list)):
        ws["D" + str(i+2)] = "1 : " + str(round((float(ws["C" + str(i+2)].value) / float(ws["B" + str(i+2)].value)),2))

    wb.save(filename="result.xlsx")