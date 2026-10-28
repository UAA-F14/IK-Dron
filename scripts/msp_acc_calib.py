"""Calibra el acelerómetro de la controladora BetaFlight por MSP.

Es lo mismo que el botón "Calibrate Accelerometer" del Configurator.
El dron debe estar en una superficie PLANA y QUIETO. La calibración se guarda
sola; se puede verificar después con:  python3 bfcli.py "get acc_calibration"
(el último valor en 1 indica que se completó).

Uso:
    python3 msp_acc_calib.py
    BF_PORT=COM5 python3 msp_acc_calib.py         # Windows
Requiere: pip install pyserial
"""
import os
import time

import serial

PORT = os.environ.get('BF_PORT', '/dev/ttyACM0')
MSP_ACC_CALIBRATION = 205

s = serial.Serial(PORT, 115200, timeout=1)
time.sleep(0.3)
s.read(10000)
# Trama MSP v1: '$M<' + tamaño(0) + comando + checksum (XOR de tamaño y comando)
s.write(b'$M<' + bytes([0, MSP_ACC_CALIBRATION, 0 ^ MSP_ACC_CALIBRATION]))
time.sleep(0.5)
print('respuesta:', s.read(64))    # esperado: b'$M>\x00\xcd\xcd'
s.close()
