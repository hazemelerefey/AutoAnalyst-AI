"""Upload page — Purity UI style for data upload."""
from dash import html, dcc
from app.components.card import Card, CardBody, CardHeader


def create_upload_layout():
    return html.Div([
        Card([
            CardHeader(html.H5("Upload Dataset", style={"color": "var(--pu-text)"})),
            html.P("Upload a CSV or Excel file to start your analysis.", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "24px"}),
            dcc.Upload(
                id="upload-data",
                children=html.Div([
                    html.I(className="bi bi-cloud-arrow-up", style={"fontSize": "48px", "color": "var(--pu-accent)", "marginBottom": "16px"}),
                    html.P("Drag and drop or click to select a file", style={"color": "var(--pu-text)", "marginBottom": "4px"}),
                    html.Small("Supports CSV, XLSX, XLS (max 100MB)", style={"color": "var(--pu-text-muted)"}),
                ], style={"textAlign": "center", "padding": "40px"}),
                style={"border": "2px dashed var(--pu-border)", "borderRadius": "15px", "cursor": "pointer", "marginBottom": "24px"},
                multiple=False,
            ),
            html.Div([
                html.Div([
                    html.Label("Target Column", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                    dcc.Dropdown(id="target-column", placeholder="Select target...", style={"marginBottom": "24px"}),
                ], style={"flex": "1", "marginRight": "16px"}),
                html.Div([
                    html.Label("Model Task", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                    dcc.Dropdown(id="model-task", options=[
                        {"label": "Auto-detect", "value": "auto"},
                        {"label": "Classification", "value": "classification"},
                        {"label": "Regression", "value": "regression"},
                    ], value="auto", style={"marginBottom": "24px"}),
                ], style={"flex": "1"}),
            ], style={"display": "flex"}),
            html.Button([html.I(className="bi bi-play-fill", style={"marginRight": "8px"}), "Run Analysis Pipeline"], id="run-pipeline-btn", className="pu-btn pu-btn-primary", style={"width": "100%", "padding": "12px", "marginBottom": "24px"}, disabled=True),
            dcc.Loading(id="pipeline-loading", type="dot", children=html.Div(id="pipeline-status")),
            html.Div(id="dataset-preview"),
        ], style={"padding": "28px"}),
        dcc.Store(id="stored-raw-data"),
        dcc.Store(id="pipeline-result"),
    ], style={"paddingTop": "120px"})
