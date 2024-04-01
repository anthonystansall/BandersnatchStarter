"""Module to create visualizations of Monsters collection."""
from altair import Chart


def chart(df, x, y, target) -> Chart:
    """Creates a scatterplot based on parameters.

    Parameters:
        df: DataFrame of data to display.
        x: String name of feature to display on x-axis.
        y: String name of feature to display on y-axis.
        target: String name of feature to color code the points by.
    """
    scatter = Chart(df).mark_circle().encode(
        x=x,
        y=y,
        color=target,
        tooltip=[x, y, target]
    )
    return scatter
