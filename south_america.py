import pandas as pd
import numpy as np
import plotly.graph_objects as go


'''
L.S. Very nice project! You put a lot of effort in it. I particularly liked that you were able to use the plotly library to
develop your own interactive programme. It shows that you know how to direcly implement data-related issues in practice for
a specific purpose. There are some minor errors in the others files, but this happens in data exploration. This file looks really good and the code is nice and clean. Some comments would have been nice though. Also: you could have made clever use
of functions which could have prevented you from using loops that look similar all the time. The file containing the Map code
also looks really code and shows how much improvement you've made over these last weeks. Well done! 
'''


cities = pd.read_csv('cities_input.csv')
total = pd.read_csv('total.csv')

print('\n¡Hola amigo! \n\n'
      'Great that you want to move to South-America! \n'
      'Find your top destination by rating 19 factors, such as safety, weather and healthcare. \n'
      'You can choose from the following options: \n'
      ' 0 - not at all important \n'
      ' 1 - somewhat important \n'
      ' 2 - very important \n'
      '\n'
      '¡Salud! \n')

end = 'No'
step = 1
while end != 'Yes':
    while step == 1:
        a = input('How important is the average maximum temperature: ') 
        if a == '0' or a == '1' or a == '2':
            a = int(a)
            a = a*5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 2:
        b = input('How important is the average minimum temperature: ')   
        if b == '0' or b == '1' or b == '2':
            b = int(b)
            b = b*5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 3:
        c = input('How important are the hours of sun per day: ')  
        if c == '0' or c == '1' or c == '2':
            c = int(c)
            c = c*5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 4:
        d = input('How important are the number rain days: ')   
        if d == '0' or d == '1' or d == '2':
            d = int(d)
            d = d * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 5:
        e = input('How important is affordable housing: ')  
        if e == '0' or e == '1' or e == '2':
            e = int(e)
            e = e * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 6:
        f = input('How important is the cost of living: ')   
        if f == '0' or f == '1' or f == '2':
            f = int(f)
            f = f * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 7:
        g = input('How important is startup friendliness: ') 
        if g == '0' or g == '1' or g == '2':
            g = int(g)
            g = g * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 8:
        h = input('How important is the international connectivity: ')  
        if h == '0' or h == '1' or h == '2':
            h = int(h)
            h = h * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue    
    while step == 9:
        i = input('How important is your commute: ')
        if i == '0' or i == '1' or i == '2':
            i = int(i)
            i = i * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 10:
        j = input('How important is business freedom: ')
        if j == '0' or j == '1' or j == '2':
            j = int(j)
            j = j * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 11:
        k = input('How important is safety: ')
        if k == '0' or k == '1' or k == '2':
            k = int(k)
            k = k * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 12:
        l = input('How important is healthcare: ')
        if l == '0' or l == '1' or l == '2':
            l = int(l)
            l = l * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 13:
        m = input('How important is the environmental quality (e.g. air quality): ')
        if m == '0' or m == '1' or m == '2':
            m = int(m)
            m = m * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 14:
        n = input('How important is the economy: ')
        if n == '0' or n == '1' or n == '2':
            n = int(n)
            n = n * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 15:
        o = input('How important is taxation: ')
        if o == '0' or o == '1' or o == '2':
            o = int(o)
            o = o * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 16:
        p = input('How important is internet access: ')
        if p == '0' or p == '1' or p == '2':
            p = int(p)
            p = p * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 17:
        q = input('How important is leisure & culture: ')
        if q == '0' or q == '1' or q == '2':
            q = int(q)
            q = q * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 18:
        r = input('How important is LGBT+ tolerance: ')
        if r == '0' or r == '1' or r == '2':
            r = int(r)
            r = r * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue
    while step == 19:
        s = input('How important is the outdoors (e.g. mountains): ')
        if s == '0' or s == '1' or s == '2':
            s = int(s)
            s = s * 5
            step += 1
        else:
            print('Please choose: \n'
                  ' 0 - not at all important \n'
                  ' 1 - somewhat important \n'
                  ' 2 - very important \n')
            continue

    print('\nGreat! These were your choises:\n')
    print('Average maximum temperature:', int(a/5)) 
    print('Average minimum temperature:', int(b/5)) 
    print('Hours of sun:', int(c/5)) 
    print('Little rain days:', int(d/5))
    print('Housing:', int(e/5)) 
    print('Cost of living:', int(f/5))
    print('Startup friendliness:', int(g/5))
    print('International connectivity:', int(h/5)) 
    print('Commute:', int(i/5))
    print('Business freedom:', int(j/5))
    print('Safety:', int(k/5))
    print('Healthcare:', int(l/5))
    print('Environmental quality:', int(m/5)) 
    print('Economy:', int(n/5))
    print('Taxation:', int(o/5))
    print('Internet access:', int(p/5))
    print('Leisure & culture:', int(q/5))
    print('LGBT+ tolerance:', int(r/5)) 
    print('Outdoors:', int(s/5))
    
    end = input('\nAre you happy with your choises? Yes/No \n')
    if end == 'No':
        step = 1
        print("Oke, let's start again")
    continue

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

result['text'] = result['name']
limits = [(0,20)]
colors = ["orangered"]
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

