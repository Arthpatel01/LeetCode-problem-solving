def gcdOfStrings(str1: str, str2: str) -> str:
    import math
    if str1 + str2 != str2 + str1:
        return ""

    gdc_length = math.gcd(len(str1), len(str2)) 
    return str1[:gdc_length]


print(gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))