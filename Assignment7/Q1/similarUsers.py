import recommendations as re
f = open('similarUsers.txt', 'w')
input = open("u.user", 'r')

data = re.loadMovieLens

users = []
#not acessing the input file
for line in input:
    u = (id, age, gender, occupation, zip) = line.split('|')[0:5]

    if (u[1] == '21' and u[2] == 'M' and u[3] == 'student'):
        users.append(u)
for item in users:
    print>> f, item
