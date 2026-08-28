import random

sirli_raqam = random.randint(1, 10)
taxmin = int(input("1 dan 10 gacha son o'yladim, toping: "))

if taxmin == sirli_raqam:
    print("Tabriklayman, topdingiz!")
else:
    print(f"Topolmadingiz, sirli raqam {sirli_raqam} edi.")
