# Import the required package
import plotly.express as px


###########################################
######### Define a plot function ##########
###########################################
def visualize(x,  # x-axis
              y,  # y-axis
              title='Signal',  # Title of the figure
              ylabel='Amplitude',  # Label of the y-axis
              xlabel='Time [sec]',  # Label of the x-axis
              line_color='#FF0000',  # Line Color
              ):
    # Define the plotly.express figure
    fig = px.line(x=x, y=y)
    fig.update_layout({"title": {"text": title,
                                 "font": {"size": 30, "family": "Times New Roman, bold"},
                                 "x": 0.5,
                                 "xanchor": "center",
                                 "yanchor": "top"},
                       "xaxis": {"title": xlabel},
                       "yaxis": {"title": ylabel},
                       "hovermode": "x unified"
                       })
    fig.update_traces(line_color=line_color,
                      line_width=1,
                      hovertemplate="Time= %{x}<br>Amplitude= %{y}")
    return fig
