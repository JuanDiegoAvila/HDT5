import simpy
import random

def proceso (env,CPU, RAM, procesos, speed):
    # env, name, bcs, driving_time, charge_duration
    asignacion_memoria = random.randint(1,10)
    RAM.get(asignacion_memoria)
    # Tiempo de Trabajo de la CPU
    tiempoInicial = env.now
    # NEW


    # WAITING
    while RAM == 0:
        with RAM.request() as turno:
            yield turno

    # READY


    # RUNNING
    tiempoTrabajo = env.now - tiempoInicial
    # Enviar el proceso al CPU
    instrucciones = random.randint(1, 10)
    # Si hay otros 3 procesos, deberá hacer cola
    with CPU.request() as turno:
        yield turno  # Entra el proceso a la CPU
        yield env.timeout(tiempoTrabajo)  #

    global totalProceso
    totalProceso += totalProceso + tiempoTrabajo

    RAM.put(asignacion_memoria)
    
# ---------------------
totalProceso = 0

env = simpy.Environment() # Ambiente de simulación
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env,capacity = 3)

for i in range(25):
    env.process(proceso(env, CPU, RAM, random.expovariate(1.0/10), 1))

# inicia la simulacion
env.run()