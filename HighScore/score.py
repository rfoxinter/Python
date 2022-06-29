def diff(a:list,b:list=0)->list:
    b=list(set(a)) if b==0 else b
    return [i for i in a if not i in b or b.remove(i)]

def moy(a:list)->float:
    return sum(a)/5

def score(val:list)->int:
    _d=diff(val)
    _diff,_set,_min,_max,_moy=len(_d),len(list(set(_d))),min(val),max(val),moy(val)
    del _d
    if _diff==1:
        return 1
    elif _diff==2 and _set==1:
        return 3
    elif _diff==3 and _set==1:
        return 6
    elif _diff==4:
        return 10
    elif _diff==2 and _set==2:
        return 3
    elif _diff==3 and _set==2:
        return 8
    elif _max==_min + 4 and _moy==_min + 2:
        return 12 if 2 in val or 12 in val else 8
    else:
        return 0
