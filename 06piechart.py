from openpyxl import Workbook
from openpyxl.chart import PieChart3D, Reference,PieChart

data = [
    ['Fruta', 'Cantidad'],
    ['Pera', 10],
    ['Manzana', 30],
    ['Fresa', 20],
    ['Plátano', 40],
]

wb = Workbook()
ws = wb.active

for row in data:
    ws.append(row)

pie = PieChart3D()
labels = Reference(ws, min_col=1, min_row=2, max_row=5)
data = Reference(ws, min_col=2, min_row=1, max_row=5)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.title = "Pies sold by category"

ws.add_chart(pie, "E1")

pie2 = PieChart()
pie2.add_data(data, titles_from_data=True)
pie2.set_categories(labels)
pie2.title = "Pies sold by category"

ws.add_chart(pie2, "L1")

wb.save("06pie.xlsx")
