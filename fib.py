import sys
import os
from concurrent.futures import ProcessPoolExecutor, as_completed


def fibonacchi(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    else:
        return a


def main():
    n = int(sys.argv[1])
    print("返される値は環境で異なる")
    print(f"{os.cpu_count()=}")
    nums = [n] * os.cpu_count()

    # get_sequential(nums)
    get_multi_process(nums)


def get_sequential(nums):
    for num in nums:
        fibonacchi(num)


def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacchi, num) for num in nums]

        for futures in as_completed(futures):
            futures.result()


if __name__ == "__main__":
    main()
