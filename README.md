import tkinter as tk
import random
from tkinter import messagebox, FLAT

# --- 1. VARIABEL GLOBAL & KONFIGURASI ---
HUMAN_PLAYER = "X"
COMPUTER_PLAYER = "O"
curr_player = HUMAN_PLAYER
game_over = False

# Skema Warna Neon
COLOR_BG = "#000000"        
COLOR_GRID_NEON = "#9b59b6"  # Ungu Neon
COLOR_NEON_X = "#e74c3c"     # Merah Neon
COLOR_NEON_O = "#3498db"     # Biru Neon
COLOR_TEXT_NORMAL = "#ecf0f1" 
COLOR_TEXT_HIGHLIGHT = "#f1c40f" 

# Font (Compact)
FONT_DEFAULT = ("Orbitron", 10) 
FONT_CELL = ("Orbitron", 40, "bold") 
FONT_STATUS = ("Orbitron", 18, "bold") 
FONT_BUTTON = ("Orbitron", 14, "bold") 

# Papan Tic Tac Toe 3x3
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board_state = [['' for _ in range(3)] for _ in range(3)]
difficulty_var = None

# --- 2. FUNGSI AI (MINIMAX) ---

def check_winner_ai(current_board):
    """Memeriksa pemenang pada papan internal."""
    # Cek Baris, Kolom, Diagonal
    for i in range(3):
        if current_board[i][0] == current_board[i][1] == current_board[i][2] != '':
            return 10 if current_board[i][0] == COMPUTER_PLAYER else -10
        if current_board[0][i] == current_board[1][i] == current_board[2][i] != '':
            return 10 if current_board[0][i] == COMPUTER_PLAYER else -10
    if current_board[0][0] == current_board[1][1] == current_board[2][2] != '':
        return 10 if current_board[0][0] == COMPUTER_PLAYER else -10
    if current_board[0][2] == current_board[1][1] == current_board[2][0] != '':
        return 10 if current_board[0][2] == COMPUTER_PLAYER else -10
    return 0

def is_moves_left(current_board):
    """Memeriksa apakah ada langkah tersisa."""
    for row in current_board:
        if '' in row:
            return True
    return False

def minimax(current_board, depth, is_maximizing):
    """Algoritma Minimax."""
    score = check_winner_ai(current_board)
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not is_moves_left(current_board): return 0
    
    if is_maximizing:
        best_score = -float('inf')
        # ... (Minimax memaksimalkan untuk COMPUTER_PLAYER)
        for r in range(3):
            for c in range(3):
                if current_board[r][c] == '':
                    current_board[r][c] = COMPUTER_PLAYER
                    best_score = max(best_score, minimax(current_board, depth + 1, False))
                    current_board[r][c] = ''
        return best_score
    else:
        best_score = float('inf')
        # ... (Minimax meminimalkan untuk HUMAN_PLAYER)
        for r in range(3):
            for c in range(3):
                if current_board[r][c] == '':
                    current_board[r][c] = HUMAN_PLAYER
                    best_score = min(best_score, minimax(current_board, depth + 1, True))
                    current_board[r][c] = ''
        return best_score

def minimax_best_move():
    """Mencari langkah terbaik dari Minimax."""
    best_score = -float('inf')
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board_state[r][c] == '':
                board_state[r][c] = COMPUTER_PLAYER
                move_score = minimax(board_state, 0, False)
                board_state[r][c] = ''
                if move_score > best_score:
                    best_score = move_score
                    best_move = (r, c)
    return best_move

