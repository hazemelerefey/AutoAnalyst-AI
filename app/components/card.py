"""Purity UI Card components — Card, CardBody, CardHeader."""
from dash import html


def Card(children=None, className="", **kwargs):
    """Purity UI Card wrapper."""
    return html.Div(children, className=f"pu-card {className}".strip(), **kwargs)


def CardBody(children=None, className="", **kwargs):
    """Purity UI CardBody wrapper."""
    return html.Div(children, className=f"pu-card-body {className}".strip(), **kwargs)


def CardHeader(children=None, className="", **kwargs):
    """Purity UI CardHeader wrapper."""
    return html.Div(children, className=f"pu-card-header {className}".strip(), **kwargs)
