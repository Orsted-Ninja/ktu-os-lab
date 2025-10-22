import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
marks = [99, 86, 87, 88, 91, 86, 93, 87, 94, 78]
model=np.poly1d(np.polyfit(year,marks,3))
line=np.linspace(2011,2020,100)
per=model(2017)
print(per)
print(f"r2 score is:{r2_score(marks,model(year))}")
plt.scatter(year,marks)
plt.plot(line,model(line))

plt.show()
