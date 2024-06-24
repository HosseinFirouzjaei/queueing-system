import numpy as np
import math

P_max = 0.00015
TX1_Power = 0.00010 # transfer power of TX1 in watt
TX1_fading_samples = 1000 # Number of fading samples in the channel between TX1 and RX1
RX1_Noise_Power = pow(10,-5) # Noise power in watt
TX1_Bandwidth = pow(10,3) # Bandwidth of the communication channel between TX1 and RX1
TX1_communication_time = 0.0003 # Communication time TX1-RX1

Harvesting_power_TX1 = P_max - TX1_Power  # Power that TX1 allocates for energy harvesting
EH_eta = 0.1 # power conversion efficiency
energy_harvesting_time = 0.0004
EH_fading_samples = 1000

TX2_fading_samples = 1000 # Number of fading samples in the channel between TX1 and RX1
RX2_Noise_Power = pow(10,-5) # Noise power in watt
TX2_Bandwidth = pow(10,3) # Bandwidth of the communication channel between TX1 and RX1
TX2_communication_time = 0.0003 # Communication time TX1-RX1

def FadingChannel(TX_Power, distance, ALPHA, fading_samples):# Rayleigh fading model
    # Generate Rayleigh fading samples (complex Gaussian random variables)
    fading = np.random.normal(0, 1, fading_samples) + 1j * np.random.normal(0, 1, fading_samples)
    
    # Calculate received power
    received_power = TX_Power * pow(distance, -ALPHA) * np.abs(fading)**2
    
    # Calculate average received power
    RX_Power = np.mean(received_power)
    return RX_Power

def calculate_transferred_data(Received_Power, Noise_Power, Bandwidth, communication_time):
    SNR = Received_Power/Noise_Power
    Rate = Bandwidth * math.log2(1+SNR)
    Data = Rate * communication_time
    return SNR, Rate, Data  

def calculate_harvested_power(power, eta, distance, ALPHA, EH_fading_samples):
    Harvested_power = eta * FadingChannel(power, distance, ALPHA, EH_fading_samples)
    return Harvested_power

