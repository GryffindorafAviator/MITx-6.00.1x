# Paste your code into this box
for i in range(1, 13):
    balance = balance * (1 - monthlyPaymentRate) * (1 + annualInterestRate/12.0)
    ans = round(balance, 2)

print(ans)
