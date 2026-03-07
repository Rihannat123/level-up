import matplotlib.pyplot as plt
bloodsugarman=[113,85,90,150,149,88,93,115,135,80,77,82,120,]
bloodsugarwomen=[67,98,89,120,132,150,84,69,89,79,120,110,100]
type=[bloodsugarman,bloodsugarwomen]
colors=['g','r']
label=['men','women']
bins=[80,100,120,150]
plt.xlabel("Blood Sugar Range")
plt.ylabel("Total no. of pateint")

plt.hist(type, bins=bins, rwidth=0.95 , color=colors, label=label, orientation="horizontal")
plt.title("Blood Sugar Level Chart ")
plt.legend()
plt.show()