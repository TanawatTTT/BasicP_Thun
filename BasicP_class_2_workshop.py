x = int(input("ระยะทาง"))
if x >= 5 and x <= 50 :
    print("10 บาท")
elif x >= 51 and x <= 100 :
    print("15 บาท")
elif x >= 101 and x <= 300 :
    print("25 บาท")
elif x >= 301 and x <= 500 :
    print("35 บาท")
elif x >= 501 :
    print("45 บาท")
else: 
    print("ไม่สามารถส่งได้")