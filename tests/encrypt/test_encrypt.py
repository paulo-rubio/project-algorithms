from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    data = encrypt_message('test amg', 3)
    criptyDataImpar = 'set_gma t'
    assert data == criptyDataImpar

    dataPar = encrypt_message('test amg', 2)
    criptyDataPar = 'gma ts_et'
    assert dataPar == criptyDataPar

    dataZero = encrypt_message('test amg', 0)
    criptyDataZero = 'gma tset'
    assert dataZero == criptyDataZero

    pytest.raises(TypeError, lambda: encrypt_message(0, "test amg"))
