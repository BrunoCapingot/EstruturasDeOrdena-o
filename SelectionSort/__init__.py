class SelectionSort:
    def __init__(self, vetor):
        self.vetor = vetor


    def selection_sort(self):
            for i in range(0, len(self.vetor)-1):
                pos_menor = i
                for j in range(i+1, len(self.vetor)):
                    if self.vetor[j] > self.vetor[pos_menor]:
                        pos_menor = j
                    if i != pos_menor:
                        aux= self.vetor[i]
                        self.vetor[i] = self.vetor[pos_menor]
                        self.vetor[pos_menor] = aux





