import json

def readJSON():
    with open('COCOMO.json', 'r') as file:
        data = json.load(file)
    return data

def calMOD():
    # 'sehr niedrig', 'niedrig', 'normal', 'hoch', 'sehr hoch', 'extrem hoch'
    rely = 'normal'     # Erforderliche Systemzuverlaessigkeit
    data = 'normal'     # Groeße der verwendeten Datenbank
    cplx = 'normal'     # Komplexitaet des Produktes
    time = 'normal'     # Beschrankung in der Rechenzeit
    stor = 'normal'     # Speicherbeschraenkung
    virt = 'normal'     # Systemaenderungen
    turn = 'normal'     # Computer-Antwortenzeiten
    acap = 'normal'     # Faehigkeit der Problemanalytiker
    aexp = 'normal'     # Analytikererfahrung auf dem Gebiet
    pcap = 'normal'     # Faehigkeit der Programmierer
    vexp = 'normal'     # Erfahrung mit dem System
    ltex = 'normal'     # Erfahrung mit der Sprache
    modp = 'normal'     # moderne Programmierpraktiken
    tool = 'normal'     # SE-Werkzeuge
    sced = 'normal'     # verfuegbare Entwicklungszeit

    mod = 1
    geaendert = []
    mod_list = [const['mod']['rely'][rely], const['mod']['data'][data], const['mod']['cplx'][cplx], const['mod']['time'][time], const['mod']['stor'][stor],
            const['mod']['virt'][virt], const['mod']['turn'][turn], const['mod']['acap'][acap], const['mod']['aexp'][aexp], const['mod']['pcap'][pcap],
            const['mod']['vexp'][vexp], const['mod']['ltex'][ltex], const['mod']['modp'][modp], const['mod']['tool'][tool], const['mod']['sced'][sced]]
    for i in mod_list:
        mod = mod * i
        if i != 1:
            geaendert.append(i)
    return mod, geaendert

if __name__ == '__main__':
    const = readJSON()
    ufp = 2600
    projektkomplexitaet = 'embedded'            # Projektkomplexitaet: 'embedded', 'organic', 'semi-detatched'
    programmiersprache = 'haskell'               # programmiersprache: 'assambler', 'c', 'fortran 95', 'pascal', 'tcl', 'c++', 'java' ,'haskell', 'visual basics 5', 'smalltalk', 'sql'
    kloc = const['loc'][programmiersprache] * (ufp / 1000)
    alpha = const['komplexitaet'][projektkomplexitaet]['alpha']
    beta = const['komplexitaet'][projektkomplexitaet]['beta']
    gamma = const['komplexitaet'][projektkomplexitaet]['gamma']
    
    mod, geaendert = calMOD()

    print(f'Sprache: {programmiersprache}')
    print(f'KLOC = {const["loc"][programmiersprache]} * ({ufp} / 1000) = {const["loc"][programmiersprache]} * {ufp / 1000} = {kloc}')
    pm = int(alpha * kloc ** beta * mod + 1)
    print(f'PM = {alpha} * {kloc} ^ {beta} * {geaendert} = {alpha * kloc ** beta * mod} = {pm}')
    tdev = int(2.5 * pm ** gamma + 1)
    print(f'TDEV = 2.5 * PM ^ gamma = 2.5 * {pm ** gamma} = {2.5 * pm ** gamma} = {tdev} Monate')
    tg = int(pm / tdev + 1)
    print(f'TG = {pm} / {tdev} = {pm / tdev} = {tg}')