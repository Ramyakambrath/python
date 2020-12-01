import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('C:/Users/Ramya.Kambrath/Downloads/ELPV2/ELPv2ELP EntitlementViewReport.csv')
vendors = df['Vendor'].unique()
LTs = df['Licence Title'].unique()
print( df[df["Vendor"].str.contains("1E")]['Licence Title'])




# is_1e=df['Vendor']=='1E'
# f_df=df[is_1e]
# print('DATA',f_df.head())

app.layout = html.Div(children=[
    html.H1(children='ELP Data',
    style={
        'textAlign':'center',
        'color': 'black'
    }),
    html.Div(children='ELP: Microsoft ELP Data.', style={
        'textAlign': 'center',
        'color': 'black'
    }),
     html.Div([
    html.Label('Vendor Dropdown',style={
        'textAlign': 'left',
        'color': 'black'
    }),
    dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in vendors],
        value='1E',      
    id='dropdown1'  
     ) ,
     html.Label('Licence Title'),
     dcc.Dropdown(    
        value='1E PXE Lite Local 2',
        id='dropdown2'  
    ),
     dcc.RadioItems(
        options=[{'label': i, 'value': i} for i in ['Allocation Summary', 'Allocation with Detail']],
        value='Allocation Summary',
         id='radio'  
    )],
     style={
        'color': 'black',
        'background':'grey',
        'width': '48%',
        'display': 'inline-block'
    }),
    html.Div([
    html.Br()
    ]),
    
    html.Div(id='table')
])

@app.callback(
    dash.dependencies.Output('dropdown2', 'options'),
    [dash.dependencies.Input('dropdown1', 'value')]
)
def update_dropdown(name):
    return [{'label': i, 'value': i} for i in df[df["Vendor"].str.contains(name)]['Licence Title']]


@app.callback(
    Output('table', 'children'),
    [Input('dropdown1', 'value'),
     Input('dropdown2', 'value')])

def update_table(selectedValue1,selectedValue2,max_rows=100):  
    filtered_data1=df[df['Vendor']== selectedValue1].head()
    filtered_data= filtered_data1[ filtered_data1['Licence Title']== selectedValue2].head()

    return html.Table(
        # Header
        [html.Tr([html.Th(col, style={
        'textAlign': 'center',
        'color': '#7FDBFF',
        'background': '#111111',
         'width' :'50%'
    }) for col in filtered_data.columns])] +

        # Body
        [html.Tr([
            html.Td(filtered_data.iloc[i][col], style={
        'textAlign': 'center',
        'color': '#7FDBFF',
        'background': '#111111'
    }) for col in filtered_data.columns
        ]) for i in range(min(len(filtered_data), max_rows))]
    )




# def generate_table(dataframe, max_rows=100):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col, style={
#         'textAlign': 'center',
#         'color': '#7FDBFF',
#         'background': '#111111'
#     }) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col], style={
#         'textAlign': 'left',
#         'color': '#7FDBFF',
#         'background': '#111111'
#     }) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )





if __name__ == '__main__':
    app.run_server(debug=True)