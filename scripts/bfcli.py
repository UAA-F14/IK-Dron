"""Envía comandos al CLI de BetaFlight por USB e imprime la respuesta.

Uso:
    python3 bfcli.py version status "diff all"
    python3 bfcli.py "set dshot_bidir = OFF" save
    BF_PORT=COM5 python3 bfcli.py status          # Windows

Si el último comando no es `save`, al terminar se envía `exit`, que reinicia
la controladora SIN guardar. Con `save` la controladora se reinicia sola y
el puerto se desconecta (puede salir un error de pyserial, es normal).
Requiere: pip install pyserial
"""
import os
import sys
import time

import serial

PORT = os.environ.get('BF_PORT', '/dev/ttyACM0')

cmds = sys.argv[1:]
s = serial.Serial(PORT, 115200, timeout=0.5)
s.write(b'#')                      # entrar al CLI
time.sleep(0.5)
s.read(10000)                      # descartar el saludo del CLI
for c in cmds:
    s.write((c + '\r\n').encode())
    out = b''
    idle = 0
    while idle < 4:                # esperar ~2 s sin datos para dar por terminada la respuesta
        d = s.read(4096)
        if d:
            out += d
            idle = 0
        else:
            idle += 1
    print(f'===== {c} =====\n' + out.decode(errors='replace'))
s.write(b'exit\r\n')               # salir sin guardar -> reinicia, sin cambios
s.close()
