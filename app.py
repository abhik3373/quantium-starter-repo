import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# -------------------------------
# Load and prepare data
# -------------------------------
df = pd.read_csv("data/processed_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# -------------------------------
# Initialize Dash app
# -------------------------------
app = Dash(__name__)

# -------------------------------
# Layout
# -------------------------------
app.layout = html.Div(
    children=[
        html.H1(
            "Impact of Pink Morsel Price Increase on Sales",
            style={"textAlign": "center", "marginBottom": "20px"}
        ),

        html.Div(
            children=[
                html.Label("Select Region:", style={"fontWeight": "bold"}),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                ),
            ],
            style={"textAlign": "center", "marginBottom": "30px"}
        ),

        dcc.Graph(id="sales-line-chart")
    ],
    style={
        "maxWidth": "1100px",
        "margin": "0 auto",
        "padding": "20px",
        "fontFamily": "Arial"
    }
)

# -------------------------------
# Callback for region filtering
# -------------------------------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    return fig

# -------------------------------
# Run app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
