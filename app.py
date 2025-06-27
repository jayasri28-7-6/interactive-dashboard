import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# --- 1. Load Data ---
# Try to load the data, if not found, instruct the user to generate it
try:
    df = pd.read_csv('sales_data.csv')
    # Convert Date column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    print("Data loaded successfully for Dash app.")
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Please run 'python data_generator.py' first.")
    exit() # Exit if data is not available
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# --- 2. Initialize the Dash app ---
app = dash.Dash(__name__)

# --- 3. Define the App Layout ---
app.layout = html.Div(
    className="min-h-screen bg-gray-100 p-8 flex flex-col items-center font-sans",
    style={'fontFamily': 'Inter, sans-serif'},
    children=[
        # Header Section
        html.Div(
            className="w-full max-w-6xl bg-white shadow-xl rounded-lg p-6 mb-8 text-center",
            children=[
                html.H1(
                    "Interactive Sales Performance Dashboard",
                    className="text-4xl font-extrabold text-gray-800 mb-2"
                ),
                html.P(
                    "Analyze sales trends, product performance, and regional profitability.",
                    className="text-lg text-gray-600"
                )
            ]
        ),

        # Controls Section (Filters)
        html.Div(
            className="w-full max-w-6xl bg-white shadow-lg rounded-lg p-6 mb-8 flex flex-wrap justify-center gap-6",
            children=[
                html.Div(
                    className="flex-1 min-w-[250px]",
                    children=[
                        html.Label("Filter by Region:", className="block text-gray-700 text-md font-medium mb-2"),
                        dcc.Dropdown(
                            id='region-dropdown',
                            options=[{'label': 'All Regions', 'value': 'All'}] +
                                    [{'label': region, 'value': region} for region in df['Region'].unique()],
                            value='All',
                            clearable=False,
                            className="rounded-md shadow-sm"
                        )
                    ]
                ),
                html.Div(
                    className="flex-1 min-w-[250px]",
                    children=[
                        html.Label("Filter by Product Category:", className="block text-gray-700 text-md font-medium mb-2"),
                        dcc.Dropdown(
                            id='category-dropdown',
                            options=[{'label': 'All Categories', 'value': 'All'}] +
                                    [{'label': category, 'value': category} for category in df['ProductCategory'].unique()],
                            value='All',
                            clearable=False,
                            className="rounded-md shadow-sm"
                        )
                    ]
                )
            ]
        ),

        # Dashboard Visualizations
        html.Div(
            className="w-full max-w-6xl grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
            children=[
                # Sales Over Time Chart
                html.Div(
                    className="bg-white shadow-lg rounded-lg p-4",
                    children=[
                        html.H3("Sales Over Time", className="text-xl font-semibold text-gray-800 mb-4 text-center"),
                        dcc.Graph(id='sales-over-time-chart', className="h-[300px]")
                    ]
                ),
                # Sales by Product Category Chart
                html.Div(
                    className="bg-white shadow-lg rounded-lg p-4",
                    children=[
                        html.H3("Sales by Product Category", className="text-xl font-semibold text-gray-800 mb-4 text-center"),
                        dcc.Graph(id='sales-by-category-chart', className="h-[300px]")
                    ]
                ),
                # Profit by Region Chart
                html.Div(
                    className="bg-white shadow-lg rounded-lg p-4",
                    children=[
                        html.H3("Profit by Region", className="text-xl font-semibold text-gray-800 mb-4 text-center"),
                        dcc.Graph(id='profit-by-region-chart', className="h-[300px]")
                    ]
                ),
            ]
        ),

        # Footer
        html.Div(
            className="w-full max-w-6xl mt-8 text-center text-gray-500 text-sm",
            children=[
                html.P("Dashboard developed using Plotly Dash and Tailwind CSS for styling.")
            ]
        )
    ]
)

# --- 4. Define Callbacks for Interactivity ---
@app.callback(
    Output('sales-over-time-chart', 'figure'),
    Output('sales-by-category-chart', 'figure'),
    Output('profit-by-region-chart', 'figure'),
    Input('region-dropdown', 'value'),
    Input('category-dropdown', 'value')
)
def update_charts(selected_region, selected_category):
    filtered_df = df.copy()

    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['ProductCategory'] == selected_category]

    # Sales Over Time
    sales_over_time_df = filtered_df.groupby(pd.Grouper(key='Date', freq='M'))['Sales'].sum().reset_index()
    fig_sales_time = px.line(
        sales_over_time_df,
        x='Date',
        y='Sales',
        title='Monthly Sales Trend',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig_sales_time.update_layout(
        margin={"t":40,"b":20,"l":20,"r":20},
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis_title=None, yaxis_title=None,
        hovermode="x unified"
    )

    # Sales by Product Category
    sales_by_category_df = filtered_df.groupby('ProductCategory')['Sales'].sum().reset_index()
    fig_sales_category = px.bar(
        sales_by_category_df.sort_values('Sales', ascending=False),
        x='ProductCategory',
        y='Sales',
        title='Total Sales by Product Category',
        color='ProductCategory',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig_sales_category.update_layout(
        margin={"t":40,"b":20,"l":20,"r":20},
        plot_bgcolor='white', paper_bgcolor='white',
        xaxis_title=None, yaxis_title=None
    )

    # Profit by Region
    profit_by_region_df = filtered_df.groupby('Region')['Profit'].sum().reset_index()
    fig_profit_region = px.pie(
        profit_by_region_df,
        values='Profit',
        names='Region',
        title='Profit Distribution by Region',
        hole=0.4, # Donut chart
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig_profit_region.update_traces(textposition='inside', textinfo='percent+label')
    fig_profit_region.update_layout(
        margin={"t":40,"b":20,"l":20,"r":20},
        plot_bgcolor='white', paper_bgcolor='white',
    )


    return fig_sales_time, fig_sales_category, fig_profit_region

# --- 5. Run the App ---
if __name__ == '__main__':
    app.run_server(debug=True)
