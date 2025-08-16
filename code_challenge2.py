money = int(input("Enter amount you want to deposit: "))
bluebill = money // 1000
print("This is the breakdown of the amount you deposited:")
print("1000: ", bluebill)
money = money - (bluebill * 1000)

yellowbill = money // 500
print("500: ", yellowbill)
money = money - (yellowbill * 500)

greenbill = money // 200
print("200: ", greenbill)
money = money - (greenbill * 200)

purplebill = money // 100
print("100: ", purplebill)
money = money- (purplebill * 100)

redbill = money // 50
print("50: ", redbill)
money = money- (redbill * 50)

coin20 = money // 20
print("20: ", coin20)
money = money - (coin20 * 20)

coin5 = money // 5
print("5: ", coin5)
money = money0 - (coin5 * 5)

print("Remaining coins: ", deposit)
