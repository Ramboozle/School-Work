#A266 Big O Display
import math
from matplotlib.pyplot import plot,show
xlog = [1,2,3,4,5,6]
ylog = [math.log(1),math.log(2),math.log(3),math.log(4),math.log(5),math.log(6)]
xquad = [1,2,3,4,5,6]
yquad = [(xquad[0]-3)**2,(xquad[1]-3)**2,(xquad[2]-3)**2,(xquad[3]-3)**2,(xquad[4]-3)**2,(xquad[5]-3)**2]
xexpo = [1,2,3,4,5,6]
yexpo = [xexpo[0]**2,xexpo[1]**2,xexpo[2]**2,xexpo[3]**2,xexpo[4]**2,xexpo[5]**2]
xgrow = [1,2,3,4,5,6]
ygrow = [math.exp(xgrow[0]),math.exp(xgrow[1]),math.exp(xgrow[2]),math.exp(xgrow[3]),math.exp(xgrow[4]),math.exp(xgrow[5])]
plot(xlog,ylog,xquad,yquad,xexpo,yexpo,xgrow,ygrow)
show()