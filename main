def kriptografiruy(s, k):
    zagl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stroch = 'abcdefghijklmnopqrstuvwxyz'
    s_new = ''
    for i in s:
        if i.lower() != i:
            i = zagl.index(i) + k
            if i >= 27:
                l = (i - 27) // 27
                if l == 0:
                    l += 1
                for k in range(l-1):
                    zagl = zagl + zagl
            s_new = s_new + zagl[i]
        else:
            i = stroch.index(i) + k
            if i >= 27:    
                l = (i - 27) // 27
                if l == 0:
                    l += 1
                for k in range(l-1):
                    stroch = stroch + stroch
            s_new = s_new + stroch[i]
    return s_new

print(kriptografiruy(input(), int(input())))
