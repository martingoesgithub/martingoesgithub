weight = float(input("Bitte geben Sie ihr Gewicht in [kg] an:"))
height = float(input("Bitte geben Sie ihre Körpergröße in [cm] an:"))/100
bmi = weight/(height**2)
minNormalgewicht = 18.5
minUebergewicht = 25
minAdipositas1 = 30
minAdipositas2 = 35
minAdipositas3 = 40


if bmi < minNormalgewicht:
    bmikategorie = "Untergewicht"
elif bmi >= minNormalgewicht and bmi < minUebergewicht:
    bmikategorie = "Normalgewicht"
elif bmi >= minUebergewicht and bmi < minAdipositas1:
    bmikategorie = "Übergewicht"
elif bmi >= minAdipositas1 and bmi < minAdipositas2:
    bmikategorie = "Adipositas Grad I"
elif bmi >= minAdipositas2 and bmi < minAdipositas3:
    bmikategorie = "Adipositas Grad II"
elif bmi >= minAdipositas3:
    bmikategorie = "Adipositas Grad III"

print("Ihr BMI beträgt: " + str(bmi))
print("Dies entspricht: " + bmikategorie)

