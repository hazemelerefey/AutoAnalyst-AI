"""Dashboard page — exact Purity UI layout adapted for AutoAnalyst."""
from dash import html, dcc
from app.components.mini_stat import MiniStatistics
from app.components.card import Card, CardBody, CardHeader
from app.components.charts import line_chart, gradient_bar_chart

# Sample data (replaced by pipeline results via callbacks)
SAMPLE_TIMELINE = [
    {"icon": "bi-bell", "color": "#48BB78", "title": "Data Loaded", "desc": "CSV file uploaded successfully", "time": "2 min ago"},
    {"icon": "bi-bar-chart", "color": "#38B2AC", "title": "Profiling Complete", "desc": "15 columns analyzed, 3 with missing values", "time": "1 min ago"},
    {"icon": "bi-graph-up", "color": "#9F7AEA", "title": "EDA Generated", "desc": "Distribution and correlation charts ready", "time": "45 sec ago"},
    {"icon": "bi-cpu", "color": "#ECC94B", "title": "Model Trained", "desc": "RandomForest achieved 92% accuracy", "time": "30 sec ago"},
    {"icon": "bi-file-text", "color": "#ED64A6", "title": "Report Generated", "desc": "Markdown report ready for download", "time": "Just now"},
]

SAMPLE_PROJECTS = [
    {"name": "Chakra Soft UI Version", "members": ["A", "B", "C"], "budget": "$14,000", "completion": 60},
    {"name": "Add Progress Track", "members": ["D", "E"], "budget": "$3,000", "completion": 10},
    {"name": "Fix Platform Errors", "members": ["F", "G", "H"], "budget": "Not set", "completion": 100},
    {"name": "Launch our Mobile App", "members": ["I", "J"], "budget": "$32,000", "completion": 100},
    {"name": "Add the New Pricing Page", "members": ["K"], "budget": "$400", "completion": 25},
]


def _mini_stat_row():
    """Create the 4 mini statistics cards matching Purity UI."""
    return html.Div(
        [
            MiniStatistics("Today's Money", "$53,000", 55, html.I(className="bi bi-wallet2"), "#38B2AC"),
            MiniStatistics("Today's Users", "2,300", 5, html.I(className="bi bi-globe"), "#38B2AC"),
            MiniStatistics("New Clients", "+3,020", -14, html.I(className="bi bi-file-earmark"), "#38B2AC"),
            MiniStatistics("Total Sales", "$173,000", 8, html.I(className="bi bi-cart3"), "#38B2AC"),
        ],
        style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))",
            "gap": "24px",
            "marginBottom": "26px",
        },
    )


def _built_by_developers():
    """Built by Developers card (matches Purity UI)."""
    return Card(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Built by Developers", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "8px"}),
                            html.H4("AutoAnalyst AI", style={"color": "var(--pu-text)", "fontSize": "22px", "fontWeight": "700", "marginBottom": "12px"}),
                            html.P("From data loading to model training, automated AI-powered analysis pipeline.", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "24px", "lineHeight": "1.6"}),
                            html.A("Read More", href="#", className="pu-btn pu-btn-primary", style={"fontSize": "14px"}),
                        ],
                        style={"flex": "1", "paddingRight": "24px"},
                    ),
                    html.Div(
                        html.I(className="bi bi-bar-chart-line", style={"fontSize": "80px", "color": "var(--pu-accent)", "opacity": "0.3"}),
                        style={"display": "flex", "alignItems": "center", "justifyContent": "center", "minWidth": "200px"},
                    ),
                ],
                style={"display": "flex", "alignItems": "center"},
            ),
        ],
        style={"padding": "28px"},
    )


def _work_with_rockets():
    """Work with the Rockets card (matches Purity UI)."""
    return Card(
        [
            html.Div(
                [
                    html.I(className="bi bi-rocket", style={"fontSize": "48px", "color": "white", "marginBottom": "16px"}),
                    html.H5("Work with the Rockets", style={"color": "white", "fontSize": "18px", "fontWeight": "700", "marginBottom": "8px"}),
                    html.P("Data-driven analysis is a revolutionary approach. It is all about who takes the opportunity first.", style={"color": "rgba(255,255,255,0.7)", "fontSize": "14px", "lineHeight": "1.6"}),
                ],
                style={
                    "background": "linear-gradient(81.62deg, #313860 2.25%, #151928 79.87%)",
                    "borderRadius": "15px",
                    "padding": "28px",
                    "height": "100%",
                    "display": "flex",
                    "flexDirection": "column",
                    "justifyContent": "flex-end",
                },
            ),
        ],
        style={"padding": "0", "background": "transparent", "boxShadow": "none"},
    )


