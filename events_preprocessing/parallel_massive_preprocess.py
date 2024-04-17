import numpy as np
import pickle
import matplotlib.pyplot as plt
from input_process import *
from shutil import copy
import os
from concurrent.futures import ProcessPoolExecutor

# 多线程加速
data_path = 'F:\Files\PhD/Braille/Code\Events_Examples\Experiment_Data'
raw_place = 'rawData'
processed_place = 'processedData'

def process_file(filename, temporal_compress=False, compress_time=350):
    with open(data_path + '/' + raw_place + '/' + filename, 'rb') as file:
        data = pickle.load(file)
    
    print(filename)
    
    data = clip_pretime(data, 700)
    input_psth = crop(data, 700, temporal_compress, compress_time).astype(np.int8) # 修改为int8类型，直接减小文件大小，方便运输

    np.save(data_path + '/' + processed_place + '/' + filename[5:-10] + '.npy', input_psth)


def main():
    file_names = os.listdir(data_path + '/' + raw_place)

    with ProcessPoolExecutor(max_workers=20) as executor:
        executor.map(process_file, file_names)

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)