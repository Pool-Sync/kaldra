from sentence_transformers import SentenceTransformer

# Load the Sentence Transformer model only once when the module is imported.
# This ensures efficiency by avoiding reloading the model on every call.
MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str) -> list[float]:
    """
    Generates a sentence embedding for the given text.

    Args:
        text: The input string to be encoded.

    Returns:
        A list of floats representing the embedding of the text.
    """
    # Generate the embedding for the text.
    embedding = MODEL.encode(text)

    # Convert the NumPy array to a list of floats for JSON serialization.
    return embedding.tolist()
