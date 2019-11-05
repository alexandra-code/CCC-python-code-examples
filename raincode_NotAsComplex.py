#Rainfall list collector thing STAR Institute


rain = []


def computeRainAmt(rain):
   
    x = 0
    while x != 12:
        y = int(input("What is the total amount of rainfall for the target month? "))
        rain.append(y)
        x+=1

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



    


computeRainAmt(rain)
print(rain)
computeRainTotal(rain)
computeRainAvg(rain)
rainHighest(rain)
rainLowest(rain)

