.data
	.align 2

.text
	.globl main

main: 
	li $t0, 4
	move $t1, $t0

	li $t2, 2 
	move $t3, $t2

	li $t4, 0 

	move $t5, $t4
	move $t6, $t1
	move $t7, $t3

	div $t8, $t6, $t7 
	
	li $v0,1
 	move $a0,$t8
	syscall