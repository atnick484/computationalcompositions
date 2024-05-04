import matplotlib.pyplot as plt

# Dictionary of epochs and loss values for the new model
epoch_loss_data = {
    1: 5.0605, 2: 4.7363, 3: 4.7319, 4: 4.7201, 5: 4.7181, 6: 4.7176, 7: 4.7115, 8: 4.709, 9: 4.707,
    10: 4.6977, 11: 4.6877, 12: 4.6767, 13: 4.6553, 14: 4.6318, 15: 4.6125, 16: 4.5891, 17: 4.5663,
    18: 4.545, 19: 4.5287, 20: 4.5193, 21: 4.5133, 22: 4.5101, 23: 4.5043, 24: 4.4931, 25: 4.4758,
    26: 4.4617, 27: 4.4437, 28: 4.4291, 29: 4.4143, 30: 4.3998, 31: 4.3876, 32: 4.3739, 33: 4.3595,
    34: 4.3484, 35: 4.3378, 36: 4.3231, 37: 4.3099, 38: 4.2928, 39: 4.2789, 40: 4.2647, 41: 4.2537,
    42: 4.2421, 43: 4.2328, 44: 4.2188, 45: 4.2122, 46: 4.2032, 47: 4.1939, 48: 4.1854, 49: 4.1755,
    50: 4.1637, 51: 4.1548, 52: 4.1466, 53: 4.1366, 54: 4.1242, 55: 4.1188, 56: 4.109, 57: 4.0996,
    58: 4.0892, 59: 4.0844, 60: 4.074, 61: 4.0602, 62: 4.0511, 63: 4.0427, 64: 4.0339, 65: 4.0218,
    66: 4.01, 67: 4.0011, 68: 3.9888, 69: 3.9736, 70: 3.9626, 71: 3.9453, 72: 3.9361, 73: 3.9244,
    74: 3.9173, 75: 3.9063, 76: 3.8932, 77: 3.8778, 78: 3.8607, 79: 3.8445, 80: 3.8352, 81: 3.8219,
    82: 3.8089, 83: 3.7889, 84: 3.777, 85: 3.7623, 86: 3.7478, 87: 3.7374, 88: 3.7241, 89: 3.7168,
    90: 3.7097, 91: 3.701, 92: 3.6911, 93: 3.6756, 94: 3.6642, 95: 3.6526, 96: 3.6407, 97: 3.6268,
    98: 3.6163, 99: 3.5957, 100: 3.5745, 101: 3.5576, 102: 3.5467, 103: 3.5379, 104: 3.5245, 105: 3.5132,
    106: 3.5014, 107: 3.4956, 108: 3.4946, 109: 3.4912, 110: 3.4861, 111: 3.4736, 112: 3.4659, 113: 3.4495,
    114: 3.431, 115: 3.4138, 116: 3.4134, 117: 3.4239, 118: 3.4457, 119: 3.468, 120: 3.4855, 121: 3.4872,
    122: 3.4994, 123: 3.4898, 124: 3.4862, 125: 3.4629, 126: 3.4396, 127: 3.4152, 128: 3.3901, 129: 3.3674,
    130: 3.3444, 131: 3.3232, 132: 3.3038, 133: 3.2989, 134: 3.2927, 135: 3.2874, 136: 3.3007, 137: 3.3023,
    138: 3.2565, 139: 3.2396, 140: 3.2263, 141: 3.2201, 142: 3.2199, 143: 3.2206, 144: 3.205, 145: 3.209,
    146: 3.2164, 147: 3.211, 148: 3.203, 149: 3.1895, 150: 3.1939, 151: 3.1953, 152: 3.2067, 153: 3.2327,
    154: 3.2545, 155: 3.2094, 156: 3.1646, 157: 3.14, 158: 3.1368, 159: 3.1378, 160: 3.1601, 161: 3.1698,
    162: 3.1867, 163: 3.1832, 164: 3.1833, 165: 3.1804, 166: 3.1798, 167: 3.1776, 168: 3.1753, 169: 3.16,
    170: 3.1332, 171: 3.1089, 172: 3.0971, 173: 3.1108, 174: 3.1171, 175: 3.1225, 176: 3.1212, 177: 3.1175,
    178: 3.126, 179: 3.1338, 180: 3.1223, 181: 3.1316, 182: 3.1676, 183: 3.1837, 184: 3.1124, 185: 3.1054,
    186: 3.1079
}


# Creating lists of epochs and loss values from the dictionary
epochs = list(epoch_loss_data.keys())
loss_values = list(epoch_loss_data.values())

# Plotting the graph
plt.figure(figsize=(7, 5))
plt.plot(epochs, loss_values, marker='o', linestyle='-', color='r')
plt.title('Model With Duration and Rests Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.show()