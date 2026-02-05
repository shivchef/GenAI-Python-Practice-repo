def add_vat(price, vat_rate):
    return price *(100 + vat_rate)/100

order = [192,32,3312]

for price in order:
    final_amount = add_vat(price, 10)
    print(f"Original: {price},final with VAT :{final_amount}")