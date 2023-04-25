# from challenges.challenge_encrypt_message import encrypt_message
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="test", key="")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=1, key=3)

    assert encrypt_message(message="message test", key=22) == "tset egassem"
    assert encrypt_message(message="message test", key=3) == "sem_tset egas"
    assert encrypt_message(message="message test", key=4) == "tset ega_ssem"
