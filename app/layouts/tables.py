"""Tables page — exact Purity UI layout."""
from dash import html
from app.components.card import Card, CardBody, CardHeader

AUTHORS = [
    {"name": "Elaine Benes", "email": "elaine@vandelay.com", "function": "Manager", "org": "Organization", "status": "Online", "date": "14/06/21", "color": "#48BB78"},
    {"name": "Sidra Holland", "email": "sidra@vandelay.com", "function": "Programmer", "org": "Developer", "status": "Offline", "date": "14/06/21", "color": "#ECC94B"},
    {"name": "Cosmo Kramer", "email": "kramer@vandelay.com", "function": "Executive", "org": "Projects", "status": "Online", "date": "14/06/21", "color": "#48BB78"},
    {"name": "Newman", "email": "newman@usps.com", "function": "Manager", "org": "Organization", "status": "Online", "date": "14/06/21", "color": "#48BB78"},
    {"name": "Frank Costanza", "email": "frank@vandelay.com", "function": "Programmer", "org": "Developer", "status": "Offline", "date": "14/06/21", "color": "#ECC94B"},
]

PROJECTS = [
    {"name": "Chakra Soft UI Version", "budget": "$14,000", "status": "Working", "completion": 60, "color": "#38B2AC"},
    {"name": "Add Progress Track", "budget": "$3,000", "status": "Cancelled", "completion": 10, "color": "#F56565"},
    {"name": "Fix Platform Errors", "budget": "Not set", "status": "Done", "completion": 100, "color": "#48BB78"},
    {"name": "Launch Mobile App", "budget": "$32,000", "status": "Done", "completion": 100, "color": "#48BB78"},
    {"name": "Add New Pricing Page", "budget": "$400", "status": "Working", "completion": 25, "color": "#38B2AC"},
]


def _authors_table():
    rows = []
    for a in AUTHORS:
        rows.append(html.Tr([
            html.Td(html.Div([html.Div(a["name"][0], className="pu-avatar", style={"width": "36px", "height": "36px", "fontSize": "13px"}), html.Div([html.P(a["name"], style={"margin": "0", "fontWeight": "500", "fontSize": "14px"}), html.P(a["email"], style={"margin": "0", "color": "var(--pu-text-muted)", "fontSize": "13px"})])], style={"display": "flex", "alignItems": "center", "gap": "12px"})),
            html.Td(html.Div([html.P(a["function"], style={"margin": "0", "fontWeight": "500", "fontSize": "14px"}), html.P(a["org"], style={"margin": "0", "color": "var(--pu-text-muted)", "fontSize": "13px"})])),
            html.Td(html.Span(a["status"], className=f"pu-badge {'pu-badge-success' if a['status']=='Online' else 'pu-badge-info'}")),
            html.Td(a["date"], style={"fontSize": "14px"}),
            html.Td(html.A("Edit", href="#", style={"color": "var(--pu-text-muted)", "fontSize": "13px", "textDecoration": "none"})),
        ], style={"borderBottom": "1px solid var(--pu-border)"}))

    return Card([
        CardHeader(html.H5("Authors Table", style={"color": "var(--pu-text)"})),
        html.Table([
            html.Thead(html.Tr([html.Th("AUTHOR"), html.Th("FUNCTION"), html.Th("STATUS"), html.Th("EMPLOYED"), html.Th("")])),
            html.Tbody(rows),
        ], className="pu-table"),
    ], style={"padding": "28px", "marginBottom": "24px"})


def _projects_table():
    rows = []
    for p in PROJECTS:
        rows.append(html.Tr([
            html.Td(p["name"], style={"fontWeight": "500"}),
            html.Td(p["budget"], style={"fontWeight": "500"}),
            html.Td(html.Span(p["status"], className=f"pu-badge {'pu-badge-success' if p['status']=='Done' else 'pu-badge-danger' if p['status']=='Cancelled' else 'pu-badge-info'}")),
            html.Td([
                html.Span(f"{p['completion']}%", style={"marginRight": "8px", "fontSize": "13px"}),
                html.Div(html.Div(style={"width": f"{p['completion']}%", "height": "4px", "backgroundColor": p["color"], "borderRadius": "2px"}), style={"width": "100%", "height": "4px", "backgroundColor": "var(--pu-border)", "borderRadius": "2px"}),
            ]),
            html.Td(html.A("Edit", href="#", style={"color": "var(--pu-text-muted)", "fontSize": "13px", "textDecoration": "none"})),
        ], style={"borderBottom": "1px solid var(--pu-border)"}))

    return Card([
        CardHeader(html.H5("Projects Table", style={"color": "var(--pu-text)"})),
        html.P("30 done this month", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
        html.Table([
            html.Thead(html.Tr([html.Th("COMPANIES"), html.Th("BUDGET"), html.Th("STATUS"), html.Th("COMPLETION"), html.Th("")])),
            html.Tbody(rows),
        ], className="pu-table"),
    ], style={"padding": "28px"})


def create_tables_layout():
    return html.Div([_authors_table(), _projects_table()])
