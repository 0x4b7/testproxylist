s='Аааа Аааа, ну и ещё Ааааа'
r=lambda s:len([a for a in s if a.lower()=='а' or a.lower()=='a'])>5
print(r(s))




