import numbers

operators="+-*/"
asignations = {}
code = [".text", "main:"]
data = [".data", 'newline: .asciiz "\n"']
register_counter = 1
parameter_counter = 0
received_parameters = 0
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

parameters  = [
    ["0", None],
    ["1", None],
    ["2", None],
    ["3", None],
]

def get_temporal_for_parameters():
    global received_parameters
    return received_parameters % 4 

#Functions for parameter control
def available_parameter_temporal():
    global parameter_counter
    returnable = parameter_counter
    parameter_counter += 1
    parameter_counter %= 4
    while (parameters[returnable][1] != None):
        returnable = parameter_counter
        parameter_counter += 1
        parameter_counter %= 4
    return str(returnable)

def asign_parameter_temporal(address):
    register = available_parameter_temporal()
    parameters[int(register)][1] = address
    return str(register)
    
def get_parameter_temporal(var=None):
    if(var!=None):
        for register in parameters:
            if register[1] == var:
                return register[0]
        return None
    return available_parameter_temporal()

#Functions for register control
def available():
    global register_counter
    returnable = register_counter
    register_counter += 1
    register_counter %= 10
    areThereFree = False
    for register in registers:
        if(register[1] == None):
            areThereFree = True
    if(not areThereFree):
        return None
    while (registers[returnable][1] != None):
        returnable = register_counter
        register_counter += 1
        register_counter %= 10
    return str(returnable)

