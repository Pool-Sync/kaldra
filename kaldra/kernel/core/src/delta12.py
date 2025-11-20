import numpy as np

def _softmax(x: np.ndarray) -> np.ndarray:
    """
    Computes the softmax of a vector, a numerically stable version.
    """
    # Subtract the max for numerical stability
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def project_to_delta12(embedding: list[float]) -> list[float]:
    """
    Projects a high-dimensional embedding into a 12-dimensional archetypal space.

    The projection is a simple v0.1 implementation that works as follows:
    1. Splits the embedding vector into 12 equal blocks.
    2. Calculates the mean value of each block.
    3. Applies a softmax function to the resulting 12-value vector to normalize it.

    Args:
        embedding: A high-dimensional embedding vector as a list of floats.

    Returns:
        A 12-dimensional vector as a list of floats, where each value is
        between 0 and 1, and the sum of all values is 1.
    """
    if not isinstance(embedding, list) or not all(isinstance(i, float) for i in embedding):
        raise TypeError("Input embedding must be a list of floats.")

    # Convert the list to a NumPy array for efficient computation
    embedding_array = np.array(embedding)

    # 1. Split the embedding into 12 equal-sized chunks
    # numpy.array_split handles cases where the length is not perfectly divisible by 12
    chunks = np.array_split(embedding_array, 12)

    # 2. Calculate the mean of each chunk to get the 12 archetypal weights
    mean_vector = np.array([chunk.mean() for chunk in chunks])

    # 3. Apply softmax to normalize the vector into a probability distribution
    delta12_vector = _softmax(mean_vector)

    # 4. Convert the final NumPy array back to a list of floats
    return delta12_vector.tolist()
