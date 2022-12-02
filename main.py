# Hii ni kwa ajili ya caesar cipher any key in range

print("KARIBU KWENYE CIPHER CAESAR (2-8 value)CHAGUA ")
print("Chagua \n1.KUFICHA NENO\n2.KUFICHUA NENO\n3.KUJITOA")
chaguo = int(input("Andika Namba ya Uchaguzi wako"))

if chaguo == 1:
    siri = input("Ingiza ujumbe wako ufiche siri\n")
    ufunguo = int(input("Ingiza namba ya ufunguo"))


    def tufunge_siri_yetu(maneno_yetu, funguo_zetu):
        siri_yetu = ""
        for herufi_moja in maneno_yetu:
            if herufi_moja.isalpha():
                herufi_moja_kwenye_ascii = ord(herufi_moja) + funguo_zetu
                if herufi_moja_kwenye_ascii > ord('z'):
                    herufi_moja_kwenye_ascii = -26
                herufi_moja_kwenye_letter_tena = chr(herufi_moja_kwenye_ascii)
            siri_yetu += herufi_moja_kwenye_letter_tena

        return print("\nNeno lake:" + maneno_yetu + "\nFumbo lake:" + siri_yetu.upper())


    tufunge_siri_yetu(siri, ufunguo)
elif chaguo == 2:
    siri = input("Ingiza siri wako ufichue neno\n")
    ufunguo = int(input("Ingiza namba ya ufunguo"))


    # I just reverserd the code as the logic formula says..cheers Erick Wilfred
    def tufunge_siri_yetu(maneno_yetu, funguo_zetu):
        siri_yetu = ""
        for herufi_moja in maneno_yetu:
            if herufi_moja.isalpha():
                herufi_moja_kwenye_ascii = ord(herufi_moja) - funguo_zetu
                if herufi_moja_kwenye_ascii > ord('z'):
                    herufi_moja_kwenye_ascii = +26
                herufi_moja_kwenye_letter_tena = chr(herufi_moja_kwenye_ascii)
            siri_yetu += herufi_moja_kwenye_letter_tena

        return print("\nFumbo lako:" + maneno_yetu + "\nNeno lake:" + siri_yetu.casefold())


    tufunge_siri_yetu(siri, ufunguo)

elif chaguo == 3:
    print("Karibu Tena")
    exit()
else:
    print("UMEFANYA UCHAGUZI USIO SAHIHI")
    print("Karibu Tena")
    exit()
