"""
Por que testar nosso codigo ?

Testes Automatizados !

        aplicação web
--------------------------------
|                              |
|   frontend e backend         |
--------------------------------
|    testes automatizados      |
-------------------------------

Para que testar o codigo?

    - Reduzir bugs no codigo existentes;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recurso antingos;
    - Testes garantem que bugs que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que constumamaos a fazer nao traga, novos bugs;

TDO - Teste Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é ultlizado estagios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então voce escreve o codigo minimo suficiente para fazer o teste passar (ou seja, executar
    com sucesso);
    - Então refatorar o codigo para realizar a funcionalidade e teste novamente;
    - Uma vez que o teste passe, o recurso e considerado completo;

Estes estagios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;


"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)

















