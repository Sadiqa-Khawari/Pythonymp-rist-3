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

