# pages/seller_page.py

import dash_bootstrap_components as dbc
from dash import html

# Seller page layout with header and vertically stacked cards
seller_page_layout = dbc.Container(
    [
        # Header section with menu button and CoDEx title
        dbc.Row(
            [
                dbc.Col(
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Home", href="/"),
                            dbc.DropdownMenuItem("Notifications", href="/notifications"),
                            dbc.DropdownMenuItem("Your Metrics", href="/metrics"),
                            dbc.DropdownMenuItem("Linked Accounts", href="/linked-accounts"),
                            dbc.DropdownMenuItem("Logout", href="/logout"),
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
                    html.H1(
                        "CoDEx", 
                        className="text-right", 
                        style={"color": "#d9534f", "fontWeight": "bold", "fontSize": "2em"}
                    ),
                    width="auto", style={"textAlign": "right", "flex": "1"}, xs=10, sm=10, md=11, lg="auto"
                ),
            ],
            align="center", justify="between", className="mb-4", style={"marginTop": "20px"}
        ),

        # Page Welcome Header
        dbc.Row(
            dbc.Col(
                html.H2(
                    "Welcome STEPHEN", 
                    className="text-center mb-4", 
                    style={"fontWeight": "bold", "color": "#d9534f"}
                ),
                width=12
            ),
            className="mb-4"
        ),

        # Notifications Card
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                "Notifications Snapshot", 
                                className="card-title text-center", 
                                style={"fontWeight": "bold"}
                            ),
                            html.P(
                                "You have 3 new notifications.",
                                className="text-center", 
                                style={"color": "#6c757d"}
                            ),
                        ]
                    ),
                    style={
                        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)", 
                        "borderRadius": "12px", 
                        "backgroundColor": "#ffffff"
                    },
                    className="p-3 mb-4"
                ),
                width=12  # Full-width card to stack vertically
            )
        ),

        # Your Metrics Card
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                "Your Metrics Snapshot", 
                                className="card-title text-center", 
                                style={"fontWeight": "bold"}
                            ),
                            html.P(
                                "Your metrics are up to date.",
                                className="text-center", 
                                style={"color": "#6c757d"}
                            ),
                        ]
                    ),
                    style={
                        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)", 
                        "borderRadius": "12px", 
                        "backgroundColor": "#ffffff"
                    },
                    className="p-3 mb-4"
                ),
                width=12  # Full-width card to stack vertically
            )
        ),

        # Linked Accounts Card
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                "Linked Accounts Snapshot", 
                                className="card-title text-center", 
                                style={"fontWeight": "bold"}
                            ),
                            html.P(
                                "2 accounts linked.",
                                className="text-center", 
                                style={"color": "#6c757d"}
                            ),
                        ]
                    ),
                    style={
                        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)", 
                        "borderRadius": "12px", 
                        "backgroundColor": "#ffffff"
                    },
                    className="p-3 mb-4"
                ),
                width=12  # Full-width card to stack vertically
            )
        ),
    ],
    fluid=True,
    style={"backgroundColor": "#f8f9fa", "padding": "0px 20px"}
)
