#!/usr/bin/python
#coding:utf-8
from bokeh.charts import Area, show, vplot, output_file

# create some example data
data = dict(
    p_top = [120,120,120],
    python = [110,110,100],
    bottom = [100,100,90]
)
#zhushi = '''
area = Area(data, #x = [25,1000,10000],
            title="Area Chart", legend="top_left",
            #x_axis_type="log",
            #y_range=(60,120),
            xlabel='频率（Hz）', ylabel='限值（dBμA）')

output_file('area.html')

p=area

show(p)
#'''
#print data[p_top]
