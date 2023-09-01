n = int(input())


s = str(n)

if n > 0:
    print(n)
else:

    remove_last = s[:-1]
    remove_before_last = s[:-2] + s[-1]
    

    print(max(int(remove_last), int(remove_before_last)))