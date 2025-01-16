"""
MIT License

Copyright (c) 2024 yuhari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# https://gist.github.com/harigro/28df9ec639f74f217473f85065acf9d8 

from typing import List, Dict

def divide_array_to_graph(arr: List[int], base: int) -> Dict[int, List[int]]:
    """
    Splits an array into smaller parts and returns them in a dictionary, simulating a graph 
    structure where each part of the array is a node connected to other parts.

    Args:
        arr (List[int]): The array to be divided.
        base (int): The divisor that determines the number of parts.

    Returns:
        Dict[int, List[int]]: A dictionary representing the graph structure, 
                              where each key is a node and the value is a list of connected nodes.

    Example:
        >>> divide_array_to_graph(arr=[1, 2, 3, 4, 5, 6, 7, 8], base=2)
        {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [7, 8]}
        >>> divide_array_to_graph(arr=[1, 2, 3, 4, 5, 6, 7, 8], base=3)
        {0: [1, 2, 3, 4], 1: [5, 6, 7, 8]}
    """
    length = len(arr)
    parts = len(arr)//base  # Desired number of parts
    part_size = length // parts  # Size of each part
    
    # Divide the array into smaller parts
    result = [arr[i * part_size: (i + 1) * part_size] for i in range(parts)]
    
    # Insert the result into a dictionary with keys from 0 to 3
    result_dict = {i: result[i] for i in range(parts)}
    
    return result_dict

if __name__ == "__main__":
    # Example usage
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(divide_array_to_graph(array, 2))
    
    import doctest
    doctest.testmod()