import pandas as pd

def calculate_metrics(sim_data, actual_sim_time, c):
    pd.options.mode.chained_assignment = None
    patients_df = pd.DataFrame(sim_data['patients'])
    queue_df = pd.DataFrame(sim_data['queue_log'])
    
    res = {
        'patients_df': patients_df,
        'queue_df': queue_df,
        'avg_wait_mins': 0,
        'avg_q_len': 0,
        'doc_util': 0,
        'emer_wait_mins': 0,
        'norm_wait_mins': 0
    }
    
    if not queue_df.empty:
        res['avg_q_len'] = queue_df['Queue Length'].mean()
        
    if not patients_df.empty:
        res['avg_wait_mins'] = patients_df['Waiting Time (mins)'].mean()
        
        # Empirical doctor utilization
        tot_service = patients_df['Service Duration (hrs)'].sum()
        res['doc_util'] = min(tot_service / (c * actual_sim_time), 1.0)
        
        if 'Type' in patients_df.columns:
            emer_df = patients_df[patients_df['Type'] == 'Emergency']
            norm_df = patients_df[patients_df['Type'] == 'Normal']
            if not emer_df.empty:
                res['emer_wait_mins'] = emer_df['Waiting Time (mins)'].mean()
            if not norm_df.empty:
                res['norm_wait_mins'] = norm_df['Waiting Time (mins)'].mean()
                
    return res
