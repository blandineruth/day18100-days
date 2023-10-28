
# J'ai ecrit un programme qui permet de determiner le nombre exact que vous avez entrer.

print("Bienvenue au jeu de nombre")
print()
print("devine un nombre compris entre 1 et 10000 et je vous dirai si vous avez trop bas ou trop haut")
print("vous êtes prêts ?")

nombre_correct = 350
nombre_essais =  1

while True:
  nombre_utilisateur = int(input(" choisissez un nombre compris entre 1 et 10000 : "))
  print()
  if nombre_utilisateur < 0:
    print("nous ne connaissons pas le nombre...")
    exit()
  if nombre_utilisateur < nombre_correct:
    print(" votre nombre est très bas! reprenez le jeu ")
    print()
    nombre_essais =+ 1
  elif nombre_utilisateur > nombre_correct:
    print(" votre nombre est très haut! Reprenez le jeu svp! ")
    nombre_essais =+ 1
  elif nombre_utilisateur == nombre_correct:
     print("votre nombre est juste! felicitations à  l'africaine :  whoouuuuuuuuuu")
     break
  else:
    print("ce n'est pas un nombre reconnu")
  