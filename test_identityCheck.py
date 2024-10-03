# Yksikkötestit moduulille indentityCheck.py

import identityCheck

def test_opeskelijanumeroOk_4():
    assert identityCheck.opeskelijanumeroOk("1234") == True

def test_opeskelijanumeroOk_6():
    assert identityCheck.opeskelijanumeroOk("123456") == True
    
def test_opeskelijanumeroOk_8():
    assert identityCheck.opeskelijanumeroOk("12345678") == True

def test_opeskelijanumeroOk_7():
    assert identityCheck.opeskelijanumeroOk("1234567") == True

def test_opeskelijanumeroOk_5():
    assert identityCheck.opeskelijanumeroOk("12345") == False


















def test_checkHeTuOk():
    assert identityCheck.checkHeTu("130728-478N") == (0, "OK")

def test_checkHeTuShort():
    assert identityCheck.checkHeTu("13028-478N") == (1, "Henkilötunnus liian lyhyt")

# Henkilötunnuksessa pitää olla 11 merkiä, merkijä on liika
def test_checkHeTuLong():
    assert identityCheck.checkHeTu("1307288-478N") == (2, "Henkilötunnus liian piykä")

# Henkilötunnuksen päiväosassa saa olla 01 - 31
def test_checkHeTuDays():
    assert identityCheck.checkHeTu("450728-478N") == (3, "Päivä viheellinen")

# Henkilötunnuksenkuukausiosassa saa olla 01 - 12
def test_checkHeTuMonths():
    assert identityCheck.checkHeTu("132728-478N") == (4, "Kuukausi virheellinen")

# Henkilötunnuksen vuosiossa saa olla 00 -99
def test_checkHeTuYears():
    assert identityCheck.checkHeTu("13072x-478N") == (5, "Vuosi virheellinen")

# Käytössaä olevat vuosisakoodit + (1800), - (1900) ja (2000)
def test_checkHeTuCenturyCode():
    assert identityCheck.checkHeTu("130728s478N") == (5, "Vuosisatakoodi virheellinen")

# Henkilötunnuksen numeroista tehdään luku. esim 130728478 ja jaetaan se luvulla
# 31. Jkojäännös on tarkiste. Jos se on alle 10, käytetään numeroa, jos yli haetaan taulukosta vastaava kirainmrkki
# 10 -> A, 11 -> B. G ja I eivät ole käyt
def test_checkHeTuModulo():
    assert identityCheck.checkHeTu("130728-478M")
