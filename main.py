from keras.models import load_model

model = load_model("/home/maina/PycharmProjects/Predicting_Stock_Prices/Stock_Prices_Prediction.model")

print(model.input_shape)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
