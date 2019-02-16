def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter x: "))
    y = eval(input("Enter y: "))
    for i in range(10):
        x = 3.9 * (x - x**2)
        y = 3.9 * (y - y**2)
        print("**************")
        print(round(x,3),"  ",round(y,3))
main()