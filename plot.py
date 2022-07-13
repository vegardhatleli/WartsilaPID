import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

#Sett inn filepath i main metode, så fikser scriptet resten.
#Husk .xlsx fil, og husk å fjern lese/skrive lås på filen (med andre ord, lukk den!)


filepath = r"C:\Users\VHA025\Desktop\test_1-1.xlsx"
 
def main(path):
    data = pd.read_excel(path)

    time = np.array(data["Time"].tolist())
    time2 = np.array(data["Time2"].tolist())
    time2 = (time2*11.96)/60
    ms= np.array(data["ms"].tolist())
    sp = np.array(data["Pane1-SP"].tolist())
    #ext_sp = np.array(data["Pane1-Ext SP"].tolist())
    pv = np.array(data["Pane1-PV"].tolist())
    cv = np.array(data["Pane1-CV"].tolist())


    plt.subplot(2,1,1)
   
    plt.plot(time2,sp, label = "SP")
    plt.plot(time2,pv, label = "PV")
    plt.xlabel(f"Tid")
    plt.legend()    
    plt.grid(linewidth = 1)

    plt.subplot(2,1,2)
    plt.plot(time2,cv, label = "CV")
    plt.xlabel(f"Tid")
    plt.legend()    
    plt.grid(linewidth = 1)

    plt.show()

 
def plot_SP():
    x = time
    y = sp
    plt.title(f"Tid plottet mot SP")
    plt.plot(x,y)
    plt.xlabel(f"Tid")
    plt.ylabel(f"SP")
    plt.grid()
    plt.show()

def plot_Exp_SP():
    x = time
    y = ext_sp
    plt.title(f"Tid plottet mot Exp_SP")
    plt.plot(x,y)
    plt.xlabel(f"Tid")
    plt.ylabel(f"Exp_SP")
    plt.grid()
    plt.show()

def plot_PV():
    x = time
    y = pv
    plt.title(f"Tid plottet mot PV")
    plt.plot(x,y)
    plt.xlabel(f"Tid")
    plt.ylabel(f"PV")
    plt.grid()
    plt.show()

def plot_CV():
    x = time
    y = ext_sp
    plt.title(f"Tid plottet mot CV")
    plt.plot(x,y)
    plt.xlabel(f"Tid")
    plt.ylabel(f"CV")
    plt.grid()
    plt.show()


main(r"C:\Users\VHA025\OneDrive - Wärtsilä Corporation\40TIC5647\Current PI controller\Step_-135_-10\Step_-135_-145\Step_-135_-145.xlsx")

