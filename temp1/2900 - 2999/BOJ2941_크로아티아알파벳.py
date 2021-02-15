croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for ca in croatian_alphabet:
    word = word.replace(ca, "0")

print(len(word))
