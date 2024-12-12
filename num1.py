import itertools

def variant(kl):
    kl=kl+kl
    k=0
    l1=itertools.combinations_with_replacement(kl,6)
    l2=list(l1)
    for i in range(len(l2)):
        if (l2[i][0] == "Р") and (l2[i][5] == "К"):
            k+=1
    print(l2)  #Добавил для проверки
    return(k)



print("Существует",variant("КАТЕР"),"различных выражений начинающихся с Р и заканчивающихся К")
