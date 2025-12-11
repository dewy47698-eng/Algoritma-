import time
import os

# =============================
#       WARNA ANSI
# =============================
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

# =============================
#     ANIMASI SEDERHANA
# =============================
def anim(text):
    for i in range(3):
        print(f"{Color.CYAN}{text}{'.' * (i+1)}{Color.RESET}", end="\r")
        time.sleep(0.25)
    print(" " * 20, end="\r")

# =============================
#       STRUKTUR STACK
# =============================
stack = []

def push(data):
    anim("Menambahkan")
    stack.append(data)
    print(f"{Color.GREEN}✔ Push: {data}{Color.RESET}")
    show_stack()

def pop():
    anim("Menghapus")
    if len(stack) == 0:
        print(Color.RED + "✘ Stack kosong, tidak bisa POP!" + Color.RESET)
    else:
        val = stack.pop()
        print(Color.YELLOW + f"✔ Pop: {val}" + Color.RESET)
    show_stack()

def peek():
    if len(stack) == 0:
        print(Color.RED + "✘ Stack kosong!" + Color.RESET)
    else:
        print(Color.BLUE + f"Top → {stack[-1]}" + Color.RESET)

def is_empty():
    return len(stack) == 0

# =============================
#  VISUALISASI STACK (VERTIKAL)
# =============================
def show_stack():
    print(Color.MAGENTA + "\nTampilan Stack:" + Color.RESET)
    if len(stack) == 0:
        print(Color.RED + "[ KOSONG ]\n" + Color.RESET)
        return
    
    for i in range(len(stack)-1, -1, -1):
        print(Color.GREEN + f"|   {stack[i]}   |" + Color.RESET)
        print(Color.GREEN + "+-------+" + Color.RESET)
    print()

# =============================
#        PROGRAM UTAMA
# =============================
os.system("cls" if os.name == "nt" else "clear")

print(Color.YELLOW + "==== PROGRAM STACK MENARIK ====\n" + Color.RESET)

push(10)
time.sleep(0.5)
push(20)
time.sleep(0.5)
push(30)

time.sleep(0.5)
peek()

time.sleep(0.7)
pop()

time.sleep(0.7)
push(99)

print(Color.CYAN + "\n==== PROGRAM SELESAI ====" + Color.RESET)