import time
import numpy as np
from src.dashboard import ExecutionDashboard

def main():
    desk = ExecutionDashboard("AAPL", "MSFT")
    
    # Simulated execution loop
    for _ in range(3):
        mock_z = np.random.uniform(-2.5, 2.5)
        mock_vol = np.random.uniform(0.015, 0.035)
        
        if mock_z > 2.0:
            rec = "SHORT SPREAD (ENTRY)"
            size = 50000 / (mock_vol * 100)
        elif mock_z < -2.0:
            rec = "LONG SPREAD (ENTRY)"
            size = 50000 / (mock_vol * 100)
        else:
            rec = "NEUTRAL / NO ENTRY"
            size = 0.0
            
        desk.render_desk(mock_z, mock_vol, rec, size)
        time.sleep(1)

if __name__ == "__main__":
    main()
