"""AutoAnalyst AI — Main Dash Application (Purity UI Dashboard)."""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import dash
from dash import html, dcc, Input, Output
from app.config import get_config
from app.components.sidebar import create_sidebar
from app.components.navbar import AdminNavbar
from app.layouts.dashboard import create_dashboard_layout
from app.layouts.tables import create_tables_layout
from app.layouts.billing import create_billing_layout
from app.layouts.profile import create_profile_layout
from app.layouts.auth import create_signin_layout, create_signup_layout
from app.layouts.rtl import create_rtl_layout
from app.layouts.upload import create_upload_layout
from app.layouts.eda import create_eda_layout
from app.layouts.models import create_models_layout
from app.layouts.report import create_report_layout

config = get_config()

# ── App initialization ──────────────────────────────────────
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="AutoAnalyst AI — Purity Dashboard",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    ],
)

server = app.server

# ── Layout ──────────────────────────────────────────────────
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    dcc.Store(id="theme-store", data="light"),

    # Sidebar
    html.Div(id="sidebar-container"),

    # Main panel
    html.Div([
        # Navbar
        html.Div(id="navbar-container"),
        # Page content
        html.Div(id="page-content", className="pu-main-content"),
    ], className="pu-main-panel"),
])


# ── Router callback ─────────────────────────────────────────
@app.callback(
    Output("page-content", "children"),
    Output("sidebar-container", "children"),
    Output("navbar-container", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    """Route to the correct page layout."""
    if pathname is None:
        pathname = "/dashboard"

    # Auth pages — no sidebar/navbar
    if pathname in ("/auth/signin", "/auth/signup"):
        if pathname == "/auth/signup":
            return create_signup_layout(), html.Div(), html.Div()
        return create_signin_layout(), html.Div(), html.Div()

    # Determine breadcrumb
    page_map = {
        "/dashboard": "Dashboard", "/tables": "Tables",
        "/reports": "Reports", "/rtl": "RTL",
        "/profile": "Profile", "/upload": "Upload",
        "/eda": "EDA", "/models": "Models", "/report": "Report",
    }
    page_name = page_map.get(pathname, "Dashboard")

    # Layout
    layout_map = {
        "/dashboard": create_dashboard_layout,
        "/tables": create_tables_layout,
        "/reports": create_billing_layout,
        "/rtl": create_rtl_layout,
        "/profile": create_profile_layout,
        "/upload": create_upload_layout,
        "/eda": create_eda_layout,
        "/models": create_models_layout,
        "/report": create_report_layout,
    }
    layout_fn = layout_map.get(pathname, create_dashboard_layout)

    sidebar = create_sidebar(current_path=pathname)
    navbar = AdminNavbar(breadcrumb_page=page_name)

    return layout_fn(), sidebar, navbar


# ── Import and register page callbacks ──────────────────────
from app.callbacks import data, charts  # noqa: E402

data.register_callbacks(app)
charts.register_callbacks(app)


if __name__ == "__main__":
    app.run(debug=config.debug, host=config.host, port=config.port)
