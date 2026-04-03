# Hospital Queue Optimization Dashboard

A professional, production-ready Streamlit dashboard for modeling and simulating hospital outpatient department (OPD) queuing systems using **M/M/c Queuing Theory**.

## 🚀 Overview
This application uses **SimPy** to run discrete-event simulations of patient arrivals and service processes. It provides interactive decision support for hospital administrators to optimize staffing (number of doctors) based on arrival rates and service times.

## ✨ Key Features
- **M/M/c Simulation**: Model multi-server queues with Poisson arrivals and Exponential service times.
- **Priority Queue Support**: Simulate emergency vs. normal patient priorities.
- **Scenario Presets**: Instantly switch between *Underloaded*, *Stable*, and *Overloaded* system states.
- **Dynamic KPIs**: Real-time calculation of system utilization ($\rho$), average waiting times, and queue lengths.
- **Advanced Visualizations**: Interactive Plotly charts for queue length trends, waiting time distributions, and resource utilization gauges.
- **Decision Support**: Context-aware recommendations for system stabilization.

## 🛠️ Tech Stack
- **Dashboard**: [Streamlit](https://streamlit.io/)
- **Simulation**: [SimPy](https://simpy.readthedocs.io/)
- **Data Engineering**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualization**: [Plotly](https://plotly.com/python/)

## 📂 Project Structure
```text
hospital-queue-dashboard/
├── app.py                  # Main entry point & layout orchestration
├── requirements.txt         # Project dependencies
├── README.md               # Project documentation
├── assets/                 # Static files
│   ├── images/             # Visual illustrations
│   └── styles/             # Global dashboard styling (CSS)
├── components/             # Reusable UI components
│   ├── graphs.py           # Plotly visualization logic
│   ├── header.py           # Title & hero section
│   ├── insights.py         # Recommendation & logic engine
│   ├── kpi_cards.py        # Metric display components
│   └── sidebar.py          # Input controls & scenarios
├── src/                    # Core business logic
│   ├── analytics/          # Metric calculation engine
│   ├── simulation/         # SimPy discrete-event engine
│   └── utils/              # Helper functions & utilities
└── data/                   # Data storage (optional)
```

## ⚙️ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd hospital-queue-dashboard
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 🎓 Academic Context
This project was developed as a mini-project for **Operations Research**, demonstrating the practical application of queuing theory in healthcare management settings.

## Preview
https://shalaka127-hospital-queue-management-dashboard--app-qlrjk0.streamlit.app/
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/a5104cfb-cdf4-4acc-8b52-f2db2e7b8e0e" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/6833f5ce-ed01-47ae-bb4f-0a5a76d7760e" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/3c420ad9-3c13-485d-9f86-96dd1eab90ce" />



