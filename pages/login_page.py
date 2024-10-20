# pages/login_page.py

import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, dcc, callback
import dash

# Login page layout
login_page_layout = dbc.Container(
    [
        # Header section
        dbc.Row(
            [
                dbc.Col(
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Home", href="/"),
                            dbc.DropdownMenuItem("Join", href="/join"),
                            dbc.DropdownMenuItem("Contact", href="/contact"),
                        ],
                        label=html.I(className="fas fa-ellipsis-h", style={"fontSize": "1.7em"}),
                        caret=False,
                        color="primary",
                        size="lg",
                        className="d-inline-block",
                        toggle_class_name="d-inline-block",
                        toggle_style={
                            "width": "50px", "height": "50px", "borderRadius": "15px",
                            "backgroundColor": "#d9534f", "color": "white",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)", "border": "none",
                            "display": "flex", "alignItems": "center", "justifyContent": "center",
                            "padding": "0"
                        }
                    ),
                    width="auto", style={"textAlign": "left", "marginTop": "10px"}, xs=2, sm=2, md=1, lg="auto"
                ),
                dbc.Col(
                    html.H1("CoDEx", className="text-right", 
                            style={"color": "#d9534f", "fontWeight": "bold", "fontSize": "2em"}),
                    width="auto", style={"textAlign": "right", "flex": "1"}
                ),
            ],
            align="center", justify="between", className="mb-4", style={"marginTop": "20px"}
        ),

        # Login form section
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H2("Login", className="text-center mb-4", 
                                        style={"fontWeight": "bold", "color": "#d9534f"}),
                                dbc.Input(id="username", placeholder="Username", type="text", className="mb-3"),
                                dbc.Input(id="password", placeholder="Password", type="password", className="mb-3"),
                                dbc.Button("Login", id="login-button", color="primary", className="d-block mx-auto",
                                           style={"width": "100%", "borderRadius": "30px"}),
                                dcc.Location(id='url-login', refresh=True)  # This will update the URL on successful login
                            ]
                        ),
                        style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)", "borderRadius": "12px", "backgroundColor": "#ffffff"},
                        className="p-4"
                    ),
                    xs=10, sm=8, md=6, lg=4, xl=3  # Responsive widths for the login card
                )
            ],
            justify="center", align="center", style={"minHeight": "70vh"}
        ),
    ],
    fluid=True, style={"backgroundColor": "#f8f9fa", "padding": "0px 20px"}
)

# Hardcoded usernames and passwords
VALID_USERS = {
    'seller': 'sellerpass',
    'buyer': 'buyerpass'
}

# Login callback
@callback(
    Output('url-login', 'href'),
    Input('login-button', 'n_clicks'),
    State('username', 'value'),
    State('password', 'value'),
    prevent_initial_call=True  # Prevent callback from triggering on page load
)
def login(n_clicks, username, password):
    if n_clicks:
        if username in VALID_USERS and VALID_USERS[username] == password:
            # Redirect to the appropriate page
            return f'/pages/{username}'
        else:
            # Stay on the login page if credentials are invalid
            return '/login'
    return dash.no_update
