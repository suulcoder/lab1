import numbers


f = open("./intermediate_code.txt", "r")
operators="+-*/"
asignations = {}
code = [".text", "main:"]
register_counter = 0
numbers_list = "0123456789"

registers  = [
    ["0", None],
    ["1", None],
    ["2", None],
    ["3", None],
    ["4", None],
    ["5", None],
    ["6", None],
    ["7", None],
    ["8", None],
    ["9", None],
]

def available():
    global register_counter
    returnable = register_counter
    register_counter += 1
    register_counter %= 10
    while (registers[returnable][1] != None):
        returnable = register_counter
        register_counter += 1
        register_counter %= 10
    return str(returnable)

def asign(address):
    register = available()
    registers[int(register)][1] = address
    return str(register)
    
def get_temporal(var=None):
    if(var!=None):
        for register in registers:
            if register[1] == var:
                return register[0]
        return None
    return available()


for line in f:
    words = line.split()
    word_index = 0
    #When an atribute is declared
    if ":" in line and "_(" not in line and ")_" not in line:
        temporal = get_temporal(words[-1])
        if temporal == None:
            asignations[words[0]] = asign(words[-1])
    #When a temporal is declared
    if "=" in line and "T" in words[0] and "x" in words[-1] and "&" not in line:
        temporal = get_temporal(words[-1])
        asignations[words[0]] = temporal
    if line.count("=")==1:
        if words[-1] in numbers_list:
            if "T" in words[0]:
                temporal = get_temporal()
                code.append("li $t" + temporal + ", " + words[2])
                asignations[words[0]] = temporal
        if "T" in words[-1] and len(words) == 3:
            first = asignations.get(words[0])
            last = asignations.get(words[-1])
            code.append("move $t" + first + ", $t" + last)
    if "+" in line and "++" not in line:
        temporal = get_temporal()
        first = asignations.get(words[2])
        last = asignations.get(words[4])
        code.append("add $t" + temporal + ", $t" + first + ", $t" + last)
        asignations[words[0]] = temporal
    
    #Acá hay que poner todas las operaciones aritmeticas y lógicas
    # la resta, la multi, la division, los mayor que, los mayor o igual
    # los iguales, los nots, etc. 
        
print(registers)
print(asignations)

print("----------- Code -----------")
for line in code:
    print(line)