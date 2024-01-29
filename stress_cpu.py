from multiprocessing import Pool
from multiprocessing import cpu_count

# Do intensive computation to stress the CPU
def stress_cpu(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

if __name__ == '__main__':
    # Create as many processes as there are CPU cores
    processes = cpu_count()
    pool = Pool(processes)
    print(pool.map(stress_cpu, [110000000, 110000000]))
