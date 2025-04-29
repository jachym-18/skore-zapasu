# Načtení skóre 10 hráčů
skore = []
for i in range(10):
    while True:
        try:
            hodnota = int(input(f"Zadejte skóre hráče {i + 1} (0-60): "))
            if 0 <= hodnota <= 60:
                skore.append(hodnota)
                break
            else:
                print("Zadejte číslo mezi 0 a 60.")
        except ValueError:
            print("Neplatný vstup, zadejte celé číslo.")

# Výpis všech skóre
print("\nSkóre hráčů:", skore)

# Výpočty
prumer = sum(skore) / len(skore)
max_skore = max(skore)
min_skore = min(skore)

print(f"Průměrné skóre: {prumer:.2f}")
print(f"Nejvyšší skóre: {max_skore}")
print(f"Nejnižší skóre: {min_skore}")

# Vyhodnocení výkonu
vysoke_skore = sum(1 for s in skore if s > 50)
if vysoke_skore > 5:
    print("Výborný výkon!")
else:
    print("Můžete to příště zkusit lépe.")
