
import pandas as pd 
import plotly.express as px
from dash import Dash,html,dcc
from dash import html
import json 
import plotly.utils 

df = pd.read_csv('https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/main/world_population.csv')

df.fillna(method = 'ffill' , inplace = True)
df.drop_duplicates()
sorted_df = df.sort_values(by = '2022 Population' , ascending = False )


fig =px.treemap(
    sorted_df ,
    path = [px.Constant("world population"),"Continent" , 'Country'],
    values = '2022 Population' ,
    color= "Continent" ,
    hover_data =['2022 Population'] ,
    title = '2022 worldwide Population Treemap by Continent and Country' ,
    color_continuous_scale ='RdBu' ,

)
# update layout for better readability
fig.update_layout(
    margin = dict(t=50 , l=25 , r=25 , b=25)
)

fig.update_traces(
    texttemplate = '%{label}<br>%{customdata[0]: , .0f}' ,
    textposition = 'middle center' ,
    hovertemplate =' <b>%{label}</b><br>Population: %{value: , .0f}<extra></extra>' ,
)

fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)

html_content = f"""
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2022 World Population Treemap</title>
    <script src="http://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div id="plotly-div"></div>
    <script>
        var figureJSON = {fig_json}:
        plotly.newPlot('plotly-div' , figureJSON.data , figureJSON.layout);
    </script>

</body>

</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)


print("HTML file 'index.html' has been created . you can now push this  to github pages")