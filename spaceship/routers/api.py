from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/multiply_matrices')
def multiply_matrices() -> dict:
    matrix_a = np.random.randint(0, 100, (10, 10)).tolist()
    matrix_b = np.random.randint(0, 100, (10, 10)).tolist()
    
    product = np.dot(matrix_a, matrix_b).tolist()
    
    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product
    }
