import numpy as np

def border_with_zeros(arr):
    '''
    Takes in a 2D numpy array and adds
    a border of zeros around the outer edge

    Example:

        arr = np.array([
            [1,1],
            [1,1]
        ])
        border_with_zeros(arr)

    Would return:

        np.array([
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ])
    '''

    # your code here!
    shape = arr.shape
    print(shape)
    arr1 = np.zeros([shape[0]+ 2, shape[1] + 2])
    arr1[1:-1,1:-1] = arr
    int_array = arr1.astype(int)
    print(int_array)



if __name__ == '__main__':
    # Test your code here!
    arr = np.array([
        [1,1],
        [1,1]
    ])
    print(border_with_zeros(arr))
