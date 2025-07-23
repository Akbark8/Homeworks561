from distance import Distance

d1 = Distance(150, 'см')
d2 = Distance(1, 'м')
d3 = Distance(2, 'м')

print("Объект d1:", d1)
print("Объект d2:", d2)

print("Сумма d1 + d2:", d1 + d2)

print("Разность d3 - d1:", d3 - d1)

print("d1 == d2:", d1 == d2)
print("d1 < d3:", d1 < d3)
print("d3 <= d3:", d3 <= d3)
