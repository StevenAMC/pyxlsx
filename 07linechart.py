from datetime import date

from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.axis import DateAxis

wb = Workbook()
ws = wb.active

rows = [
    ['Fecha', 'Lote 1', 'Lote 2', 'Lote 3'],
    [date(2013,9, 1), 15, 10, 20],
    [date(2013,9, 2), 55, 15, 30],
    [date(2013,9, 3), 22, 20, 45],
    [date(2013,9, 4), 40, 25, 30],
    [date(2013,9, 5), 55, 35, 30],
    [date(2013,9, 6), 50, 30, 25],
]

for row in rows:
    ws.append(row)

c1 = LineChart()
c1.title = "Line Chart"
#c1.legend = None
c1.style = 15
c1.y_axis.title = 'Tamaño'
c1.x_axis.title = 'Numeros de prueba'

data = Reference(ws, min_col=2, min_row=1, max_col=4, max_row=7)
c1.add_data(data, titles_from_data=True)

ws.add_chart(c1, "F4")

wb.save("07line.xlsx")