def get_random_move():
    """Mengambil langkah acak yang tersedia."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board_state[r][c] == '']
    return random.choice(empty_cells) if empty_cells else (-1, -1)

def get_ai_move():
    """Menentukan langkah AI berdasarkan kesulitan yang dipilih."""
    difficulty = difficulty_var.get()
    if difficulty == "Easy": return get_random_move()
    elif difficulty == "Medium":
        if random.random() < 0.2: return get_random_move()  # 20% membuat kesalahan
        else: return minimax_best_move() 
    elif difficulty == "Hard": return minimax_best_move()  # 100% langkah terbaik
    return get_random_move()

# --- 3. FUNGSI GUI ---

def highlight_winning_line(winning_cells, winner_char):
    """Menyorot garis kemenangan."""
    accent_color = COLOR_NEON_X if winner_char == HUMAN_PLAYER else COLOR_NEON_O
    for r, c in winning_cells:
        board[r][c].config(
            background=COLOR_GRID_NEON, 
            foreground=accent_color
        )

def update_gui_after_move(row, col, player, check_win=True):
    """Mengupdate tampilan setelah sebuah langkah."""
    global curr_player, game_over

    text_color = COLOR_NEON_X if player == HUMAN_PLAYER else COLOR_NEON_O
    
    board[row][col].config(
        text=player, 
        foreground=text_color,
        background=COLOR_BG
    )
    
    board_state[row][col] = player

    if check_win:
        score = check_winner_ai(board_state)
        
        if score != 0 or not is_moves_left(board_state):
            game_over = True
            winner_text = ""
            if score == 10: winner_text = f"{COMPUTER_PLAYER} WINS!"
            elif score == -10: winner_text = f"{HUMAN_PLAYER} WINS!"
            else: winner_text = "IT'S A TIE!"
            
            label.config(text=winner_text, foreground=COLOR_TEXT_HIGHLIGHT)

            if score != 0:
                # Logika pencarian garis kemenangan
                winning_cells = []
                for r_idx in range(3):
                    if board_state[r_idx][0] == board_state[r_idx][1] == board_state[r_idx][2] == player:
                        winning_cells = [(r_idx, 0), (r_idx, 1), (r_idx, 2)]; break
                if not winning_cells:
                    for c_idx in range(3):
                        if board_state[0][c_idx] == board_state[1][c_idx] == board_state[2][c_idx] == player:
                            winning_cells = [(0, c_idx), (1, c_idx), (2, c_idx)]; break
                if not winning_cells:
                    if board_state[0][0] == board_state[1][1] == board_state[2][2] == player:
                        winning_cells = [(0, 0), (1, 1), (2, 2)]
                    elif board_state[0][2] == board_state[1][1] == board_state[2][0] == player:
                        winning_cells = [(0, 2), (1, 1), (2, 0)]
                
                if winning_cells: highlight_winning_line(winning_cells, player)
                
            messagebox.showinfo("Game Over", winner_text)
            return True
    
    return False

def ai_move():
    """Langkah Komputer."""
    global curr_player
    if game_over: return
    row, col = get_ai_move()
    if row != -1:
        curr_player = COMPUTER_PLAYER
        if update_gui_after_move(row, col, COMPUTER_PLAYER): return 
        curr_player = HUMAN_PLAYER
        label.config(text=f"{curr_player}'s TURN", foreground=COLOR_TEXT_NORMAL)

def set_tile(row, col):
    """Langkah Pemain Manusia."""
    global curr_player, game_over
    if game_over or board_state[row][col] != '' or curr_player == COMPUTER_PLAYER: return

    if update_gui_after_move(row, col, HUMAN_PLAYER): return
    ai_move()

def new_game():
    """Mengatur ulang permainan."""
    global game_over, curr_player, board_state
    
    # Pastikan variabel/objek yang tidak digunakan tidak ada dalam fungsi ini (menghindari 'Nejin')
    
    game_over = False
    curr_player = HUMAN_PLAYER
    board_state = [['' for _ in range(3)] for _ in range(3)]

    label.config(text=f"{curr_player}'s TURN", foreground=COLOR_TEXT_NORMAL)

    for row in range(3):
        for col in range(3):
            board[row][col].config(
                text="", 
                foreground=COLOR_TEXT_NORMAL, 
                background=COLOR_BG,
                relief=FLAT, 
                bd=0 
            )
    
# --- 4. PENGATURAN UI UTAMA (TKINTER) ---

window = tk.Tk()
window.title("Tic Tac Toe (Neon Glow - Compact)")
window.resizable(False, False)
window.config(bg=COLOR_BG)

main_frame = tk.Frame(window, bg=COLOR_BG, padx=10, pady=10)
main_frame.pack()

# Inisialisasi difficulty_var di luar fungsi
global difficulty
difficulty_var = tk.StringVar(window)
difficulty_var.set("Hard")

# 4.1. Pemilihan Kesulitan
DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"]
difficulty_menu = tk.OptionMenu(main_frame, difficulty_var, *DIFFICULTY_OPTIONS)
difficulty_menu.config(
    font=FONT_DEFAULT, 
    bg=COLOR_GRID_NEON, 
    fg=COLOR_TEXT_NORMAL, 
    activebackground=COLOR_NEON_O, 
    relief=FLAT, 
    bd=0,
    highlightthickness=0
)

difficulty_label = tk.Label(
    main_frame, 
    text="DIFFICULTY:", 
    font=FONT_DEFAULT, 
    background=COLOR_BG, 
    foreground=COLOR_TEXT_NORMAL
)

difficulty_label.grid(row=0, column=0, sticky="w", padx=(0, 5), pady=5)
difficulty_menu.grid(row=0, column=1, columnspan=2, sticky="we", padx=(0, 0), pady=5)


# 4.2. Label Status Pemain
label = tk.Label(
    main_frame, 
    text=f"{curr_player}'s TURN",
    font=FONT_STATUS,
    background=COLOR_BG,
    foreground=COLOR_TEXT_NORMAL,
    pady=10 
)
label.grid(row=1, column=0, columnspan=3, sticky="we")

# Frame untuk papan permainan (dengan grid neon)
board_frame = tk.Frame(main_frame, bg=COLOR_GRID_NEON, bd=3, relief=FLAT) 
board_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=0)


# 4.3. Membuat 9 Tombol Papan Game
for row in range(3):
    for col in range(3):
        button = tk.Button(
            board_frame,
            text="", 
            font=FONT_CELL,
            background=COLOR_BG,
            foreground=COLOR_TEXT_NORMAL,
            width=3, 
            height=1, 
            command=lambda r=row, c=col: set_tile(r, c),
            relief=FLAT,
            bd=0,
            highlightthickness=0,
            activebackground=COLOR_BG,
            activeforeground=COLOR_TEXT_NORMAL
        )
        board[row][col] = button
        button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew") 

for i in range(3):
    board_frame.grid_rowconfigure(i, weight=1)
    board_frame.grid_columnconfigure(i, weight=1)


# 4.4. Tombol Restart
restart_button = tk.Button(
    main_frame,
    text="RESTART GAME",
    font=FONT_BUTTON,
    background=COLOR_GRID_NEON,
    foreground=COLOR_TEXT_NORMAL,
    command=new_game,
    relief=FLAT,
    bd=0,
    highlightthickness=0,
    activebackground=COLOR_NEON_O,
    activeforeground=COLOR_TEXT_HIGHLIGHT,
    pady=10
)
restart_button.grid(row=3, column=0, columnspan=3, sticky="we", pady=10)


# Penempatan di tengah layar
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int(screen_width / 2 - window_width / 2)
window_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

new_game() 

window.mainloop()
