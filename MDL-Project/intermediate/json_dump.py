import json
data = [
#10 best vectors in decreasing order of your preference
 [ 0.00000000e+00,-1.45799022e-12,-2.28980078e-13,4.62010753e-11,
 -1.75214813e-10,-1.83669770e-15 ,8.52944060e-16,2.29423303e-05,
 -2.04721003e-06 ,-1.59792834e-08 , 9.83759863e-10],
 [ 0.00000000e+00 ,-1.36886031e-12 ,-2.28980078e-13 , 4.49993699e-11,
 -1.90944579e-10 ,-1.83669770e-15  ,8.98874388e-16  ,2.10350231e-05,
 -2.04721003e-06, -1.44588735e-08,  9.98214034e-10],
 [ 0.00000000e+00 ,-1.45799022e-12 ,-2.28980078e-13 , 4.41792015e-11,
 -1.75214813e-10, -1.83669770e-15 , 8.90297379e-16 , 2.29423303e-05
 -2.04721003e-06 ,-1.59792834e-08 , 9.98214034e-10],
 [ 0.00000000e+00 ,-1.45799022e-12, -2.16766300e-13 , 4.62010753e-11
 -1.75214813e-10 ,-1.83062278e-15 , 8.52944060e-16 , 2.29423303e-05,
 -2.04721003e-06 ,-1.59792834e-08 , 9.98214034e-10],
 [ 0.00000000e+00 ,-1.45799022e-12, -2.28980078e-13 , 4.82446257e-11,
 -1.75214813e-10, -1.83669770e-15 , 8.90641080e-16 , 2.29423303e-05,
 -2.04721003e-06 ,-1.59792834e-08 , 9.98347032e-10],
 [ 0.00000000e+00, -1.54664265e-12, -2.28980078e-13 , 4.43099045e-11,
 -1.77238881e-10 ,-1.83821968e-15 , 8.90936122e-16 , 2.26969026e-05,
 -2.04721003e-06 ,-1.57836407e-08 , 9.98214034e-10],
 [ 0.00000000e+00 ,-1.45799022e-12, -2.28980078e-13 , 4.47809621e-11
 -1.63492462e-10, -1.97560561e-15 , 8.52600359e-16 , 2.29423303e-05
 -2.04721003e-06, -1.59792834e-08 , 9.83626866e-10],
 [ 0.00000000e+00, -1.45799022e-12 ,-2.28980078e-13 , 4.62010753e-11,
 -1.75214813e-10 ,-1.84077227e-15,  8.52944060e-16 , 2.29423303e-05,
 -2.04721003e-06 ,-1.51994333e-08 , 9.64670012e-10],
 [ 0.00000000e+00 ,-1.54664265e-12, -2.28980078e-13 , 4.43099045e-11,
 -1.77238881e-10 ,-1.83821968e-15 , 8.90936122e-16  ,2.26969026e-05,
 -2.04721003e-06, -1.57836407e-08 , 9.98214034e-10],
 [ 0.00000000e+00 ,-1.45799022e-12, -2.28980078e-13,  4.42847855e-11,
 -1.75214813e-10, -1.83669770e-15 , 8.88346757e-16 , 2.27169668e-05,
 -2.04721003e-06, -1.59792834e-08 , 9.97459225e-10]
]

with open('35.json','w') as outfile:
	json.dump(data,outfile)