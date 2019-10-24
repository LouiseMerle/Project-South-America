import pandas as pd
import numpy as np
import plotly.graph_objects as go

cities = pd.read_csv('cities_input.csv')
total = pd.read_csv('total.csv')

print('\n¡Hola amigo! \n\n'
      'Great that you want to move to South-America! \n'
      'Find your top destination by rating 19 factors, such as safety, weather and healthcare. \n'
      'You can choose from the following options: \n'
      ' 0 - not at all important \n'
      ' 3 - not very important \n'
      ' 6 - somewhat important \n'
      ' 9 - very important \n'
      '\n'
      '¡Salud! \n')  

a = int(input('Average maximum temperature: '))
b = int(input('Average minimum temperature: '))
c = int(input('Hours of sun: '))
d = int(input('Little rain days: '))
e = int(input('Housing: '))
f = int(input('Cost of living: '))
g = int(input('Startup friendliness: ')) #check what it is 
h = int(input('Travel connectivity: ')) #check what is it
i = int(input('Commute to work: '))
j = int(input('Business freedom: '))
k = int(input('Safety: '))
l = int(input('Healthcare: '))
m = int(input('Environmental Quality: ')) #check what is it
n = int(input('Economy: '))
o = int(input('Taxation: '))
p = int(input('Internet access: '))
q = int(input('Leisure & culture: '))
r = int(input('Tolerance: '))
s = int(input('Outdoors: '))

categories = ['avg_max_temp', 'avg_min_temp', 'hours_of_sun', 'rain_days_per_month', 'Housing', 'Cost of Living', 'Startups', 'Travel Connectivity', 'Commute', 'Business Freedom', 'Safety', 'Healthcare', 'Environmental Quality', 'Economy', 'Taxation', 'Internet Access', 'Leisure & Culture', 'Tolerance', 'Outdoors']

dic = {'Categories': categories, 'Weights': [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]}

weights_df = pd.DataFrame.from_dict(dic, orient='index').transpose()

city_names = ['Asuncion', 'Bogota', 'Buenos Aires', 'Caracas', 'Curitiba', 'Florianopolis', 'Medellin', 'Montevideo', 'Porto Alegre', 'Quito', 'Rio de Janeiro', 'Santiago', 'Sao Paulo']

personal_means_dic = {}
for city in city_names: 
    score = np.average(total[city], weights=weights_df.Weights)
    personal_means_dic[city] = score
    
personal_means = pd.DataFrame(list(personal_means_dic.items()), columns=['name', 'mean'])

result = pd.merge(personal_means, cities, on='name')

result['text'] = result['name'] + ' Score ' + result['mean'].astype(str) + '\nWant to know more about this city, follow this link: '+ result['link']
limits = [(0,20)]
colors = ["orange"]
scale = 5

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = result[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'country names',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = (df_sub['mean']/3.3)**10,
            color = colors[i],
            line_color='rgb(255,255,255)',
            line_width= 0.0002,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        title_text = 'Best city for you!',
        showlegend = False,
        geo = dict(
            scope = 'south america',
            landcolor = 'rgb(217, 217, 217)',
            countrycolor = "white" ,
            coastlinecolor = "white",

        )
    )


fig.show()

