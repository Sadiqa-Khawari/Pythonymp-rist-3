# TESTATAAN MODUULIN identityCheck2.py LUOKKIEN TOIMINTAA

import identityCheck2
import pytest

# Testeissä käytettävät henkilötunnukset
testSsnOk = identityCheck2.NationalSSN("130728-478N")
testSsnShort = identityCheck2.NationalSSN("130728-78N")
testSsnLong = identityCheck2.NationalSSN("1300728-478N")
testSsnWrongDay = identityCheck2.NationalSSN("120728-478N")
testSsnWorngMonth = identityCheck2.NationalSSN("130628-478N")
testSsnWrongYear = identityCheck2.NationalSSN("130722-478N")
testSsnWrongCentury = identityCheck2.NationalSSN("130728x478N")
testSsnWrongNumber = identityCheck2.NationalSSN("130728-477N")
testSsnWrongCheckSum = identityCheck2.NationalSSN("130728-478A")
testSsnWrongCenturySymbol = identityCheck2.NationalSSN("130728x478N")

# Testitapauukset palautusarvojen ja ominaisuuksien päivittykisen testaamiseen
# ----------------------------------------------------------------------------

#Testitapaus 1: Hetun pituus on oikein -> True
def test_checkSsnLengthOk():
    assert testSsnOk.checkSsnLengthOk() == True
    
# Testitapaus 2: Henkilötunnuksen vartussumma on oikein
def test_isValidSSN():
    assert testSsnOk.isValidSsn() == True
   
# Testitapaus 3: Henkilötunnuksen syntymäaika väärin -> False
def test_birthdayWrong():
    assert testSsnWrongDay.isValidSsn() == False
    assert testSsnWorngMonth.isValidSsn() == False
    assert testSsnWrongYear.isValidSsn() == False

# Testitapaus 4: Vuosisatamerkki väärin -> True (vuosisataa ei tarkisteta moduli 31)
def test_centuryWorng():
    assert testSsnWrongCentury.isValidSsn() == True

# Testitaupaus 5: Iän laskenta, huom korjattava vuosittain testin tulos
def test_age():
    assert testSsnOk.calculateAge() == 96

# Testitapaus 6: Sukupuolen selvittämien
def test_genter():
    testSsnOk.getGender()
    assert testSsnOk.gender == "Nainen"

# Virhetilannetestit
# ------------------

# Testitapaus 7: Liian lyhyen HeTu:n virheilmoitus, huom
def test_tooShortError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnShort.checkSsnLengthOk()
    assert str(exeptionMessage.value) == "Henkilötunnukswsta puutu merkkejä"

# Testitapaus 8: Liian pitkä HeTu:n virheilmoitus
def test_tooLongError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnLong.checkSsnLengthOk()
    assert str(exeptionMessage.value) == "Henkilötunnuksessa ylemääräisiä merkkejä"

# Testitapaus 9: Väärän vuosisatamerkin virheilmoitus, muutoin oikea HeTu
def test_SsnWrongCenturySymbolError():
    with pytest.raises(ValueError) as exeptionMessage:
        testSsnWrongCenturySymbol.getDateOfBirth()
    assert str(exeptionMessage.value) == "Vuosisatamerkki virheellinen"
