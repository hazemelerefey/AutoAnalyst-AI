"""Chart factory functions with Purity UI styling."""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Purity UI color palette
PURITY_COLORS = ["#38B2AC", "#319795", "#2C7A7B", "#48BB78", "#F56565",
                 "#ECC94B", "#9F7AEA", "#ED64A6", "#4299E1", "#FC8181"]

PURITY_TEMPLATE = "plotly_dark"


def _apply_purity_layout(fig, title="", height=350):
    """Apply Purity UI styling to a Plotly figure."""
    fig.update_layout(
        template=PURITY_TEMPLATE,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Roboto, sans-serif", color="#A0AEC0"),
        title=dict(text=title, font=dict(size=18, color="white", family="Roboto"), x=0.05) if title else None,
        margin=dict(l=24, r=24, t=40, b=24),
        height=height,
        hoverlabel=dict(bgcolor="#1F2733", font_color="white", font_family="Roboto"),
        xaxis=dict(gridcolor="rgba(160,174,192,0.15)", zerolinecolor="rgba(160,174,192,0.15)"),
        yaxis=dict(gridcolor="rgba(160,174,192,0.15)", zerolinecolor="rgba(160,174,192,0.15)"),
    )
    fig.update_traces(marker_color="#38B2AC")
    return fig


def line_chart(x, y, title="", color="#38B2AC"):
    """Create a Purity UI line chart (matches SalesOverview)."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="lines+markers",
        line=dict(color=color, width=3, shape="spline"),
        marker=dict(size=6, color=color),
        fill="tozeroy",
        fillcolor="rgba(56, 178, 172, 0.1)",
    ))
    return _apply_purity_layout(fig, title)


def bar_chart(x, y, title="", colors=None):
    """Create a Purity UI bar chart (matches ActiveUsers)."""
    fig = go.Figure()
    if colors is None:
        colors = PURITY_COLORS
    for i, (xi, yi) in enumerate(zip(x, y)):
        fig.add_trace(go.Bar(
            x=[xi], y=[yi],
            marker_color=colors[i % len(colors)],
            marker_line_width=0,
            hoverinfo="x+y",
        ))
    fig.update_layout(barmode="group", showlegend=False)
    return _apply_purity_layout(fig, title)


def gradient_bar_chart(categories, series_data, series_names=None, title=""):
    """Create a gradient bar chart matching Purity UI's ActiveUsers style."""
    fig = go.Figure()
    for i, series in enumerate(series_data):
        name = series_names[i] if series_names else f"Series {i+1}"
        fig.add_trace(go.Bar(
            x=categories, y=series,
            name=name,
            marker_color=PURITY_COLORS[i % len(PURITY_COLORS)],
            marker_line_width=0,
        ))
    fig.update_layout(
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                    font=dict(color="#A0AEC0")),
    )
    return _apply_purity_layout(fig, title)


def donut_chart(labels, values, title=""):
    """Create a donut chart matching Purity UI style."""
    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values,
        hole=0.5,
        marker=dict(colors=PURITY_COLORS[:len(labels)]),
        textfont=dict(size=12, color="white"),
        hovertemplate="<b>%{label}</b><br>%{value}<br>%{percent}<extra></extra>",
    )])
    return _apply_purity_layout(fig, title)
