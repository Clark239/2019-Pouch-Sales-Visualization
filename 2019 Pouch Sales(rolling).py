import matplotlib.pyplot as plt 
import pandas as pd  
import numpy as np

coffee_names = ['Asoprocafees', 'El Progreso', 'La Union', 'Los Idolos', 'Sabana',
                'Hondurita', 'Dari', 'Kossa', 'Kossa Spro', 'Neja Fadil', 'Tegegne',
                'Asobagri', 'San Pedro', 'Todos Santos', 'Acacias', 'Kiriga', 'Method',
                'Capitan Luis', 'Un Regalo', 'Technique']
ppp = [13.5, 13.5, 13.5, 16, 17.5, 15.5, 14, 15.5, 15.5, 15.5, 16, 13.5, 13.5,
       13.5, 13.5, 18, 13.5, 13.5, 17, 14.5]
oct_2019_sales = [81, 135, 27, 32, 140, 155, 140, 139.5, 108.5, 15.5, 96, 94.5,
                  135, 108, 121.5, 90, 121.5, 81, 85, 116]
nov_2019_sales = [67.5, 135, 48, 87.5, 62, 98, 108.5, 77.5, 108.5, 128, 135,
                  81, 27, 135, 121.5, 144, 175, 121.5, 136, 101.5]
dec_2019_sales = [40.5, 189, 96, 52.5, 77.5, 98, 62, 77.5, 124, 128, 121.5, 189,
                  94.5, 202.5, 108, 54, 121.5, 119,58,0]

#print(len(dec_2019_sales))

plt.title('2019 Holiday Pouch Sales')
plt.xticks(rotation=80)
ax = plt.subplot()
ax.bar(coffee_names, oct_2019_sales)
ax.bar(coffee_names, nov_2019_sales)
ax.bar(coffee_names, dec_2019_sales)
plt.tight_layout()
plt.legend(['October', 'November', 'December'])
plt.savefig('2019_monthly_sales.png')
plt.show()

oct_median = np.median(oct_2019_sales)
oct_avg = np.mean(oct_2019_sales)
print(oct_avg, oct_median)
nov_median = np.median(nov_2019_sales)
nov_avg = np.mean(nov_2019_sales)
print(nov_avg, nov_median)
dec_median = np.median(dec_2019_sales) 
dec_avg = np.mean(dec_2019_sales)
print(dec_avg, dec_median)
ppp_avg = np.mean(ppp)
ppp_median = np.median(ppp)
print(ppp_avg, ppp_median)

total_holiday_sales = oct_2019_sales + nov_2019_sales + dec_2019_sales
sorted_holiday_sales = np.sort(total_holiday_sales)
holiday_sales_avg = np.mean(sorted_holiday_sales)
holiday_sales_median = np.median(sorted_holiday_sales)
print(holiday_sales_avg, holiday_sales_median)