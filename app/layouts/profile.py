"""Profile page — Purity UI style adapted for AutoAnalyst data profile."""
from dash import html, dcc
from app.components.card import Card, CardBody, CardHeader
from app.components.charts import donut_chart

PROFILE_BG = "linear-gradient(81.62deg, #313860 2.25%, #151928 79.87%)"


def _profile_header():
    return html.Div([
        html.Div(style={"height": "200px", "background": PROFILE_BG, "borderRadius": "15px 15px 0 0"}),
        html.Div([
            html.Div("A", className="pu-avatar", style={"width": "74px", "height": "74px", "fontSize": "28px", "border": "4px solid var(--pu-card-bg)", "marginTop": "-37px", "marginRight": "24px"}),
            html.Div([
                html.H4("AutoAnalyst AI", style={"margin": "0", "color": "var(--pu-text)", "fontWeight": "700"}),
                html.P("Data Analysis Platform", style={"margin": "0", "color": "var(--pu-text-muted)", "fontSize": "14px"}),
            ], style={"flex": "1"}),
            html.Button("Edit Profile", className="pu-btn pu-btn-outline", style={"fontSize": "14px"}),
        ], style={"display": "flex", "alignItems": "center", "padding": "0 24px 24px", "marginTop": "-37px"}),
    ], style={"marginBottom": "24px"})


def _profile_info():
    return Card([
        CardHeader(html.H5("Profile Information", style={"color": "var(--pu-text)"})),
        html.P("Hi, I'm Alec Thompson. Decisions: If you can't decide, the answer is no. If two paths seem equally viable, choose the harder one.", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "lineHeight": "1.6", "marginBottom": "24px"}),
        html.Hr(className="pu-separator"),
        html.Div([
            html.Div([html.Span("Full Name:", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}), html.Span("Alec M. Thompson", style={"color": "var(--pu-text)", "fontWeight": "500", "fontSize": "14px", "marginLeft": "8px"})]),
            html.Div([html.Span("Mobile:", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}), html.Span("(44) 123 1234 123", style={"color": "var(--pu-text)", "fontWeight": "500", "fontSize": "14px", "marginLeft": "8px"})]),
            html.Div([html.Span("Email:", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}), html.Span("alecthompson@mail.com", style={"color": "var(--pu-text)", "fontWeight": "500", "fontSize": "14px", "marginLeft": "8px"})]),
            html.Div([html.Span("Location:", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}), html.Span("United States", style={"color": "var(--pu-text)", "fontWeight": "500", "fontSize": "14px", "marginLeft": "8px"})]),
        ], style={"display": "flex", "flexDirection": "column", "gap": "12px"}),
    ], style={"padding": "28px", "marginBottom": "24px"})


def _platform_settings():
    return Card([
        CardHeader(html.H5("Platform Settings", style={"color": "var(--pu-text)"})),
        html.Div([
            html.Div([html.Span("Email me when someone follows me", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle active")], className="pu-toggle-row"),
            html.Div([html.Span("Email me when someone answers me", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle active")], className="pu-toggle-row"),
            html.Div([html.Span("Email me when someone mentions me", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle")], className="pu-toggle-row"),
            html.Div([html.Span("New launches and projects", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle active")], className="pu-toggle-row"),
            html.Div([html.Span("Monthly product changes", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle active")], className="pu-toggle-row"),
            html.Div([html.Span("Subscribe to newsletter", style={"color": "var(--pu-text)", "fontSize": "14px"}), html.Button(className="pu-theme-toggle")], className="pu-toggle-row"),
        ]),
    ], style={"padding": "28px", "marginBottom": "24px"})


def _profile_projects():
    projects = [
        {"name": "Modern", "desc": "As Uber works through a huge amount of internal management turmoil.", "color": "#38B2AC"},
        {"name": "Scandinavian", "desc": "Music is something that every person has his or her own specific opinion about.", "color": "#9F7AEA"},
        {"name": "Minimalist", "desc": "Different people have different taste, and various types of music.", "color": "#ECC94B"},
    ]
    cards = []
    for p in projects:
        cards.append(html.Div([
            html.Div(style={"height": "8px", "backgroundColor": p["color"], "borderRadius": "8px 8px 0 0"}),
            html.Div([
                html.P(p["name"], style={"margin": "0 0 8px 0", "fontWeight": "700", "color": "var(--pu-text)"}),
                html.P(p["desc"], style={"margin": "0", "fontSize": "14px", "color": "var(--pu-text-muted)", "lineHeight": "1.5"}),
            ], style={"padding": "20px"}),
        ], className="pu-card", style={"padding": "0", "marginBottom": "16px"}))

    return Card([
        CardHeader(html.H5("Projects", style={"color": "var(--pu-text)"})),
        html.P("Architects design houses", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
        html.Div(cards, style={"display": "grid", "gridTemplateColumns": "repeat(auto-fit, minmax(250px, 1fr))", "gap": "16px"}),
    ], style={"padding": "28px"})


def create_profile_layout():
    return html.Div([
        _profile_header(),
        html.Div([
            html.Div([_profile_info(), _platform_settings()], style={"flex": "1"}),
            html.Div([_profile_projects()], style={"flex": "1"}),
        ], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "24px"}),
    ], style={"paddingTop": "120px"})
