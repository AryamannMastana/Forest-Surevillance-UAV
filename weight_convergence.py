import numpy as np
import matplotlib.pyplot as plt
import math

W0 = 8
W0i = []
Wbi = []
Wei =[]
it = []

for i in range (1,40):
    W0i.append(W0)
    Wbi.append(1.0417+0.3403*W0i[i-1])
    Wei.append((0.5635*math.pow(W0,-0.0624))*W0)
    it.append(i)
    print(W0i[i-1])
    print(Wbi[i-1])
    print(Wei[i-1])
    k = 1 - (Wei[i-1]/W0i[i-1]) - (Wbi[i-1]/W0i[i-1])
    W0 = .5/k
    print(W0)

plt.plot(it, W0i, color = 'red', label = 'Convergence plot')
plt.ylabel('Maximum takeoff weight (kg)')
plt.xlabel('No. of iterations')
plt.title('MTOW vs No. of iterations')
plt.tight_layout()
plt.legend()
plt.xticks(np.arange(0,41,4))
plt.yticks()
plt.show()