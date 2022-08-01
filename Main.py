class Hero:

    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
    
    def serang(self, lawan):
        print("\n"+self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armor
        print("serangan terasa : " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah : " + self.name + " tersisa " + str(self.health))
        if self.health < 0:
            print("\n------- WINNER -------")
            print(self.name + " telah mati")
            print("pemenangnya adalah " + lawan.name)
            print("------- WINNER -------")
            quit()


sniper = Hero("sniper", 100, 90, 5)
nanda = Hero("nanda", 150, 200, 2)

sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)