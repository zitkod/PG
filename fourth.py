def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    r1, s1 = pozice
    r2, s2 = cilova_pozice

    if pozice == cilova_pozice:
        return False

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if typ == "věž":
        if r1 != r2 and s1 != s2:
            return False
        
        if r1 == r2:
            start, end = sorted([s1, s2])
            cesta = [(r1, s) for s in range(start + 1, end)]
            for pozice in cesta:
                if pozice in obsazene_pozice:
                    return False
        if s1 == s2:
            start, end = sorted([r1, r2])
            cesta = [(r, s1) for r in range(start + 1, end)]
            for pozice in cesta:
                if pozice in obsazene_pozice:
                    return False
        return True

    if typ == "pěšec":
        if (r2, s2) in obsazene_pozice:
            return False
        if s1 != s2:
            return False
        if r1 == 2:
            if r2 - r1 == 2 and (r1 + 1, s1) not in obsazene_pozice:
                return True
            elif r2 - r1 == 1 and s1 == s2:
                return True
            else:
                return False
        else:
            if r2 - r1 == 1 and s1 == s2:
                return True
            else:
                return False
            
    if typ == "král":
        if abs(r2 - r1) <= 1 and abs(s2 - s1) <= 1:
            return True
        else:
            return False
        
    if typ == "střelec":
        if abs(r2 - r1) != abs(s2 - s1) or (r2, s2) == (r1, s1):
            return False
        kr = 1 if r2 > r1 else -1
        ks = 1 if s2 > s1 else -1

        cesta = [(r1 + i * kr, s1 + i * ks) for i in range(1, abs(r2 - r1))]

        for pozice in cesta:
            if pozice in obsazene_pozice:
                return False
        if (r2, s2) in obsazene_pozice:
            return False
        else: 
            return True
        
    if typ == "dáma":
        if r2 != r1 and s2 != s1:
            if abs(r2 - r1) != abs(s2 - s1) or (r2, s2) == (r1, s1):
                return False
            kr = 1 if r2 > r1 else -1
            ks = 1 if s2 > s1 else -1

            cesta = [(r1 + i * kr, s1 + i * ks) for i in range(1, abs(r2 - r1))]

            for pozice in cesta:
                if pozice in obsazene_pozice:
                    return False
            if (r2, s2) in obsazene_pozice:
                return False
            else: 
                return True
        if r2 == r1 or s2 == s1:
            if r1 != r2 and s1 != s2:
                return False
        
            if r1 == r2:
                start, end = sorted([s1, s2])
                cesta = [(r1, s) for s in range(start + 1, end)]
                for pozice in cesta:
                    if pozice in obsazene_pozice:
                        return False
            if s1 == s2:
                start, end = sorted([r1, r2])
                cesta = [(r, s1) for r in range(start + 1, end)]
                for pozice in cesta:
                    if pozice in obsazene_pozice:
                        return False
            return True
    if typ == "jezdec":
        if (r2, s2) in obsazene_pozice:
            return False
        if abs(r2 - r1) == 2 and abs(s2 - s1) == 1:
            return True
        if abs(r2 - r1) == 1 and abs(s2 - s1) == 2:
            return True
        return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
