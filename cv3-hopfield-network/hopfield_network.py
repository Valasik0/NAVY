import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        #inicializace Hopfieldovy site
        #size: celkovy pocet neuronu v siti (pro mrizku 10x10 je to 100)
        self.size = size
        #inicializace matice vah jako nulove matice o rozmerech size x size
        self.weights = np.zeros((self.size, self.size))

    def train(self, patterns):
        #trenovani site na sade vzoru
        #patterns: seznam vzoru, kde kazdy vzor je reprezentovan jako seznam hodnot 1 a -1
        
        #vynulovani matice vah pred trenovanim
        self.weights.fill(0)
        
        #pro kazdy vzor pridame do matice vah soucin vzoru se sebou samym
        for pattern in patterns:
            #prevedeni vzoru na sloupcovy vektor
            p = np.array(pattern).reshape(self.size, 1)
            #aktualizace matice vah pomoci vnejsiho soucinu vzoru se sebou samym
            #p @ p.T vytvori matici, kde kazdy prvek (i,j) je soucinem p[i] a p[j]
            self.weights += p @ p.T
            
        #nastaveni diagonaly matice vah na nulu, aby se zabranilo auto-asociaci
        #(neuron by nemel ovlivnovat sam sebe)
        np.fill_diagonal(self.weights, 0)

    def sync_update(self, pattern):
        #synchronni aktualizace - vsechny neurony jsou aktualizovany soucasne
        #pattern: vstupni vzor, ktery chceme opravit
        
        #vypocet noveho stavu vsech neuronu najednou pomoci nasobeni matice vah a vstupniho vzoru
        #np.sign vraci 1 pro kladne hodnoty, -1 pro zaporne a 0 pro nulove
        new_pattern = np.sign(self.weights @ pattern)
        
        #nahrazeni nulovych hodnot jednickam (pokud je soucin nulovy, neuron zustane aktivni)
        new_pattern[new_pattern == 0] = 1
        
        return new_pattern

    def async_update(self, pattern):
        #asynchronni aktualizace - neurony jsou aktualizovany postupne jeden po druhem
        #pattern: vstupni vzor, ktery chceme opravit
        
        #vytvoreni kopie vstupniho vzoru, abychom nemodifikovali original
        new_pattern = pattern.copy()
        
        #postupna aktualizace kazdeho neuronu
        for i in range(self.size):
            #vypocet noveho stavu i-teho neuronu jako skalarniho soucinu i-teho radku matice vah
            #a aktualniho stavu vzoru
            new_pattern[i] = np.sign(np.dot(self.weights[i], new_pattern))
            
            #nahrazeni nulovych hodnot jednickam
            if new_pattern[i] == 0:
                new_pattern[i] = 1
                
        return new_pattern