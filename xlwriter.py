from xlwt import Workbook, Formula, easyxf
import math
from datetime import datetime as dt


def xlt(n,number,lab,fac):
    wb = Workbook()
    sheet1 = wb.add_sheet(n)
    style1 = easyxf('pattern: pattern solid, fore_colour red; align: horiz center')
    style2 = easyxf('align: horiz center;')
    now = dt.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    sheet1.write(0,0,"Name",style1)
    sheet1.write(0,1,"ID",style1)
    sheet1.write(0,2, "Date & Time", style1)
    for i in range(1,number+1):
        sheet1.write(i,0,fac[i-1])
        sheet1.write(i,1,lab[i-1],style2)
        sheet1.write(i,2,date_time)


    sheet1.col(0).width = 7000
    sheet1.col(1).width = 7000
    sheet1.col(2).width = 7000

    wb.save(n+".xls")


