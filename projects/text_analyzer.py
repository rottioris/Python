txt = input("Texto: ")
ltrs = []

txt = txt.lower()

ltrs.append(input("ltr1: ").lower())  # 0
ltrs.append(input("ltr2: ").lower())  # 1
ltrs.append(input("ltr3: ").lower())  # 2

print("\n")

cnt_1 = txt.count(ltrs[0])
cnt_2 = txt.count(ltrs[1])
cnt_3 = txt.count(ltrs[2])

print(f"Letra {ltrs[0]} rp {cnt_1}")
print(f"Letra {ltrs[1]} rp {cnt_2}")
print(f"Letra {ltrs[2]} rp {cnt_3}")

p = txt.split()
print(f"Palabras: {len(p)}")

print("\n")

l_inicio = txt[0]
l_fin = [-1]
print(f"primera letra: '{l_inicio}' \n letra final: '{l_fin}'")

print("\n")

p.reverse()
txt_rv = " ".join(p)
print(f"Texto invertido: '{txt_rv}'")

print("\n")

src_py = "python" in txt
dic = {True: "si", False: "no"}
print(f"Python {dic[src_py]} se encuentra")
