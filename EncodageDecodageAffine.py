def diviseurs(a): # liste des diviseurs premiers de a
    n=2
    d=[]
    while n<=a:
        while a/n==a//n:
            a=a//n
            d.append(n)
        n+=1
    return d

def premiers_entre_eux(a,b): # compare les diviseurs premiers de a et b
    div_b=diviseurs(b)
    for i in diviseurs(a):
        if i in div_b:
            return False
    return True

def retirer_accents(texte): # remplace les caractères accentués
    from re import sub
    texte=sub(u"[àáâãäå]",'a',texte)
    texte=sub(u"[èéêë]",'e',texte)
    texte=sub(u"[ìíîï]",'i',texte)
    texte=sub(u"[òóôõö]",'o',texte)
    texte=sub(u"[ùúûü]",'u',texte)
    texte=sub(u"[ç]",'c',texte)
    texte=sub(u"[ýÿ]",'y',texte)
    texte=sub(u"[ß]",'ss',texte)
    texte=sub(u"[ñ]",'n',texte)
    return texte 

def encodage_affine(texte,a=1,b=0): # encode avec a=1 et b=0 par défaut 
    if not premiers_entre_eux(abs(a),26) or a==0: # vérifie si a et 26 sont premiers entre eux ou si a≠0
        raise ValueError ('Clé invalide') # retourne une erreur
    try: # vérifie s'il n'y a pas d'accents
        (texte.encode(encoding='utf-8')).decode(encoding='ascii')
    except:
        texte=retirer_accents(texte)
    texte=texte.upper() # met le texte en majuscules
    encode=''
    for i in texte:
        if i==' ' or ord(i)<ord('A') or ord(i)>ord('Z'): # n'encode pas les espaces et les caractères spéciaux
            encode+=i
        else:
            encode+=chr(((ord(i)-ord('A'))*a+b)%26+ord('A')) # y≡ax+b[26]
    return encode

def decodage_affine(texte,a=1,b=0): # décode avec a=1 et b=0 par défaut
    if not premiers_entre_eux(abs(a),26) or a==0: # vérifie si a et 26 sont premiers entre eux ou si a≠0
        raise ValueError ('Clé invalide') # retourne une erreur
    try: # vérifie s'il n'y a pas d'accents
        (texte.encode(encoding='utf-8')).decode(encoding='ascii')
    except:
        texte=retirer_accents(texte)
    x=1
    while (26**x+1)/a != (26**x+1)//a: # trouve l'inverse de a [26]
        x+=1
    ancien_a=a
    a=((26**x+1)//a)%26 # calcul du nouveau a
    b=(-b*((26**x+1)//ancien_a))%26 # calcul du nouveau b
    del x,ancien_a # supprime les variables inutiles
    texte=texte.upper() # met le texte en majuscules
    decode=''
    for i in texte:
        if i==' ' or ord(i)<ord('A') or ord(i)>ord('Z'): # ne décode pas les espaces et les caractères spéciaux
            decode+=i
        else:
            decode+=chr(((ord(i)-ord('A'))*a+b)%26+ord('A')) #x≡ax+b[26]
    return decode
