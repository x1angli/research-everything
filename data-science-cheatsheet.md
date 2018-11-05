# Numpy
**NumPy** is an extension library for Python language, supporting operations of a large number of high-dimensional arrays and matrices. In addition, it also provides a large number of mathematical function libraries for array operations. Machine learning involves a lot of transformations and operations on arrays, which makes NumPy one of the essential tools.

## Matrix Operations in Numpy

### Matrix Multiplication
The key point here is that the `*` operator performs element-wise multiplication for `numpy.array`, but dot multiplicator for `numpy.matrix`

Preparation code:

    import numpy as np
    m1 = np.arange(9).reshape(3, 3) + 1                  
    m2 = m1.copy()
    mm1, mm2 = np.matrix(m1), np.matrix(m2)       # Note: the type of m1 differs from mm1! m1 is of "np.array", while m2 is of "np.matrix" 

* Dot Multiplication
    The following lines of code will yield the same mathmatical outcome (but not necessarily the exact same outcome, since programatically they same outcome might be expressed in different Python classes).

      product = np.matmul(m1, m2)
      product = m1.dot(m2)
      product = mm1 * mm2                                 # Note: the type of "product" is np.matrix
      product = m1 @ m2                                   # Note: the "@" operator is available in Python 3.5+ only.
      product = mm1 @ mm2                                 # Note: the type of "product" is np.matrix, and the "@" operator is available in Python 3.5+ only.
    
* Element-wise Multiplication
    The following lines of code will yield the same mathmatical outcome.

      product = m1 * m2


## 100 NumPy Exercises
https://labex.io/lab/403

**100 NumPy Exercises** 
Despite its name of "exercises", it's essentially a cheatsheet containing 100 most-frequent usage. 

It is divided into _basic part_ and _advanced part_, each with 50 exercises. The basic part of the exercise helps you familiarize yourself with the use of NumPy's common methods and the advanced part focuses on the combined application of the NumPy methods. 

<html><hr /></html>

