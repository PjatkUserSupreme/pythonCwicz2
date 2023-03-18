import sys

dict1 = {
    "Q" : "W jakich okolicznościach czytasz książki najczęściej?",
    "A" : "w czasie wolnym (po pracy, na urlopie)",
    "B" : "podczas pracy/nauki (to ich element)",
    "C" : "w ogóle nie czytam"
}
dict2 = {
    "Q" : "Po książki w jakiej formie sięgasz najczęściej? ",
    "A" : "papierowej (tradycyjnej)",
    "B" : "e-booki na specjalnym czytniku (np. Kindle)",
    "C" : "e-booki (książki elektroniczne) na komputerze"
}
dict3 = {
    "Q" : "Po jakie gatunki książek sięgasz najczęściej?",
    "A" : "dla dzieci i młodzieży",
    "B" : "historyczne",
    "C" : "hobbystyczne (gotowanie, wędkarstwo itp.)"
}

print("pytanie: Jak masz na imię oraz nazwisko?")
imie = input()
print(dict1.get("Q"))
print("A - " + dict1.get("A"))
print("B - " + dict1.get("B"))
print("C - " + dict1.get("C"))
q1 = input()
if (q1 != "A") & (q1 != "B") & (q1 != "C"):
    print("Niepoprawna odpowiedz!")
    sys.exit(1)

print(dict2.get("Q"))
print("A - " + dict2.get("A"))
print("B - " + dict2.get("B"))
print("C - " + dict2.get("C"))
q2 = input()
if (q2 != "A") & (q2 != "B") & (q2 != "C"):
    print("Niepoprawna odpowiedz!")
    sys.exit(1)

print(dict3.get("Q"))
print("A - " + dict3.get("A"))
print("B - " + dict3.get("B"))
print("C - " + dict3.get("C"))
q3 = input()
if (q3 != "A") & (q3 != "B") & (q3 != "C"):
    print("Niepoprawna odpowiedz!")
    sys.exit(1)

print("pytanie: Jak masz na imię oraz nazwisko?")
print("odpowiedz: " + imie)

print("pytanie: " + dict1.get("Q"))
print("odpowiedz: " + dict1.get(q1))

print("pytanie: " + dict2.get("Q"))
print("odpowiedz: " + dict2.get(q2))

print("pytanie: " + dict3.get("Q"))
print("odpowiedz: " + dict3.get(q3))
