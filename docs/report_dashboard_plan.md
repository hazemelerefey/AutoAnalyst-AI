# Report & Dashboard Plan — Team 7

**Team:** Squad 7 — Reporting & Dashboard
**Members:** Member 13, Member 14
**Branch:** `feature/reporting-dashboard`
**Date:** 2026-06-03

---

## 1. Report Structure

The final auto-generated report will be a structured Markdown document with 10 sections. Each section is populated automatically from the pipeline results (`PipelineResult` dataclass in `src/autoanalyst/pipeline.py`).

### Section Breakdown

| # | Section | Source | Content |
|---|---------|--------|---------|
| 1 | **Executive Summary** | Auto-generated | One-paragraph overview of the dataset, key findings, and model performance |
| 2 | **Dataset Overview** | `PipelineResult.profile` | Row count, column count, data types, file name |
| 3 | **Data Profiling** | `PipelineResult.profile` + `missing_values_report` | Missing values table, duplicate count, data quality score |
| 4 | **EDA Results** | `PipelineResult.eda_results` | Numeric summary statistics, correlation highlights, distribution observations |
| 5 | **Preprocessing** | Pipeline config + cleaning log | Steps applied: duplicate removal, missing value strategy, encoding method |
| 6 | **Modeling** | `PipelineResult.model_results` | Task type, model name, train/test split, feature count |
| 7 | **Evaluation** | `PipelineResult.evaluation_results` | Accuracy/F1 (classification) or MAE/MSE/R² (regression), confusion matrix or residuals |
| 8 | **Insights** | `PipelineResult.insights` | Auto-generated bullet-point insights from the insight generator |
| 9 | **Recommendations** | Derived from insights + evaluation | Actionable next steps based on data quality and model performance |
| 10 | **Conclusion** | Auto-generated | Summary of what was learned and suggested next analysis steps |

### Report Format

- **Primary:** Markdown (.md) — clean, readable, version-controllable
- **Secondary:** PDF export (future enhancement via markdown-to-PDF conversion)
- **Charts:** Embedded as Plotly HTML or base64 PNG images

### Report Template Structure

```
# AutoAnalyst AI — Analysis Report
Generated: [timestamp]

## 1. Executive Summary
[Auto-generated paragraph]

## 2. Dataset Overview
- Rows: [N]
- Columns: [N]
- Data types: [breakdown]

## 3. Data Profiling
- Missing values: [count] ([percentage]%)
- Duplicate rows: [count]
- [Missing values table]

## 4. EDA Results
- [Numeric summary table]
- [Correlation highlights]
- [Key distribution observations]

## 5. Preprocessing
- Duplicates removed: [count]
- Missing value strategy: [strategy]
- Categorical encoding: [method]

## 6. Modeling
- Task: [classification/regression]
- Model: [model name]
- Train/Test split: [ratio]

## 7. Evaluation
- [Metrics table]
- [Confusion matrix or regression diagnostics]

## 8. Insights
- [Insight 1]
- [Insight 2]
- ...

## 9. Recommendations
- [Recommendation 1]
- [Recommendation 2]

## 10. Conclusion
[Summary paragraph]
```

---

## 2. Dashboard Page Structure

**Framework:** Dash by Plotly (production-grade, Python-only, interactive charts)
**Theme:** Dark mode (professional, modern)
**Layout:** Sidebar navigation + main content area

### Page Map

```
┌──────────┬───────────────────────────────────────────┐
│          │                                           │
│ SIDEBAR  │         MAIN CONTENT AREA                 │
│          │                                           │
│ Home     │  (content changes per page)               │
│ Upload   │                                           │
│ Profile  │                                           │
│ EDA      │                                           │
│ Models   │                                           │
│ Report   │                                           │
│          │                                           │
└──────────┴───────────────────────────────────────────┘
```

### Page Details

#### Page 1: Home (`/`)
- Project description and purpose
- Quick-start guide (5 steps)
- Feature highlight cards
- Recent analysis summary (if data loaded)

#### Page 2: Upload (`/upload`)
- Drag-and-drop file upload (CSV, Excel)
- URL input for remote datasets
- Auto-detect encoding and separator
- Preview table (first 10 rows)
- Column type detection display
- Target column selector (dropdown)
- Model task selector (auto / classification / regression)
- "Run Pipeline" button with loading spinner

#### Page 3: Data Profile (`/profile`)
- Summary metric cards: rows, columns, missing %, duplicates
- Column statistics table (name, type, missing count, unique values)
- Missing values bar chart (per column)
- Data type distribution pie chart
- Data quality score indicator

#### Page 4: EDA (`/eda`)
- Column selector (multi-select for numeric columns)
- Distribution plots: histogram + KDE per column
- Box plots for outlier detection
- Correlation heatmap (interactive, hover shows r-value)
- Scatter matrix (select 2-4 columns)
- Categorical column bar charts
- Target variable analysis chart

#### Page 5: Models (`/models`)
- Target column dropdown
- Task type selector (auto/classification/regression)
- Test size slider (0.1 – 0.5)
- "Train Model" button
- Results metrics table
- Confusion matrix heatmap (classification)
- ROC curve with AUC (classification)
- Residual plot (regression)
- Feature importance bar chart

#### Page 6: Report (`/report`)
- Auto-generated report preview (rendered Markdown)
- Download as Markdown button
- Download as PDF button (future)
- Analysis summary cards

---

## 3. User Flow

