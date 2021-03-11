import simpy
import random


def proceso(env, CPU, RAM, tiempoEntrada, speed, name):
    yield env.timeout(tiempoEntrada)
    # env, name, bcs, driving_time, charge_duration
    asignacion_memoria = random.randint(1, 10)
    # Tiempo de Trabajo de la CPU
    tiempoInicial = float(env.now)

    # NEW
    with RAM.get(asignacion_memoria) as getRAM:
        yield getRAM
        print('\nEl nuevo proceso %s usa %s de la memoria RAM' % (name, asignacion_memoria))

    global capacidad_instrucciones

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

        if instrucciones < capacidad_instrucciones:  # Si hay menos de tres instrucciones, la resta da 0

            instrucciones = 0  # TERMINATED
            print('El proceso %s se encuentra en estado TERMINATED' % (name))
            exit = True

        elif instrucciones >= capacidad_instrucciones:
            instrucciones -= capacidad_instrucciones
            waiting = random.randint(1, 2)  # Se genera numero al azar, 1 sale y 2 sigue

            if waiting == 1:
                #  entra a WAITING
                print('El proceso %s se encuentra en estado WAITING' % (name))
                yield env.timeout(2)
                print('El proceso %s ya no se encuentra en estado WAITING' % (name))


    tiempoTrabajo = float(env.now) - tiempoInicial

    global totalProceso
    totalProceso += tiempoTrabajo

    global numeros_procesos
    numeros_procesos += 1

    print("Se devuelve " + str(asignacion_memoria) + " a la memoria RAM")
    RAM.put(asignacion_memoria)
    print('La RAM tiene actualmente %s de memoria disponible' % (RAM.level))


# ---------------------
totalProceso = 0
numeros_procesos = 0
capacidad = 1
capacidad_instrucciones = 3
intervalos = 10
capacidad_procesos = 200

random.seed(10)

env = simpy.Environment()  # Ambiente de simulación
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env, capacity=capacidad)

for i in range(capacidad_procesos):
    env.process(proceso(env, CPU, RAM, random.expovariate(1.0 / intervalos), 1, i + 1))

# inicia la simulacion
env.run()
print("\n\tEl promedio de tiempo por proceso es de : " + str(totalProceso/capacidad_procesos))
print("\tSe realizaron " + str(numeros_procesos) + " procesos.")
