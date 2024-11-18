# ------------------ NUMPY ---------------------

'''

Numpy Github Codebase - https://github.com/numpy/numpy

> Numpy - It is a library in python programming language, that adss support for large, multi-dimensional arrays and matrices, along with a large collection of high level mathematical functions to operate on these arrays.

> Why use Numpy?

    1. Speed: Numpy is much faster than Python lists for numerical computations.
    2. Memory Efficiency: Numpy arrays are more memory efficient than Python lists.
    3. Vectorized Operations: Numpy allows you to perform operations on entire arrays at once.    
    4. Integration with Other Libraries: Numpy integrates well with other popular Python libraries like Pandas.
    5. Support for Large Arrays: Numpy can handle large arrays and matrices efficiently.
    6. Support for Complex Numbers: Numpy supports complex numbers and can perform operations on them.
    7. Support for Linear Algebra: Numpy has built-in support for linear algebra operations like matrix multiplication, eigenvalue decomposition, singular value decomposition, etc.

> Why is Numpy faster than Python Lists?

    NumPy array are stored at one continuous places in memeory unlike lists so processes can access and manipulate them very efficiently. This behaviour is known as Locality of Reference. This is the main reason why NumPy arrays are faster than lists. 

> Which language NumPy is written in?

    It is partially written in Python but most of the parts that require fast computation are written in C or C++.


'''


# Importing NumPy Library
import numpy as np

arr = np.array([1,2,3,4]) # NumPy Array
print(arr)

print(f"NumPy Version: {np.__version__}")