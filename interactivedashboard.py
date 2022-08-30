import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Output, Input

# Data Exploration with Pandas
df = pd.read_csv("data.csv")

'''print(df[:5])
print(df.loc[:5, ["World Sales"]])
print(df.iloc[:5, [2,3,5,6]])
print(df.Genre.nunique())# count how many different Genre
print(df.Genre.unique()) # list all Genre'''

# fig_pie = px.pie(data_frame=df, names="Genre", values="Japan Sales")
# fig_pie = px.pie(data_frame=df, names="Genre", values="North American Sales")
#
# fig_pie.show()
# fig_bar = px.bar(data_frame=df, x="Genre", y="North American Sales")
# fig_bar.show()
# fig_hist = px.histogram(data_frame=df, x="Genre", y="North American Sales")
# fig_hist.show()

# Interactive Graphing with Dash
app = dash.Dash(__name__)

app.layout = html.Div([
        dash.html.H1("Graph Analysis Practice"),
        dash.dcc.Dropdown(id="genre_choice", options=[{"label":x, "value":x} for x in sorted(df.Genre.unique())],
                          value="Sports"),
        dash.dcc.Graph(id="my_graph", figure={})
])
@app.callback(
    Output(component_id="my_graph",component_property="figure"),
    Input(component_id="genre_choice",component_property="value")
)

def interactive_graph(value_genre):
    #print(value_genre)
    dff = df[df.Genre == value_genre]
    fig_bar = px.bar(data_frame=dff, x="Year", y="World Sales")

    return fig_bar
if __name__ == "__main__":
    app.run_server()
