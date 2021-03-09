import simpy
import random

def proceso (env,CPU, RAM):
    asignacion_memoria = random.randit(1,10)
    RAM.get(asignacion_memoria)
    #Tiempo de Trabajo de la CPU
    tiempoTrabajo = random.randit(1,7)

    if RAM != 0:
        print("READY")
    else:
        print("WAITING")
    #Enviar el proceso al CPU
    #Si hay otros 3 procesos, deberá hacer cola
    with CPU.request() as turno:
        yield turno #Entra el proceso a la CPU
        yield env.timeout(tiempoTrabajo) #

    RAM.put(asignacion_memoria)
    
#---------------------
RAM = simpy.Container(env, init=100, capacity=100)
env = simpy.Enviroment() #Ambiente de simulación
CPU = simpy.Resource(env,capacity = 3)

proceso(CPU, env, RAM)
