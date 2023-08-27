from openpyxl.chart import BarChart, Reference, LineChart  # chart module
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")  # sample.xlsx file open
ws = wb.active  # active s

# bar_value = Reference(ws, min_row=2, max_row=11,
#                       min_col=2, max_col=3)  # B2:C11
# bar_chart = BarChart()  # bar chart(BarChart, LineChart, PieChart)
# bar_chart.add_data(bar_value)  # add data

# ws.add_chart(bar_chart, "E1")  # add chart to E1 cell

line_value = Reference(ws, min_row=1, max_row=11,
                       min_col=2, max_col=3)  # B2:C11
line_chart = LineChart()  # bar chart(BarChart, LineChart, PieChart)
line_chart.add_data(line_value, titles_from_data=True)  # add data
line_chart.title = "Score"  # chart title
line_chart.style = 20  # chart style
line_chart.y_axis.title = "Score"  # y axis title
line_chart.x_axis.title = "Number"  # x axis title
ws.add_chart(line_chart, "E1")  # add chart to E1 cell

wb.save("sample_chart.xlsx")
