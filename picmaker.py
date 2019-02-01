pic = open("picmaker.ppm", 'w')
pic.write("P3 \n500 500 \n255 \n")  #heading

for row in range(500):
    for column in range(500):
        pic.write(str(row % 200) + " ")
        pic.write(str(column % 100) + " ")
        pic.write(str(row % 256) + " ")

pic.close()
