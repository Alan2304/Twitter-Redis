from RedisConfig import *
import matplotlib.pyplot as plt

def obtainKeys(keys):
    r, isConnected = connect()
    if isConnected:
        return r.keys(pattern = keys)

def countValues(key):
    r, isConnected = connect()
    if isConnected:
        return  r.llen(key)

def main():
    keys = obtainKeys('i4:*')
    values = []
    for key in keys:
        values.append(countValues(key))

    plt.bar(keys, values, width=0.5)
    plt.title('Cantidad tweets')
    plt.xlabel('Tema')
    plt.ylabel('Numero de tweets')
    plt.show()

main()
