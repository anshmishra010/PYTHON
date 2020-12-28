<<<<<<< HEAD
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt1 = "We have {:d} chickens."
print(txt1.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):
txt2 = "We have {:e} chickens."
print(txt2.format(5))

#Use "E" to convert a number into scientific number format (with an upper-case E):
txt3 = "We have {:E} chickens."
print(txt3.format(5))

#Use "o" to convert the number into octal format:
txt4 = "The octal version of {0} is {0:o}"
print(txt4.format(10))

#Use "x" to convert the number into Hex format:
txt5 = "The Hexadecimal version of {0} is {0:x}"
print(txt5.format(255))

#Use "X" to convert the number into upper-case Hex format:
txt6 = "The Hexadecimal version of {0} is {0:X}"
=======
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt1 = "We have {:d} chickens."
print(txt1.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):
txt2 = "We have {:e} chickens."
print(txt2.format(5))

#Use "E" to convert a number into scientific number format (with an upper-case E):
txt3 = "We have {:E} chickens."
print(txt3.format(5))

#Use "o" to convert the number into octal format:
txt4 = "The octal version of {0} is {0:o}"
print(txt4.format(10))

#Use "x" to convert the number into Hex format:
txt5 = "The Hexadecimal version of {0} is {0:x}"
print(txt5.format(255))

#Use "X" to convert the number into upper-case Hex format:
txt6 = "The Hexadecimal version of {0} is {0:X}"
>>>>>>> 15e6342b75e4ba00fee9f6172d792ad043e8e111
print(txt6.format(255))