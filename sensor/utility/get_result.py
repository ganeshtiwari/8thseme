import numpy as np

def main(ls, model):
    # print(len(ls))
    print('length is', len(ls))
    # sensor_data = [float(ls[i]) for i in range(270)]  # 90(x,y,z)data i.e 270 data
    input_node = []
    for a in range(90):
        b = [[ls[a * 3]], [ls[3 * a + 1]], [ls[3 * a + 2]]]
        input_node.insert(a, b)
    input_node = np.array(input_node)
    # pprint(input_node)
    # print("\n\n")
    # print("START TIME:  ", str(datetime.datetime.now().time()))
    prediction = model.predict(input_node.reshape(-1, 90, 3, 1))
    # print("\n\n")
    label = ['downstair', 'jogging', 'sitting', 'standing', 'upstair', 'walking']
    result = label[np.argmax(prediction)]
    return result
