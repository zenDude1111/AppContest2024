# pages/seller_page.py

import dash_bootstrap_components as dbc
from dash import html

# Seller page layout with header and cards
buyer_page_layout = dbc.Container(
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
                        label=html.I(className="fas fa-ellipsis-h", style={"fontSize": "1.7em"}),  # Font size matches main page
                        caret=False,
                        color="primary",
                        size="lg",
                        className="d-inline-block",
                        toggle_class_name="d-inline-block",
                        toggle_style={
                            "width": "50px", "height": "50px", "borderRadius": "15px",  # Adjusted to match main page
                            "backgroundColor": "#d9534f",
                            "color": "white",
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                            "border": "none",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",  # Center the icon within the button
                            "padding": "0"  # Ensure the padding doesn't affect centering
                        }
                    ),
                    width="auto",
                    style={"textAlign": "left", "marginTop": "10px"},  # Consistent margin to match main page
                    xs=2, sm=2, md=1, lg="auto"  # Responsive column widths
                ),
                dbc.Col(
                    html.H1("CoDEx", className="text-right", style={"color": "#d9534f", "fontWeight": "bold", "fontSize": "2em"}),  # Title matches main page
                    width="auto",
                    style={"textAlign": "right", "flex": "1"},
                    xs=10, sm=10, md=11, lg="auto"  # Responsive column widths
                ),
            ],
            align="center",
            justify="between",
            className="mb-4",
            style={"marginTop": "20px"}  # Consistent top margin to align properly with main page
        ),

        # Page Welcome Header
        dbc.Row(
            dbc.Col(
                html.H2("Welcome STEPHEN", className="text-center mb-4", style={"fontWeight": "bold", "color": "#d9534f"}),
                width=12
            ),
            className="mb-4"
        ),

        # Cards Section with Snapshots
        dbc.Row(
            [
                # Snapshot of Notifications Card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Notifications Snapshot", className="card-title text-center", style={"fontWeight": "bold"}),
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
                    xs=12, sm=6, md=4  # Responsive column widths for notifications card
                ),

                # Snapshot of Your Metrics Card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Your Metrics Snapshot", className="card-title text-center", style={"fontWeight": "bold"}),
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
                    xs=12, sm=6, md=4  # Responsive column widths for metrics card
                ),

                # Snapshot of Linked Accounts Card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Linked Accounts Snapshot", className="card-title text-center", style={"fontWeight": "bold"}),
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
                    xs=12, sm=6, md=4  # Responsive column widths for linked accounts card
                ),
            ],
            justify="center",
            className="mb-4"
        ),
    ],
    fluid=True,
    style={"backgroundColor": "#f8f9fa", "padding": "0px 20px"}  # Consistent padding to match main page
)
