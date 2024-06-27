import estrela
import gulosa
import largura
import estrela_evitando_estados_repetidos
import estrela_Manhattan

# Menu de Seleção de Algoritmo
def menu_principal():
    while True:
        print("\nMenu de Seleção de Algoritmo")
        print("1. Executar Algoritmo de Largura")
        print("2. Executar Algoritmo Gulosa")
        print("3. Executar Algoritmo Estrela")
        #euristicas
        print("-----------------------------")
        print("5 Executar Algoritmo Estrela com heurística de manhattan")
        print("6 Executar Algoritmo Estrela com heurística de manhattan e evitando estados repetidos")
        print("4. Sair")

        escolha = input("Digite sua escolha (1-4): ")

        if escolha == '1':
            print("Executando Algoritmo de Largura")
            largura.run_largura()
        elif escolha == '2':
            print("Executando Algoritmo Gulosa")
            gulosa.run_gulosa()
        elif escolha == '3':
            print("Executando Algoritmo Estrela")
            estrela.run_estrela()
        elif escolha == '5':
            print("Executando Algoritmo Estrela com heurística de manhattan")
            estrela_Manhattan.run_estrela()
        elif escolha == '6':
            print("Executando Algoritmo Estrela com heurística de manhattan e evitando estados repetidos")
            estrela_evitando_estados_repetidos.run_estrela()
        elif escolha == '7':
            print("Saindo do menu.")
            break
        else:
            print("Escolha inválida. Por favor, digite um número entre 1 e 4.")

# Ponto de entrada para o menu
if __name__ == "__main__":
    menu_principal()
