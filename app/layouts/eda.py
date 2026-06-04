"""EDA page — Purity UI style for exploratory data analysis."""
from dash import html, dcc
from app.components.card import Card, CardBody, CardHeader


def create_eda_layout():
    return html.Div([
        html.Div([
            Card([
                CardHeader(html.H5("Column Selection", style={"color": "var(--pu-text)"})),
                html.Label("Select Columns", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                dcc.Dropdown(id="eda-columns", multi=True, placeholder="Select numeric columns...", style={"marginBottom": "16px"}),
                html.Label("Color By", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                dcc.Dropdown(id="eda-color-col", placeholder="Color by category..."),
            ], style={"padding": "28px", "marginBottom": "24px"}),
            Card([
                CardHeader(html.H5("Distribution", style={"color": "var(--pu-text)"})),
                dcc.Loading(dcc.Graph(id="eda-distribution-chart", config={"displayModeBar": False}), type="dot"),
            ], style={"padding": "28px", "marginBottom": "24px"}),
            Card([
                CardHeader(html.H5("Outlier Detection", style={"color": "var(--pu-text)"})),
                dcc.Loading(dcc.Graph(id="eda-boxplot-chart", config={"displayModeBar": False}), type="dot"),
            ], style={"padding": "28px"}),
        ], style={"flex": "1"}),
        html.Div([
            Card([
                CardHeader(html.H5("Correlation Matrix", style={"color": "var(--pu-text)"})),
                dcc.Loading(dcc.Graph(id="eda-correlation-chart", config={"displayModeBar": False}), type="dot"),
            ], style={"padding": "28px", "marginBottom": "24px"}),
            Card([
                CardHeader(html.H5("Scatter Matrix", style={"color": "var(--pu-text)"})),
                dcc.Loading(dcc.Graph(id="eda-scatter-chart", config={"displayModeBar": False}), type="dot"),
            ], style={"padding": "28px"}),
        ], style={"flex": "1"}),
    ], style={"display": "flex", "gap": "24px", "paddingTop": "120px"})
