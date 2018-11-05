'''
Animal sale brainteaser:
The cost of a bull is $10, the cost of a cow is $2.50,
and the cost of a calf is $0.50. The person has $100
and wants to buy 100 animals; how will he do that?
November 5, 2018'''

bull = 10
cow = 2.5
calf = .5

TOTAL = 100

combos = []

for b in range(11):
    for co in range(41):
        for ca in range(201):
            cost = b*bull + co*cow + ca*calf
            num = b + co + ca
            thisList = [b,co,ca]
            if cost == TOTAL:
                if num == 100:
                    print(num, thisList,cost)

'''My results were
100 [0, 25, 75] 100.0
100 [4, 6, 90] 100.0
But if there have to be at least one of each type of animal
the answer is 4 bulls, 6 cows and 90 calfs.
'''
