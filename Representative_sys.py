import pandas as pd
import numpy as np
car = pd.read_csv('C:/Users/User/Downloads/carsystem.csv' )
car.head(10)
car1 = car.groupby(car.carname).mean().sort_values('featurerating',ascending = True).drop(['driverrating','fare/km','presentloc'],axis =1)
car1
car2 = car.groupby(car.carname).mean().sort_values(['fare/km','presentloc'],ascending = True).drop(['driverrating','featurerating'],axis =1)
car2
print (car1)
print(car2)
car3 = car.query('featurerating > 3.5').drop(['driverid', 'driverrating', 'fare/km', 'vehicletype', 'presentloc'], axis = 1).sort_values('featurerating')
car3
car4 = car.query('featurerating > 3.5').sort_values(['driverrating', 'driverid'], ascending = True)
car4
car5 = car.groupby('driverid').mean().sort_values(['presentloc', 'driverrating'], ascending = True)
car5