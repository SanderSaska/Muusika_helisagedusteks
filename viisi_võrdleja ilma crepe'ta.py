from crepe.core import process_file
import os
from pathlib import Path
import matplotlib.pyplot as plt

print('Enne programmi kasutamist on sul vaja alla laadida teek Crepe: https://pypi.org/project/crepe/')

################# def Funktsioonid

def otsi_asukohta(failinimi, faili_asukoht): # Otsib faili asukoha https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/
    try:
        for root, dirs, files in os.walk(faili_asukoht):
            for name in files:
                if name == failinimi:
                    faili_sihtkoht = str(os.path.abspath(os.path.join(root, name)))
                    print('Fail leitud')
                    return faili_sihtkoht
    except:
        print('Faili asukoht ei ole õigesti kirjutatud')

def loe_andmeid(failinimi): # Loe failist vajalikud andmed 
    f = open(failinimi, 'r', encoding='utf-8')
    aeg = []
    helisagedus = []
    f.readline() # Jätab päise vahele
    for rida in f:
        rida = rida.split(',')
        aeg.append(float(rida[0]))
        helisagedus.append(float(rida[1]))
    f.close()
    return aeg, helisagedus

################# Põhiprogramm

while True:
    print('Kas soovite uurida pala? (1)')
    print('Kas soovite koostada graafikut? (2)')
    print('Välju (3)')
    valik = input('Mida soovite teha (1,2,3)?: ')

    # if valik == '1': # Uurib muusikapala

    #     fail_1 = input('Sisesta faili nimi ("_____.wav" tüüpi), mida tahad uurida: ')
    #     faili_asukoht_1 = input('Sisesta faili asukoht (nt. C:\\Users\\...\\Desktop või lihtsalt C:\\): ')
    #     kaust_1 = input('Sisesta kausta nimi, kuhu andmed salvestatakse (kui ei soovi, vajuta Enter): ')
    #     täpsus = int(input('Kui täpselt soovite saada tulemust (mitme ns tagant uuritakse helisagedust): ')) 

    #     faili_asukoht_1 = faili_asukoht_1.replace('\\','/')
    #     faili_sihtkoht_1 = otsi_asukohta(fail_1, faili_asukoht_1)

    #     try:
    #         if faili_sihtkoht_1 != None and täpsus > 0 and kaust_1 == '': # Kui uut kausta ei loodud
    #             process_file(faili_sihtkoht_1, output=None, model_capacity='full', viterbi=True, center=True, save_activation=True, save_plot=True, plot_voicing=False, step_size=täpsus, verbose=True) # https://github.com/marl/crepe/blob/master/crepe/core.py
    #             print('Tulemused salvestatud')
    #         elif faili_sihtkoht_1 != None and täpsus > 0: # Kui loodi uus kaust
    #             sihtkoht = str(os.path.join(faili_sihtkoht_1.strip(fail_1), kaust_1))
    #             Path(sihtkoht).mkdir(parents=True, exist_ok=True) # https://www.geeksforgeeks.org/create-a-directory-in-python/
    #             process_file(faili_sihtkoht_1, output=sihtkoht, model_capacity='full', viterbi=True, center=True, save_activation=True, save_plot=True, plot_voicing=False, step_size=täpsus, verbose=True) # https://github.com/marl/crepe/blob/master/crepe/core.py
    #             print('Tulemused salvestatud faili ' + kaust_1)
    #         elif faili_sihtkoht_1 != None and täpsus <= 0: # Kui täpsus on negatiivne
    #             print('Ei saanud salvestada, täpsus oli antud negatiivsena')
    #     except:
    #         print('Faili ei leidu antud aadressil')
    
    if valik == '2': # Koostab matplotlib'iga graafiku
        
        print('Kas soovite luua graafikut(1)') 
        print('Kas soovite võrrelda kahte graafikut(2)')
        print('Välju(3)')
        valikud = input('Mida soovite teha (1,2,3)?: ')
        
        if valikud == '1':
            
            fail_2_1 = input('Sisesta .csv tüüpi faili nimi, millest soovid luua graafikut: ')
            faili_asukoht_2_1 = input('Sisesta faili asukoht (nt. C:\\Users\\...\\Desktop või lihtsalt C:\\): ')

            faili_sihtkoht_2_1 = otsi_asukohta(fail_2_1, faili_asukoht_2_1)

            aeg, helisagedus = loe_andmeid(faili_sihtkoht_2_1)
            
            # Vajalikute andmetega loob graafiku
            plt.plot(aeg, helisagedus, 'r')
            plt.plot()
            plt.axis([0, round(max(aeg)+5, 1), 0, round(max(helisagedus), 1)])
            plt.ylabel('Helisagedused')
            plt.xlabel('Aeg')
            plt.show()

        if valikud == '2':
            
            fail_2_2_1 = input('Sisesta .csv tüüpi faili nimi, millest soovid luua graafikut: ')
            faili_asukoht_2_2_1 = input('Sisesta faili asukoht (nt. C:\\Users\\...\\Desktop või lihtsalt C:\\): ')
            fail_2_2_2 = input('Sisesta .csv tüüpi faili nimi, millest soovid luua graafikut: ')
            faili_asukoht_2_2_2 = input('Sisesta faili asukoht (nt. C:\\Users\\...\\Desktop või lihtsalt C:\\): ')

            faili_sihtkoht_2_2_1 = otsi_asukohta(fail_2_2_1, faili_asukoht_2_2_1)
            faili_sihtkoht_2_2_2 = otsi_asukohta(fail_2_2_2,  faili_asukoht_2_2_2)

            aeg_1, helisagedus_1 = loe_andmeid(faili_sihtkoht_2_2_1)
            aeg_2, helisagedus_2 = loe_andmeid(faili_sihtkoht_2_2_2)

            # Vajalikute andmetega loob graafiku
            plt.plot(aeg_1, helisagedus_1, 'r', aeg_2, helisagedus_2, 'b')
            plt.ylabel('Helisagedused')
            plt.xlabel('Aeg')
            plt.show()

        else:
            continue
        
    else:
        break




# # if the exe just in current dir
# faili_sihtkoht = str(os.path.abspath(fail))