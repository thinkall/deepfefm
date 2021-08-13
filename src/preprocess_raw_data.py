import os

data_dir = 'raw_data'
file_list = [os.path.join(data_dir, x) for x in os.listdir(data_dir)]

dense_max = [0.] * 13
dense_min = [0.] * 13

cur_line = 0
for file in file_list:
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            cur_line += 1
            if cur_line % 10000 == 0:
                print(f'current line: {cur_line}')
            features = line.rstrip('\n').split('\t')
            continuous_range_ = range(1, 14)
            for idx in continuous_range_:
                if features[idx] != '':
                    tmp = float(features[idx])
                    if dense_max[idx - 1] < tmp:
                        dense_max[idx - 1] = tmp
                    elif dense_min[idx - 1] > tmp:
                        dense_min[idx - 1] = tmp
            line = f.readline()

print(f'dense_max: {dense_max}')
print(f'dense_min: {dense_min}')

"""
raw data:
dense_max: [5775.0, 257675.0, 65535.0, 969.0, 23159456.0, 367553.0, 56311.0, 6047.0, 29019.0, 11.0, 231.0, 4008.0, 7393.0]
dense_min: [0.0, -3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

test data:
dense_max: [527.0, 24763.0, 65535.0, 409.0, 2491178.0, 431037.0, 12796.0, 1224.0, 18345.0, 8.0, 143.0, 360.0, 5934.0]
dense_min: [0.0, -2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

paddle dataset:
self.cont_min_ = [0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
self.cont_max_ = [5775, 257675, 65535, 969, 23159456, 431037, 56311, 6047, 29019, 46, 231, 4008, 7393]
"""
