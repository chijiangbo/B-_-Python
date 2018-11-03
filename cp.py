def cpt_cp(ma):
    """计算不同马赫数Ma下对应的cp*"""
    cp = ( ((1.0/1.2)**(1.4/0.4)) * ((1+0.2*ma*ma)**(1.4/0.4)) - 1 ) * (2/1.4) * (1/(ma**2))
    return cp
ma = float(input('请输入要计算Cp*的马赫数 Ma = '))
print('Cp* = ' + str(cpt_cp(ma)))