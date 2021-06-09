import pandas as pd
import os
import io


def createScript(timesheet, script_file_name):
    file_name = os.path.splitext("script/"+script_file_name)[0] + '.txt'
    all_lines = []
    for i, row in timesheet.iterrows():
        for j, column in row.iteritems():
            all_lines.append(
                "document.getElementById('input_17_{}_{}').value = '{}';\n".format(i, j, column))
    script_file = io.open(file_name, "w", encoding="utf-8")
    script_file.writelines(all_lines)
    script_file.close()


for file in [file for file in os.listdir("timesheet") if file.endswith('.csv')]:
    timesheet = pd.read_csv("timesheet/"+file, header=None)
    createScript(timesheet, os.path.splitext(file)[0])
