from sympy.stats import given, density, Die

Die6 = Die("Die6", 6)
Die6_dict = density(Die6).dict
print(Die6)
print(Die6_dict)

condi = given(Die6, Die6 > 3)
condi_dict = density(condi).dict
print(condi)
print(condi_dict)