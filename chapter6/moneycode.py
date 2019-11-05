#instructional Purposes only


employeeName = " "
hourlyRate = 0.0
hoursWorked = 0.0
federalTax =0.0
stateTax = 0.0
restartCode = ""

def employeeInfo():
    employeeName = input("What is your name? ")
    hourlyRate = float(input("How much do you make an hour? "))
    hoursWorked = float(input("How many hours did you work? "))
    return(employeeName, hourlyRate, hoursWorked)

def grossPayCalc(hourlyRate, hoursWorked):
    grossPay = hourlyRate * hoursWorked
    return(grossPay)

def fedTaxPay(grossPay):
    federalTax = grossPay * 0.14
    return(federalTax)

def stateTaxPay(grossPay):
    stateTax = grossPay * 0.04
    return(stateTax)

def netPayCalc(grossPay, stateTax, federalTax):
    netPay = grossPay - stateTax - federalTax
    return(netPay)

def printEmpInf(employeeName, hourlyRate, hoursWorked, federalTax, stateTax, grossPay, netPay):
    print(employeeName)
    print(employeeName, "'s hourly rate is ", hourlyRate)
    print("Her hours per week are ", hoursWorked)
    print("Her gross pay is " , grossPay)
    print("Her paid Federal Taxes were " , federalTax)
    print("Her paid State Taxes are ", stateTax)
    print("Her net pay is ", netPay)

def restartInc():
    restartCode = input("Would you like to calculate someone's pay? y/n: ").lower()
    if restartCode == "y":
        printFunc(employeeName, hourlyRate, hoursWorked, stateTax)

    return(restartCode)





def printFunc(employeeName, hourlyRate, hoursWorked, stateTax):
    employeeName, hourlyRate, hoursWorked = employeeInfo()
    grossPay = grossPayCalc(hoursWorked, hourlyRate)
    federalTax = fedTaxPay(grossPay)
    stateTax = stateTaxPay(grossPay)
    netPay = netPayCalc(grossPay, federalTax, stateTax)
    printEmpInf(employeeName, hourlyRate, hoursWorked, federalTax, stateTax, grossPay, netPay)

    restartInc()




printFunc(employeeName, hourlyRate, hoursWorked, stateTax)

while restartCode == "y":
    printFunc(employeeName, hourlyRate, hoursWorked, stateTax)
else:
    input("press Enter to close code. ")






























#created by Alexandra with CCC Star Institute. For instructional purposes only.
