# Autonomous Drone System (in progress)

This project is an indoor autonomous drone platform built on ESP32 microcontrollers with custom C++ firmware.  
It uses wireless ESP-NOW communication for real-time control, nested PID loops for position/velocity regulation, and SBUS output to a Betaflight-compatible flight controller.

---

## 🧠 Architecture

The system consists of:
- **ESP32 Sender** connected to a computer via USB, receiving control signals from a Python backend and relaying them to the drone over ESP-NOW
- **ESP32 Receiver** on the drone, parsing incoming commands and feeding them to a nested PID control system
- **SBUS signal generation** to communicate with the flight controller
- **FPV video** is streamed separately to the computer via analog signal and processed by OpenCV

---

## ✅ Features

- ✅ ESP-NOW wireless communication
- ✅ C++ firmware with nested PID loops (position + velocity)
- ✅ SBUS signal generation
- ✅ Ground effect compensation logic
- 🟣 Python-based trajectory optimizer + vision tracking *(coming soon)*

> The drone is controlled based on real-time analysis of FPV video received by the computer.  
> The backend processes the video and calculates control commands sent to the drone via ESP-NOW.

---

## 🔧 Tech Stack

- **ESP32**
- **C++ (Arduino Core)**
- **SBUS Protocol**
- **Betaflight**
- **OpenCV, Numpy, Scipy** *(in progress)*

---

## 🚧 Status

- [x] Firmware for drone and sender implemented
- [ ] Python backend in development (OpenCV + trajectory logic)
- [ ] Indoor 2D mapping module

---

## 📷 Block Diagram

![blok_Schema](https://github.com/user-attachments/assets/8291ffef-eb89-44dd-a07f-c39db87e1031)


---

## 📨 Contact

Created by Dávid Husár  
Feel free to reach out at: daviidhusar@gmail.com
