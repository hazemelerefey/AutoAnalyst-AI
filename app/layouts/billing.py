"""Billing/Reports page — exact Purity UI layout adapted for AutoAnalyst."""
from dash import html
from app.components.card import Card, CardBody, CardHeader
from app.components.mini_stat import MiniStatistics

INVOICES = [
    {"name": "March, 01, 2020", "number": "#MS-415646", "price": "$180"},
    {"name": "February, 10, 2021", "number": "#RV-126749", "price": "$250"},
    {"name": "April, 05, 2020", "number": "#QW-103578", "price": "$120"},
    {"name": "June, 25, 2019", "number": "#MS-415646", "price": "$180"},
    {"name": "March, 01, 2019", "number": "#AR-803481", "price": "$300"},
]

TRANSACTIONS = [
    {"name": "Netflix", "type": "Automatic", "date": "27 March 2020", "amount": "-$2,500", "color": "#F56565"},
    {"name": "Apple", "type": "Automatic", "date": "27 March 2020", "amount": "+$2,000", "color": "#48BB78"},
    {"name": "Stripe", "type": "Manual", "date": "26 March 2020", "amount": "+$750", "color": "#48BB78"},
    {"name": "HubSpot", "type": "Automatic", "date": "26 March 2020", "amount": "+$1,000", "color": "#48BB78"},
    {"name": "HubSpot", "type": "Manual", "date": "25 March 2020", "amount": "-$250", "color": "#F56565"},
    {"name": "Webflow", "type": "Pending", "date": "25 March 2020", "amount": "Pending", "color": "#ECC94B"},
]


def _credit_cards():
    return html.Div([
        Card([
            html.Div([
                html.P("Credit Card", style={"color": "rgba(255,255,255,0.7)", "fontSize": "14px", "marginBottom": "8px"}),
                html.P("7812 2139 0823 XXXX", className="card-number", style={"color": "white", "fontSize": "18px", "letterSpacing": "3px", "marginBottom": "20px"}),
                html.Div([
                    html.Div([html.P("VALID THRU", style={"color": "rgba(255,255,255,0.5)", "fontSize": "10px", "margin": "0"}), html.P("11/26", style={"color": "white", "fontSize": "14px", "margin": "0"})]),
                ], style={"display": "flex", "gap": "24px"}),
            ], className="pu-credit-card pu-credit-card-visa"),
        ], style={"padding": "0", "background": "transparent", "boxShadow": "none"}),
        Card([
            html.Div([
                html.P("Credit Card", style={"color": "rgba(255,255,255,0.7)", "fontSize": "14px", "marginBottom": "8px"}),
                html.P("7812 2139 0823 XXXX", className="card-number", style={"color": "white", "fontSize": "18px", "letterSpacing": "3px", "marginBottom": "20px"}),
                html.Div([
                    html.Div([html.P("VALID THRU", style={"color": "rgba(255,255,255,0.5)", "fontSize": "10px", "margin": "0"}), html.P("11/26", style={"color": "white", "fontSize": "14px", "margin": "0"})]),
                ], style={"display": "flex", "gap": "24px"}),
            ], className="pu-credit-card pu-credit-card-mastercard"),
        ], style={"padding": "0", "background": "transparent", "boxShadow": "none"}),
    ], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "24px", "marginBottom": "24px"})


def _payment_method():
    return Card([
        CardHeader(html.H5("Payment Method", style={"color": "var(--pu-text)"})),
        html.Div([
            html.Button([html.I(className="bi bi-credit-card-2-front", style={"marginRight": "8px"}), "Add New Card"], className="pu-btn pu-btn-primary"),
        ], style={"marginBottom": "16px"}),
        html.Div([
            html.Div([
                html.I(className="bi bi-credit-card-2-front", style={"fontSize": "24px", "color": "var(--pu-text-muted)", "marginRight": "16px"}),
                html.Div([
                    html.P("7812 2139 0823 XXXX", style={"margin": "0", "fontWeight": "500", "color": "var(--pu-text)"}),
                    html.P("Card expires at 11/26", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)"}),
                ], style={"flex": "1"}),
                html.Button("Delete", className="pu-btn pu-btn-outline", style={"fontSize": "13px", "padding": "6px 16px"}),
            ], style={"display": "flex", "alignItems": "center", "padding": "12px 0", "borderBottom": "1px solid var(--pu-border)"}),
            html.Div([
                html.I(className="bi bi-credit-card-2-front", style={"fontSize": "24px", "color": "var(--pu-text-muted)", "marginRight": "16px"}),
                html.Div([
                    html.P("7812 2139 0823 XXXX", style={"margin": "0", "fontWeight": "500", "color": "var(--pu-text)"}),
                    html.P("Card expires at 11/26", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)"}),
                ], style={"flex": "1"}),
                html.Button("Delete", className="pu-btn pu-btn-outline", style={"fontSize": "13px", "padding": "6px 16px"}),
            ], style={"display": "flex", "alignItems": "center", "padding": "12px 0"}),
        ]),
    ], style={"padding": "28px"})


