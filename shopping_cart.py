foods = []
price = []


while True:
    food = input("Masukkan nama makanan: ")
    if food.lower() == "q":
        break
    else:
        foods.append(str(food))
        price.append(float(input("Masukkan harga makanan: Rp")))

for i in range(len(foods)):
    print(f"{i+1}. {foods[i]}: Rp{price[i]}")
    
total_price = sum(price)

member = input("Apakah anda member? (y/n): ")
if member.lower() == "y":
    print("Selamat anda mendapatkan diskon 10%")
    total_price = total_price - (total_price * 0.1)
    print("Rp ",total_price)
else:
    print("Rp ",total_price)
