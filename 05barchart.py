from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference,Series

wb = Workbook()
ws = wb.active

for i in range(15):
    ws.append([i])
ws.append([2])
values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=16)
chart = BarChart()
chart.add_data(values)

ws.add_chart(chart, "C1")

wb.save("05chart.xlsx")