def _invoices():
    rows = []
    for inv in INVOICES:
        rows.append(html.Tr([
            html.Td(inv["name"], style={"fontWeight": "500"}),
            html.Td(inv["number"]),
            html.Td(inv["price"], style={"fontWeight": "500"}),
            html.Td(html.A([html.I(className="bi bi-file-earmark-pdf", style={"marginRight": "4px"}), "PDF"], href="#", style={"color": "var(--pu-text-muted)", "textDecoration": "none", "fontSize": "13px"})),
        ], style={"borderBottom": "1px solid var(--pu-border)"}))

    return Card([
        CardHeader(html.H5("Invoices", style={"color": "var(--pu-text)"})),
        html.Div(html.Button("View All", className="pu-btn pu-btn-outline", style={"fontSize": "13px", "padding": "6px 16px"}), style={"textAlign": "right", "marginBottom": "16px"}),
        html.Table([
            html.Thead(html.Tr([html.Th("DESCRIPTION"), html.Th("NUMBER"), html.Th("PRICE"), html.Th("")])),
            html.Tbody(rows),
        ], className="pu-table"),
    ], style={"padding": "28px"})


def _billing_info():
    return Card([
        CardHeader(html.H5("Billing Information", style={"color": "var(--pu-text)"})),
        html.Div([
            html.Div([
                html.P("Oliver Liam", style={"margin": "0", "fontWeight": "700", "color": "var(--pu-text)"}),
                html.P("Company Name", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)", "marginBottom": "4px"}),
                html.P("VAT: DK14567890", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)"}),
            ], style={"flex": "1"}),
            html.Button("Delete", className="pu-btn pu-btn-outline", style={"fontSize": "13px", "padding": "6px 16px", "color": "#F56565", "borderColor": "#F56565"}),
        ], style={"display": "flex", "alignItems": "center", "padding": "16px 0", "borderBottom": "1px solid var(--pu-border)"}),
        html.Div([
            html.Div([
                html.P("Lucas Harper", style={"margin": "0", "fontWeight": "700", "color": "var(--pu-text)"}),
                html.P("Company Name", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)", "marginBottom": "4px"}),
                html.P("VAT: DK14567890", style={"margin": "0", "fontSize": "13px", "color": "var(--pu-text-muted)"}),
            ], style={"flex": "1"}),
            html.Button("Delete", className="pu-btn pu-btn-outline", style={"fontSize": "13px", "padding": "6px 16px", "color": "#F56565", "borderColor": "#F56565"}),
        ], style={"display": "flex", "alignItems": "center", "padding": "16px 0"}),
    ], style={"padding": "28px"})


def _transactions():
    rows = []
    for t in TRANSACTIONS:
        rows.append(html.Tr([
            html.Td(html.I(className="bi bi-arrow-down-up", style={"color": t["color"], "marginRight": "8px"})),
            html.Td(t["name"], style={"fontWeight": "500"}),
            html.Td(t["type"]),
            html.Td(t["date"]),
            html.Td(t["amount"], style={"fontWeight": "700", "color": t["color"]}),
        ], style={"borderBottom": "1px solid var(--pu-border)"}))

    return Card([
        CardHeader(html.H5("Your Transactions", style={"color": "var(--pu-text)"})),
        html.P("23-30 March 2020", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
        html.Table([
            html.Thead(html.Tr([html.Th(""), html.Th("NAME"), html.Th("TYPE"), html.Th("DATE"), html.Th("AMOUNT")])),
            html.Tbody(rows),
        ], className="pu-table"),
    ], style={"padding": "28px"})


def create_billing_layout():
    return html.Div([
        MiniStatistics("Salary", "$1,000", 12, html.I(className="bi bi-wallet2"), "#38B2AC"),
        html.Div([
            _credit_cards(),
            html.Div([_payment_method(), _invoices()], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "24px", "marginBottom": "24px"}),
            html.Div([_billing_info(), _transactions()], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "24px"}),
        ]),
    ], style={"paddingTop": "120px"})
