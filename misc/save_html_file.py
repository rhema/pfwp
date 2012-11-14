## This example uses the old google charts (https://developers.google.com/chart/image/docs/making_charts) to produce a graph
##  and saves it to an html file.
#########

save_file = "grahps.html"

pie_data = {'this':10,'that':20 ,'the other':5 }

html_start = '''
<html>
    <head>
    <title>Charts</title>
    </head>
    <body>
        <center>
'''

html_end = '''
        </center>
    </body>
<html>
'''

def generate_pie_chart_from_dict(dict):
    text = "https://chart.googleapis.com/chart?cht=p3&chs=250x100&chd=t:NUMBERS&chl=KEYS"#keys |   numbers ,
    values = []
    for key in dict:
        values.append(str(dict[key]))
    text = text.replace('NUMBERS',','.join(values))
    text = text.replace('KEYS','|'.join(dict.keys()))
    return text

print generate_pie_chart_from_dict(pie_data)