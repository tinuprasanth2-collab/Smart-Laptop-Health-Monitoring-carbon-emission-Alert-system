# Smart-Laptop-Health-Monitoring-carbon-emission-Alert-system

This project uses **Machine Learning** and an **ESP32** to monitor laptop health and estimate carbon emissions in real time. Sensor data such as **temperature**, **vibration**, and **carbon emission** is sent to a Python application, where a trained **Random Forest** model predicts the laptop's condition as **Normal**, **Warning**, or **Critical**.

## Features

- Real-time laptop health monitoring
- Random Forest machine learning model
- ESP32 serial communication
- Carbon emission estimation
- Live prediction using Python
- 99.95% prediction accuracy

## Technologies Used

- Python
- ESP32
- Arduino IDE
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- PySerial

## Project Structure

```text
Laptop-Carbon-Emission-Monitor
│
├── Generate_DS/
│   └── generate_dataset.py      # Generates the training dataset
│
├── train_model/
│   └── train_model.py           # Trains the Random Forest model
│
├── Test_model/
│   ├── test_model.py            # Tests the trained model
│   └── Test_result/             # Stores prediction results
│
└── README.md
```
## How It Works

1. ESP32 generates and sends sensor data.
2. Python receives the data through serial communication.
3. The trained Random Forest model predicts the laptop's health status.
4. The result is displayed in real time.

# Final Result

<img width="966" height="481" alt="image" src="https://github.com/user-attachments/assets/e074ca52-dadf-476a-8eb5-4d56f1212be8" />


## Sample Output

```text
Temperature : 42.8 °C
Vibration  : 0.6
Carbon     : 28.4

Status : NORMAL
```
# Test Result

<img width="1130" height="1087" alt="image" src="https://github.com/user-attachments/assets/f0f07136-3bcb-4345-9049-8607409fd45e" />


# Confusion Matrix

<img width="672" height="492" alt="image" src="https://github.com/user-attachments/assets/7c40303a-d1b7-4ef9-ad98-dfa798df55d1" />


## Future Improvements

- Add a real CO₂ sensor
- Build a web dashboard
- Cloud data logging
- Mobile app support
- IoT integration

