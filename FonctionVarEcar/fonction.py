import math


def main():
    def variance(t):
        som = 0
        cal = 0
        for j in range(5):
            som = som + t[j]
        mean = som / 5
        for k in range(5):
            cal = cal +(t[k]-mean)**2
        var = cal/5
        return var


    def mean(t):
        som = 0
        for i in range(5):
            som = som+t[i]
        mean = som / 5
        return mean

    def standardDeviation(t):
        som = 0
        cal = 0
        for j in range(5):
            som = som + t[j]
        mean = som / 5
        for b in range(5):
            cal = cal + (t[b] - mean) ** 2
        var = cal / 5
        stdDev = math.sqrt(var);
        return stdDev

    def customTotal(t):
        som = 0
        for j in range(5):
            som = som + t[j]
        return som;
    tab = [0,25,39,60,80]
    print("La valeur de la variance est :", variance(tab))
    print("La moyenne est :", mean(tab))
    print("La valeur de l'ecarttype est :", standardDeviation(tab))
    print("La somme est :", customTotal(tab))
if __name__ == '__main__':
    main()

