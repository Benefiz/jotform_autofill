import pandas as pd
import os
import io
import constant as c
from num_thai.thainumbers import NumThai

def createScript(timesheet, script_file_name):
    num = NumThai()
    file_name = os.path.splitext("script/"+script_file_name)[0] + '.txt'
    all_lines = []
    for i, row in timesheet.iterrows():
        for j, column in row.iteritems():
            all_lines.append(
                "document.getElementById('input_17_{}_{}').value = '{}';\n".format(i, j, column))
    workDays = i+1
    salaryPerDay = c.salaryPerDay
    salarySum = salaryPerDay*workDays
    salaryThaiText = num.NumberToTextThai(salarySum)
    salaryThaiText.append("บาทถ้วน")
    # Personal Info
    # Account No.
    all_lines.append("document.getElementById('input_59').value = '{}';\n".format(c.accountNo))
    # Citizen No.
    all_lines.append("document.getElementById('input_61').value = '{}';\n".format(c.citizenNo))
    # Salary
    all_lines.append("document.getElementById('input_21').value = '{}';\n".format(workDays))
    all_lines.append("document.getElementById('input_22').value = '{}';\n".format(salaryPerDay))
    all_lines.append("document.getElementById('input_23').value = '{}';\n".format(salarySum))
    all_lines.append("document.getElementById('input_28').value = '{}';\n".format("".join(salaryThaiText)))
    script_file = io.open(file_name, "w", encoding="utf-8")
    script_file.writelines(all_lines)
    script_file.close()


for file in [file for file in os.listdir("timesheet") if file.endswith('.csv')]:
    timesheet = pd.read_csv("timesheet/"+file, header=None)
    createScript(timesheet, os.path.splitext(file)[0])
