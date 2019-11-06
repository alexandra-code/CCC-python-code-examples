#Made for instructional purposes only.
#Do not repurpose code.








a = "alpha"
b = "beta"
c = "gamma"




def greeting():
    print("Hello!")
    print("Welcome to my Function!")


greeting()



def showMax(a,b,c):

   biggest = [len(a), len(b), len(c)]

   print(max(biggest))



showMax(a,b,c)

x = int(input("What is the value of the numerator? "))
y = int(input("What is the value of the denominator? "))

def ratioGet(x,y):
    if y == 0:
        print("Undefined")
    else:
        print(x/y)


ratioGet(x,y)






h = int(input("What is the height of the cylinder? "))
r = int(input("What is the radius of the cylinder? "))


def showVolume(h,r):
    volume = 3.141592653589793238462643383 * (r ** 2) * h
    print(volume)



showVolume(h,r)














print("Made by Alexandra, STAR Institute CCC")


