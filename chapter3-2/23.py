principal = 15000
rate = 0.06
mRate = 0.06/12
mRet = 290
m = 0
Goal = principal/2
while principal>= Goal:
    principal = (1+mRate)*principal-mRet
    m+=1

print("Loan will be half paid off after",str(m),"months.")