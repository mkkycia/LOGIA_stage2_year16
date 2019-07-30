def czy_jest_slowem_bartka(slowo):
    zapas = 0
    for litera in slowo:
        if 'a' == litera:
            zapas+=1
        elif 'b' == litera:
            zapas-=1
        if zapas<0:
            return False
        elif zapas>1:
            return False
    if 'a' in slowo and 'b' in slowo:
        if zapas == 0:
            return True
        else:
            return False
    else:
        if zapas == 0 or zapas == 1:
            return True
        else:
            return False

def spr(wyraz):
    for i in range(len(wyraz)):
        a = wyraz[:i+1]
        if not czy_jest_slowem_bartka(a):
            a = wyraz[:i]
            break

    return len(a)

