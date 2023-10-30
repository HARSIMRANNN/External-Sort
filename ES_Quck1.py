import os
import struct
import time
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            stack.append((low, i))
            stack.append((i + 2, high))

    return arr

# Define a merge_sort_chunks function that sorts chunks using quicksort
def merge_sort_chunks(chunk_files, output_file):
    chunk_data = []

    # Read and sort each chunk using quicksort
    for chunk_file in chunk_files:
        with open(chunk_file, 'r') as chunk_reader:
            chunk = [int(line) for line in chunk_reader]
            sorted_chunk = quicksort(chunk)
            chunk_data.append(sorted_chunk)

    # Merge and write the sorted chunks using k-way merge sort
    sorted_output = []
    while chunk_data:
        min_chunk = min(chunk_data, key=lambda x: x[0])
        sorted_output.append(min_chunk.pop(0))
        if not min_chunk:
            chunk_data.remove(min_chunk)

    # Write the sorted data to the output file
    with open(output_file, 'w') as output_writer:
        for num in sorted_output:
            output_writer.write(str(num) + "\n")

# Number of random integers to generate
total_integers = 10000
# Number of chunk files
num_chunks = 10
# Calculate the size of each chunk
chunk_size = total_integers // num_chunks

start_time = time.time()

# Generate and store random integers in a decimal format
input_file = "Q1input_data.dat"
with open(input_file, "w") as file:
    for _ in range(total_integers):
        num = str(int(struct.unpack("I", os.urandom(4))[0] % 10000))
        file.write(num + "\n")

# Divide the data into chunks
chunk_files = []
with open(input_file, "r") as file:
    for i in range(num_chunks):
        chunk_data = []
        for _ in range(chunk_size):
            num_str = file.readline()
            if not num_str:
                break
            num = int(num_str)
            chunk_data.append(num)

        # Sort and write each chunk using quicksort
        chunk_file_name = f"Q1chunk_{i}.dat"
        chunk_files.append(chunk_file_name)
        with open(chunk_file_name, "w") as chunk_file:
            for num in quicksort(chunk_data):
                chunk_file.write(str(num) + "\n")

# Merge and sort all sorted chunks using k-way merge sort
output_file = "Q1sorted_output.dat"
merge_sort_chunks(chunk_files, output_file)


end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

print("Data sorted and stored in", output_file)

print("Execution time: {:.2f} seconds".format(execution_time))