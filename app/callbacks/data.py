"""Data callbacks — upload + pipeline execution."""
import base64
import io
from pathlib import Path
import pandas as pd
from dash import Input, Output, State, html, no_update
from app.components.card import Card, CardBody, CardHeader

from autoanalyst.pipeline import PipelineConfig, run_analysis_pipeline


def register_callbacks(app):

    @app.callback(
        [Output("stored-raw-data", "data"),
         Output("target-column", "options"),
         Output("model-target-col", "options"),
         Output("dataset-preview", "children"),
         Output("run-pipeline-btn", "disabled"),
         Output("pipeline-status", "children")],
        Input("upload-data", "contents"),
        State("upload-data", "filename"),
        prevent_initial_call=True,
    )
    def handle_upload(contents, filename):
        if not contents:
            return no_update, no_update, no_update, no_update, True, ""

        try:
            content_type, content_string = contents.split(",")
            decoded = base64.b64decode(content_string)
            suffix = Path(filename).suffix.lower()

            if suffix == ".csv":
                df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
            elif suffix in (".xlsx", ".xls"):
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return no_update, no_update, no_update, html.P("Unsupported file format.", style={"color": "#F56565"}), True, ""

            col_options = [{"label": c, "value": c} for c in df.columns]
            stored = df.to_json(date_format="iso", orient="split")

            preview = Card([
                CardHeader(html.H5(f"Preview — {df.shape[0]} rows × {df.shape[1]} columns", style={"color": "var(--pu-text)"})),
                html.Table([
                    html.Thead(html.Tr([html.Th(c) for c in df.columns[:8]])),
                    html.Tbody([html.Tr([html.Td(str(v)) for v in row[:8]]) for _, row in df.head(5).iterrows()]),
                ], className="pu-table"),
            ], style={"padding": "28px"})

            return stored, col_options, col_options, preview, False, ""

        except Exception as e:
            return no_update, no_update, no_update, html.P(f"Error: {e}", style={"color": "#F56565"}), True, ""

    @app.callback(
        [Output("pipeline-result", "data"),
         Output("pipeline-status", "children", allow_duplicate=True)],
        Input("run-pipeline-btn", "n_clicks"),
        [State("stored-raw-data", "data"),
         State("target-column", "value"),
         State("model-task", "value")],
        prevent_initial_call=True,
    )
    def run_pipeline(n_clicks, stored_data, target_col, model_task):
        if not stored_data:
            return no_update, html.P("No data uploaded.", style={"color": "#F56565"})

        try:
            df = pd.read_json(stored_data, orient="split")
            config = PipelineConfig(
                target_column=target_col or None,
                model_task=model_task or "auto",
            )
            result = run_analysis_pipeline(df, config)

            result_data = {
                "raw_df": result.raw_df.to_json(date_format="iso", orient="split"),
                "cleaned_df": result.cleaned_df.to_json(date_format="iso", orient="split"),
                "profile": result.profile,
                "missing_values_report": result.missing_values_report.to_json(date_format="iso", orient="split"),
                "eda_results": {
                    k: v.to_json(date_format="iso", orient="split") if hasattr(v, "to_json") else v
                    for k, v in result.eda_results.items()
                },
                "insights": result.insights,
                "model_results": result.model_results,
                "evaluation_results": result.evaluation_results,
                "warnings": result.warnings,
            }

            return result_data, html.P(f"Pipeline complete! {len(result.insights)} insights generated.", style={"color": "#48BB78"})

        except Exception as e:
            return no_update, html.P(f"Pipeline failed: {e}", style={"color": "#F56565"})
