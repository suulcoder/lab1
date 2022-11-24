.text
main:
li $t1, 60
move $t2, $t1
li $t3, 15
move $t4, $t3
li $t6, 1
move $t7, $t6
jal executable_Main_main_1
executable_Main_main_1:
addi $sp, $sp, -12
sw   $ra, 0($sp)
sw   $s0, 4($sp)
sw   $s1, 8($sp)
move $t8, $t2
slt $t9, $t4, $t2
move $t5, $t9
control_statement0:
if_statement0:
bne $t5, 0, true_statement0
j false_statement0
true_statement0:
li $t0, 1000
move $t7, $t0
j main0
false_statement0:
li $t1, 0
move $t7, $t1
j main0
main0:
li $t3, 0
j end
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
move $t6, $v0
move $a0, $t6
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
move $t6, $v0
seq $a0, $t6, 1
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
newline: .asciiz "
"
