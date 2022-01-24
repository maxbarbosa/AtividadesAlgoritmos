pais_X = 70000
pais_Y = 180000
i = 0
while (not(pais_X >= pais_Y)):
    pais_X *= 1.035 #pais_X = pais_X + pais_X * 0.035
    pais_Y *= 1.015 #pais_Y = pais_Y + pais_Y * 0.015

    i+=1
print("São necessários %d anos para que a população do país X ultrapasse ou se iguale a população do país Y." %(i))