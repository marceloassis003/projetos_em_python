"""
POO - Métodos Maagicos

Métodos magicos são todos os metodos que ultlizam dunder.

# dunder init -> __init__()


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


Dunder -> Double Underscore

#dunder rep (__repr__) -> Representação do objeto

  def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado na memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ' '
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('python rocks!', 'geek University', 400)
livro2 = Livro('IA com python', 'geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))



print(livro1 + livro2)

print(livro1 * 5)










































