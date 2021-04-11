#Explain your work

#Question 1
liste=["a","b","c","d","e","f"]
k=0
s=int(len(liste)/2)

while k<len(liste)/2:
    
    liste[k],liste[s]=liste[s],liste[k]
    k+=1
    s+=1
    
print(liste)

#Question 2
n=int(input("lütfen tek basamaklı bir tamsayı giriniz: "))
l=[i for i in range(n+1) if i%2==0]
print(l)
