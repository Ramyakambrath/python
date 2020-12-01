import dash
import dash_core_components as dcc
from dash.dependencies import Input,Output
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div(children=[dcc.Input(id='input',value='Enter Something',type='text'),
html.Div(id-'output')

])

@app.callback{
    Output(component)
}

if __name__=='__main__':
   app.run_server(debug=True)