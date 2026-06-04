"""Auth pages — Sign In / Sign Up matching Purity UI."""
from dash import html


def create_signin_layout():
    """Sign In page matching Purity UI auth design."""
    return html.Div([
        html.Div([
            # Left side — form
            html.Div([
                html.Div([
                    html.H3("Nice to see you!", style={"color": "var(--pu-text)", "fontWeight": "700", "marginBottom": "8px"}),
                    html.P("Enter your email and password to sign in", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "32px"}),
                    html.Div([
                        html.Label("Email", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                        html.Input(type="email", placeholder="Your email address", className="pu-input", style={"marginBottom": "24px"}),
                    ]),
                    html.Div([
                        html.Label("Password", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                        html.Input(type="password", placeholder="Your password", className="pu-input", style={"marginBottom": "24px"}),
                    ]),
                    html.Div([
                        html.Button(className="pu-theme-toggle active", id="remember-toggle"),
                        html.Span("Remember me", style={"color": "var(--pu-text)", "fontSize": "14px", "marginLeft": "12px"}),
                    ], style={"display": "flex", "alignItems": "center", "marginBottom": "24px"}),
                    html.Button("SIGN IN", className="pu-btn pu-btn-primary", style={"width": "100%", "padding": "12px", "marginBottom": "16px"}),
                    html.Div([
                        html.Span("Don't have an account? ", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}),
                        html.A("Sign up", href="/auth/signup", style={"color": "#38B2AC", "fontSize": "14px", "fontWeight": "700", "textDecoration": "none"}),
                    ], style={"textAlign": "center"}),
                ], style={"maxWidth": "400px", "width": "100%"}),
            ], style={"flex": "1", "display": "flex", "alignItems": "center", "justifyContent": "center", "padding": "40px"}),
            # Right side — gradient with image
            html.Div([
                html.Div([
                    html.H3("Discover the autoanalyst.", style={"color": "white", "fontSize": "28px", "fontWeight": "700", "marginBottom": "16px"}),
                    html.P("Automated AI-powered data analyst system. Upload datasets, run analysis, train models, and generate reports — all in one platform.", style={"color": "rgba(255,255,255,0.7)", "fontSize": "16px", "lineHeight": "1.6"}),
                ], style={"padding": "40px"}),
            ], style={"flex": "1", "background": PROFILE_BG, "borderRadius": "0 15px 15px 0", "display": "flex", "alignItems": "center", "justifyContent": "center"}),
        ], style={"display": "flex", "minHeight": "100vh", "background": "var(--pu-bg)"}),
    ])


def create_signup_layout():
    """Sign Up page matching Purity UI auth design."""
    return html.Div([
        html.Div([
            # Left side — gradient
            html.Div([
                html.Div([
                    html.H3("Welcome!", style={"color": "white", "fontSize": "28px", "fontWeight": "700", "marginBottom": "16px"}),
                    html.P("Use these awesome forms to login or create new account in your project for free.", style={"color": "rgba(255,255,255,0.7)", "fontSize": "16px", "lineHeight": "1.6"}),
                ], style={"padding": "40px"}),
            ], style={"flex": "1", "background": PROFILE_BG, "borderRadius": "15px 0 0 15px", "display": "flex", "alignItems": "center", "justifyContent": "center"}),
            # Right side — form
            html.Div([
                html.Div([
                    html.H3("Register", style={"color": "var(--pu-text)", "fontWeight": "700", "marginBottom": "8px"}),
                    html.P("Enter your email and password to register", style={"color": "var(--pu-text-muted)", "fontSize": "14px", "marginBottom": "32px"}),
                    html.Div([
                        html.Label("Name", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                        html.Input(type="text", placeholder="Your full name", className="pu-input", style={"marginBottom": "24px"}),
                    ]),
                    html.Div([
                        html.Label("Email", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                        html.Input(type="email", placeholder="Your email address", className="pu-input", style={"marginBottom": "24px"}),
                    ]),
                    html.Div([
                        html.Label("Password", style={"color": "var(--pu-text)", "fontSize": "14px", "fontWeight": "500", "marginBottom": "8px", "display": "block"}),
                        html.Input(type="password", placeholder="Your password", className="pu-input", style={"marginBottom": "24px"}),
                    ]),
                    html.Div([
                        html.Button(className="pu-theme-toggle active", id="terms-toggle"),
                        html.Span("I agree the Terms and Conditions", style={"color": "var(--pu-text)", "fontSize": "14px", "marginLeft": "12px"}),
                    ], style={"display": "flex", "alignItems": "center", "marginBottom": "24px"}),
                    html.Button("SIGN UP", className="pu-btn pu-btn-primary", style={"width": "100%", "padding": "12px", "marginBottom": "16px"}),
                    html.Div([
                        html.Span("Already have an account? ", style={"color": "var(--pu-text-muted)", "fontSize": "14px"}),
                        html.A("Sign in", href="/auth/signin", style={"color": "#38B2AC", "fontSize": "14px", "fontWeight": "700", "textDecoration": "none"}),
                    ], style={"textAlign": "center"}),
                ], style={"maxWidth": "400px", "width": "100%"}),
            ], style={"flex": "1", "display": "flex", "alignItems": "center", "justifyContent": "center", "padding": "40px"}),
        ], style={"display": "flex", "minHeight": "100vh", "background": "var(--pu-bg)"}),
    ])


PROFILE_BG = "linear-gradient(81.62deg, #313860 2.25%, #151928 79.87%)"
