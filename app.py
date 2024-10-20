# app.py

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
from flask import Flask

# Import the login and seller page layouts from the pages directory
from pages.login_page import login_page_layout
from pages.seller_page import seller_page_layout
from pages.buyer_page import buyer_page_layout

# Initialize Flask server
server = Flask(__name__)

# Initialize Dash app with additional stylesheet for icons
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[
        dbc.themes.JOURNAL,
        "https://use.fontawesome.com/releases/v5.15.4/css/all.css",
    ]
)
app.config.suppress_callback_exceptions = True  # Allow dynamic page content

# Define the color palette used across the app
MODERN_COLOR_PALETTE = {
    "primary": "#d9534f",
    "secondary": "#6c757d",
    "background": "#ffffff",
    "card_bg": "#d9534f",
    "text": "#ffffff"
}

# Header layout
header_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Home", href="/"),
                            dbc.DropdownMenuItem("Login", href="/login"),
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
                            "backgroundColor": MODERN_COLOR_PALETTE["primary"],
                            "color": "white", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                            "border": "none", "display": "flex", "alignItems": "center",
                            "justifyContent": "center", "padding": "0"
                        }
                    ),
                    width="auto", style={"textAlign": "left", "marginTop": "10px"},
                    xs=2, sm=2, md=1, lg="auto"
                ),
                dbc.Col(
                    html.H1(
                        "CoDEx", 
                        className="text-right", 
                        style={"color": MODERN_COLOR_PALETTE["primary"], "fontWeight": "bold"}
                    ),
                    width="auto", style={"textAlign": "right", "flex": "1"}
                ),
            ],
            align="center", justify="between", className="mb-4"
        )
    ],
    fluid=True
)

# Full landing page layout with all cards
landing_page_layout = dbc.Container(
    [
        html.H1(
            "Cooperative Data Exchange", 
            className="text-center", 
            style={"color": MODERN_COLOR_PALETTE["primary"], "fontSize": "2.5em"}
        ),
        html.P(
            "A Human Potential Coop", 
            className="text-center", 
            style={"color": MODERN_COLOR_PALETTE["primary"], "fontSize": "1.5em"}
        ),
        # Mission Statement Card
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("Mission Statement", className="card-title text-center", style={"color": MODERN_COLOR_PALETTE["text"]}),
                    html.P(
                        "Our mission is to empower individuals and organizations to exchange data ethically through a cooperative platform.",
                        className="text-center", style={"color": MODERN_COLOR_PALETTE["text"]}
                    )
                ]
            ),
            className="mt-4",
            style={"backgroundColor": MODERN_COLOR_PALETTE["card_bg"], "borderRadius": "12px"}
        ),
        # How It Works Card
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("How It Works", className="card-title text-center", style={"color": MODERN_COLOR_PALETTE["text"]}),
                    html.P(
                        "Participants share data securely, while buyers access it via smart contracts. Transactions are transparent and fair.",
                        className="text-center", style={"color": MODERN_COLOR_PALETTE["text"]}
                    )
                ]
            ),
            className="mt-4",
            style={"backgroundColor": MODERN_COLOR_PALETTE["card_bg"], "borderRadius": "12px"}
        ),
        # Get Started Card
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("Get Started", className="card-title text-center", style={"color": MODERN_COLOR_PALETTE["text"]}),
                    html.P(
                        "Sign up today to join the Co-Dex community and start exchanging data.",
                        className="text-center", style={"color": MODERN_COLOR_PALETTE["text"]}
                    ),
                    dbc.Button(
                        "Join Now", 
                        color="primary", 
                        href="/join", 
                        className="d-block mx-auto", 
                        size="sm", 
                        style={
                            "width": "fit-content", 
                            "borderRadius": "30px", 
                            "backgroundColor": MODERN_COLOR_PALETTE["primary"],
                            "color": "white", 
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"
                        }
                    )
                ]
            ),
            className="mt-4",
            style={"backgroundColor": MODERN_COLOR_PALETTE["card_bg"], "borderRadius": "12px"}
        ),
    ],
    fluid=True, 
    style={"marginTop": "5%", "backgroundColor": MODERN_COLOR_PALETTE["background"]}
)

# App layout with routing
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={"padding": "20px", "backgroundColor": MODERN_COLOR_PALETTE["background"]})
])

# Callback to manage routing between pages
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/login':
        return login_page_layout
    elif pathname == '/pages/seller':
        return seller_page_layout
    elif pathname == '/pages/buyer':
        return buyer_page_layout
    else:
        return [header_layout, landing_page_layout]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
