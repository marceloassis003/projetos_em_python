"""
POO - Atributos

Atributos -> Representam a características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classes;
    - Atributos Dinãmicos;


# Atributos de instãncia: São atributos declarados dentro do metodo construtor.

# Método construtor: é um método especial ultlizado para a construção do objeto.

# Em java, uma classe Lãmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean logada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

}

Em python, por convenção, ficou estabelecido que, todo atributo de uma classe
é publico. OU seja, pode ser acesado em todo o projeto.
Caso a gente queira demostrar que determinado atributo deve ser tratado como provado, ou seja,
que deve ser acessado/ultlizado somente dentro da propria classe onde está declarado,
ultliza-se o '__' duplo underline no inicio de seu nome.

Isso é conhecido tambem como Name Mang


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

# print(user.email)

# print(user.senha)   # AttributeError

print(user._Acesso__senha)  # temos acesso. Mas não deveriamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()


# O que significa atributos de instancia ?

# Significa que ao criarmos instancias/objetos de uma classe, todas as instancias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')


user1.mostra_email()
user2.mostra_email()


# Atributos de Classe


# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instancias da classe. Ou seja, ao inves de cada instancia da classe ter seus proprios
# valores como é o caso dos atributos de instancia, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.


p1 = Produto('Playstation 4', 'video game ', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.valor)  # Acesso possivel, mas incorreto   de um atributo de classe
print(p2.valor)  # Acesso possivel, mas incorreto   de um atributo de classe

# OBS : Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)      # Acesso correto


print(p1.id)
print(p2.id)

# OBS: Em Java, os atributos conhecidos como atributos de classes aqui em python
# são chamados de atributos estáticos;



"""

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# refatorar Produto

class Produto:

    # Atributo de classes
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos -> um atributo de instancia que pode ser criado em tempo de execução

# OBS: O atributo de dinamico será exclusivo da instancia que o criou.

p1 = Produto('Play 4', 'Video Game ', 2300)
p2 = Produto('Arroz ', 'Mercearia', 5.99)

# Criando um atributo em tempo de execução

p2.peso = '5kg' # note que na calsse Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso} ')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso} ') # inexistente 'peso'

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

#   print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)














