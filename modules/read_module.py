import pandas as pd


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







