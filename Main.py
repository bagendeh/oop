class Hero:

    jumlah = 0
    jumlah_serangan = 1
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
    
    def serang(self, lawan):
        print("\n"+self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)
        Hero.jumlah_serangan += 1

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armor
        print("serangan terasa : " + str(attack_diterima))
        self.health -= attack_diterima
        if self.health < 0:
            print(self.name + " telah mati")
            Hero.pemenang(self, lawan.name)
            quit()
        else:
            print("darah : " + self.name + " tersisa " + str(self.health))



        
    def pemenang(self, pemenang):
        print("======= Winner =======")
        print("PEMENANG " + pemenang )
        print("mengalahkan " + self.name + " dengan " + str(Hero.jumlah_serangan) + " kali serangan")



sniper = Hero("sniper", 100, 60, 1)
nanda = Hero("nanda", 150, 34, 2)

sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)
sniper.serang(nanda)
nanda.serang(sniper)