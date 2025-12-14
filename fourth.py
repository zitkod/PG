def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.
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
            for s in range(start + 1, end):
                if (r1, s) in obsazene_pozice:
                    return False

        if s1 == s2:
            start, end = sorted([r1, r2])
            for r in range(start + 1, end):
                if (r, s1) in obsazene_pozice:
                    return False

        if (r2, s2) in obsazene_pozice:
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
            elif r2 - r1 == 1:
                return True
            else:
                return False
        else:
            return r2 - r1 == 1

    if typ == "král":
        if (r2, s2) in obsazene_pozice:
            return False
        return abs(r2 - r1) <= 1 and abs(s2 - s1) <= 1

    if typ == "střelec":
        if abs(r2 - r1) != abs(s2 - s1):
            return False

        kr = 1 if r2 > r1 else -1
        ks = 1 if s2 > s1 else -1

        for i in range(1, abs(r2 - r1)):
            if (r1 + i * kr, s1 + i * ks) in obsazene_pozice:
                return False

        if (r2, s2) in obsazene_pozice:
            return False

        return True

    if typ == "dáma":
        if r1 == r2 or s1 == s2:
            if r1 == r2:
                start, end = sorted([s1, s2])
                for s in range(start + 1, end):
                    if (r1, s) in obsazene_pozice:
                        return False
            if s1 == s2:
                start, end = sorted([r1, r2])
                for r in range(start + 1, end):
                    if (r, s1) in obsazene_pozice:
                        return False

            if (r2, s2) in obsazene_pozice:
                return False

            return True

        if abs(r2 - r1) == abs(s2 - s1):
            kr = 1 if r2 > r1 else -1
            ks = 1 if s2 > s1 else -1

            for i in range(1, abs(r2 - r1)):
                if (r1 + i * kr, s1 + i * ks) in obsazene_pozice:
                    return False

            if (r2, s2) in obsazene_pozice:
                return False

            return True

        return False

    if typ == "jezdec":
        if (r2, s2) in obsazene_pozice:
            return False
        return (
            (abs(r2 - r1) == 2 and abs(s2 - s1) == 1) or
            (abs(r2 - r1) == 1 and abs(s2 - s1) == 2)
        )
