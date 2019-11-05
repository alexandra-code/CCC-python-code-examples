#Rainfall list collector thing STAR Institute
#Instructional Purposes only

def main():
    jan = float(input("What is the total rainfall for January? "))
    feb = float(input("What is the total rainfall for January? "))
    mar = float(input("What is the total rainfall for January? "))    
    apr = float(input("What is the total rainfall for January? "))
    may = float(input("What is the total rainfall for January? "))
    june = float(input("What is the total rainfall for January? "))
    july = float(input("What is the total rainfall for January? "))
    aug = float(input("What is the total rainfall for January? "))
    sept = float(input("What is the total rainfall for January? "))
    octo = float(input("What is the total rainfall for January? "))
    nov = float(input("What is the total rainfall for January? "))
    dec = float(input("What is the total rainfall for January? "))
    rain = [jan, feb, mar, may, apr, june, july, aug, sept, octo, nov, dec]
    return(rain)


def computeRainTotal(rain):

    rainTotal = sum(rain)
    print(rainTotal)


def computeRainAvg(rain):

    rainAvg = sum(rain) / len(rain)
    print(rainAvg)
    


def rainHighest(rain):
    highest = max(rain)
    print(highest)

def rainLowest(rain):
    lowest = min(rain)
    print(lowest)






rain = main()
print(rain)
computeRainTotal(rain)
computeRainAvg(rain)
rainHighest(rain)
rainLowest(rain)












































print("made by star institute")
#Made by Alexandra with the STAR institute. For instructional purposes ONLY
