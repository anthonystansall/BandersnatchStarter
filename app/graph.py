"""Module to create visualizations of Monsters collection."""
from altair import Chart, Tooltip


def chart(df, x, y, target) -> Chart:
    """Creates a scatterplot based on parameters.

    Parameters:
        df: DataFrame of data to display.
        x: String name of feature to display on x-axis.
        y: String name of feature to display on y-axis.
        target: String name of feature to color code the points by.
    """
    title = f"{y} by {x} for {target}"

    scatter = Chart(df).mark_circle().encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=600,
        height=400,
        title=title,
        padding=20
    )
    return scatter


def dark_theme():
    """Returns the style customizations for Altair chart."""
    return {
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
