import simpy
import random

def proceso (env,CPU, RAM):
    #env, name, bcs, driving_time, charge_duration
    asignacion_memoria = random.randit(1,10)
    RAM.get(asignacion_memoria)
    #Tiempo de Trabajo de la CPU
    tiempoInicial = env.now

    if RAM != 0:
        print("READY")
    else:
        print("WAITING")
    #Enviar el proceso al CPU
    #Si hay otros 3 procesos, deberá hacer cola
    with CPU.request() as turno:
        yield turno #Entra el proceso a la CPU
        yield env.timeout(tiempoTrabajo) #

    tiempoTrabajo = env.now - tiempoInicial

    global totalProceso
    totalProceso += totalProceso + tiempoTrabajo

    RAM.put(asignacion_memoria)
    
#---------------------
totalProceso = 0
RAM = simpy.Container(env, init=100, capacity=100)
env = simpy.Enviroment() #Ambiente de simulación
CPU = simpy.Resource(env,capacity = 3)

for i in range(25):
    env.proces(proceso(env, CPU, RAM, random.expovariate(1.0/10), 1))

#inicia la simulacion
env.run()