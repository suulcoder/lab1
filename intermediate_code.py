import numbers

operators="+-*/"
asignations = {}
code = [".text", "main:"]
register_counter = 0
on_if = []
if_count = 0

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

def get_per_line(lines):
    code = []
    for line in lines:
        words = line.split()
        #When an atribute is declxared
        if ":" in line and "_(" not in line and ")_" not in line:
            temporal = get_temporal(words[-1])
            if temporal == None:
                asignations[words[0]] = asign(words[-1])
        #When a temporal is declared
        if "=" in line and "T" in words[0] and "x" in words[-1] and "&" not in line:
            temporal = get_temporal(words[-1])
            asignations[words[0]] = temporal
        if line.count("=")==1:
            if words[-1].isnumeric():
                if "T" in words[0]:
                    temporal = get_temporal()
                    code.append("li $t" + temporal + ", " + words[2])
                    asignations[words[0]] = temporal
            if "T" in words[-1] and len(words) == 3:
                first = asignations.get(words[0])
                if(first == None):
                    first = asign(words[0])
                    asignations[words[0]] = first
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
    
    return code

def get_assembly_code(intermidate_code):
    global if_count
    global code
    for code_line in intermidate_code:
        lines = code_line.split('\n')
        if len(on_if) != 0:
            control_status = on_if[-1][0][0][1]
            if(control_status == "if"):
                if_status = len(on_if[-1][0])
                if if_status == 4:  #We are on a true statement
                    true_statement = on_if[-1][0][1]
                    true_code = get_per_line(lines)
                    for code_ in true_code:
                        on_if[-1][1][2].insert(-1, code_)
                    if(true_statement in code_line):
                        del on_if[-1][0][1]
                elif if_status == 3:  #We are on a false statement
                    false_statement = on_if[-1][0][1]
                    false_code = get_per_line(lines)
                    for code_ in false_code:
                        on_if[-1][1][3].insert(-1, code_)
                    if(false_statement in code_line):
                        del on_if[-1][0][1]
                elif if_status == 2:  #We are on a control statement
                    control_statement = on_if[-1][0][1]
                    control_code = get_per_line(lines)
                    for code_ in control_code:
                        on_if[-1][1][0] += [code_]
                    if(control_statement in code_line):
                        on_if[-1][1][1].insert(1, "bne $t" + asignations.get(control_statement) + ", 0, true_statement" + str(on_if[-1][0][0][0]))
                        #Code is added
                        if_code = on_if[-1][1][0] + on_if[-1][1][1] + on_if[-1][1][2] + on_if[-1][1][3]
                        del on_if[-1]
                        if(len(on_if)!=0):
                            control_status = on_if[-1][0][0][1]
                            if(control_status == "if"):
                                if_status = len(on_if[-1][0])
                                if if_status == 4: 
                                    for code_ in if_code:
                                        on_if[-1][1][2].insert(-1, code_)
                                elif if_status == 3: 
                                    for code_ in if_code:
                                        on_if[-1][1][3].insert(-1, code_)
                                elif if_status == 3: 
                                    for code_ in if_code:
                                        on_if[-1][1][0].insert(-1, code_)
                            elif(control_status=="while"):
                                if(while_status==5):
                                    for code_ in if_code:
                                        on_if[-1][1][0].insert(-1, code_)
                                else:
                                    on_if[-1][1][1].insert(-1, code_)
                        else:
                            code += if_code + ["main" + str(if_count) + ":"]
            elif(control_status=="while"):
                while_status = len(on_if[-1][0])
                if(while_status==5):   #We are on control_statement
                    control_statement = on_if[-1][0][1]
                    control_code = get_per_line(lines)
                    for code_ in control_code:
                        on_if[-1][1][0] += [code_]
                    if(control_statement in code_line):
                        del on_if[-1][0][1]
                else:                  #We are on while statement
                    next_statement = on_if[-1][0][-1]
                    control_statement = on_if[-1][0][-2]
                    while_code = get_per_line(lines)
                    for code_ in while_code:
                        on_if[-1][1][1].insert(-1, code_)
                    if(next_statement in code_line):
                        on_if[-1][1][1].insert(1, "bne $t" + asignations.get(control_statement) + ", 1, main" + str(on_if[-1][0][0][0]))
                        extra_code = get_per_line([on_if[-1][0][1]])
                        for code_ in extra_code:
                            on_if[-1][1][1].insert(-1, code_)
                        while_code = on_if[-1][1][0] + on_if[-1][1][1] 
                        del on_if[-1]
                        if(len(on_if)!=0):
                            control_status = on_if[-1][0][0][1]
                            if(control_status == "if"):
                                if_status = len(on_if[-1][0])
                                if if_status == 4: 
                                    for code_ in while_code:
                                        on_if[-1][1][2].insert(-1, code_)
                                elif if_status == 3: 
                                    for code_ in while_code:
                                        on_if[-1][1][3].insert(-1, code_)
                                elif if_status == 3: 
                                    for code_ in while_code:
                                        on_if[-1][1][0].insert(-1, code_)
                            elif(control_status=="while"):
                                if(while_status==5):
                                    for code_ in while_code:
                                        on_if[-1][1][0].insert(-1, code_)
                                else:
                                    on_if[-1][1][1].insert(-1, code_)
                        else:
                            code += while_code + ["main" + str(if_count) + ":"]
        elif "ifFALSE" in code_line:
            while_structure = code_line.split("\n")
            control_statement = while_structure[2].split(" ")[1]
            while_last_line = while_structure[3]
            next_statement = "_(" + str(int(while_structure[4].split(" ")[-1].replace("_(","").replace(")_","")) + 1) + ")_"
            on_if.append(
                [
                    [[if_count, "while"], control_statement, while_last_line, control_statement, next_statement],
                    [
                        ["control_statement" + str(if_count) + ":"], #Control_statement
                        ["while_statement" + str(if_count) + ":", "j control_statement" + str(if_count)], #while_statement
                    ]
                ]
            )
        elif "if" in code_line:
            if_structure = code_line.replace("\n","").split(" ")
            control_statement = if_structure[3]
            true_statement = if_structure[5]
            false_statement = if_structure[7]
            on_if.append(
                [
                    [[if_count, "if"], true_statement, false_statement, control_statement],
                    [
                        ["control_statement" + str(if_count) + ":"], #Control_statement
                        ["if_statement" + str(if_count) + ":" , "j false_statement" + str(if_count)], #if_statement
                        ["true_statement" + str(if_count) + ":", "j main" + str(if_count + 1)], #true_statement
                        ["false_statement" + str(if_count) + ":", "j main" + str(if_count + 1)] #false_statement
                    ]
                ]
            )
            if_count += 1
        else:  
            code += get_per_line(lines) 
                    
    print(registers)
    print(asignations)

    print("----------- Code -----------")
    for line in code:
        print(line)
        
    return code 