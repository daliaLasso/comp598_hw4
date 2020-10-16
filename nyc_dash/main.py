import pandas as pd
from bokeh.layouts import column
from os.path import dirname, join
from bokeh.models import Button, Select, ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.models.widgets import Dropdown

# PRELIMINARY DATA HANDLING
# Reading data from a tsc file into a dataframe.
# This is the data for all of 2020
df_all = pd.read_csv(join(dirname(__file__), 'data', '2020_data'), sep="\t")#, index_col=0)
df_zip = pd.read_csv(join(dirname(__file__), 'data', 'zipcode'), sep="\t")

df_zip['zipcode'] = df_zip['zipcode'].apply(str)

print(df_all.head(10))
print(df_zip.head(10))


def zip_list_from_df(df_zip, zip):
    ls = df_zip.loc[df_zip['zipcode'] == zip].values.tolist()
    ls = ls[0]
    ls.pop(0)
    return ls

months = range(1,10)
x = months
y = zip_list_from_df(df_zip, '10000')
p = figure(x_range=(0,10), y_range=(0,400))
r2 = p.line(x, y)
ds = r2.data_source
    
def handle_zip(attr, old, new):
	ls = zip_list_from_df(df_zip, new)
	new_data = {}
	new_data['x'] = months
	new_data['y'] = ls
	ds.data = new_data
	print(ls)

menu = Select(options=list(df_zip['zipcode'].unique()),value='10000', title = 'Zipcode 1')
menu.on_change('value', handle_zip)
####################################################
# CREATES FIGURE AND THE CURVE FOR ALL 2020 DATA
source_all = ColumnDataSource(df_all)
#print(source_all.column_names)

#p = figure()

r2 = p.line(x='month', y='avg_response_time', source=source_all)

curdoc().add_root(column(menu, p))
#curdoc().add_root(column(zipcode1, p))

