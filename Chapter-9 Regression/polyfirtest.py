import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,4]
y = [1+1,4+1,9+1,16+1]
outx=[1,2,3,4,5,6,7,8,9,10]
pfit=numpy.polyfit(x, y, 2)
print(pfit)
model = numpy.poly1d(pfit)
print(model)
output =model(outx)
print(output)
plt.scatter(output,outx)
plt.plot(output,outx)
plt.show()
