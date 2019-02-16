def sumIntervals(master,index):
    checker=True
    while checker:
        checker=False
        for i in range(index + 1):
            for j in range(i + 1, index + 1):
                if j <= index:
                    ol = bool(set(master[i]) & set(master[j]))
                    if ol:
                        master[i] = master[i] + master[j]
                        master[i] = (list(set(master[i])))
                        master[i].sort()
                        del master[j]
                        index = index - 1
                        checker = True
    sum = 0
    for x in master:
        sum = sum + (len(x) - 1)
    return sum


ans="ναι"
master=[]
index=-1
while ans=="ναι":
    x1 = int(input("δώσε αριστέρο όριο! "))
    x2 = int(input("δώσε δεξί όριο! "))
    master.append(list(range(x1,x2+1)))
    ans = input("θες να συνεχίσεις να φτιάχνεις διαστήματα; ")
    index= index +1
print ( "το αθροισμα του μηκους των διαστήματων ειναι " + str(sumIntervals(master,index)))

