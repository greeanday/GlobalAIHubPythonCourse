#Explain your work

#Question 1
k=0
l=["st1","st2","st3","st4","st5"]
s={}
while k<5:
    Midterm=int(input("öğrenci midterm notunu giriniz: "))
    Project=int(input("öğrenci proje notu: "))
    Final=int(input("öğrenci final notu: "))
    f=[Midterm,Project,Final]
    s[l[k]]=f
    k+=1
    
n=list(s.values())

st1=n[0][0]*0.3+n[0][1]*0.3+n[0][2]*0.4
st2=n[1][0]*0.3+n[0][1]*0.3+n[0][2]*0.4
st3=n[2][0]*0.3+n[0][1]*0.3+n[0][2]*0.4
st4=n[3][0]*0.3+n[0][1]*0.3+n[0][2]*0.4
st5=n[4][0]*0.3+n[0][1]*0.3+n[0][2]*0.4
passingGrade=[st1,st2,st3,st4,st5]
sonuc=[]
k=1
m=len(passingGrade)
while k<=m:
    c=passingGrade[0]
    for i in passingGrade:
        if i<=c:
            c=i
    sonuc.append(c)
    passingGrade.remove(c)
    k+=1
print(sonuc)