def _sales_overview_chart():
    """Sales overview line chart (matches Purity UI)."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    revenue = [50, 40, 300, 220, 500, 250, 400, 230, 500, 350, 450, 400]
    sales = [30, 20, 200, 120, 400, 150, 300, 130, 400, 250, 350, 300]

    fig = line_chart(months, revenue, "Sales Overview")
    fig.add_trace(go.Scatter(
        x=months, y=sales, mode="lines+markers",
        line=dict(color="#ECC94B", width=3, shape="spline"),
        marker=dict(size=6, color="#ECC94B"),
        fill="tozeroy",
        fillcolor="rgba(236, 201, 75, 0.1)",
        name="Revenue",
    ))
    fig.data[0].name = "Sales"

    return Card(
        [
            CardHeader(
                [
                    html.H5("Sales Overview", style={"color": "var(--pu-text)", "marginBottom": "6px"}),
                    html.P(
                        [html.Span("+5% more ", style={"color": "#48BB78", "fontWeight": "700"}), "in 2021"],
                        style={"color": "var(--pu-text-muted)", "fontSize": "14px", "margin": "0"},
                    ),
                ],
            ),
            dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": "300px"}),
        ],
        style={"padding": "28px 28px 16px 0"},
    )


def _active_users_chart():
    """Active users bar chart (matches Purity UI)."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    users = [400, 380, 420, 500, 450, 480, 520, 510, 550]

    fig = gradient_bar_chart(months, [users], ["Active Users"], "Active Users")
    fig.update_layout(showlegend=False)

    return Card(
        [
            CardHeader(
                [
                    html.H5("Active Users", style={"color": "var(--pu-text)", "marginBottom": "6px"}),
                    html.P(
                        [html.Span("(+23) ", style={"color": "#48BB78", "fontWeight": "700"}), "than last week"],
                        style={"color": "var(--pu-text-muted)", "fontSize": "14px", "margin": "0"},
                    ),
                ],
            ),
            dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": "300px"}),
        ],
        style={"padding": "28px 28px 16px 0"},
    )


def _projects_table():
    """Projects table (matches Purity UI)."""
    rows = []
    for p in SAMPLE_PROJECTS:
        member_avatars = html.Div(
            [html.Div(m[0], className="pu-avatar", style={"width": "28px", "height": "28px", "fontSize": "11px", "marginLeft": "-8px" if i > 0 else "0"})
             for i, m in enumerate(p["members"])],
            style={"display": "flex"},
        )
        completion_color = "#48BB78" if p["completion"] == 100 else "#38B2AC"
        rows.append(
            html.Tr([
                html.Td(p["name"], style={"fontWeight": "500"}),
                html.Td(member_avatars),
                html.Td(p["budget"], style={"fontWeight": "500"}),
                html.Td(
                    [
                        html.Span(f"{p['completion']}%", style={"marginRight": "8px", "fontSize": "13px"}),
                        html.Div(
                            html.Div(style={"width": f"{p['completion']}%", "height": "4px", "backgroundColor": completion_color, "borderRadius": "2px"}),
                            style={"width": "100%", "height": "4px", "backgroundColor": "var(--pu-border)", "borderRadius": "2px"},
                        ),
                    ],
                ),
            ], style={"borderBottom": "1px solid var(--pu-border)"})
        )

    return Card(
        [
            CardHeader(html.H5("Projects", style={"color": "var(--pu-text)"})),
            html.P("30 done this month", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
            html.Table(
                [
                    html.Thead(html.Tr([
                        html.Th("COMPANIES"), html.Th("MEMBERS"), html.Th("BUDGET"), html.Th("COMPLETION"),
                    ])),
                    html.Tbody(rows),
                ],
                className="pu-table",
            ),
        ],
        style={"padding": "28px"},
    )


def _orders_overview():
    """Orders overview timeline (matches Purity UI)."""
    items = []
    for t in SAMPLE_TIMELINE:
        items.append(
            html.Div([
                html.Div(
                    html.I(className=t["icon"]),
                    className="pu-timeline-dot",
                    style={"backgroundColor": f"{t['color']}20", "color": t["color"]},
                ),
                html.Div([
                    html.H6(t["title"]),
                    html.P(t["desc"]),
                    html.Span(t["time"], className="pu-timeline-time"),
                ], className="pu-timeline-content"),
            ], className="pu-timeline-item")
        )

    return Card(
        [
            CardHeader(html.H5("Orders Overview", style={"color": "var(--pu-text)"})),
            html.P("24% this month", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
            html.Div(items),
        ],
        style={"padding": "28px"},
    )


# Import plotly.graph_objects for the combined chart
import plotly.graph_objects as go


def create_dashboard_layout():
    """Create the main Dashboard page matching Purity UI."""
    return html.Div(
        [
            _mini_stat_row(),
            # Row 2: Built by Developers + Work with Rockets
            html.Div(
                [_built_by_developers(), _work_with_rockets()],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1.8fr 1.2fr",
                    "gap": "24px",
                    "marginBottom": "26px",
                },
            ),
            # Row 3: Active Users + Sales Overview
            html.Div(
                [_active_users_chart(), _sales_overview_chart()],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1.3fr 1.7fr",
                    "gap": "24px",
                    "marginBottom": "26px",
                },
            ),
            # Row 4: Projects Table + Orders Timeline
            html.Div(
                [_projects_table(), _orders_overview()],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1.6fr 1.4fr",
                    "gap": "24px",
                },
            ),
        ],
    )
