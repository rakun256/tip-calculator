landing_message = "\nBienvenue dans le calculateur de pourboire.\n"
total_bill_message = "Quelle était la facture totale? £"
how_much_tip_message = "\nQuel pourboire souhaiteriez-vous donner? %"
how_many_people_message = "\nCombien de personnes pour partager l'addition? "
each_person_message = "\nChaque personne devrait payer: £"
jaime = "ECEM \u2764\ufe0f EMRE"

print(landing_message)

total_bill = input(total_bill_message)
tip_percentage = input(how_much_tip_message)
people_count = input(how_many_people_message)

total_bill = float(total_bill)
tip_percentage = float(tip_percentage)/100
people_count = int(people_count)

tip_amount = (total_bill * tip_percentage)
total_payment = (total_bill + tip_amount)

person_payment = (total_payment / people_count)
round(person_payment, 2)

print(each_person_message + str(person_payment)+ "\n")

for i in range(people_count):
    i += 1
    print(f"TEK GERÇEK {jaime}")