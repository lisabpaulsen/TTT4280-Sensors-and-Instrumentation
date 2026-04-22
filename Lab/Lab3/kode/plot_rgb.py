import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
MAPPE = r'C:\Users\lisa\Desktop\6. semester\Sensorer og Instrumetering\Lab\Lab3\kode\data'

DATAFILER = [
    #'finger_burpees_data.txt',
    #'finger_data.txt',
    #'finger_data2.txt',
    #'finger_data3.txt',
    #'finger_data4.txt',
    #'finger_data5.txt',
    #'finger_test6_data.txt',
    #'finger_test7_data.txt',
    #'finger_test8_data.txt',
    #'finger_test9_data.txt',
    #'finger_test10_data.txt',
    #'finger_test11_data.txt',
    #'finger_test12_data.txt',
    #'finger_test13_data.txt',
    #'finger_test14_data.txt',
    #'toe_test_data.txt',
    #'finger_t_2_data.txt',
    #'finger_t_3_data.txt',
    #'finger_t_5_data.txt',
    #'finger_t_56BMP_mob1_data.txt',
    'finger_t_63BMP_data.txt',
    
]

fps = 40  # frames per sekund
# -------------------------------------------------------

import os

for datafil in DATAFILER:
    filepath = os.path.join(MAPPE, datafil)

    data = np.loadtxt(filepath)
    R = data[:, 0]
    G = data[:, 1]
    B = data[:, 2]

    t = np.arange(len(R)) / fps

    plt.figure(figsize=(12, 6))
    plt.plot(t, R, 'r', label='Rød')
    plt.plot(t, G, 'g', label='Grønn')
    plt.plot(t, B, 'b', label='Blå')
    plt.xlabel('Tid (sekunder)')
    plt.ylabel('Gjennomsnittlig pikselverdi')
    plt.title(f'RGB-signal fra ROI - {datafil}')
    plt.legend()
    plt.grid()
    plt.show()
