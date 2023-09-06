from os import name, system
from colorama import Fore, Style
from time import sleep

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

class Game_grid:
    def __init__(self, columns:int | None = 5, rows:int | None = 5, sheet_size = str, selected_level = int, grid = {}, levels = {}, levels_conclusion = {}, colors = {"Black":"30", "Red":"31", "Green":"32", "Yellow":"33", "Blue":"34", "Magenta":"35", "Cyan":"36", "White":"37", "Light black":"90", "Light red":"91", "Light green":"92", "Light yellow":"93", "Light blue":"94", "Light magenta":"95", "Light cyan":"96", "Light white":"97"}, aktive_colors = []):
        self.columns = columns
        self.rows = rows
        self.sheet_size = sheet_size
        self.selected_level = selected_level
        self.grid = grid
        self.levels = levels
        self.levels_conclusion = levels_conclusion
        self.colors = colors
        self.aktive_colors = aktive_colors
    def generate_grid(self):
        for i in range(self.columns):
            self.grid[i] = {}
            for j in range(self.rows):
                self.grid[i][j] = "-"
        
    def print_grid(self):
        print("   ", end="")
        for i in range(1, self.columns + 1):
            print(i, end="   ")
        print("Level colors:")
        for i in self.grid.keys():
            print(i + 1,end="")
            for j in self.grid[i].keys():
                print(f"| {self.grid[j][i]} ", end="")
            print("|", end="      ")
            print(self.aktive_colors[i])
            
    
    def select_level_new(self):
        clear()
        with open("levels.txt") as l: # Takes levels from document and ads them in class dictionary in layerformat: {sheet_size:[index is levels and has lists in lists where the index is cordinates, x then y then colored '-']}
            levels_list = l.read().split("\n")
            for i in range(len(levels_list)):
                if len(levels_list[i]) <= 5:
                    sheet_size = levels_list[i]
                    self.levels[sheet_size] = []
                else:
                    self.levels[sheet_size].append(levels_list[i].split("|"))
                    for j in range(len(self.levels[sheet_size][-1])):
                        self.levels[sheet_size][-1][j] = self.levels[sheet_size][-1][j].split(":")
                        self.levels[sheet_size][-1][j][-1] = "[" + self.levels[sheet_size][-1][j][-1] + "m-[0m"
        
        with open("levels_conclusion.txt") as lc: # Does the same but with the conclusion of all the levels and in the same format
            levels_conclusion_list = lc.read().split("\n")
            for i in range(len(levels_conclusion_list)):
                if len(levels_conclusion_list[i]) <= 5:
                    sheet_size = levels_conclusion_list[i]
                    self.levels_conclusion[sheet_size] = []
                else:
                    self.levels_conclusion[sheet_size].append(levels_conclusion_list[i].split("|"))
                    for j in range(len(self.levels_conclusion[sheet_size][-1])):
                        self.levels_conclusion[sheet_size][-1][j] = self.levels_conclusion[sheet_size][-1][j].split(":")
                        self.levels_conclusion[sheet_size][-1][j][-1] = "[" + self.levels_conclusion[sheet_size][-1][j][-1] + "m-[0m"
            
        
        print("Select sheet size: ")
        for i in self.levels.keys():
            print(i)
        
        self.sheet_size = input()
        for i in self.levels.keys():
            if self.sheet_size == i:
                grid_size = self.sheet_size.split("x")
                self.columns = int(grid_size[0])
                self.rows = int(grid_size[-1])
                print("Select the level: ")
                for j in range(len(self.levels[i])):
                    print(f"Level {j + 1}")
                
                selected_level = input().capitalize()
                for j in range(len(self.levels[i])):
                    if selected_level.endswith(str(j + 1)) == True:
                        self.selected_level = j 
                        self.generate_grid()
                        print(self.levels)
                        for k in range(len(self.levels[i][j])):
                            self.grid[int(self.levels[i][j][k][0])][int(self.levels[i][j][k][1])] = self.levels[i][j][k][-1]
                            self.aktive_colors.append(self.levels[i][j][k][-1])
                    else:
                        pass    
            else:
                pass
    
    
    def check_level_completion(self):
        for i in self.grid.keys():
            for j in self.grid[i].keys():
                #print(self.grid)
                #print(self.sheet_size)
                #print(self.selected_level)
                #print(self.grid[i][j])
                #print(self.selected_level)
                #print(self.levels_conclusion)
                #print(self.levels_conclusion[self.sheet_size][self.selected_level][i][j])
                if self.grid[i][j] == self.levels_conclusion[self.sheet_size][self.selected_level][i][j]:
                    pass
                else:
                    return False
        return True
            
    
    
    def select_level(self):
        clear()
        with open("levels.txt") as l:
            levels_list = l.read().split("\n") # Seperates different levels
            for i in range(len(levels_list)):
                self.levels[i] = levels_list[i].split("|") # Seperates each color nodes from each other in the same level
                for j in range(len(self.levels[i])):
                    self.levels[i][j] = self.levels[i][j].split(":") # Seperates each colornodes into their own list as -> [x,y,color key]
                    
                    for k in self.colors.keys(): # Replaces the color key with a '-' in said color
                        if self.levels[i][j][-1] == self.colors[k]:
                            self.levels[i][j][-1] = "[" + self.levels[i][j][-1] + "m-[0m"
                
                
        print("Select the level: ")
        for i in range(len(self.levels.keys())):
            print(f"Level {i + 1}")
        
        selected_level = input().capitalize()
        for i in range(len(self.levels.keys())): # Selects level
            if selected_level.endswith(str(i + 1)) == True: # Checking if it exists
                self.generate_grid()
                print(self.levels)
                for j in range(len(self.levels[i])): # Selects color node and adds it to the grid
                    self.grid[int(self.levels[i][j][0])][int(self.levels[i][j][1])] = self.levels[i][j][-1]
            else:
                pass
    
        
    def playing_level(self):
        while True:
            clear()
            self.print_grid()
            print("Select cordinate where you want to change the color:")
            col = int(input("Select x: ")) -1
            row = int(input("Select y: ")) -1
            color = input("Select color:").capitalize()
            if color in self.colors:
                pass
            else:
                print("Invalide color or cordinate, please try again.")
                
            for i in self.colors.keys():
                if color == i:
                    color = "[" + self.colors[i] + "m-[0m"
                    self.grid[col][row] = color
                    if self.check_level_completion() == True:
                        print("You completed the level!")
                    else:
                        pass
                    continue
            sleep(1)
            
        
        
        
    def main(self):
        while True:
            clear()
            match (input("Flowy game\n\nSelect level\nQuit\n").capitalize()):
                case "Select level":
                    self.select_level_new()
                    self.playing_level()
                case "Quit":
                    break
    
