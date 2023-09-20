import threading
import time
import random

num_caixas = 3
tamanho_max_fila = 30

semaphore = threading.Semaphore(num_caixas)

def atender_cliente(cliente_id):
    atendimento_time = random.randint(3, 10)
    print(f"Cliente {cliente_id} está sendo atendido por {atendimento_time} segundos.")
    time.sleep(atendimento_time)
    print(f"Cliente {cliente_id} foi atendido.")

def fila_de_espera():
    for cliente_id in range(1, tamanho_max_fila + 1):
        print(f"Cliente {cliente_id} chegou ao banco.")
        semaphore.acquire()
        threading.Thread(target=atender_cliente, args=(cliente_id,)).start()

if __name__ == "__main__":
    fila_thread = threading.Thread(target=fila_de_espera)
    fila_thread.start()
    fila_thread.join()