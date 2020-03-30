while True:
    num = input('Enter temperature, or type end to close the program.\n')
    if num == "end":
        break
    if int(num) >= 21:
        print('Turn heater off')
    else:
        print('Turn heater on')