if __name__ == "__main__":
# Add color or level in format below or write directly in file in the following format:
# '|' seperates colors
# ':' seperates cordinates and colored '-'
# Index for different collors are:
#   Black: [30m-[0m
#   Red: [31m-[0m
#   Green: [32m-[0m
#   Yellow: [33m-[0m
#   Blue: [34m-[0m
#   Magenta: [35m-[0m
#   Cyan: [36m-[0m
#   White: [37m-[0m
#
#   Light Black: [90m-[0m
#   Light Red: [91m-[0m
#   Light Green: [92m-[0m
#   Light Yellow: [93m-[0m
#   Light Blue: [94m-[0m
#   Light Magenta: [95m-[0m
#   Light Cyan: [96m-[0m
#   Light White: [97m-[0m
#
#    with open("levels.txt", "a") as l:
#        l.write("|0:4:" + Fore.GREEN + "-" + Style.RESET_ALL + "|1:4:" + Fore.RED + "-" + Style.RESET_ALL + "|2:4:" + Fore.BLUE + "-" + Style.RESET_ALL + "|3:4:" + Fore.CYAN + "-" + Style.RESET_ALL + "|4:4:"+ Fore.YELLOW + "-" + Style.RESET_ALL)
#    with open("levels.txt", "a") as l:
#        l.write("0:0:" + Fore.WHITE + "White" + Style.RESET_ALL)
    new_game_grid = Game_grid()
    new_game_grid.main()