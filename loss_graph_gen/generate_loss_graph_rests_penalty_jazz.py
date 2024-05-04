import matplotlib.pyplot as plt

# Dictionary of epochs and loss values for the new model
epoch_loss_data = {1: 6.8385, 2: 6.8274, 3: 6.8095, 4: 6.8016, 5: 6.8419, 6: 6.7689, 7: 6.758, 8: 6.7367, 9: 6.7211, 10: 6.7337, 11: 6.7025, 12: 6.6917, 13: 6.6873, 14: 6.6672, 15: 6.6451, 16: 6.6559, 17: 6.6179, 18: 6.6098, 19: 6.5995, 20: 6.5962, 21: 6.5719, 22: 6.5597, 23: 6.5861, 24: 6.5371, 25: 6.6253, 26: 6.5121, 27: 6.5024, 28: 6.4929, 29: 6.5429, 30: 6.4828, 31: 6.4671, 32: 6.4522, 33: 6.435, 34: 6.4349, 35: 6.4154, 36: 6.4024, 37: 6.406, 38: 6.3916, 39: 6.3847, 40: 6.3719, 41: 6.3649, 42: 6.3477, 43: 6.3363, 44: 6.3355, 45: 6.3188, 46: 6.3102, 47: 6.3022, 48: 6.2956, 49: 6.2848, 50: 6.2709, 51: 6.2659, 52: 6.2648, 53: 6.255, 54: 6.2355, 55: 6.2296, 56: 6.2442, 57: 6.215, 58: 6.2304, 59: 6.1961, 60: 6.196, 61: 6.1866, 62: 6.1732, 63: 6.174, 64: 6.163, 65: 6.1602, 66: 6.153, 67: 6.1523, 68: 6.1409, 69: 6.1252, 70: 6.1208, 71: 6.1476, 72: 6.1144, 73: 6.1022, 74: 6.0841, 75: 6.1014, 76: 6.0751}




# Creating lists of epochs and loss values from the dictionary
epochs = list(epoch_loss_data.keys())
loss_values = list(epoch_loss_data.values())

# Plotting the graph
plt.figure(figsize=(7, 5))
plt.plot(epochs, loss_values, marker='o', linestyle='-', color='g')
plt.title('Model Trained on Jazz Dataset Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
