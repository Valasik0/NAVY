import numpy as np
import random

class QLearningManager:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.q_table = np.zeros((rows * cols, 4))  #Q-tabulka pro vsechny stavy a akce
        self.visits = np.zeros((rows * cols, 4))   #matice navstev pro sledovani frekvence akci
        self.alpha = 0.1                           #rychlost uceni - jak rychle se aktualizuji hodnoty
        self.gamma = 0.9                           #diskontni faktor - vaha budoucich odmen
        self.epsilon = 0.1                         # Pravdepodobnost nahodneho prozkoumavani
        self.actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  #nahoru, dolu, vlevo, vpravo
        self.mouse_pos = None                  
        self.cheese_pos = None               
        self.walls = []                       
        self.traps = []                         

        
    def set_environment(self, mouse_pos, cheese_pos, walls, traps):
        self.mouse_pos = mouse_pos
        self.cheese_pos = cheese_pos
        self.walls = walls
        self.traps = traps
        
    def get_state_index(self, position):
        #prevadi 2D pozici (radek, sloupec) na 1D index pro Q-tabulku
        row, col = position
        return row * self.cols + col
        
    def get_valid_actions(self, position):
        #vraci seznam platnych akci z dane pozice (vyhyba se zdem a hranicim)
        valid_actions = []
        for i, (dr, dc) in enumerate(self.actions):
            new_row, new_col = position[0] + dr, position[1] + dc

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if (new_row, new_col) not in self.walls:
                    valid_actions.append(i)
        return valid_actions
    
    def get_next_state(self, state, action):
        row, col = state
        dr, dc = self.actions[action]
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < self.rows and 0 <= new_col < self.cols and (new_row, new_col) not in self.walls:
            return (new_row, new_col)
        return state  #zustane pokud narazi na stenu
    
    def get_reward(self, state):
        if state == self.cheese_pos:
            return 100  #odmena za syr
        elif state in self.traps:
            return -100  #trest za past
        return -1  #maly trest za kazdy krok (motivace najit nejkratsi cestu)
    
    def choose_action(self, state, valid_actions):
        if random.random() < self.epsilon:
            return random.choice(valid_actions)
        else:
            state_index = self.get_state_index(state)
            q_values = [self.q_table[state_index][a] for a in valid_actions]
            max_q = max(q_values)
            best_actions = [valid_actions[i] for i, q in enumerate(q_values) if q == max_q]
            return random.choice(best_actions)
    
    def train(self, max_episodes=1000):
    #hlavni metoda pro uceni Q-tabulky
        episodes = 0
        
        for episode in range(max_episodes):
            current_state = self.mouse_pos
            done = False
            
            while not done:
                #vyber a provedeni akce
                valid_actions = self.get_valid_actions(current_state)
                action = self.choose_action(current_state, valid_actions)
                
                next_state = self.get_next_state(current_state, action)
                reward = self.get_reward(next_state)

                #aktualizace Q-tabulky
                current_state_index = self.get_state_index(current_state)
                next_state_index = self.get_state_index(next_state)

                old_value = self.q_table[current_state_index][action]
                next_max = np.max(self.q_table[next_state_index])
                
                new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
                self.q_table[current_state_index][action] = new_value
                
                self.visits[current_state_index][action] += 1
                
                current_state = next_state

                #kontrola ukonceni epizody
                if next_state == self.cheese_pos or next_state in self.traps:
                    done = True
            
            episodes += 1

            #predcasne ukonceni pokud agent uz umi najit cestu
            if episode > 100 and self.test_path():
                break
                
        return episodes

    
    def test_path(self):
    # testuje zda agent umi najit cestu k syru
        current_state = self.mouse_pos
        visited = set([current_state])
        max_steps = self.rows * self.cols * 2  #maximalni pocet kroku
        
        for _ in range(max_steps):
            valid_actions = self.get_valid_actions(current_state)
            state_index = self.get_state_index(current_state)

            #vyber nejlepsi akce podle naucene Q-tabulky
            best_action = np.argmax([self.q_table[state_index][a] if a in valid_actions else -np.inf for a in range(4)])
            
            next_state = self.get_next_state(current_state, best_action)

            #kontrola cyklu
            if next_state in visited:
                return False
            
            visited.add(next_state)
            current_state = next_state
            
            # Kontrola cile nebo pasti
            if current_state == self.cheese_pos:
                return True
            if current_state in self.traps:
                return False
                
        return False

    def find_path(self, start_pos, end_pos):
        #hleda cestu od startu k cili pomoci naucene Q-tabulky
        path = [start_pos]
        current_state = start_pos
        max_steps = self.rows * self.cols * 2  #maximalni pocet kroku
        
        for _ in range(max_steps):
            valid_actions = self.get_valid_actions(current_state)
            state_index = self.get_state_index(current_state)
            
            #vyber nejlepsi akce
            action_values = [self.q_table[state_index][a] if a in valid_actions else -np.inf for a in range(4)]
            best_action = np.argmax(action_values)
            
            next_state = self.get_next_state(current_state, best_action)
            path.append(next_state)
            
            #kontrola dosazeni cile
            if next_state == end_pos:
                return path
                
            current_state = next_state

            #kontrola cyklu
            if path.count(next_state) > 1:
                return None  #cyklus detekovan
                
        return None  #cesta nenalezena
