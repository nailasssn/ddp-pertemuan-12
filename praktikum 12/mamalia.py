from animal import Animal

# setiap class child itu memiliki 2 properti dan method
# class 1
class Mamalia1(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_gigi ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_gigi = jenis_gigi

    def info_mamalia1(self):
        super().info_animal()
        print("ukuran tubuh \t\t\t : ", self.ukuran_tubuh,
        "\njenis gigi \t\t\t :", self.jenis_gigi,
        '\n---------------------------------------'
        )

Mamalia1 = Mamalia1("kucing", "karnivora", "liar di darat", "vivipar", "4kg", "tajam")
Mamalia1.info_mamalia1()

# class 2
class Mamalia2(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_gigi ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_gigi = jenis_gigi

    def info_mamalia2(self):
        super().info_animal()
        print("ukuran tubuh \t\t\t : ", self.ukuran_tubuh,
        "\njenis gigi \t\t\t :", self.jenis_gigi,
        '\n---------------------------------------'
        )

Mamalia2 = Mamalia2("monyet", "pisang", "liar di darat", "vivipar", "menengah tinggi", "gigi serbaguna")
Mamalia2.info_mamalia2()

# class 3
class Mamalia3(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_gigi ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_gigi = jenis_gigi

    def info_mamalia3(self):
        super().info_animal()
        print("ukuran tubuh \t\t\t : ", self.ukuran_tubuh,
        "\njenis gigi \t\t\t :", self.jenis_gigi,
        '\n---------------------------------------'
        )

Mamalia3 = Mamalia3("sapi", "rumput", "di ternak di darat", "vivipar", "bisa sampai 700kg >", "gigi seri")
Mamalia3.info_mamalia3()