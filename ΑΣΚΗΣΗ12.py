#ανοιγμα του αρχειου
f = open("ΑΣΚΗΣΗ12ΕΓΡ.txt","r")
s= f.read().lower()
f.close()
#δημιουργει ενα λεξικο με τις συχνοτητες του καθε γραματος
freqs = {}
for line in s:
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
#βγαζει τα κενα και τις νεες γραμμες
if " " in freqs:
    freqs.pop(" ")
if "\n" in freqs:
    freqs.pop("\n")
#δημιουργει δυο λιστες σε φθινουσα σειρα βαση των συχνοτητων
keys1 = sorted(freqs, key=freqs.get, reverse=True)
val1 = sorted(freqs.values(),reverse=True)
#Αλλάζει τις θέσεις των γραμμάτων και τα κανει κεφαλαια
ran = len(keys1)
if (ran-1) % 2 == 0:
    mid= int (ran/2 -1)
else:
    mid=int (ran/2 - 0.5)
for i in range(mid+1):
    dif = ran-i-1
    s = s.replace(keys1[i],keys1[dif])
#δημιουργια νεου αρχειου για την εγγραφη του νεου κειμενου
f=open("ΑΣΚΗΣΗ12ΕΓΡΝΕΟ.txt","w")
f.write(s.upper())
f.close()
