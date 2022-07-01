#Code Made: To copy my payslips to later filter as DateModified as where not downloaded as per their month
#Dated: datetime.datetime(2022, 7, 1, 9, 27, 48, 40834)

import shutil
import calendar
from time import sleep
files = [f"{calendar.month_abbr[i%12].upper()}_2021" if i<13 else f"{calendar.month_abbr[i%12].upper()}_2022" for i in range(6, 19)]
files[6] = "DEC_2021"
print(files)
for file_name in files:
    new_f= f"C:/Users/zeta/Desktop/Payslips/New folder/{file_name}.pdf"
    old_f= f"C:/Users/zeta/Desktop/Payslips/{file_name}.pdf"
    sleep(2)
    shutil.copyfile(old_f, new_f)
