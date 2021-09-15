import math

def run():
    dict_raiz= {i:round(math.sqrt(i),2) for i in range(1,1000)}
    print(dict_raiz)

if __name__ == '__main__':
    run()