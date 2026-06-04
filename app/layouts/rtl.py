"""RTL page — Purity UI Arabic layout."""
from dash import html
from app.components.card import Card, CardBody, CardHeader
from app.components.mini_stat import MiniStatistics


def create_rtl_layout():
    """RTL page matching Purity UI's Arabic layout."""
    return html.Div(dir="rtl", children=[
        # Mini stats in Arabic
        html.Div([
            MiniStatistics("أموال اليوم", "$53,000", 55, html.I(className="bi bi-wallet2"), "#38B2AC"),
            MiniStatistics("المستخدمون اليوم", "2,300", 5, html.I(className="bi bi-globe"), "#38B2AC"),
            MiniStatistics("عملاء جدد", "+3,020", -14, html.I(className="bi bi-file-earmark"), "#38B2AC"),
            MiniStatistics("المبيعات الكلية", "$173,000", 8, html.I(className="bi bi-cart3"), "#38B2AC"),
        ], style={
            "display": "grid",
            "gridTemplateColumns": "repeat(auto-fit, minmax(220px, 1fr))",
            "gap": "24px",
            "marginBottom": "26px",
        }),
        # Info card in Arabic
        Card([
            html.Div([
                html.Div([
                    html.P("بواسطة المطورين", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "8px"}),
                    html.H4("لوحة القيادة", style={"color": "var(--pu-text)", "fontSize": "22px", "fontWeight": "700", "marginBottom": "12px"}),
                    html.P("من الألوان والبطاقات والطباعة إلى العناصر المعقدة ، ستجد الوثائق الكاملة.", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "24px", "lineHeight": "1.6"}),
                    html.A("اقرأ المزيد", href="#", className="pu-btn pu-btn-primary", style={"fontSize": "14px"}),
                ], style={"flex": "1", "paddingRight": "24px"}),
                html.Div(
                    html.I(className="bi bi-bar-chart-line", style={"fontSize": "80px", "color": "var(--pu-accent)", "opacity": "0.3"}),
                    style={"display": "flex", "alignItems": "center", "justifyContent": "center", "minWidth": "200px"},
                ),
            ], style={"display": "flex", "alignItems": "center"}),
        ], style={"padding": "28px", "marginBottom": "24px"}),
        # Projects table in Arabic
        Card([
            CardHeader(html.H5("المشاريع", style={"color": "var(--pu-text)"})),
            html.P("30 مشروع مكتمل هذا الشهر", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "16px"}),
            html.Table([
                html.Thead(html.Tr([html.Th("الشركات"), html.Th("الأعضاء"), html.Th("الميزانية"), html.Th("الإنجاز")])),
                html.Tbody([
                    html.Tr([html.Td("نسخة Chakra Soft UI"), html.Td("3"), html.Td("$14,000"), html.Td("60%")], style={"borderBottom": "1px solid var(--pu-border)"}),
                    html.Tr([html.Td("إضافة تقدم المسار"), html.Td("2"), html.Td("$3,000"), html.Td("10%")], style={"borderBottom": "1px solid var(--pu-border)"}),
                    html.Tr([html.Td("إصلاح أخطاء المنصة"), html.Td("3"), html.Td("غير محدد"), html.Td("100%")], style={"borderBottom": "1px solid var(--pu-border)"}),
                    html.Tr([html.Td("إطلاق تطبيق الجوال"), html.Td("2"), html.Td("$32,000"), html.Td("100%")]),
                ]),
            ], className="pu-table"),
        ], style={"padding": "28px"}),
    ], style={"paddingTop": "120px"})