def asign(address, save=False):
    register = available()
    if register == None:
        print("Here")
        return
    if(save):
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
    global data
    code = []
    for line in lines:
        print(line)
        words = line.split()
        #When an atribute is declxared
        if ":" in line and "_(" not in line and ")_" not in line:
            temporal = get_temporal(words[-1])
            if temporal == None:
                asignations[words[0]] = "$t" +  asign(words[-1], True)
        #When a temporal is declared
        if "=" in line and "T" in words[0] and "x" in words[-1] and "&" not in line:
            temporal = get_temporal(words[-1])
            asignations[words[0]] = "$t" +  temporal
        if line.count("=")==1:
            if words[-1].isnumeric():
                if "T" in words[0] and "call" not in line:
                    temporal = get_temporal()
                    code.append("li $t" + temporal + ", " + words[2])
                    asignations[words[0]] = "$t" + temporal
            elif '"' in line:
                string_name = "string_" + words[0]
                string = line.split('"')[-2]
                data.append(string_name + ': .asciiz "' + string + '"')
                asignations[words[0]] = string_name
            elif "T" in words[-1] and len(words) == 3:
                first = asignations.get(words[0])
                if(first == None):
                    first = "$t" + asign(words[0])
                    asignations[words[0]] = first
                last = asignations.get(words[-1])
                if("string_" in last):
                    code.append("la " + first + ", " + last)
                else:    
                    code.append("move " + first + ", " + last)
            elif "T" in words[0] and "0x" not in words[-1] and "call" not in line:
                first = asignations.get(words[0])
                if(first == None):
                    first = "$t" + asign(words[0])
                    asignations[words[0]] = first
                last = asignations.get(words[-1])    
                if("string_" in last):
                    code.append("la " + first + ", " + last)
                else:    
                    code.append("move " + first + ", " + last)
        if "++" in line:
            if " Exucatbles at" in line:
                if "Main.main  " in line:
                    pass
                else:
                    code += [
                        "executable_" + line.replace("++++++++++++++++  Exucatbles at ","").replace("  ++++++++++++++++","").replace(".","_") + ":",
                        "addi $sp, $sp, -12",
                        "sw   $ra, 0($sp)",
                        "sw   $s0, 4($sp)",
                        "sw   $s1, 8($sp)"
                        ] 
            if "Atributes of " in line:
                if "Main" in line:
                    pass
                else:
                    code += [
                        "atributes_" + line.replace("++++++++++++++++  Atributes of ", "").replace("  ++++++++++++++++","") + ":"
                        "addi $sp, $sp, -12",
                        "sw   $ra, 0($sp)",
                        "sw   $s0, 4($sp)",
                        "sw   $s1, 8($sp)"
                        ]
            if " End of " in line:
                if "Main.main.1 " in line:
                    code += ["j end"]
                else:
                    code += [
                        "lw   $ra, 0($sp)",        
                        "lw   $s0, 4($sp)",
                        "lw   $s1, 8($sp)",
                        "addi $sp, $sp, 12", 
                        "jr $ra"
                        ]
        if "execute " in line:
            function_name = "executable_" + line.replace("execute ","").replace(".","_")
            code += ["jal " + function_name]
        elif "received param" in line:
            global received_parameters
            temporal = get_temporal()
            asignations[line.split(" ")[-1]] = "$t" + temporal
            code.append("move $t" + temporal + ", $a" + str(received_parameters))
            received_parameters = received_parameters + 1
        elif "call " in line:
            words = line.replace(",","").split(" ")
            code += ["jal executable_" + words[3].replace(".","_")]
            temporal_ = asignations.get(words[0])
            if temporal_ == None:
                temporal_ = "$t" + get_temporal()
                asignations[words[0]] = temporal_
            code += ["move " + temporal_ + ", $a0"]
            global parameters
            parameters  = [
                ["0", None],
                ["1", None],
                ["2", None],
                ["3", None],
            ]
        elif "param" in line:
            temporal = asign_parameter_temporal(line.split(" ")[-1])
            first = asignations.get(line.split(" ")[-1])
            if("string_" in first):
                code.append("la $a" + temporal + ", " + first)
            else:    
                code += ["move $a" + temporal + ", " + first]
        elif "+" in line and "++" not in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("add " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "-" in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("sub " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "==" in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("seq " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "NOT" in line:
            temporal = "$t" + get_temporal()
            temporal_ = "$t" + get_temporal()
            last = asignations.get(words[-1])
            code.append("li " + temporal_ + ", 1")
            code.append("slt " + temporal + ", " + last + ", " + temporal_)
            asignations[words[0]] = temporal
        elif "*" in line and not "= *":
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("mul " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "/" in line and "//" not in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("div " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "<" in line and "<=" not in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("slt " + temporal + ", " + first + ", " + last)
            asignations[words[0]] = temporal
        elif "<=" in line:
            temporal = "$t" + get_temporal()
            first = asignations.get(words[2])
            last = asignations.get(words[4])
            code.append("sle " + temporal + ", " + first + ", " + last)
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
                        on_if[-1][1][1].insert(1, "bne " + asignations.get(control_statement) + ", 0, true_statement" + str(on_if[-1][0][0][0]))
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
                            code += if_code + ["main" + str(if_count - 1) + ":"]
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
                        on_if[-1][1][1].insert(1, "bne " + asignations.get(control_statement) + ", 1, main" + str(on_if[-1][0][0][0]))
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
                            code += while_code + ["main" + str(if_count - 1) + ":"]
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
            if_count += 1
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
                        ["true_statement" + str(if_count) + ":", "j main" + str(if_count)], #true_statement
                        ["false_statement" + str(if_count) + ":", "j main" + str(if_count)] #false_statement
                    ]
                ]
            )
            if_count += 1
        else:  
            code += get_per_line(lines) 
    code += [
        "end:",
        "li $v0, 10",
        "syscall"
        ]
    
    print(registers)
    print(asignations)
        
    in_int = get_temporal()
    code += [
        "",
        "executable_in_int:",
        "addi $sp, $sp, -12",
        "sw   $ra, 0($sp)",
        "sw   $s0, 4($sp)",
        "sw   $s1, 8($sp)",
        "li $v0, 5",
        "syscall",
        "move $t" + in_int +", $v0",
        "move $a0, $t" + in_int,
        "lw   $ra, 0($sp)",        
        "lw   $s0, 4($sp)",
        "lw   $s1, 8($sp)",
        "addi $sp, $sp, 12", 
        "jr $ra",
        " ",
        "executable_out_int:",
        "addi $sp, $sp, -12",
        "sw   $ra, 0($sp)",
        "sw   $s0, 4($sp)",
        "sw   $s1, 8($sp)",
        "li $v0, 1",
        "syscall",
        "li $v0, 4",
        "la $a0, newline",
        "syscall",
        "lw   $ra, 0($sp)",        
        "lw   $s0, 4($sp)",
        "lw   $s1, 8($sp)",
        "addi $sp, $sp, 12", 
        "jr $ra",
        " "
        "",
        "executable_in_bool:",
        "addi $sp, $sp, -12",
        "sw   $ra, 0($sp)",
        "sw   $s0, 4($sp)",
        "sw   $s1, 8($sp)",
        "li $v0, 5",
        "syscall",
        "move $t" + in_int +", $v0",
        "seq $a0, $t" + in_int + ", 1",
        "lw   $ra, 0($sp)",        
        "lw   $s0, 4($sp)",
        "lw   $s1, 8($sp)",
        "addi $sp, $sp, 12", 
        "jr $ra",
        " ",
        "executable_out_bool:",
        "addi $sp, $sp, -12",
        "sw   $ra, 0($sp)",
        "sw   $s0, 4($sp)",
        "sw   $s1, 8($sp)",
        "li $v0, 1",
        "syscall",
        "li $v0, 4",
        "la $a0, newline",
        "syscall",
        "lw   $ra, 0($sp)",        
        "lw   $s0, 4($sp)",
        "lw   $s1, 8($sp)",
        "addi $sp, $sp, 12", 
        "jr $ra",
        " ",
        "executable_out_string:",
        "addi $sp, $sp, -12",
        "sw   $ra, 0($sp)",
        "sw   $s0, 4($sp)",
        "sw   $s1, 8($sp)",
        "li $v0, 4",
        "syscall",
        "lw   $ra, 0($sp)",        
        "lw   $s0, 4($sp)",
        "lw   $s1, 8($sp)",
        "addi $sp, $sp, 12", 
        "jr $ra",
        ""
    ]
    
    global data
    code += data
    print("----------- Code - start -----------")
    for line in code:
        print(line)
    with open('MIPS_generated/code.asm', 'w') as file:
        for n in code:
            file.write(n + "\n")

    print("------------ Code - end ------------")
        
    return code 