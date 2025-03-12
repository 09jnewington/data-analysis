import numpy as np
def get_rows(arr: np.ndarray):
    return [np.array(i) for i in arr]
def get_columns(arr: np.ndarray):
    T_arr = arr.T
    return get_rows(T_arr)

a = np.array([[5, 0, 3, 3],
 [7, 9, 3, 5],
 [2, 4, 7, 6],
 [8, 8, 1, 6]])

def get_row_vectors(arr: np.ndarray):
    return np.split(arr, arr.shape[0], axis=0)

def get_col_vectors(arr: np.ndarray):
    return np.split(arr, arr.shape[1], axis=1)

def diamond(num:int):
    bottom_left = np.eye(num)
    bottom_right = bottom_left[::-1, 1:]
    bottom = np.concatenate((bottom_left, bottom_right), axis=1)
    top = bottom[num-1:0:-1, ::]
    full = np.concatenate((top, bottom))
    return full

def vector_lengths(arr: np.ndarray):
    return np.sqrt(np.sum(arr, axis=1))

def multiplication_table(n:int) -> np.ndarray:
    row = np.arange(n)
    column = row.reshape(n, 1)
    return row*column

print(multiplication_table(4))