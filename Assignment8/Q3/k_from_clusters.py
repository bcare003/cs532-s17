import clusters


print('k = 5')
k = clusters.kcluster(data, k=5)
w = [blogname[r] for r in k[0]]
print str(w) + '\n'

print('k = 10')
k = clusters.kcluster(data, k=10)
w = [blogname[r] for r in k[0]]
print str(w) + '\n'

print('k =20')
k = clusters.kcluster(data, k=20)
w = [blogname[r] for r in k[0]]
print str(w) + '\n'

