"""Models page — Purity UI style for model training."""
from dash import html, dcc
from app.components.card import Card, CardBody, CardHeader


def create_models_layout():
    return html.Div([
        Card([
            CardHeader(html.H5("Model Training", style={"color": "var(--pu-text)"})),
            html.Div([
                html.Div([
                    html.Label("Target Column", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                    dcc.Dropdown(id="model-target-col", placeholder="Select target..."),
                ], style={"flex": "1", "marginRight": "16px"}),
                html.Div([
                    html.Label("Task Type", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                    dcc.Dropdown(id="model-task-type", options=[
                        {"label": "Auto-detect", "value": "auto"},
                        {"label": "Classification", "value": "classification"},
                        {"label": "Regression", "value": "regression"},
                    ], value="auto"),
                ], style={"flex": "1", "marginRight": "16px"}),
                html.Div([
                    html.Label("Test Size", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                    dcc.Slider(id="model-test-size", min=0.1, max=0.5, step=0.05, value=0.2, marks={0.1: "0.1", 0.3: "0.3", 0.5: "0.5"}),
                ], style={"flex": "1"}),
            ], style={"display": "flex", "marginBottom": "24px"}),
            html.Button([html.I(className="bi bi-play-fill", style={"marginRight": "8px"}), "Train Model"], id="train-model-btn", className="pu-btn pu-btn-primary"),
        ], style={"padding": "28px", "marginBottom": "24px"}),
        dcc.Loading(id="model-training-loading", type="dot", children=html.Div(id="model-training-status")),
        html.Div(id="model-metrics-table", style={"marginBottom": "24px"}),
        html.Div([
            dcc.Graph(id="model-confusion-matrix", config={"displayModeBar": False}),
            dcc.Graph(id="model-roc-curve", config={"displayModeBar": False}),
        ], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "24px", "marginBottom": "24px"}),
        dcc.Graph(id="model-feature-importance", config={"displayModeBar": False}),
    ], style={"paddingTop": "120px"})
