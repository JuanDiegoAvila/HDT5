import simpy
import random

def proceso (env,CPU, RAM, procesos, speed, name):
    # env, name, bcs, driving_time, charge_duration
    asignacion_memoria = random.randint(1,10)
    # Tiempo de Trabajo de la CPU
    tiempoInicial = env.now

    # NEW
    while True:
        if RAM.level >= asignacion_memoria:
            RAM.get(asignacion_memoria)
            print(str(name)+" usa "+str(asignacion_memoria))
            print(str(RAM.level)+" en el ram")
            break;
        #else:
            #print("Esperando")

    # Instrucciones a realizar
    instrucciones = random.randint(1, 10)
    waiting = 0

    exit = false;
    # COLA DE READY
    while exit == false:
        print("Cantidad de instrucciones de "+str(name)+": "+str(instrucciones))
        # RUNNING
        tiempoTrabajo = env.now - tiempoInicial

        # Si hay otros 3 procesos, deberá hacer cola
        with CPU.request() as turno:
            yield turno  # Entra el proceso a la CPU
            yield env.timeout(tiempoTrabajo)  # El proceso se trabaja en la CPU por un tiempo

        if instrucciones < 3: # Si hay menos de tres instrucciones, la resta da 0
            instrucciones = 0 # TERMINATED

            exit = true
        elif instrucciones >= 3:
            instrucciones -= 3
            waiting = random.randint(1, 2)  # Se genera numero al azar, 1 sale y 2 sigue
            if waiting == 1:
                #  entra a WAITING
                print("WAITING")




    global totalProceso
    totalProceso += totalProceso + tiempoTrabajo
    print("Se asigna: "+str(asignacion_memoria))
    RAM.put(asignacion_memoria)
    print(RAM.level)
    
# ---------------------
totalProceso = 0

random.seed(69)
env = simpy.Environment() # Ambiente de simulación
RAM = simpy.Container(env, init=100, capacity=100)
CPU = simpy.Resource(env,capacity = 1)

for i in range(25):
    env.process(proceso(env, CPU, RAM, random.expovariate(1.0/10), 1, i+1))

# inicia la simulacion
env.run()
