import numbers


f = open("./intermediate_code.txt", "r")
operators="+-*/"
code = [".text", "main:"]
registers  = [
    ["0", True],
    ["1", True],
    ["2", True],
    ["3", True],
    ["4", True],
    ["5", True],
    ["6", True],
    ["7", True],
    ["8", True],
    ["9", True],
]
def available():
    for register in registers:
        if register[1] == True:
            register[1] = False
            return register
    print("No registers available")

for line in f:
    words = line.split()
    word_index = 0
    line_stack = []
    asignations = {}
    numbers_list = "0123456789"
    for word in words:
        word_index += 1
        if word == "&":
            # print("pointer")
            None
        elif "_(" in word and ")_" in word:
            #usefull for while functionality
            # print("line reference")
            None
        elif ":" in line and "_(" not in word and ")_" not in word:
            # print("var_name : 0xn")
            asignations[words[0]] = words[-1]
        elif word == "++++++++++++++++":
            # print('title')
            None
        elif "T" in word and word_index == 1 and words[2] in numbers_list:
            code.append("li $t" + available()[0] + ", " + words[2])
        elif "T" not in word and word_index == 1:
            code.append("move ")

print(code)

        
    #ignore &
    #ignore _()
    #ignore execute
    #Queres usar los Tn para conectar las referencias de a con su valor asignado.


# main: 
# 	li $t0, 1            	#Parte que dice T1 = 1
# 	move $t1, $t0	#Parte que dice a = T1	(Importante saber que la $t1, ya no se puede usar, porque guarda un atributo, podes notar que las que tienen cosas como 0x0 con las que no se pueden tocar)

# 	li $t2, 2            	#Parte que dice T3 = 2
# 	move $t3, $t2	#Parte que dice b = T3.    (Importante saber que la $t3, ya no se puede usar, porque guarda un atributo, 0x4)

# 	li $t4, 0 		#Parte que dice c : 0x8.    (Importante saber que la $t4, ya no se puede usar, porque guarda un atributo)

# 	move $t5, $t4	#Parte que dice T6 = 0x8
# 	move $t6, $t1 	#Parte que dice T9 = 0x0
# 	move $t7, $t3 	#Parte que dice T10 = 0x4

# 	add $t8, $t6, $t7 #Parte que dice T8 = T9 + T10 (date cuenta que en las ultimas lineas declaramos que registro hace referencia a esas variables temporales)

# 	#Lo demás lo podes ignorar solo hace esto para hacer el print

# 	la $4, $t8
# 	jal printf
# 	j_exit

# 	.end main






# .data
# msg: .asciiz "The result of addition is: "

# .text

# li $t0,5
# li $t1,5

# Add $t3,$t0,$t1

# li $v0,4
# la $a0,msg
# syscall

# li $v0,1
# move $a0,$t3
# syscall

# li $v0,10
# syscall