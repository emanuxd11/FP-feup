topay = int(input())
received = int(input())

fifty = int((received - topay) / 50)
twenty = int((received - topay + fifty * 50) / 20)
ten = int((received - topay + fifty * 50 + twenty * 20) / 10)
five = int((received - topay + fifty * 50 + twenty * 20 + ten * 10) / 5)

print(f"{fifty} {twenty} {ten} {five}")