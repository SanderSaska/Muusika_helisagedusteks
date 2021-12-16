# Muusika helisagedusteks
Programm, millega saab uurida muusikapala.
## Enne kasutamist
  - :grey_exclamation: Lae alla teek [**Crepe**](https://pypi.org/project/crepe/) ja [**Tensorflow**](https://www.tensorflow.org/install) :grey_exclamation:
  - :grey_exclamation: [**Python**](https://www.python.org/downloads/) :grey_exclamation:
  - :exclamation: Programm töötab ainult **.wav** tüüpi helifailidega :exclamation:
  
## Töö põhimõte
### Helifaili uurimine
Programmiga on võimalik uurida helifaile, mis on **.wav** tüüpi.

Programm küsib järgmiselt:

![Programm küsib järgmiselt:](/pildid/valik_1.png)

Vaja on: 
- sisestada uuritava helifaili nimi;
- sisestada faili asukoht;
- sisestada, kui täpselt uurib programm helifaili.

Soovi korral võib sisestada kausta nime, kuhu andmed salvestatakse.

Programm seejärel uurib sisestatud helifaili ning loob 3 faili nagu [**siin**](/mozart).

### Graafikute koostamine
Programmiga on võimalik luua graafikuid kasutades matplotlib teeki. Võimalik on luua ühte graafikut või võrrelda kahte.
![Näide:](/pildid/Graafik.jpg)

Vaja on topelt: 
- sisestada uuritava helifaili nimi;
- sisestada faili asukoht.

##

Vajalikud selgitused käskudele on toodud kommentaaridena programmis.

Kui programm ei peaks käivituma või ei lase uurida faili:
  - kontrolli, kas vajalikud teegid on installitud.
