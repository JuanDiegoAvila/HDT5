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
    # Instrucciones a realizar
    instrucciones = random.randint(1, 10)
    while instrucciones != 0:
        
        
        # RUNNING
        tiempoTrabajo = env.now - tiempoInicial
    
        # Si hay otros 3 procesos, deberá hacer cola
        with CPU.request() as turno:
            yield turno  # Entra el proceso a la CPU
            yield env.timeout(tiempoTrabajo)  #El proceso se trabaja en la CPU por un tiempo


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
