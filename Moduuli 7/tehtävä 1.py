vuodenajat = ('Talvi','Talvi','Kevät','Kevät','Kevät','Kesä',
              'Kesä','Kesä','Syksy','Syksy','Syksy','Talvi')
kuukausi = int(input('Anna kuukauden numero (1-12): '))
if 1<=kuukausi<=12:
    vuodenaika = vuodenajat[kuukausi-1]
    print(f' {kuukausi}.kuukausi kuuluu vuodenaikaan {vuodenaika}')
else:
    print('Virheellinen syöte...')