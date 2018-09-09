

def tickerrequest(tickersymbol, start_date, end_date):
    import requests
    import numpy
    import pandas
    import json
    from bokeh.plotting import figure, output_file, show
    r = requests.get('https://www.quandl.com/api/v3/datasets/EOD/'+tickersymbol+'?start_date='+start_date+'&end_date='+end_date+'&api_key=fdgASPFup4AQXySis6vB')
    dat = r.json()
    prettydat= dat['dataset']['data']; prettydat_col = dat['dataset']['column_names']
    df = pandas.DataFrame(prettydat, columns=prettydat_col)
    ###start plot
    output_file("finalplot.html")
    p = figure(tools="pan,box_zoom,reset,save", \
               x_axis_type='datetime', \
               title='Quandl End of Day Prices for '+tickersymbol, \
               x_axis_label='Date', \
               y_axis_label='Price (USD)')#,
    p.line(pandas.to_datetime(df.Date), df.Close, line_color="red", legend='Close')
    p.line(pandas.to_datetime(df.Date), df.Adj_Close, line_color="blue", legend='Adjusted Close')
    show(p)
     