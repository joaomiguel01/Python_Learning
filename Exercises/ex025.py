trip = int(input("Digite a distância da viagem: "))
if trip <= 200:
    print(f"Para uma viagem de {trip}km, pague R${trip*0.5:.2f}")
else:
    print(f"Para uma viagem de {trip}km, pague R${trip*0.45:.2f}")
