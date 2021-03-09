import simpy
import random

def proceso (env,CPU)
    asignacion_memoria = random.randit(1,10)
    
    #Tiempo de Trabajo de la CPU
    tiempoTrabajo = random.randit(1,7)
    
    #Enviar el proceso al CPU
    #Si hay otros 3 procesos, deberá hacer cola
    with CPU.request() as turno
        yield turno #Entra el proceso a la CPU
        yield env.timeout(tiempoTrabajo) #
    
    
#---------------------
env = simpy.Enviroment() #Ambiente de simulación
CPU = simpy.Resource(env,capacity = 3)
