def isYearLeap(year):
    if year % 4 != 0: 
	    return False
    elif year % 4 == 0 and year % 100 != 0: 
	    return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
	    return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
	    return True
#
# tu código del laboratorio anterior
#

def daysInMonth(year, month):
    x = isYearLeap(year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2 and x == True:
        return 29
    elif month == 2 and x == False:
        return 28
#
# coloca tu código aqui
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
