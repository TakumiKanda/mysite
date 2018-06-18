import matplotlib.pyplot as plt

steps = [148376, 149539, 150699, 152262, 153901, 155779, 157450]
labels = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(labels, steps, color = 'red', align='center')

plt.yticks(positions, labels)
plt.xlabel('Population')
plt.ylabel('Year')
plt.title('Population transition of Tokorozawa city')
 
plt.grid()
plt.show()