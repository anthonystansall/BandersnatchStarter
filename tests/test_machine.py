"""Module to test the Machine class in machine.py"""
from Fortuna import random_float, random_int
from pandas import DataFrame


def test_machine(mock_machine):
    """Test machine class initialization."""
    assert mock_machine.name == "Logistic Regression Model"
    assert mock_machine.model is not None


def test_machine_call(mock_machine):
    """Tests if call method produces prediction and confidence."""
    options = ["Level", "Health", "Energy", "Sanity", "Rarity"]
    stats = [round(random_float(1, 250), 2) for _ in range(3)]
    level = random_int(1, 20)
    health = stats.pop()
    energy = stats.pop()
    sanity = stats.pop()
    prediction, confidence = mock_machine(DataFrame(
        [dict(zip(options, (level, health, energy, sanity)))]
    ))
    assert prediction.startswith('Rank')
    assert 0 <= confidence <= 1


def test_machine_info(mock_machine):
    """Tests if info method returns expected values."""
    info = mock_machine.info()
    assert "Logistic Regression Model" in info
    assert "Timestamp" in info
