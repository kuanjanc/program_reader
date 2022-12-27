setpass_pongo_HV = open("AminiAQ_HUAYRA_HV.txt","r")
import pandas as pd
Report = open("suppressbinning_filter.csv","w")
Report.write("Suite,Setpass_status,")
Report.write("\n")
for line in setpass_pongo_HV:
    for line in setpass_pongo_HV:
        if line.__contains__("suite"):
            suite_name1 = line.split("calls")[0]
            suite_name = suite_name1.split("suite")[1]
            Report.write(suite_name)
            Report.write(",")
        if line.__contains__("suppressBinning = "):
            if line.__contains__("suppressBinning = false"):
                Report.write("N,\n")
            elif line.__contains__("suppressBinning = true"):
                Report.write("Y,\n")
        if line.__contains__("bypass"):
            Report.write("\n")
            break
Report.close()
setpass_report = pd.read_csv('suppressbinning_filter.csv')
setpass_report = setpass_report.drop(["Unnamed: 2"], axis = 1)
setpass_report = setpass_report.fillna("N")
setpass_report.to_excel('setpass_report.xlsx') # report for setpass status

######################below process is for bypass status########################
bypass_pongo_HV = open("AminiAQ_HUAYRA_HV.txt","r")
Bypass_Report = open("Bypass_filter.csv","w")
Bypass_Report.write("Suite,Bypass,")
Bypass_Report.write("\n")

for line in bypass_pongo_HV:
    for line in bypass_pongo_HV:
        if line.__contains__("suite"):
            suite_name3 = line.split("calls")[0]
            suite_name2 = suite_name3.split("suite")[1]
            Bypass_Report.write(suite_name2)
            Bypass_Report.write(",")
        if line.__contains__("bypass ="):
            if line.__contains__("bypass = false"):
                Bypass_Report.write("N,\n")
            elif line.__contains__("bypass = true"):
                Bypass_Report.write("Y,\n")
Bypass_Report.close()
bypass_report = pd.read_csv('Bypass_filter.csv')
bypass_report = bypass_report.drop(["Unnamed: 2"], axis = 1)
bypass_report = bypass_report.fillna("N")
bypass_report.to_excel('Bypass_Report.xlsx') # report for bypass status
df1 = pd.read_excel('setpass_report.xlsx')
df2 = pd.read_excel('Bypass_Report.xlsx')
report_setpass_bypass = pd.merge(df2,df1,how='left')
report_setpass_bypass1 = report_setpass_bypass.drop(["Unnamed: 0"], axis = 1)
report_setpass_bypass1.to_excel('AminiAQ_coverage.xlsx',index = False)# final report
print(report_setpass_bypass1)