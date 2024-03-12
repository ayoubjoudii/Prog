def Valeur(pas):
    x_max = 0
    v_max = 0
    x_values = [i * pas for i in range(int(10/pas) + 1)]
    for x in x_values:
        v = x * (10 - 2*x)**2
        if v > v_max:
            v_max = v
            x_max = x
    return x_max

pas_values = [10**(-i) for i in range(1, 6)]
for pas in pas_values:
    x_result = Valeur(pas)
    volume_result = x_result * (10 - 2*x_result)**2
    print(f"Pour pas = {pas}, valeur de x = {x_result}, volume = {volume_result}")
#bruhhhhhhh