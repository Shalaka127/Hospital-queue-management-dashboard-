import random
import numpy as np
from src.simulation.patient import patient

def patient_generator(env, arrival_rate, service_rate, doctors, priority_enabled, emergency_pct, sim_data):
    patient_id = 0
    while True:
        # Exponential inter-arrival time
        interarrival_time = np.random.exponential(1.0 / arrival_rate)
        yield env.timeout(interarrival_time)
        
        patient_id += 1
        name = f"P{patient_id}"
        
        if priority_enabled:
            is_emergency = random.random() < (emergency_pct / 100.0)
            if is_emergency:
                patient_type = 'Emergency'
                priority = 1
            else:
                patient_type = 'Normal'
                priority = 2
        else:
            patient_type = 'Normal'
            priority = 2
            
        env.process(patient(env, name, patient_type, priority, doctors, service_rate, sim_data))
