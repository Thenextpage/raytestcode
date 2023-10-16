import ray

# Connect to the existing Ray cluster
ray.init()

@ray.remote
def multiply(arr):
    return [i * 2 for i in arr]

def main():
    arr = list(range(1, 11))
    arr1, arr2 = arr[:5], arr[5:]
    task1 = multiply.remote(arr1)
    task2 = multiply.remote(arr2)
    result1, result2 = ray.get([task1, task2])
    print(result1 + result2)

if __name__ == "__main__":
    main()
