import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

csvfile_path = r"C:\Users\Yu Zen\Documents\Coding\grape_soju\Project-holowiki\tidy_fanwiki.csv"


table = pd.read_csv(r"C:\Users\Yu Zen\Documents\Coding\grape_soju\Project-holowiki\tidy_fanwiki.csv")

# converting formatted string subscriber values into proper integer subscriber values
subnum = []
for s in table['Subs']:
    num = s.replace(' subscribers', '')
    if 'M' in num:
        num = float(num[:-1]) * 10**6
    elif 'K' in num:
        num = float(num[:-1]) * 10**3
    subnum.append(int(num))

# adding converted subscriber values to csv under a new column
table['subnum'] = subnum
table.to_csv(csvfile_path, mode='w', header=True, index=False)

# getting sum of subscribers for each generation
gen0 = 0
gamers = 0
gen1 = 0
gen2 = 0
gen3 = 0
gen4 = 0
gen5 = 0
idgen1 = 0
idgen2 = 0
enmyth = 0
enpromise = 0
gen6 = 0
idgen3 = 0
enadvent = 0
regloss = 0
enjustice = 0


for i in range(len(table)):
    if table.loc[i, 'gen'] == 'hololive Generation 0':
        gen0 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive Gamers':
        gamers += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 1st Generation':
        gen1 +=(table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 2nd Generation':
        gen2 +=(table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 3rd Generation':
        gen3 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 4th Generation':
        gen4 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 5th Generation':
        gen5 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive ID 1st Generation':
        idgen1 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive ID 2nd Generation':
        idgen2 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive EN -Myth-':
        enmyth += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive EN -Promise-':
        enpromise += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive 6th Generation':
        gen6 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive ID 3rd Generation':
        idgen3 += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive EN -Advent-':
        enadvent += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive DEV_IS ReGLOSS':
        regloss += (table.loc[i, 'subnum'])
    elif table.loc[i, 'gen'] == 'hololive EN -Justice-':
        enjustice += (table.loc[i, 'subnum'])

gens = [gen0, gamers, gen1, gen2, gen3, gen4, gen5, idgen1, idgen2, enmyth, enpromise, gen6, idgen3, enadvent, regloss, enjustice]
gennames = ['gen0', 'gamers', 'gen1', 'gen2', 'gen3', 'gen4', 'gen5', 'idgen1', 'idgen2', 'enmyth', 'enpromise', 'gen6', 'idgen3', 'enadvent', 'regloss', 'enjustice']

values = []


# time to plot the graph
plt.bar(gennames, gens)
plt.title('Total number of subscribers in each gen')
def format_subs(value, pos):
    return '{}M'.format(int(value/1000000))
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_subs))
plt.xlabel('Gen')
plt.xticks(rotation = 40, ha = 'right')
plt.ylabel('No. of subs')
plt.show()
