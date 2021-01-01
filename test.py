numlist = []
for x in "user0,user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user100".split(','):
    numlist.append(int(x[4:]))
print (numlist)