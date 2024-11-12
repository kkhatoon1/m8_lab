# khateej akhatoon
# nov 12 2024

class character:
    def __init__(self, nickname, weapons, weaknesses):
     self.nickname = nickname
     self.weapons = weapons
     self.weaknesses = weaknesses
    def get_model(self):
     return self.nickname
    def get_year(self):
     return self.weapons
    def get_color(self):
     return self. weaknesses
    def profile(self):
     return self.nickname, self.weapons, self. weaknesses
    
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

khateeja= character("khateeja", ['rope','pen', 'paper', 'idea'],['weak1,weak2'])
print(f"my nickname is{khateeja.nickname}")
print(f"my nickname is {khateeja.get_model()}")