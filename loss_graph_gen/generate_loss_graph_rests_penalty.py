import matplotlib.pyplot as plt

# Dictionary of epochs and loss values for the new model
epoch_loss_data = {1: 5.0702, 2: 5.0644, 3: 5.0601, 4: 5.0614, 5: 5.0498, 6: 5.0184, 7: 5.0254, 8: 5.0082, 9: 5.0003, 10: 4.9963, 11: 4.9861, 12: 4.9886, 13: 4.9752, 14: 4.9623, 15: 4.9571, 16: 4.9487, 17: 4.9504, 18: 4.9294, 19: 4.9263, 20: 4.9097, 21: 4.8889, 22: 4.9075, 23: 4.9022, 24: 4.8825, 25: 4.8998, 26: 4.8633, 27: 4.8686, 28: 4.8602, 29: 4.8674, 30: 4.8605, 31: 4.8437, 32: 4.8392, 33: 4.8229, 34: 4.808, 35: 4.8151, 36: 4.8132, 37: 4.8159, 38: 4.8098, 39: 4.7913, 40: 4.7863, 41: 4.7748, 42: 4.7663, 43: 4.7585, 44: 4.7823, 45: 4.7573, 46: 4.7526, 47: 4.7409, 48: 4.752, 49: 4.7277, 50: 4.7339, 51: 4.7235, 52: 4.7288, 53: 4.7168, 54: 4.7066, 55: 4.7111, 56: 4.7101, 57: 4.7026, 58: 4.6999, 59: 4.6879, 60: 4.6856, 61: 4.6787, 62: 4.6769, 63: 4.669, 64: 4.6574, 65: 4.6685, 66: 4.6597, 67: 4.6458, 68: 4.6585, 69: 4.6435, 70: 4.6472, 71: 4.6487, 72: 4.6401, 73: 4.6444, 74: 4.6216, 75: 4.631, 76: 4.6186, 77: 4.6135, 78: 4.6123, 79: 4.6109, 80: 4.6103, 81: 4.5971, 82: 4.6102, 83: 4.6033, 84: 4.584, 85: 4.6049, 86: 4.6049, 87: 4.596, 88: 4.5819, 89: 4.5717, 90: 4.5856, 91: 4.5708, 92: 4.5808, 93: 4.5697, 94: 4.5729, 95: 4.565, 96: 4.565, 97: 4.5565, 98: 4.5679, 99: 4.5519, 100: 4.5513}




# Creating lists of epochs and loss values from the dictionary
epochs = list(epoch_loss_data.keys())
loss_values = list(epoch_loss_data.values())

# Plotting the graph
plt.figure(figsize=(7, 5))
plt.plot(epochs, loss_values, marker='o', linestyle='-', color='m')
plt.title('Model With Duration and Penalized Rests Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
