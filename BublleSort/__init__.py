class BubbleSort:
    def __init__(self, vetor):
        self.vetor = vetor


    def bubble_sort(self):
            for i in range(0, len(self.vetor)):
                for j in range(0, len(self.vetor)-i-1):
                    if self.vetor[j] > self.vetor[j+1]:
                        temp = self.vetor[j]
                        self.vetor[j] = self.vetor[j+1]
                        self.vetor[j+1] = temp




