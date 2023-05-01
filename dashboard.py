import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

#---------------------------------------------------------------#
#DATAFRAMES DF DATASETS 

placement = pd.read_csv("dash_data/placements.csv")
scores = pd.read_csv("dash_data/scores.csv")
melted = pd.read_csv('dash_data/melted_scores.csv')

placement_col = ['bottom', 'low', 'safe', 'high', 'semiwin', 'win']

placement = placement.drop(columns=['Unnamed: 0'])

table_header = [html.Th(col) for col in placement.columns]

table_body = [html.Tr([html.Td(placement.iloc[i][col]) for col in placement.columns]) for i in range(len(placement))]


#---------------------------------------------------------------#
#STYLING
dark_template = {
    "layout": {
        "plot_bgcolor": "#1f2630",
        "paper_bgcolor": "#1f2630",
        "font": {"color": "#ffffff"}
    }
}

external_stylesheets = [
    {
        'href': 'file.css', 
        'rel':'stylesheet',
        'integrity':'sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor',
        'crossorigin':'anonymous'
     }
]

#SIDEBAR STYLE
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#fdf9de",
}

#CONTENT STYLE
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'backgroundColor':'#faeeeb',
}

#---------------------------------------------------------------#
#APP INITIALIZATION
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
server = app.server
#---------------------------------------------------------------#
#HEADER

header = html.Div([
    html.H1("You're a Winner, Baby!"),
    html.H2("A RuPaul's Drag Race Dashboard for Finalists"),
])

#---------------------------------------------------------------#
#FOOTER

footer = html.Div()

#---------------------------------------------------------------#
#GRAPHS PLOTS
content = dbc.Container(
    [
#opening text
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        """ 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc a est consequat, posuere purus sed, pharetra nulla. 
                            Morbi tempus eget mi lacinia semper. Quisque ut laoreet risus, quis semper urna. Nam quis tristique dolor. 
                            Nunc efficitur consequat aliquam. Aliquam erat volutpat. Pellentesque sit amet laoreet dui. 
                            Morbi id sapien sed sem tempor dignissim eget in neque. Sed sapien lacus, ornare a cursus et, commodo a tortor. 
                            Sed vel ipsum consectetur, vestibulum ipsum id, dictum elit. 
                            Nulla tempor, lacus vel elementum ultrices, arcu diam scelerisque augue, quis consequat elit tellus non ante. 
                            Aliquam magna quam, vestibulum sit amet tempus congue, molestie ultrices sem.
                            """),
                    width = 4,
                ),
                dbc.Col(
                    html.Div(
                        """ 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc a est consequat, posuere purus sed, pharetra nulla. 
                            Morbi tempus eget mi lacinia semper. Quisque ut laoreet risus, quis semper urna. Nam quis tristique dolor. 
                            Nunc efficitur consequat aliquam. Aliquam erat volutpat. Pellentesque sit amet laoreet dui. 
                            Morbi id sapien sed sem tempor dignissim eget in neque. Sed sapien lacus, ornare a cursus et, commodo a tortor. 
                            Sed vel ipsum consectetur, vestibulum ipsum id, dictum elit. 
                            Nulla tempor, lacus vel elementum ultrices, arcu diam scelerisque augue, quis consequat elit tellus non ante. 
                            Aliquam magna quam, vestibulum sit amet tempus congue, molestie ultrices sem.
                            """),
                    width = 8,
                ),

            ],
            className="mt-4 mb-4",
        ),

#SCATTER PLOT 
        dbc.Row(
            [
                        html.H2('Score and Placement Scatter Plot'),
                dbc.Col(
                    [

                        dcc.Graph(id="scatter-plot"),
                        
                    ], width = 7,
                ),

                dbc.Col(
                    [

                        html.P("Filter by placement:",
                               style={'font-weight': 'bold'},
                               className="mb-4"),
                        dcc.Dropdown(
                            id='dropdown',
                            options=[{'label': col, 'value': col} for col in placement[placement_col]],
                            value = 'win',
                            className = 'dropdown2 mb-4',                            
                        ),
                        html.H3("Instructions:",
                               style={'font-weight': 'bold'},
                               className="mt-4"),
                        html.P(
                            """ 
                               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc a est consequat, posuere purus sed, pharetra nulla. 
                               Morbi tempus eget mi lacinia semper. Quisque ut laoreet risus, quis semper urna. Nam quis tristique dolor. 
                               Nunc efficitur consequat aliquam. Aliquam erat volutpat. Pellentesque sit amet laoreet dui. 
                               Morbi id sapien sed sem tempor dignissim eget in neque. Sed sapien lacus, ornare a cursus et, commodo a tortor. 
                               Sed vel ipsum consectetur, vestibulum ipsum id, dictum elit. 
                               Nulla tempor, lacus vel elementum ultrices, arcu diam scelerisque augue, quis consequat elit tellus non ante. 
                               Aliquam magna quam, vestibulum sit amet tempus congue, molestie ultrices sem.
                               """,
                               className="mt-4"),

                    ], width = 5
                )
            ], className="mt-4 mb-4",
        ),

