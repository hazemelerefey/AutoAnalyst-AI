"""Purity UI MiniStatistics component — exact replica."""
from dash import html

from app.components.card import Card, CardBody


def MiniStatistics(title, amount, percentage=None, icon=None, icon_bg="var(--pu-accent)"):
    """Create a MiniStatistics card matching Purity UI exactly.

    Args:
        title: Stat label (e.g., "Today's Money")
        amount: Main value (e.g., "$53,000")
        percentage: Change percentage (positive or negative)
        icon: Dash component for the icon
        icon_bg: Background color for icon box
    """
    stat_change = None
    if percentage is not None:
        is_positive = percentage > 0
        stat_change = html.Span(
            f"+{percentage}%" if is_positive else f"{percentage}%",
            className=f"pu-stat-change {'positive' if is_positive else 'negative'}",
        )

    icon_box = html.Div(
        icon or html.I(className="bi bi-bar-chart"),
        className="pu-stat-icon",
        style={"backgroundColor": icon_bg},
    )

    return Card(
        CardBody(
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(title, className="pu-stat-label"),
                            html.Div(
                                [html.Span(amount, className="pu-stat-value"), stat_change],
                                style={"display": "flex", "alignItems": "baseline"},
                            ),
                        ],
                        style={"flex": "1"},
                    ),
                    icon_box,
                ],
                style={"display": "flex", "alignItems": "center", "justifyContent": "center", "width": "100%"},
            ),
        ),
        className="pu-mini-stat",
    )
