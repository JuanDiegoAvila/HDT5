import simpy
import random


def proceso(env, CPU, RAM, tiempoEntrada, speed, name):
    yield env.timeout(tiempoEntrada)
    # env, name, bcs, driving_time, charge_duration
    asignacion_memoria = random.randint(1, 10)
    # Tiempo de Trabajo de la CPU
    tiempoInicial = env.now

    # NEW
    while True:
        if RAM.level >= asignacion_memoria:
            yield RAM.get(asignacion_memoria)
            print('\nEl nuevo proceso %s usa %s de la memoria RAM' % (name, asignacion_memoria))
            break

    # Instrucciones a realizar
    instrucciones = random.randint(1, 10)
    waiting = 0
    exit = False

    # COLA DE READY
    while exit == False:
        # RUNNING
        # Si hay otros 3 procesos, deberá hacer cola
        with CPU.request() as req:
            yield req  # Entra el proceso a la CPU
            yield env.timeout(speed)  # El proceso se trabaja en la CPU por un tiempo

        if instrucciones < 3:  # Si hay menos de tres instrucciones, la resta da 0

            instrucciones = 0  # TERMINATED
            print('El proceso %s se encuentra en estado TERMINATED' % (name))
            exit = True
        elif instrucciones >= 3:
            instrucciones -= 3
            waiting = random.randint(1, 2)  # Se genera numero al azar, 1 sale y 2 sigue
            if waiting == 1:
                #  entra a WAITING
                print('El proceso %s se encuentra en estado WAITING' % (name))

    tiempoTrabajo = env.now - tiempoInicial

    global totalProceso
    totalProceso += totalProceso + tiempoTrabajo
    global procesos
    procesos += 1
    print("Se devuelve " + str(asignacion_memoria) + " a la memoria RAM")
    RAM.put(asignacion_memoria)
    print('La RAM tiene actualmente %s de memoria disponible' % (RAM.level))


# ---------------------
totalProceso = 0
procesos = 0

random.seed(10)
env = simpy.Environment()  # Ambiente de simulación
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env, capacity=1)

for i in range(25):
    env.process(proceso(env, CPU, RAM, random.expovariate(1.0 / 10), 1, i + 1))

# inicia la simulacion
env.run()
print("\n\tEl tiempo total es de : " + str(totalProceso/25))
print("\tSe realizaron " + str(procesos) + " procesos.")
