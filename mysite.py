from dash import Dash, dcc
import dash_bootstrap_components as dbc

# Build the components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="Hey, just practice!")

# Customize your own Layout
app.layout = dbc.Container(mytext)

# Run app
if __name__ == '__main__':
    app.run_server(port=8001)
