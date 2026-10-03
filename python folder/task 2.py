def clean(i):
    if isinstance(i,list):
        n_list = []
        for x in i:
            cl_x = clean(x)
            if cl_x:
                n_list.append(cl_x)
        return n_list
    elif isinstance(i,dict):
        n_dict = {}
        for y,z in i.items():
            cl_y = clean(y)
            cl_z = clean(z)
            if cl_y and cl_z:
                n_dict[cl_y]=cl_z
        return n_dict
    if not i:
        return None
    return i
s = [{"":123},[],'a','',[[],[1]],[[],[]]]
res = clean(s)
print(res)