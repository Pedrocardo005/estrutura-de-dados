from stack import Stack

stack = Stack()

def op_um():
    print()
    print('Digite O valor a ser posto:')
    valor = int(input())
    stack.push(valor)

def op_dois():
    print()
    print('O valor: {} foi retirado da pilha'.format(stack.pop()))

def op_tres():
    print()
    print('O que tem no topo: {}'.format(stack.peek()))

def op_four():
    print()
    print('Está vazio?', stack.isempty())

def op_five():
    print()
    stack.clear()
    print('A pilha foi limpa')

def op_six():
    print()
    print('A quantidade de itens:', stack.size())

def op_seven():
    print()
    print('A lista impressa:')
    print(stack.__str__())


while True:
    print('Digite um numero para cada opção')
    print('1) Adicionar mais item a pilha')
    print('2) Remover item da pilha')
    print('3) Devolver item que está no topo')
    print('4) Verifica se está vazio')
    print('5) Limpa a pilha')
    print('6) Retorna a quantidade de itens na pilha')
    print('7) Imprimir a lista completa')
    print('8) Para sair')
    op = int(input())

    if op == 1:
        op_um()
    elif op == 2:
        op_dois()
    elif op == 3:
        op_tres()
    elif op == 4:
        op_four()
    elif op == 5:
        op_five()
    elif op == 6:
        op_six()
    elif op == 7:
        op_seven()
    elif op == 8:
        break

