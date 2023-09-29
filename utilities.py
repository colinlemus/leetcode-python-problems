import sys
import timeit


def benchmark(function, *args, num_runs=1000):
    """
    Benchmark the given function with the provided arguments.

    Parameters:
    - function: The function to be benchmarked.
    - *args: Arguments to pass to the function.
    - num_runs: Number of times to run the function for benchmarking.

    Returns:
    - result: Result of the function execution.
    - elapsed_time: Time taken for execution in seconds.
    - memory_used: Approximate memory used by the result in bytes.
    """

    # Wrap the function call in a lambda to pass to timeit
    func_lambda = lambda: function(*args)

    # Use timeit to get the average time over multiple runs
    total_time = timeit.timeit(func_lambda, number=num_runs)
    average_time = total_time / num_runs

    # Execute the function once to get the result and memory usage
    result = function(*args)
    memory_used = sys.getsizeof(result)

    return result, average_time, memory_used


def display_benchmark_results(
    problem_name, function, time_complexity, space_complexity, *args
):
    result, elapsed_time, memory_used = benchmark(function, *args)
    elapsed_time_us = (
        elapsed_time * 1000 * 1000
    )  # Convert to microseconds for better precision

    header = f"📋 Problem: {problem_name}"
    inputs = f"🔠 Inputs: {', '.join(map(str, args))}"
    output = f"🎯 Result: {result}"

    complexities = f"🛠 Time: {time_complexity} | Space: {space_complexity}"
    metrics = f"⏱ Elapsed: {elapsed_time_us:.4f} μs | 📦 Memory: {memory_used} bytes"

    print(f"{header}\n{inputs}\n{output}\n{complexities}\n{metrics}")
    print("─" * 40)
