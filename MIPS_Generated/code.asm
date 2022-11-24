.text
main:
li $t2, 5
move $t3, $t2
li $t4, 1
move $t5, $t4
jal executable_Main_main_1
executable_Main_main_1:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $t6, 0
move $t1, $t6
li $t7, 210
seq $t8, $t1, $t7
move $t9, $t8
li $t2, 1
slt $t0, $t8, $t2
move $t5, $t0
control_statement0:
move $t4, $t5
while_statement0:
bne $t4, 1, main0
move $t6, $t1
move $a0, $t6
jal executable_out_int
move $t7, $a0
jal executable_Main_main_2
j control_statement0
main0:
j end
executable_Main_main_2:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $t8, 5
move $t9, $t8
add $t0, $t1, $t8
move $t1, $t0
li $t2, 210
seq $t4, $t1, $t2
move $t6, $t4
li $t8, 1
slt $t7, $t4, $t8
move $t5, $t7
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra
end:
li $v0, 10
syscall

executable_in_int:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $v0, 5
syscall
move $t9, $v0
move $a0, $t9
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra
 
executable_out_int:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $v0, 1
syscall
li $v0, 4
la $a0, newline
syscall
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra
 
executable_in_bool:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $v0, 5
syscall
move $t9, $v0
seq $a0, $t9, 1
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra
 
executable_out_bool:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $v0, 1
syscall
li $v0, 4
la $a0, newline
syscall
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra
 
executable_out_string:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
li $v0, 4
syscall
lw   $ra, 0($sp)
lw   $s0, 4($sp)
lw   $s1, 8($sp)
addi $sp, $sp, 12
jr $ra

.data
newline: .asciiz "\n"
