import simpy
import random
from src.simulation.patient import patient
from src.simulation.generator import patient_generator

def log_queue(env, doctors, log_list):
    while True:
        if isinstance(doctors, simpy.PriorityResource):
            q_len = len(doctors.put_queue)
        else:
            q_len = len(doctors.queue)
        log_list.append({'Time': env.now, 'Queue Length': q_len})
        yield env.timeout(0.05) # Track queue length every ~3 minutes

def simulate_queue(arrival_rate, service_rate, doc_count, s_time, p_enabled, e_pct):
    # Initialize environment and stores
    env = simpy.Environment()
    sim_data = {'patients': [], 'queue_log': []}
    
    if p_enabled:
        doctors = simpy.PriorityResource(env, capacity=doc_count)
    else:
        doctors = simpy.Resource(env, capacity=doc_count)
        
    # Optional Initial Burst: Start 3 patients immediately to create early queue behavior
    for i in range(3):
        if p_enabled:
            is_emergency = random.random() < (e_pct / 100.0)
            patient_type = 'Emergency' if is_emergency else 'Normal'
            priority = 1 if is_emergency else 2
        else:
            patient_type, priority = 'Normal', 2
        env.process(patient(env, f"P_burst_{i}", patient_type, priority, doctors, service_rate, sim_data))
        
    env.process(log_queue(env, doctors, sim_data['queue_log']))
    env.process(patient_generator(env, arrival_rate, service_rate, doctors, p_enabled, e_pct, sim_data))
    
    env.run(until=s_time)
    return sim_data
