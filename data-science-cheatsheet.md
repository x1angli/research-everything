# Numpy
**NumPy** is an extension library for Python language, supporting operations of a large number of high-dimensional arrays and matrices. In addition, it also provides a large number of mathematical function libraries for array operations. Machine learning involves a lot of transformations and operations on arrays, which makes NumPy one of the essential tools.

## Matrix Multiplication in Numpy

The key point here is that the `*` operator performs element-wise multiplication for `numpy.array`, but dot multiplicator for `numpy.matrix`

Preparation code:

    import numpy as np
    m1 = np.arange(9).reshape(3, 3) + 1                  
    m2 = m1.copy()
    mm1, mm2 = np.matrix(m1), np.matrix(m2)       # Note: the type of m1 differs from mm1! m1 is of "np.array", while m2 is of "np.matrix" 

* Dot Multiplication

__TL;DR__: In short, the asterisk `*` operand distiguishes between np.array and np.array: it performs element-wise multiplication for np.array, while dot multiplication for matrix. However, an at `@` operand guarantees dot multiplication.
<html><ul>
<sup><li> Note #1: The following lines of code will yield the same mathmatical outcome (but not necessarily the exact same outcome, since programatically they same outcome might be expressed in different Python classes). </sup>
<sup><li> Note #2: the `@` operator is available in Python 3.5+ only.</sup>
</ul></html>
      product = np.matmul(m1, m2)
      product = m1.dot(m2)
      product = mm1 * mm2                                 # Note: the types of product, m1, and m2 are np.matrix
      product = m1 @ m2                                   # Note: the types of product, m1, and m2 are np.array 
      product = mm1 @ mm2                                 # Note: the types of product, m1, and m2 are np.matrix
    
* Element-wise Multiplication

      product = m1 * m2                                   # Note: the types of product, m1, and m2 are np.array

## Useful links

### PyTorch Tutorials
* Link: https://pytorch.org/tutorials/
* Source Code Repo: https://github.com/pytorch/tutorials
It uses sphinx-gallery's notebook styled examples to create the tutorials

### Mindmap: Data Science for Managers ###
* Description: https://activewizards.com/blog/intro-to-data-science-for-managers-mindmap/?utm_source=reddit&utm_medium=programming&utm_campaign=ds_mindmap
* Source File: https://coggle.it/diagram/WypjBWlbpEHkyhcg/t/data-science-for-managers/c0083ef2d003b849535618df0b84e6dad73e301910c45e7eab5b72ff12f016e0

Data science is incredibly broad and complex discipline, an interception of computer science, math and statistics, and a domain of knowledge requiring the understanding the source of data: medical, financial, web, and other domains. The mindmap below contains a condensed introduction to the key data science concepts and techniques that have revolutionized the business landscape and became essential for making beneficial data-driven decisions. We are confident that it will be useful and informative for both the data science managers and for those facing this rapidly developing field as a client or user.

![Mindmap: data science for managers](./data-science-for-managers.png)


### 100 NumPy Exercises
* Link: https://labex.io/lab/403

Despite its name of "exercises", it's essentially a cheatsheet containing 100 most-frequent usage. 

It is divided into _basic part_ and _advanced part_, each with 50 exercises. The basic part of the exercise helps you familiarize yourself with the use of NumPy's common methods and the advanced part focuses on the combined application of the NumPy methods. 

<html><hr /></html>

