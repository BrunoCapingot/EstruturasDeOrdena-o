class MergeSort:
    def __init__(self, vetor, esq, meio, dir):
        self.vetor = vetor
        self.esq = esq
        self.meio = meio
        self.dir = dir

    def merge_sort(self):
        helper = [0] * len(self.vetor)
        for i in range(self.esq, self.dir):
            helper[i] = self.vetor[i]
        i = self.esq
        j = self.meio + 1
        k = self.esq
        while i <= self.meio and j <= self.dir:
            if helper[i] <= helper[j]:
                i += 1
            else:
                self.vetor[k] = helper[j]
                j += 1
            k += 1
        while i <= self.meio:
            self.vetor[k] = helper[i]
            i += 1
            k += 1

