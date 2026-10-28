# IK-Dron
A 5" FPV racing drone (LS210 carbon-fiber frame) built, diagnosed and flown as a university electronics project. The drone originally shipped with a CC3D flight controller on LibrePilot, which suffered an unrecoverable microcontroller failure during testing — documented here is the migration to a modern SpeedyBee F405 V4 stack on BetaFlight, the full diagnostic process from BetaFlight's CLI, and the configuration that got it to a stable, controlled flight on October 13, 2026. On October 23 it was updated to BetaFlight 2026.6.2 to add altitude hold using the flight controller's onboard barometer.

| Component | Spec |
|---|---|
| Frame | LS-210, 3K carbon fiber, 210 mm motor-to-motor |
| Flight controller | SpeedyBee F405 V4 (STM32F405, ICM42688P gyro, DPS310 baro) |
| ESC | SpeedyBee BLS 60A 4-in-1, DSHOT300 |
| Motors | FlashHobby BE1806, 2300 KV |
| Receiver | FlySky FS-iA6B, IBUS |
| Firmware | BetaFlight 2026.6.2, target `SPEEDYBEEF405V4` |
| Total weight | 497 g |
| Flight modes | ANGLE (always on), ALTHOLD on AUX2 |

## Directory structure
```
├── design
│   └── design
│       ├── design.kicad_pcb
│       ├── design.kicad_pro
│       ├── design.kicad_sch
│       ├── readme.md
│       └── src
│           └── logFile
├── doc
│   ├── generalconfig.tex
│   ├── PY2.pdf
│   ├── PY2.tex
│   ├── Requirements.md
│   ├── Requirements.pdf
│   ├── sn-jnl.cls
│   └── src
├── LICENSE
├── README.md
├── scripts
│   ├── bode.ipynb
│   ├── design.ipynb
│   └── PID.m
└── sim
    └── RLC.asc

```

- `Design.kicad_sch` / `.kicad_pcb` / `.kicad_pro` — KiCad design
- `Design.step` — 3D model
- `requirements.pdf` — project requirements
- `PY2.pdf` — project report
- `RLC.asc` — LTspice simulation


![Dron](images/dron.png)
![schematic](images/schematic.png)
**Photos of the built board — coming soon**


## Credit

Built with [Orlando Contreras (DasReyxr)](https://github.com/DasReyxr) as a two-person team project, advised by Dr. Luis Antonio Raygoza Pérez — Department of Electronic Systems, Universidad Autónoma de Aguascalientes.





## Template
```
mkdir code design doc scripts sim src
```

```
tree >> README.md
```

![QR Code](images/QR.png)
