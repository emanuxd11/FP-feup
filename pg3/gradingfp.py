def fun():
    grade = 0
    components = [-1, -2, -3, -4]
    for x in range(len(components)):
        n = int(input())
        if components[x] < -2:
            if n not in range(40, 101):
                print("RFF")
                return
        if n not in range(0, 101):
            print("Input error")
            return
        components[x] = int(n)

    grade = (components[0] + components[1] + 13 * components[2] + 5 * components[3]) / 100

    print(components[0])
    if int(grade+0.5) == int(grade+1):
        print(int(grade+1))
    else:
        print(int(grade))

fun()