```
START
  │
  ▼
┌─────────────────────┐
│ 1. Open Dashboard   │ → Home page loads with overview
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 2. Upload Dataset   │ → User drags CSV or enters URL
│    Click "Run"      │ → Pipeline executes (loading spinner)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 3. View Profile     │ → Navigate to Profile page
│                     │ → See summary cards, missing values chart
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 4. Explore EDA      │ → Navigate to EDA page
│                     │ → Select columns, view distributions
│                     │ → Check correlations, outliers
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 5. Train Models     │ → Navigate to Models page
│                     │ → Select target, configure, train
│                     │ → View metrics, charts
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ 6. Download Report  │ → Navigate to Report page
│                     │ → Preview auto-generated report
│                     │ → Download as Markdown
└──────────┬──────────┘
           │
           ▼
         END
```

### Navigation Rules
- Sidebar visible on all pages
- URL routing: each page has a unique URL (`/upload`, `/profile`, etc.)
- Browser back/forward buttons work
- Data persists across page changes (stored in browser memory via `dcc.Store`)

### Error Handling
- Invalid file format → clear error toast
- Empty dataset → warning message
- Pipeline failure → error message with details, data preserved
- Missing columns for EDA → info message, graceful skip

---

## 4. Integration with Existing Pipeline

The dashboard does NOT duplicate any backend logic. It calls the central pipeline directly:

```python
from autoanalyst.pipeline import PipelineConfig, run_analysis_pipeline

# Upload callback calls this:
result = run_analysis_pipeline(df, PipelineConfig(target_column=target))

# Each page reads from result:
# Profile page  → result.profile, result.missing_values_report
# EDA page      → result.eda_results
# Models page   → result.model_results, result.evaluation_results
# Report page   → result.insights, result.report_path
```

### Module Mapping (Dashboard Page → Backend Module)

| Dashboard Page | Backend Module | Data Used |
|---|---|---|
| Upload | `data_loading/loader.py` | `load_csv()`, `load_excel()` |
| Profile | `data_profiling/profiler.py` | `generate_basic_profile()`, `get_missing_values_report()` |
| EDA | `eda/analyzer.py` | `get_numeric_summary()`, `get_correlation_matrix()` |
| Models | `modeling/` + `evaluation/` | `ClassificationModel`, `RegressionModel`, evaluators |
| Report | `reporting/report_generator.py` | `create_markdown_report()` |
| All | `pipeline.py` | `run_analysis_pipeline()` — single entry point |

---

## 5. Technology Stack

| Component | Choice | Reason |
|---|---|---|
| Framework | Dash 2.x | Python-only, production-grade, callback-based |
| Charts | Plotly 5.x | Interactive, publication-quality, dark theme |
| UI Kit | Dash Bootstrap Components | Professional cards, grids, modals |
| Theme | Dark mode (plotly_dark + custom CSS) | Modern, professional appearance |
| Server | Gunicorn | Production WSGI |
| Deploy | Docker + Railway/Render | One-click cloud deployment |
| Cache | Flask-Caching | Avoid re-running pipeline on page refresh |

### Why Dash over Streamlit

| Feature | Streamlit | Dash |
|---|---|---|
| Reruns | Entire script on every click | Only affected callbacks |
| URL routing | Limited | Full multi-page routing |
| Layout control | Minimal | Full CSS/Bootstrap control |
| Charts | Matplotlib (static) | Plotly (interactive) |
| Production use | Demo/staging | Production (Bloomberg, Siemens) |
| Dark theme | Manual CSS hacks | Built-in plotly_dark template |

---

## 6. File Structure

```
app/
├── app.py                    # Main Dash app + routing
├── config.py                 # Configuration
├── callbacks/
│   ├── upload.py             # File upload + pipeline execution
│   ├── profile.py            # Data profile display
│   ├── eda.py                # EDA chart generation
│   ├── models.py             # Model training + results
│   └── report.py             # Report generation + download
├── layouts/
│   ├── sidebar.py            # Navigation sidebar
│   ├── home.py               # Home page
│   ├── upload.py             # Upload page
│   ├── profile.py            # Profile page
│   ├── eda.py                # EDA page
│   ├── models.py             # Models page
│   └── report.py             # Report page
├── components/
│   ├── cards.py              # Stat cards
│   ├── charts.py             # Chart factory (consistent styling)
│   ├── tables.py             # Data tables
│   └── notifications.py      # Toast alerts
├── assets/
│   └── custom.css            # Dark theme CSS
└── Dockerfile

src/autoanalyst/              # UNTOUCHED — existing pipeline
```

---

## 7. Deliverables Checklist

- [x] Report outline with 10 sections
- [x] Dashboard page structure (6 pages)
- [x] User flow diagram
- [x] Integration mapping (dashboard → backend modules)
- [x] Technology stack decision (Dash over Streamlit)
- [x] File structure plan

---

## 8. Next Steps (Week 2)

Week 1 is planning. Week 2 starts implementation:
1. Set up Dash project structure (`app/` directory)
2. Build sidebar navigation
3. Implement Upload page (file upload + preview)
4. Connect to `run_analysis_pipeline()`
5. Display basic results on Profile page

---

## 9. End-to-End Integration Duty

Per `docs/team_roles.md`, Team 7's integration duty is:

> Use `run_analysis_pipeline` in the dashboard and avoid duplicating backend logic.

The dashboard calls `run_analysis_pipeline()` from `src/autoanalyst/pipeline.py` as its single entry point. No profiling, cleaning, EDA, modeling, or evaluation logic is reimplemented in the dashboard layer. All results are read from the `PipelineResult` dataclass.
