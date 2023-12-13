import pandas as pd
from transformers import pipeline


def read_any_table(file_name, file_st_obj):
    """
    Reads a table from a file based on its extension using pandas.

    Args:
        file_path: Path to the file containing the table.

    Returns:
        A pandas DataFrame containing the table data.
    """
    # Check if the file is empty
    if file_st_obj is None or file_st_obj.size == 0:
        raise ValueError("Empty file or unsupported format")
    else:
        # Extract file extension
        extension = file_name.split(".")[-1]

        # Choose appropriate pandas read function based on extension
        if extension == "csv":
            df = pd.read_csv(file_st_obj)
        elif extension in ["xls", "xlsx"]:
            df = pd.read_excel(file_st_obj)
        elif extension == "html":
            df = pd.read_html(file_st_obj)[0]
        elif extension == "json":
            df = pd.read_json(file_st_obj)
        else:
            raise ValueError(f"Unsupported file format: {extension}")

    return df


def load_classifier_model():
    """
    Loads a pre-trained zero-shot classification model from Hugging Face.

    Args:
        None

    Returns:
        A Hugging Face pipeline object for zero-shot classification.
    """
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

def extract_target_columns(columns_list, target_list: list = ['Transaction ID', 'Sold Products']):
    """
    Extracts target columns from a list of columns based on their predicted labels from a zero-shot classifier.

    Args:
        columns_list: A list of column names.
        target_list: A list of target labels for the zero-shot classifier.

    Returns:
        A dictionary where keys are target labels and values are corresponding predicted sequences.
    """
    classifier = load_classifier_model()
    targeting_result = {}

    for col in columns_list:
        prediction = classifier(col, candidate_labels=target_list, multi_label=True)

        # Check if any target label has high confidence score
        for i, score in enumerate(prediction['scores']):
            if score > 0.7:
                targeting_result[prediction['labels']] = prediction['sequence'][i]

    return targeting_result




