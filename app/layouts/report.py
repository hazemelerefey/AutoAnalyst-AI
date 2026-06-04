"""Report page — Purity UI style for report generation."""
from dash import html, dcc
from app.components.card import Card, CardBody, CardHeader


def create_report_layout():
    return html.Div([
        html.Div([
            html.Button([html.I(className="bi bi-download", style={"marginRight": "8px"}), "Download Markdown"], id="download-md-btn", className="pu-btn pu-btn-primary", style={"marginRight": "12px"}, disabled=True),
            html.Button([html.I(className="bi bi-file-pdf", style={"marginRight": "8px"}), "Download PDF"], id="download-pdf-btn", className="pu-btn pu-btn-outline", disabled=True),
        ], style={"marginBottom": "24px"}),
        Card([
            CardHeader(html.H5("Analysis Report", style={"color": "var(--pu-text)"})),
            html.Div(id="report-preview", children=[
                html.P("Run the analysis pipeline first to generate a report.", style={"color": "var(--pu-text-muted)", "textAlign": "center", "padding": "40px", "fontSize": "14px"}),
            ]),
        ], style={"padding": "28px"}),
        dcc.Download(id="download-report"),
    ], style={"paddingTop": "120px"})
