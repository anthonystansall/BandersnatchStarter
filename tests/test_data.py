"""Module to test methods of the Database class in data.py."""


def test_seed(mock_db):
    """Tests the seed method of the Database class."""
    mock_db.seed(5)
    assert mock_db.count() == 5


def test_reset(mock_db):
    """Tests the reset method of the Database class."""
    mock_db.seed(5)
    assert mock_db.count() == 5
    mock_db.reset()
    assert mock_db.count() == 0


def test_count(mock_db):
    """Tests the count method of the Database class."""
    mock_db.seed(3)
    assert mock_db.count() == 3


def test_dataframe(mock_db):
    """Tests the dataframe method of the Database class."""
    mock_db.seed(1)
    df = mock_db.dataframe()
    assert df is not None
    assert len(df) == 1


def test_html_table(mock_db):
    """Tests the html_table method of the Database class."""
    mock_db.seed(1)
    html_table = mock_db.html_table()
    assert html_table is not None
    assert "<table" in html_table
