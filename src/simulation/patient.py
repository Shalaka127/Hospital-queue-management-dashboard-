import numpy as np
import simpy

def patient(env, name, patient_type, priority, doctors, service_rate, sim_data):
    arrival_time = env.now
    
    # Request a doctor based on priority resource or normal resource
    if isinstance(doctors, simpy.PriorityResource):
        req = doctors.request(priority=priority)
    else:
        req = doctors.request()
        
    with req as request:
        yield request
        service_start_time = env.now
        waiting_time = service_start_time - arrival_time
        
        # Exponential service time calculation
        service_time = np.random.exponential(1.0 / service_rate)
        yield env.timeout(service_time)
        
        sim_data['patients'].append({
            'Patient ID': name,
            'Type': patient_type,
            'Arrival Time': arrival_time,
            'Service Start': service_start_time,
            'Waiting Time (hrs)': waiting_time,
            'Waiting Time (mins)': waiting_time * 60,
            'Service Duration (hrs)': service_time,
            'Departure Time': env.now
        })
