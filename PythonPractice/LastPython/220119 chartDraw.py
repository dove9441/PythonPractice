import openpyxl
from openpyxl.chart import Reference, Series, LineChart #Barchart, PieChart 가능

company=["LG전자","삼성전자","현대자동차"]
for i in company:
    book=openpyxl.load_workbook("./엑셀데이터/2017년_광고비_{}.xlsx".format(i))
    sheet=book.active
    #차트 만들기
    chart=LineChart()
    chart.title="{}회사 월별 광고비".format(i)
    
    for j in ["C","D","E","F","G"]:
        value=Reference(sheet,range_string="sheet1!{}2:{}13".format(j,j))
        value_series=Series(value,title=sheet["{}1".format(j)].value)
        chart.append(value_series)
         #위 3줄은 형식 고정이다
         
    sheet.add_chart(chart,"J1")
    book.save("./엑셀데이터/2017년_광고비_{}_차트.xlsx".format(i))
    