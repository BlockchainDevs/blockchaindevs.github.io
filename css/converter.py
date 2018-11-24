ifile=open("animate1.css","r")
ofile=open("animate.css","w")
for i in ifile.read():
    ofile.write(i)
    if i=="{" or i=="}":
        ofile.write("\n")

ofile.close()
ifile.close()
