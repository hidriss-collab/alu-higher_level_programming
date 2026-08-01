#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        The matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
