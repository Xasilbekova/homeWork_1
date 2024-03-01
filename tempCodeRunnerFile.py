data = data.split("\n")[:-1]
# for i in range(len(data)):
#     data[i] = data[i].split(" ")
#     data[i][3] = int(data[i][3])


# birinchi = ikkinchi = uchinchi = 0
# for i in range(len(data)):
#     data[i][4] = data[i][4].split("-")
#     data[i][4][0] = int(data[i][4][0])
#     if data[i][4][0] == 1:
#         birinchi += 1
#     elif data[i][4][0] == 2:
#         ikkinchi += 1
#     else:
#         uchinchi += 1

# for name, dew, month, bonus, bolim in data:
#     if bonus > 0 and uchinchi < birinchi > ikkinchi:
#         print("Birinchi bo'lim")
#         break
#     elif bonus > 0 and birinchi < ikkinchi > uchinchi:
#         print("Ikkinchi bo'lim")
#         break
#     elif bonus > 0 and birinchi < uchinchi > ikkinchi:
#         print("Uchinchi bo'lim")
#         break
