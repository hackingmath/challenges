def accountBalanceAfterPurchase(purchaseAmount):
    a = 100 - purchaseAmount
    m = a % 10
    if m <= 5:
        return 10 * (a // 10)
    else:
        return 10*((a//10)+1)

print(accountBalanceAfterPurchase(14))