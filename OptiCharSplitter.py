def splitString():
    string = input("Enter string: ")
    count = 0
    unique = []
    diff = 0
    flag = 0
    n = 1
    for i in range(len(string)-1):
        if string[i]!=string[i+1]:
            flag = 1
            break
    if flag == 0:
        count = len(string) - 1
        print("\nCount: ",count)
    else:
        while n!=(len(string)-1):
            sub1 = string[:n]
            sub2 = string[n:]
            for i in sub1:
                if i not in unique:
                    unique.append(i)
            count1 = len(unique)
            unique = []
            for i in sub2:
                if i not in unique:
                    unique.append(i)
            count2 = len(unique)
            unique = []
            diff = abs(count2 - count1)
            if diff == 0:
                count = count + 1
            if diff>2:
                jump = diff//2
                n = n+jump
    
            else:
                n = n+1
        print("\nCount: ",count)
                
#main environment
splitString()