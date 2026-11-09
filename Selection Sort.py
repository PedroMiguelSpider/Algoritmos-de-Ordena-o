import random
import time
 
# Vantagens:
# - Simples de implementar e entender.
# - Faz o número mínimo de trocas (no máximo n-1), bom quando escrever na memória é caro.
# - Ordena in-place: não precisa de memória extra (O(1) auxiliar).
# - Tempo de execução previsível: não varia conforme a ordem inicial dos dados.
# - Não usa recursão, então não há risco de estouro de pilha.
# Desvantagens:
# - Sempre faz N(N-1)/2 comparações: O(n²) no melhor, médio e pior caso.
# - Muito lento para listas grandes.
# - Não é estável: elementos iguais podem trocar de ordem relativa.
# - Não se beneficia de listas já ordenadas ou parcialmente ordenadas.
 
 
def selection_sort(lista):
    if not lista:
        return lista
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista
 
 
if __name__ == "__main__":
    TAMANHO = 100000
    lista = [random.randint(0, 100_000) for _ in range(TAMANHO)]
 
    print(f"Ordenando 100.000 elementos...")
 
    inicio = time.time()
    selection_sort(lista)
    fim = time.time()
 
    print(f"Lista com 100.000 elementos ordenada em {fim - inicio:.2f} segundos")
    print("Ordenada corretamente:", all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1)))
    print("Primeiros 100 elementos:", lista[:100])
