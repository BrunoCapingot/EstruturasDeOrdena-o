class InsertionSort:
    def __init__(self, vetor):
        self.vetor = vetor


    def insertion_sort(self):
            for i in range(1, len(self.vetor)):
                elemento = self.vetor[i]
                j = i-1
                while j >= 0 and self.vetor[j] > elemento:
                    self.vetor[j+1] = self.vetor[j]
                    j -= 1
                self.vetor[j+1] = elemento





