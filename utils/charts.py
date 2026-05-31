import pandas as pd
import plotly.express as px


def category_chart(df):

    if len(df) == 0:
        return None

    fig = px.pie(
        df,
        names="category",
        title="Complaints by Category"
    )

    return fig


def priority_chart(df):

    if len(df) == 0:
        return None

    counts = (
        df["priority"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "priority",
        "count"
    ]

    fig = px.bar(
        counts,
        x="priority",
        y="count",
        title="Priority Distribution"
    )

    return fig


def status_chart(df):

    if len(df) == 0:
        return None

    counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "status",
        "count"
    ]

    fig = px.bar(
        counts,
        x="status",
        y="count",
        title="Complaint Status"
    )

    return fig