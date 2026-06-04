"""Chart callbacks — EDA and report page updates."""
import json
import pandas as pd
from datetime import datetime
from dash import Input, Output, State, no_update, html
import plotly.graph_objects as go

from app.components.charts import line_chart, bar_chart, donut_chart


def register_callbacks(app):

    @app.callback(
        [Output("eda-distribution-chart", "figure"),
         Output("eda-boxplot-chart", "figure"),
         Output("eda-correlation-chart", "figure"),
         Output("eda-scatter-chart", "figure")],
        [Input("eda-columns", "value"),
         Input("eda-color-col", "value")],
        State("stored-raw-data", "data"),
    )
    def update_eda_charts(selected_columns, color_col, stored_data):
        empty = go.Figure()
        empty.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        if not stored_data or not selected_columns:
            return empty, empty, empty, empty

        df = pd.read_json(stored_data, orient="split")

        # Distribution
        dist = go.Figure()
        dist.add_trace(go.Histogram(x=df[selected_columns[0]], marker_color="#38B2AC", opacity=0.8))
        dist.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          title=dict(text=f"Distribution of {selected_columns[0]}", font=dict(color="white")),
                          margin=dict(l=24, r=24, t=40, b=24))

        # Box plot
        box = go.Figure()
        colors = ["#38B2AC", "#ECC94B", "#9F7AEA", "#ED64A6", "#4299E1"]
        for i, col in enumerate(selected_columns):
            box.add_trace(go.Box(y=df[col], name=col, marker_color=colors[i % len(colors)]))
        box.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         title=dict(text="Outlier Detection", font=dict(color="white")),
                         margin=dict(l=24, r=24, t=40, b=24))

        # Correlation
        try:
            numeric_df = df.select_dtypes(include="number")
            corr = numeric_df.corr()
            corr_fig = go.Figure(data=go.Heatmap(
                z=corr.values, x=corr.columns, y=corr.columns,
                colorscale="Teal", zmin=-1, zmax=1,
                text=corr.round(2).values, texttemplate="%{text}",
                textfont=dict(size=10),
            ))
            corr_fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                                  title=dict(text="Correlation Matrix", font=dict(color="white")),
                                  margin=dict(l=24, r=24, t=40, b=24),
                                  height=max(400, len(corr.columns) * 40))
        except Exception:
            corr_fig = empty

        # Scatter matrix
        scatter_cols = selected_columns[:4]
        scatter = go.Figure(data=go.Splom(
            dimensions=[dict(label=c, values=df[c]) for c in scatter_cols],
            marker=dict(color="#38B2AC", size=3, opacity=0.6),
        ))
        scatter.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                             title=dict(text="Scatter Matrix", font=dict(color="white")),
                             margin=dict(l=24, r=24, t=40, b=24),
                             height=max(500, len(scatter_cols) * 150))

        return dist, box, corr_fig, scatter

    @app.callback(
        [Output("report-preview", "children"),
         Output("download-md-btn", "disabled"),
         Output("download-pdf-btn", "disabled")],
        Input("pipeline-result", "data"),
    )
    def update_report(result_data):
        if not result_data:
            return html.P("Run the pipeline first.", style={"color": "var(--pu-text-muted)", "textAlign": "center", "padding": "40px"}), True, True

        insights = result_data.get("insights", [])
        profile = result_data.get("profile", {})

        sections = [
            html.H3("AutoAnalyst AI — Analysis Report", style={"color": "var(--pu-text)", "marginBottom": "8px"}),
            html.Small(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", style={"color": "var(--pu-text-muted)"}),
            html.Hr(className="pu-separator"),
            html.H4("Dataset Overview", style={"color": "var(--pu-text)", "marginBottom": "12px"}),
            html.Ul([
                html.Li(f"Rows: {profile.get('rows', 'N/A')}"),
                html.Li(f"Columns: {profile.get('columns', 'N/A')}"),
                html.Li(f"Missing: {profile.get('missing_values_total', 'N/A')}"),
            ], style={"color": "var(--pu-text-muted)", "marginBottom": "24px"}),
            html.H4("Key Insights", style={"color": "var(--pu-text)", "marginBottom": "12px"}),
            html.Ul([html.Li(i) for i in insights], style={"color": "var(--pu-text-muted)"}),
        ]
        return html.Div(sections), False, False

    @app.callback(
        Output("download-report", "data"),
        Input("download-md-btn", "n_clicks"),
        State("pipeline-result", "data"),
        prevent_initial_call=True,
    )
    def download_md(n_clicks, result_data):
        if not result_data:
            return no_update

        insights = result_data.get("insights", [])
        profile = result_data.get("profile", {})
        lines = [
            "# AutoAnalyst AI — Analysis Report",
            f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "\n## Dataset Overview\n",
            f"- Rows: {profile.get('rows', 'N/A')}",
            f"- Columns: {profile.get('columns', 'N/A')}",
            f"- Missing: {profile.get('missing_values_total', 'N/A')}",
            "\n## Key Insights\n",
        ]
        for i in insights:
            lines.append(f"- {i}")

        return dict(content="\n".join(lines), filename="autoanalyst_report.md")
