from altair import Chart


def chart(df, x, y, target) -> Chart:
    chart = Chart(df).mark_circle().encode(
        x=x,
        y=y,
        color=target
    )
    return chart