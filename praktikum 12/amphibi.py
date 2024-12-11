from animal import Animal

# setiap class child itu memiliki 2 properti dan method
class Amphibi1(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi1(self):
        super().info_animal()
        print("jenis air \t\t\t : ", self.jenis_air,
        "\nbernapas \t\t\t :", self.bernapas,
        '\n---------------------------------------'
        )

Amphibi1 = Amphibi1("Buaya", "Daging", "dua alam", "bertelur", "air tawar", "paru-paru")
Amphibi1.info_amphibi1()

# class 2
class Amphibi2(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi2(self):
        super().info_animal()
        print("jenis air \t\t\t : ", self.jenis_air,
        "\nbernapas \t\t\t :", self.bernapas,
        '\n---------------------------------------'
        )

Amphibi2 = Amphibi2("katak", "serangga", "di tempat lembab", "bertelur", "air tawar", "insang dan paru-paru")
Amphibi2.info_amphibi2()

# class 3
class Amphibi3(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi3(self):
        super().info_animal()
        print("jenis air \t\t\t : ", self.jenis_air,
        "\nbernapas \t\t\t :", self.bernapas,
        '\n---------------------------------------'
        )

Amphibi3 = Amphibi3("salamander", "cacing", "Danau/ bawah dedaunan", "bertelur", "air tawar", "insang, kulit, dan paru-paru")
Amphibi3.info_amphibi3()