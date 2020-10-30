import xlsxwriter

#Code modelling cumulative cases in the UK from March 22nd to April 22nd
#Most data is extrapolated at the time
#Limited by the testing capacity of the country
#Rate of increase based on the available testing information at the time

workbook = xlsxwriter.Workbook("CoronavirusInfections.xlsx")
worksheet = workbook.add_worksheet("March2April")

#Rates of increase
#Different rates considered since increase won't always be the same

list35 = ["35%"] #When rate of increase is 35%
list25 = ["25%"] #When rate of increase is 25%
list15 = ["15%"] #When rate of increase is 15%

for i in range(0,30):
    num35 = 5000 * (1.35 ** i)
    num25 = 5000 * (1.25 ** i)
    num15 = 5000 * (1.15 ** i)

    list35.append(num35)
    list25.append(num25)
    list15.append(num25)

worksheet.write_column("A1", list35)
worksheet.write_column("B1", list25)
worksheet.write_column("C1", list15)

print("Cases at 35%:",list35)
print("Cases at 25%:",list25)
print("Cases at 15%:",list15)

workbook.close()



