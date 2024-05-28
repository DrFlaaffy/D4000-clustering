no_1Mpc = np.array(no_1Mpc)
no_5Mpc = np.array(no_5Mpc)
mean_d4000_1mpc = []
std_d4000_1mpc = []
x_1Mpc = []
for i in range(0,15): 
    search = np.where(no_1Mpc == i)[0]
    mean_d4000_1mpc.append(np.mean(pri_d4000[search]))
    std_d4000_1mpc.append(np.std(pri_d4000[search]))
    x_1Mpc.append(i)
    
mean_d4000_5mpc = []
std_d4000_5mpc = []
x_5Mpc = []
for i in range(0,80): 
    index = np.where(np.array(no_5Mpc) == i)[0]
    mean_d4000_5mpc.append(np.mean(pri_d4000[index]))
    std_d4000_5mpc.append(np.std(pri_d4000[index]))
    x_5Mpc.append(i)

index = np.where((no_1Mpc==1) | (no_1Mpc==2))[0]
number_1_3Mpc = []
cor_D4000 = []
for i in index:
    z1 = pri_z[i]
    cor_D4000.append(pri_d4000[i])
    kpc_per_arcmin = distance(z1)
    sep = pri_position[i].separation(sec_position).arcsecond
    sep_mpc = sep*kpc_per_arcmin/1000
    v_dis = 3E5*(sec_z-z1)
    number3 = len(np.where((abs(v_dis)<250)&(sep_mpc>1)&((sep_mpc<3)))[0])
    number_1_3Mpc.append(number3)

number_1_3Mpc = np.array(number_1_3Mpc)
cor_D4000 = np.array(cor_D4000)
mean_d4000_1_3mpc = []
std_d4000_1_3mpc = []
x12 = []
for i in range(0,20): 
    index = np.where(number_1_3Mpc == i)[0]
    mean_d4000_1_3mpc.append(np.mean(pri_d4000[index]))
    std_d4000_1_3mpc.append(np.std(pri_d4000[index]))
    x12.append(i)

index = np.where((no_1Mpc>8) | (no_1Mpc<12))[0]
number_8_12Mpc = []
cor_D4000 = []
for i in index:
    z1 = pri_z[i]
    cor_D4000.append(pri_d4000[i])
    kpc_per_arcmin = distance(z1)
    sep = pri_position[i].separation(sec_position).arcsecond
    sep_mpc = sep*kpc_per_arcmin/1000
    v_dis = 3E5*(sec_z-z1)
    number8 = len(np.where((abs(v_dis)<250)&(sep_mpc>1)&((sep_mpc<3)))[0])
    number_8_12Mpc.append(number8)

number_8_12Mpc = np.array(number_8_12Mpc) 
mean_d4000_8_12mpc = []
std_d4000_8_12mpc = []
x812 = []
for i in range(0,60): 
    index = np.where(number_8_12Mpc == i)[0]
    mean_d4000_8_12mpc.append(np.mean(pri_d4000[index]))
    std_d4000_8_12mpc.append(np.std(pri_d4000[index]))
    x812.append(i)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)  
plt.title("1 Mpc Radius")  
plt.errorbar(x_1Mpc,mean_d4000_1mpc,std_d4000_1mpc)
plt.ylabel("Mean D4000")
plt.xlabel("No. of galaxies")
plt.subplot(2,2,2)
plt.title("5 Mpc Radius")  
plt.errorbar(x_5Mpc,mean_d4000_5mpc,std_d4000_5mpc)
plt.xlabel("No. of galaxies")
# plt.show()
plt.subplot(2,2,3)
plt.title("1-2 neighbors in 1 Mpc Radius")  
plt.errorbar(x12,mean_d4000_1_3mpc,std_d4000_1_3mpc)
plt.ylabel("D4000")
plt.xlabel("No. of galaxies in annulus")
plt.subplot(2,2,4)
plt.title("8-12 neighbors in 1 Mpc Radius")  
plt.errorbar(x812,mean_d4000_8_12mpc,std_d4000_8_12mpc)
plt.xlabel("No. of galaxies in annulus")
plt.tight_layout()
plt.show()