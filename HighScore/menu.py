import prgm
import couleur
import aide

menuBar=prgm.Menu(prgm.root)

menu_preference=prgm.Menu(menuBar,tearoff=0)
menu_aide=prgm.Menu(menuBar,tearoff=0)

menu_preference.add_command(label='Couleur des cases',command=couleur.main)
menu_preference.add_checkbutton(label='Couleur des diagonales',command=lambda:couleur.main(True))
menuBar.add_cascade(label='Pr\u00E9f\u00E9rences',menu=menu_preference)

menu_aide.add_command(label='Liste des combinaisons',command=aide.main)
menuBar.add_cascade(label='Aide',menu=menu_aide)

prgm.root.config(menu=menuBar)