#LINECHART
        dbc.Row(
            [
                        html.H2('Final Progress per Finalist'),
                dbc.Col(
                    [
                        
                        dcc.Graph(id="graph"),
                        
                    ], width = 7
                ),

                dbc.Col(
                    [

                        html.P("Select the queens you want to compare",
                               style={'font-weight': 'bold'},
                               className="mb-4"),
                        dcc.Dropdown(
                            id='queen-dropdown',
                            options=[{'label': queen, 'value': queen} for queen in melted['queen'].unique()],
                            value=['Sasha Colby'],
                            multi=True,
                            style={'width': '100%', 'margin': 'auto'},
                            className = 'dropdown1 mt-4',
                        ),
                        html.H3("Instructions:",
                               style={'font-weight': 'bold'},
                               className="mt-4"),
                        html.P(
                            """ 
                               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc a est consequat, posuere purus sed, pharetra nulla. 
                               Morbi tempus eget mi lacinia semper. Quisque ut laoreet risus, quis semper urna. Nam quis tristique dolor. 
                               Nunc efficitur consequat aliquam. Aliquam erat volutpat. Pellentesque sit amet laoreet dui. 
                               Morbi id sapien sed sem tempor dignissim eget in neque. Sed sapien lacus, ornare a cursus et, commodo a tortor. 
                               Sed vel ipsum consectetur, vestibulum ipsum id, dictum elit. 
                               Nulla tempor, lacus vel elementum ultrices, arcu diam scelerisque augue, quis consequat elit tellus non ante. 
                               Aliquam magna quam, vestibulum sit amet tempus congue, molestie ultrices sem.
                               """,
                               className="mt-4"),

                    ], width = 5
                )
            ], className="mt-4 mb-4",
        ),

#INFO TABLE
        dbc.Row(
            [
                dbc.Col(
                    [

                        html.H2('Queen Placements'),
                        dcc.Dropdown(
                            id='row-dropdown',
                            options=[{'label': row['queen'], 'value': str(row.name)} for _, row in placement.iterrows()],
                            placeholder='Select a row...'
                        ),
                        html.Table([
                            # Table header
                            html.Thead(
                                html.Tr([html.Th(col) for col in placement.columns])
                            ),
                            # Table body
                            html.Tbody(id='table-body')
                        ])
                    ]
                )
            ]
        )
    ]
)


#---------------------------------------------------------------#
#APP LAYOUT
app.layout = html.Div([header, content])

#---------------------------------------------------------------#
#APP CALLBACKS
@app.callback(
    Output("scatter-plot", "figure"), 
    Input("dropdown", "value")
)
def update_bar_chart(dropdown_value):
    df = placement
    fig = px.scatter(
        df, x="score", y=dropdown_value, 
        color="w/r/e",
        hover_data=['queen'],
        template=dark_template,
        size = 'score')
    return fig

@app.callback( #dropdown for line chart
    Output("graph", "figure"), 
    Input("queen-dropdown", "value"))
def update_line_chart(queens):
    df = melted
    mask = df.queen.isin(queens)
    fig = px.line(df[mask], 
        x="variable", y="value", color='queen',
        template=dark_template)
    return fig

@app.callback(
    Output('table-body', 'children'),
    [Input('row-dropdown', 'value')]
)
def update_table(selected_row):
    if selected_row is not None and selected_row != 'Unnamed: 0':
        row_num = int(selected_row)
        return [
            html.Tr([
                html.Td(data) for data in placement.iloc[row_num]
            ])
        ]
    else:
        return []



#---------------------------------------------------------------#
#RUN APP
app.run_server(debug=True)