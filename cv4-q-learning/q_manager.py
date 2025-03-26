import numpy as np
import random

class QLearningManager:
    def __init__(self, rows, cols, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.rows = rows
        self.cols = cols
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = np.zeros((rows, cols, 4))  # Akce: 0=nahoru, 1=dolů, 2=doleva, 3=doprava
        self.visits = np.zeros((rows, cols))  # Počet návštěv každého stavu

    def set_environment(self, mouse, cheese, walls, traps):
        self.mouse = mouse
        self.cheese = cheese
        self.walls = set(walls)
        self.traps = set(traps)
        # Reset statistik při změně prostředí
        self.visits = np.zeros((self.rows, self.cols))
        self.q_table = np.zeros((self.rows, self.cols, 4))

    def get_possible_actions(self, state):
        row, col = state
        actions = []
        if row > 0 and (row-1, col) not in self.walls: actions.append(0)  # Nahoru
        if row < self.rows-1 and (row+1, col) not in self.walls: actions.append(1)  # Dolů
        if col > 0 and (row, col-1) not in self.walls: actions.append(2)  # Doleva
        if col < self.cols-1 and (row, col+1) not in self.walls: actions.append(3)  # Doprava
        return actions

    def get_next_state(self, state, action):
        row, col = state
        new_row, new_col = row, col
        
        if action == 0 and row > 0:  # Nahoru
            new_row = row - 1
        elif action == 1 and row < self.rows - 1:  # Dolů
            new_row = row + 1
        elif action == 2 and col > 0:  # Doleva
            new_col = col - 1
        elif action == 3 and col < self.cols - 1:  # Doprava
            new_col = col + 1
            
        # Kontrola, zda nový stav není zeď
        if (new_row, new_col) in self.walls:
            return (row, col)  # Zůstaneme na místě
            
        return (new_row, new_col)

    def get_reward(self, state):
        if state == self.cheese:
            return 100  # Zvýšit odměnu za sýr
        if state in self.traps:
            return -100  # Zvýšit trest za past
        return -0.01 
    
    def train(self, episodes=1000):
        success_count = 0
        
        for episode in range(episodes):
            state = self.mouse
            steps = 0
            max_steps = self.rows * self.cols * 2  # Maximální počet kroků
            found_cheese = False
            
            while state != self.cheese and steps < max_steps:
                self.visits[state[0], state[1]] += 1
                
                # Epsilon-greedy strategie
                if random.uniform(0, 1) < self.epsilon:
                    possible_actions = self.get_possible_actions(state)
                    if not possible_actions:
                        break
                    action = random.choice(possible_actions)
                else:
                    # Vybereme nejlepší akci z možných
                    possible_actions = self.get_possible_actions(state)
                    if not possible_actions:
                        break
                        
                    q_values = self.q_table[state[0], state[1]]
                    # Maska pro možné akce
                    mask = np.ones(4) * float('-inf')
                    for a in possible_actions:
                        mask[a] = q_values[a]
                    action = np.argmax(mask)
                
                next_state = self.get_next_state(state, action)
                reward = self.get_reward(next_state)
                
                # Q-learning aktualizace
                old_value = self.q_table[state[0], state[1], action]
                
                # Získání maximální Q-hodnoty pro další stav
                next_possible_actions = self.get_possible_actions(next_state)
                if next_possible_actions:
                    next_q_values = [self.q_table[next_state[0], next_state[1], a] for a in next_possible_actions]
                    next_max = max(next_q_values)
                else:
                    next_max = 0
                    
                # Aktualizace Q-hodnoty
                self.q_table[state[0], state[1], action] = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)

                state = next_state
                steps += 1
                
                # Kontrola, zda jsme dosáhli cíle nebo spadli do pasti
                if state == self.cheese:
                    found_cheese = True
                    break
                    
                if state in self.traps:
                    break
            
            # Snížíme epsilon (méně průzkumu, více využití)
            self.epsilon = max(0.01, self.epsilon * 0.99)
            
            # Počítáme úspěšné epizody
            if found_cheese:
                success_count += 1
                print(f"Epizoda {episode+1}: Sýr nalezen po {steps} krocích!")
            else:
                success_count = 0
                print(f"Epizoda {episode+1}: Sýr nenalezen.")
            
            # Pokud jsme našli cestu k sýru v posledních 5 epizodách, můžeme skončit
            if success_count >= 5:
                print(f"Trénink ukončen po {episode+1} epizodách s {success_count} po sobě jdoucími úspěchy.")
                return episode + 1
                
        return episodes

def find_path(self, start, goal):
    path = [start]
    state = start
    steps = 0
    max_steps = self.rows * self.cols * 2
    visited_states = {start: 0}  # Sleduje, kolikrát jsme navštívili každý stav
    
    while state != goal and steps < max_steps:
        possible_actions = self.get_possible_actions(state)
        if not possible_actions:
            return []
        
        # Vybereme akci s nejvyšší Q-hodnotou, která nevede k cyklení
        q_values = self.q_table[state[0], state[1]]
        
        # Seřadíme akce podle Q-hodnot (od nejvyšší)
        sorted_actions = sorted(possible_actions, key=lambda a: q_values[a], reverse=True)
        
        # Zkusíme akce v pořadí od nejlepší
        next_state = None
        for action in sorted_actions:
            candidate_next = self.get_next_state(state, action)
            # Pokud jsme tento stav navštívili méně než 2x, použijeme ho
            if candidate_next not in visited_states or visited_states[candidate_next] < 2:
                next_state = candidate_next
                break
        
        if next_state is None:
            return []  # Nemůžeme najít cestu bez cyklení
        
        # Aktualizujeme počet návštěv
        visited_states[next_state] = visited_states.get(next_state, 0) + 1
        
        path.append(next_state)
        state = next_state
        steps += 1
        
        if state in self.traps:
            return []
    
    if state != goal:
        return []
        
    return path
