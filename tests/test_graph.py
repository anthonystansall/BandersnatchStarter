"""Module to test chart and customizations in graph.py"""
from altair import Chart

from app import graph


def test_chart(mock_db):
    """Tests if chart is being produced."""
    mock_db.seed(5)
    df = mock_db.dataframe()
    scatter = graph.chart(df, 'Level', 'Health', 'Rarity')
    assert isinstance(scatter, Chart)


def test_dark_theme():
    """Test dark theme for any unexpected changes."""
    expected_theme = {
        "config": {
            "background": "#333333",
            "title": {"color": "#ffffff"},
            "axis": {
                "domainColor": "#ffffff",
                "gridColor": "#444444",
                "tickColor": "#ffffff",
                "labelColor": "#ffffff",
                "titleColor": "#ffffff"
            },
            "legend": {
                "labelColor": "#ffffff",
                "titleColor": "#ffffff"
            },
            "view": {"stroke": "transparent"},
        }
    }
    actual_theme = graph.dark_theme()
    assert actual_theme == expected_theme
