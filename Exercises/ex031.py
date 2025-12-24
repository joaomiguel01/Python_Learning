trip = float(input("Digite a distâcia da viagem (km): "))
if trip <= 200:
    print(f"Para uma viagem de {trip}km você gastará R${trip*0.5:.2f}")
else:
    print(f"Para uma viagem de {trip}km você gastará R${trip*0.45:.2f}")
