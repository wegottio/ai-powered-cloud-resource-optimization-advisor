# gpu.py
import cupy as cp

def gpu_operation():
    #operation
    x_gpu = cp.array([1, 2, 3])
    y_gpu = cp.array([4, 5, 6])
    result_gpu = x_gpu + y_gpu
    return result_gpu.get()

if __name__ == '__main__':
    result = gpu_operation()
    print("GPU Result:", result)
