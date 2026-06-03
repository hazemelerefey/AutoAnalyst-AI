# Week 01 Update

## Week Objective
- Prepare the team, repository, workflow, and project documentation so all 7 sub-teams can start working professionally.

## Completed Tasks
- Project structure and team assignments reviewed
- Dashboard technology selected (Dash by Plotly over Streamlit)
- Report and dashboard plan documented

## Team Progress

### Team 1: Project Management & GitHub
-

### Team 2: Data Understanding & Profiling
-

### Team 3: EDA & Visualization
-

### Team 4: Preprocessing & Feature Engineering
-

### Team 5: Machine Learning
-

### Team 6: Evaluation & Insights
-

### Team 7: Reporting & Dashboard
- Designed report structure with 10 sections (Executive Summary through Conclusion)
- Planned dashboard architecture: 6 pages (Home, Upload, Profile, EDA, Models, Report)
- Selected Dash by Plotly as dashboard framework (production-grade, Python-only, interactive charts)
- Mapped dashboard pages to existing backend modules (pipeline.py integration)
- Defined user flow: Upload → Profile → EDA → Models → Report
- Created `docs/report_dashboard_plan.md` with full plan

## Files Created or Updated
- `docs/report_dashboard_plan.md` — Report outline, dashboard page structure, user flow, tech stack

## Pull Request Links
-

## Challenges / Blockers
- None for Week 1

## Decisions Made
- Dashboard framework: Dash by Plotly (not Streamlit) — production-grade, interactive charts, multi-page routing
- Theme: Dark mode (plotly_dark + custom CSS)
- Report format: Primary Markdown, secondary PDF (future)
- Dashboard wraps existing `pipeline.py` — no backend logic duplicated

## Next Week Plan
- Set up Dash project structure (`app/` directory)
- Build sidebar navigation
- Implement Upload page with file upload and preview
- Connect to `run_analysis_pipeline()`
- Display basic results on Profile page

## Team Notes
- Team 7 is ready to start implementation in Week 2
