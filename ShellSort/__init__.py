class ShellSort:
    def __init__(self, vetor):
        self.vetor = vetor


    def shell_sort(self):
        tamanho = self.vetor.__len__()
        h = 1
        while h < tamanho:
            h = 3 * h + 1
        while h > 1:
            for i in range(h, tamanho):
                temp = self.vetor[i]
                j = i - h
                while j>=0 and temp < self.vetor[j]:
                    self.vetor[j+h] = self.vetor[j]
                    j -= h
                self.vetor[j+h] = temp



