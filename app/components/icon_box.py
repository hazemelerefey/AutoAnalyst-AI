"""Purity UI IconBox component."""
from dash import html


def IconBox(icon, bg="var(--pu-accent)", color="white", size="30px"):
    """Create an icon box matching Purity UI style."""
    return html.Div(
        icon,
        className="pu-icon-box",
        style={
            "width": size,
            "height": size,
            "backgroundColor": bg,
            "color": color,
        },
    )
