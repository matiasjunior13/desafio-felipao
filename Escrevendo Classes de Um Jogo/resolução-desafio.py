class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso da classe Hero
heroi1 = Hero("Gandalf", 120, "mago")
heroi2 = Hero("Aragorn", 35, "guerreiro")

heroi1.atacar()  # Saída: "O mago atacou usando usou magia"
heroi2.atacar()  # Saída: "O guerreiro atacou usando usou espada"
