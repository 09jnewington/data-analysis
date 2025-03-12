import pandas as pd
import numpy as np

a=pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")['Air temperature (degC)'].values


## Masking


def column_comparison(arr: np.array) -> np.array:
    c = arr[::, 1] > arr[::,-2]
    return arr[c]

def first_half_second_half(arr: np.array) -> np.array:
    m = arr.shape[1] // 2
    mask = np.sum(arr[:, :m], axis=1) > np.sum(arr[:, m:], axis=1)
    return (arr[mask])


a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2],
              [2, 2, 2, 2],
              [3, 4, 0, 1]])

def most_frequent_first(arr: np.array, c:int) -> np.array:
    column = arr[:, c]
    unique_elements, counts = np.unique(column, return_counts=True)
    sorted_indices = np.argsort(-counts)
    sorted_elements = unique_elements[sorted_indices]

    sorted_rows = []
    for element in sorted_elements:
        sorted_rows.extend(arr[column == element])
    return np.array(sorted_rows)

def matrix_power(arr:np.array, n:int) -> np.array:
    product = arr
    for i in range(n):
        product = np.matmul(product, arr)
    return product

print(matrix_power(a, 2))


