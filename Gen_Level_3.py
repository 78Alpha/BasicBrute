import gc

lib = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`,./;'[]~!@#$%^&*()_+{}|:<>?"

for a in range(0, len(lib)):
    for b in range(0, len(lib)):
        for c in range(0, len(lib)):
            brute = lib[a] + lib[b] + lib[c]
            with open("filey.txt", 'a') as file:
                file.write(str(brute) + '\n')
                gc.collect()
