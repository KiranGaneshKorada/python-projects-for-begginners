import matplotlib.pyplot as plt

x=[1,3,5,7,9]
y=[9,5,1,5,9]

# we can plot multiple lines in one graph

x2=[7,9,7,9]
y2=[5,9,5,1]

plt.plot(x,y,label='line-v',marker='*')
plt.plot(x2,y2,label='line-k')

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("graph drawn by python code of multiple lines")

plt.legend() # adds diff colors to diff lines in graph

plt.show()

# similarly we can construct any kind of graph like bar graph ...etc explore docs for more