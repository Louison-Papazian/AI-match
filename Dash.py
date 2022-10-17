# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from Chart_data import match_diff_age
app = Dash(__name__)

#rearrangement du dataframe pour le plot
<<<<<<< Updated upstream
=======
data = model_ready
colonnes = list(data.columns)

# Emplacement des images
EasyDate = 'Image/EasyDate.png'
AI_match = 'Image/AI_match.png'




#test = px.imshow(cm)
# Mise en place du html
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.Img(src=dashF.b64_image(EasyDate),style={'width':"20%"}),
    html.Img(src=dashF.b64_image(AI_match),style={'width':"10%"}),
>>>>>>> Stashed changes

df = match_diff_age()

#Creation du Barplot
fig = px.bar(df, x="diff_age", y="Taux_match", color="diff_age", barmode="relative")
fig.update_layout(showlegend=False)

<<<<<<< Updated upstream
#Mise en place du html
app.layout = html.Div(children=[
    html.H1(children='EasyDate Dashboard'),

    html.Div(children='''
        Number of matches by age difference
    '''),
=======
        html.Label(['Choisissez une variable :'],
        style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='select_cols',
            options = colonnes,
            #options=[{'label': "Différence d'âge", 'value': colonnes[0]}],
            optionHeight=35,
            value= colonnes[0],               #dropdown value selected automatically when page loads
            multi=False,                        #allow multiple dropdown values to be selected
            style={'width':"30%"},             #use dictionary to define CSS styles of your dropdown

            ),
    ],className='three columns'),

    html.Div([
        dcc.Graph(id='our_graph')        ], style = {"width" : '40%'}),


    html.Div([
        dcc.Graph(id='our_graph2', figure = dashF.confusion_matrix())
    ], style = {"width" : '40%'})
])
>>>>>>> Stashed changes

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig
    )
], style={'width': '45%', 'display': 'inline-block', 'vertical-align': 'middle'})

if __name__ == '__main__':
    app.run_server(debug=True)