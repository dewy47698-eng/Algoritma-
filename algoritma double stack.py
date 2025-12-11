# ==========================================
#          PROGRAM DOUBLE STACK
#       Dua stack dalam satu array
# ==========================================

MAX = 10
array = [None] * MAX

top1 = -1          # Stack 1 mulai dari kiri
top2 = MAX         # Stack 2 mulai dari kanan

# ------------------------------------------
# PUSH STACK 1
# ------------------------------------------
def push1(data):
    global top1, top2
    if top1 + 1 == top2:
        print("Stack 1 & Stack 2 Penuh! Tidak bisa push.")
        return
    
    top1 += 1
    array[top1] = data
    print(f"Push Stack1 : {data}")

# ------------------------------------------
# PUSH STACK 2
# ------------------------------------------
def push2(data):
    global top1, top2
    if top2 - 1 == top1:
        print("Stack 1 & Stack 2 Penuh! Tidak bisa push.")
        return
    
    top2 -= 1
    array[top2] = data
    print(f"Push Stack2 : {data}")

# ------------------------------------------
# POP STACK 1
# ------------------------------------------
def pop1():
    global top1
    if top1 == -1:
        print("Stack1 Kosong!")
        return
    
    val = array[top1]
    top1 -= 1
    print(f"Pop Stack1 : {val}")

# ------------------------------------------
# POP STACK 2
# ------------------------------------------
def pop2():
    global top2
    if top2 == MAX:
        print("Stack2 Kosong!")
        return
    
    val = array[top2]
    top2 += 1
    print(f"Pop Stack2 : {val}")

# ------------------------------------------
# Tampilkan isi array
# ------------------------------------------
def show():
    print("Array:", array)
    print(f"Top1 = {top1}, Top2 = {top2}")
    print("-----------------------------------")

# ==========================================
#                PROGRAM UTAMA
# ==========================================

print("===== PROGRAM DOUBLE STACK DIMULAI =====\n")

push1(10)
push1(20)
push1(30)

push2(99)
push2(88)

show()

pop1()
pop2()

show()

push1(55)
push2(44)
push1(77)

show()

print("===== PROGRAM SELESAI =====")