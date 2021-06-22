import matplotlib.pyplot as plt
fig,ax=plt.subplots()
x=[1,2,3,4,5]
#x2=[2,3,6,7,9]
y=[2,4,6,8,10]
#y2=[1,2,3,4,7]
ax.plot(x,y, color = "lime", linestyle="--", marker="*")
#ax.bar(x,y2)
#ax.scatter(x2,y2)
plt.show()
