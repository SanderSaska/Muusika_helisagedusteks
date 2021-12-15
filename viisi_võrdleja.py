from crepe.core import process_file
import os
from pathlib import Path

print('Enne programmi kasutamist on sul vaja alla laadida teek Crepe: https://pypi.org/project/crepe/')

while True:
    print('Kas soovite uurida pala? (1)')
    print('Kas soovite koostada graafikut? (2)')
    print('Välju (3)')
    valik = input('Mida soovite teha (1,2,3)?: ')

    if valik == '1': # Uurib muusikapala

        fail = input('Sisesta faili nimi ("_____.wav" tüüpi), mida tahad uurida: ')
        faili_asukoht = input('Sisestage faili asukoht (nt. C:\\Users\\...\\Desktop või lihtsalt C:\\): ')
        kaust = input('Sisesta kausta nimi, kuhu andmed salvestatakse (kui ei soovi, vajuta Enter): ')
        täpsus = int(input('Kui täpselt soovite saada tulemust (mitme ns tagant uuritakse helisagedust: ')) 

        faili_asukoht = faili_asukoht.replace('\\','/')

        # Otsib faili asukoha
        try:
            for root, dirs, files in os.walk(faili_asukoht):
                for name in files:
                    if name == fail:
                        faili_sihtkoht = str(os.path.abspath(os.path.join(root, name)))
                        print('Fail leitud')
        except:
            print('Faili asukoht ei ole õigesti kirjutatud')


        try:
            if faili_sihtkoht != None and täpsus > 0 and kaust == '': # Kui uut kausta ei loodud
                process_file(faili_sihtkoht, output=None, model_capacity='full', viterbi=True, center=True, save_activation=True, save_plot=True, plot_voicing=False, step_size=täpsus, verbose=True)
                print('Tulemused salvestatud')
            elif faili_sihtkoht != None and täpsus > 0: # Kui loodi uus kaust
                sihtkoht = str(os.path.join(faili_sihtkoht.strip(fail), kaust))
                Path(sihtkoht).mkdir(parents=True, exist_ok=True)
                process_file(faili_sihtkoht, output=sihtkoht, model_capacity='full', viterbi=True, center=True, save_activation=True, save_plot=True, plot_voicing=False, step_size=täpsus, verbose=True)
                print('Tulemused salvestatud faili ' + kaust)
            elif faili_sihtkoht != None and täpsus <= 0: # Kui täpsus on negatiivne
                print('Ei saanud salvestada, täpsus oli antud negatiivsena')
        except:
            print('Faili ei leidu antud aadressil')
        
        continue
    
    elif valik == '2': # Koostab matplotlib'iga graafiku
        continue
    
    else:
        break



# # if the exe just in current dir
# faili_sihtkoht = str(os.path.abspath(fail))