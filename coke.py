amount_due=50
while amount_due>0:
  print("amount_due:",amount_due)
  coin=int(input("insert coin: "))
  if coin ==25 or coin == 10 or coin==5:
    aamount_duemount_due=amount_due-coin
print("change owed:",abs(amount_due))
