"""Purity UI Sidebar — exact replica of creativetimofficial/purity-ui-dashboard."""
from dash import html


# SVG Icons matching Purity UI's style
ICONS = {
    "home": html.I(className="bi bi-house"),
    "tables": html.I(className="bi bi-bar-chart"),
    "billing": html.I(className="bi bi-credit-card"),
    "rtl": html.I(className="bi bi-globe"),
    "profile": html.I(className="bi bi-person"),
    "signin": html.I(className="bi bi-box-arrow-in-right"),
    "signup": html.I(className="bi bi-person-plus"),
    "upload": html.I(className="bi bi-cloud-upload"),
    "eda": html.I(className="bi bi-graph-up"),
    "models": html.I(className="bi bi-cpu"),
    "report": html.I(className="bi bi-file-earmark-text"),
    "rocket": html.I(className="bi bi-rocket"),
}

# Route definitions matching Purity UI's structure
MAIN_ROUTES = [
    {"path": "/dashboard", "name": "Dashboard", "rtl_name": "لوحة القيادة", "icon": "home"},
    {"path": "/tables", "name": "Tables", "rtl_name": "الجداول", "icon": "tables"},
    {"path": "/reports", "name": "Reports", "rtl_name": "التقارير", "icon": "billing"},
    {"path": "/rtl", "name": "RTL", "rtl_name": "آرتيإل", "icon": "rtl"},
    {"path": "/upload", "name": "Upload", "rtl_name": "رفع البيانات", "icon": "upload"},
    {"path": "/eda", "name": "EDA", "rtl_name": "التحليل", "icon": "eda"},
    {"path": "/models", "name": "Models", "rtl_name": "النماذج", "icon": "models"},
]

ACCOUNT_ROUTES = [
    {"path": "/profile", "name": "Profile", "rtl_name": "الملف الشخصي", "icon": "profile"},
    {"path": "/auth/signin", "name": "Sign In", "rtl_name": "تسجيل الدخول", "icon": "signin"},
    {"path": "/auth/signup", "name": "Sign Up", "rtl_name": "إنشاء حساب", "icon": "signup"},
]


def _nav_link(path, name, icon_key, rtl_name=None, current_path="/dashboard"):
    """Create a single nav link matching Purity UI style."""
    is_active = current_path == path
    icon = ICONS.get(icon_key, ICONS["home"])

    return html.A(
        [
            html.Div(icon, className="pu-icon-box"),
            html.Span(name, **{"data-rtl": rtl_name or name}),
        ],
        href=path,
        className=f"pu-nav-link{' active' if is_active else ''}",
        id=f"nav-link-{path.replace('/', '-')}",
    )


def create_sidebar(current_path="/dashboard", direction="ltr"):
    """Create the Purity UI sidebar."""
    links = []
    for route in MAIN_ROUTES:
        links.append(_nav_link(
            route["path"], route["name"], route["icon"],
            route.get("rtl_name"), current_path,
        ))

    account_links = []
    for route in ACCOUNT_ROUTES:
        account_links.append(_nav_link(
            route["path"], route["name"], route["icon"],
            route.get("rtl_name"), current_path,
        ))

    logo_text = "AUTOANALYST AI" if direction == "ltr" else "محلل البيانات"

    return html.Nav(
        [
            # Logo
            html.A(
                [
                    html.I(className="bi bi-bar-chart-line", style={"fontSize": "24px", "color": "var(--pu-accent)"}),
                    html.Span(logo_text, style={"fontSize": "14px", "fontWeight": "700", "letterSpacing": "1px"}),
                ],
                href="/dashboard",
                className="pu-sidebar-logo",
            ),
            html.Hr(className="pu-separator"),
            # Main navigation
            html.Div(links, style={"marginBottom": "24px"}),
            # Account category
            html.Div("ACCOUNT PAGES", className="pu-nav-category"),
            html.Div(account_links),
            # Help card
            html.Div(
                [
                    html.Div(
                        [
                            html.I(className="bi bi-question-circle", style={"fontSize": "24px", "color": "white", "marginBottom": "12px"}),
                            html.P("Need help?", style={"color": "white", "fontWeight": "700", "marginBottom": "4px"}),
                            html.P("Check our docs", style={"color": "rgba(255,255,255,0.7)", "fontSize": "12px", "marginBottom": "12px"}),
                            html.A("DOCUMENTATION", href="#", className="pu-btn pu-btn-outline", style={"color": "white", "borderColor": "white", "fontSize": "12px", "padding": "8px 16px"}),
                        ],
                        style={
                            "background": "linear-gradient(81.62deg, #313860 2.25%, #151928 79.87%)",
                            "borderRadius": "15px",
                            "padding": "24px",
                            "textAlign": "center",
                            "marginTop": "auto",
                        },
                    ),
                ],
                style={"marginTop": "auto", "padding": "16px 0"},
            ),
        ],
        className="pu-sidebar",
        **{"data-dir": direction},
    )
