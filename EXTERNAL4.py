import os
import struct
import heapq
import time
def merge_sort_chunks(chunk_files, output_file):
    min_heap = []

    # Open all chunk files and read the first number from each
    chunk_readers = [open(chunk_file, 'r') for chunk_file in chunk_files]
    for i, chunk_reader in enumerate(chunk_readers):
        num_str = chunk_reader.readline()
        if num_str:
            num = int(num_str)
            heapq.heappush(min_heap, (num, i))

    # Open the output file
    with open(output_file, 'w') as output_writer:
        while min_heap:
            # Get the smallest number and its index
            num, chunk_index = heapq.heappop(min_heap)

            # Write the number to the output file
            output_writer.write(str(num) + "\n")

            # Read the next number from the corresponding chunk
            num_str = chunk_readers[chunk_index].readline()
            if num_str:
                num = int(num_str)
                heapq.heappush(min_heap, (num, chunk_index))

    # Close all chunk files
    for chunk_reader in chunk_readers:
        chunk_reader.close()

# Number of random integers to generate
total_integers = 10000000
# Number of chunk files
num_chunks = 10
# Calculate the size of each chunk
chunk_size = total_integers // num_chunks

start_time = time.time()

# Generate and store random integers in a decimal format
input_file = "input_data4.dat"
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

        # Sort and write each chunk to a file
        chunk_data.sort()
        chunk_file_name = f"chunk5_{i}.dat"
        chunk_files.append(chunk_file_name)
        with open(chunk_file_name, "w") as chunk_file:
            for num in chunk_data:
                chunk_file.write(str(num) + "\n")

# Merge and sort all sorted chunks using k-way merge sort
output_file = "sorted_output4.dat"
merge_sort_chunks(chunk_files, output_file)

# Record the end time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time

print("Data sorted and stored in", output_file)

print("Execution time: {:.2f} seconds".format(execution_time))