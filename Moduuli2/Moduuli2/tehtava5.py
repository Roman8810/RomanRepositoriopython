leiviskä_str = input('Anna leiviskät: ')
naula_str = input('Anna naulat: ')
luoti_str = input('Anna luodit: ')

leiviskä = int(leiviskä_str)
naula = int(naula_str)
luoti = float(luoti_str)

luoti_grammoina = 13.3
naula_luoteina = 32
leiviskä_nauloina = 20

kokonais_luodit = (leiviskä * leiviskä_nauloina * naula_luoteina + naula * naula_luoteina + luoti)
kokonais_grammat = kokonais_luodit * luoti_grammoina
kilot = int(kokonais_grammat // 1000)
grammat = kokonais_grammat % 1000

print(f"Massa on: {kilot} kilogrammaa ja {grammat:.2f} grammaa")
