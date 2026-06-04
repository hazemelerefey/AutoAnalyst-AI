"""Purity UI AdminNavbar — exact replica."""
from dash import html


def AdminNavbar(breadcrumb_page="Dashboard", breadcrumb_section="Pages"):
    """Create the admin navbar matching Purity UI."""
    return html.Header(
        [
            # Breadcrumb
            html.Div(
                [
                    html.Span(breadcrumb_section, className="pu-navbar-breadcrumb"),
                    html.Span(" / ", style={"color": "var(--pu-text-muted)", "margin": "0 4px"}),
                    html.Span(breadcrumb_page, style={"color": "var(--pu-text)", "fontWeight": "700", "fontSize": "14px"}),
                ],
                className="pu-navbar-breadcrumb",
            ),
            # Right side
            html.Div(
                [
                    # Search bar
                    html.Div(
                        [
                            html.I(className="bi bi-search", style={"color": "var(--pu-text-muted)"}),
                            html.Input(type="text", placeholder="Type here...", className="pu-search-bar-input"),
                        ],
                        className="pu-search-bar",
                    ),
                    # Sign In link
                    html.A(
                        [html.I(className="bi bi-box-arrow-in-right"), html.Span("Sign In", style={"marginLeft": "8px", "fontSize": "14px"})],
                        href="/auth/signin",
                        className="pu-navbar-icon",
                        style={"display": "flex", "alignItems": "center", "gap": "4px", "textDecoration": "none", "color": "var(--pu-text-muted)", "fontSize": "14px"},
                    ),
                    # Settings
                    html.Button(
                        html.I(className="bi bi-gear"),
                        className="pu-navbar-icon",
                        id="settings-btn",
                    ),
                    # Notifications
                    html.Button(
                        html.I(className="bi bi-bell"),
                        className="pu-navbar-icon",
                        id="notifications-btn",
                    ),
                    # Avatar
                    html.Div("A", className="pu-avatar"),
                ],
                className="pu-navbar-right",
            ),
        ],
        className="pu-navbar",
    )
