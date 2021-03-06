import numpy as np
# 这是一个行向量，但是我们一般用列向量。
B = np.array([1, 2, 3, 4])
# 转置方法对一维列向量无效，只能对矩阵使用。得到的结果还是行向量要先变形成（1， 4）。
print(B.transpose())
B = B.reshape((1, 4))
print(B.transpose())
# 相当于多嵌套了一层括号，变成（1，3）的特殊矩阵就可以使用了。
A = np.array([[1, 2, 3, 4]])
print(A.T)

# 向量的加法
u = np.array([[1, 2, 3]]).T
v = np.array([[5, 6, 7]]).T
print(u + v)

# 向量的数量乘法
u = np.array([[1, 2, 3]]).T
print(3*u)

# 向量的内积dot方法，无论是行向量还是列向量结果都一样
u = np.array([3, 5, 2])
v = np.array([1, 4, 7])
print(np.dot(u, v))
# 这里会报错，因为本质上（1，3）是一个特殊的矩阵。还是使用的矩阵乘法规则
u = np.array([[3, 5, 2]])
v = np.array([[1, 4, 7]])
print(np.dot(u, v))
# 这样修改即可
u = np.array([[3, 5, 2]])
v = np.array([[1, 4, 7]]).T
print(np.dot(u, v))

# 向量的外积,三维同理，得到的是法向量，遵从右手定则。
u = np.array([3, 5])
v = np.array([1, 4])
print(np.cross(u, v))

# 向量的线性组合
u = np.array([[1, 2, 3]]).T
v = np.array([[4, 5, 6]]).T
w = np.array([[7, 8, 9]]).T
print(3*u+4*v+5*w)

# 向量的坐标取决于基底，坐标必须依托于基底才有意义
# 根据一个向量在一个基底上的坐标去求在另一个基底下该向量的坐标，即向量本身不变，坐标变了。可以用点乘得到该效果，只是要把基向量的模长先转化为一。
# 基底必须是线性无关的，也就是说基底组成的矩阵是满秩的
# 两个线性无关的N维向量也可以成为二维空间的一组基，n维空间不等于R^n空间。
# 一组向量他所有线性组合构成的空间就成为该组向量的张成空间。
# 向量的个数和维数都不是张成空间的决定因素