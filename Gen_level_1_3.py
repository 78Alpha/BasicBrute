import gc

lib = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`,./;'[]~!@#$%^&*()_+{}|:<>?"
global lib2
lib2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`,./;'[]~!@#$%^&*()_+{}|:<>? "
#global libc
#libc = ""

def menu():
    print("Welcome to BasicBrute\n")
    print("You must be here to make a library of passwords")
    print("The program will start soon but we need to know a few things first\n")
    ans = str(input("How long would you like the passwords to be? (Limit of 3 characters)\n"))
    print("Which library would you like to use?\n")
    global lib
    print("1.) " + str(lib) + " (This will make passwords only as long as you selected)\n")
    print("2.) " + str(lib2) + " (This will make passwords as long as you selected as well as all lengths smaller)\n")
    print("3.) Custom (Make your own library of characters to use")
    ans2 = str(input("Make your numeric selection now: "))
    if ans == "1":
        if ans2 == "2":
            lib = lib2
            L1()
        elif ans2 == "3":
            custom_lib()
            L1()
        else:
            L1()
    elif ans == "2":
        if ans2 == "2":
            lib = lib2
            L2()
        elif ans2 == "3":
            custom_lib()
            L2()
        else:
            L2()
    elif ans == "3":
        if ans2 == "2":
            lib = lib2
            L3()
        elif ans2 == "3":
            custom_lib()
            L3()
        else:
            L3()
    else:
        print("An error has occurred")
        menu()

def custom_lib():
    global lib
    global select
    select = str(input("What would you like your library to be?\n"))
    print(select + "\n")
    print(">>Yes<<\n")
    print(">>No<<\n")
    person = str(input("Is this what you wanted?\n"))
    if person == "Yes" or person == "yes" or person == "Y" or person == "y":
        print("Your library is " + str(select) + " and will now be created...\n")
        lib = select
    elif person == "No" or person == "no" or person == "N" or person == "n":
        print("The library will not be changed\n")
        menu()
    else:
        print("An error has occurred")
        custom_lib()

def L1():
    for a in range(0, len(lib)):
        brute = lib[a]
        with open("file1.txt", 'a') as file:
            file.write(str(brute) + '\n')
            gc.collect()

def L2():
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            brute = lib[a] + lib[b]
            with open("file2.txt", 'a') as file:
                file.write(str(brute) + '\n')
                gc.collect()

def L3():
    for a in range(0, len(lib)):
        for b in range(0, len(lib)):
            for c in range(0, len(lib)):
                brute = lib[a] + lib[b] + lib[c]
                with open("file3.txt", 'a') as file:
                    file.write(str(brute) + '\n')
                    gc.collect()

menu()
