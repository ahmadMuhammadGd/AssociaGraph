from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd
import streamlit as st


def encode(item_freq):
    """
    Encodes a frequency value to 1 if it's greater than 0, else 0.

    Args:
        item_freq: The frequency value of an item.

    Returns:
        1 if the frequency is greater than 0, 0 otherwise.
    """
    res = 0
    if item_freq > 0:
        res = 1
    return res

def asso_rules(dataframe, order_id_column_name="Order_ID", product_column_name="Product"):
    df = dataframe[[order_id_column_name, product_column_name]]
    """
    Generates association rules from a pandas DataFrame containing orders and products.

    Args:
        df: A pandas DataFrame containing order IDs and product names.
        order_id_column_name: The name of the column containing order IDs (default: "Order_ID").
        product_column_name: The name of the column containing product names (default: "Product").

    Returns:
        A pandas DataFrame containing the generated association rules, including antecedents, consequents, support, confidence, and lift.
    """
    # Create a crosstab table to represent the basket data
    basket_df = pd.crosstab(df[order_id_column_name], df[product_column_name])

    # Encode the frequency values to 1 or 0
    basket_df = basket_df.applymap(encode)

    # Generate frequent itemsets
    frequent_itemsets = apriori(basket_df, min_support=0.001, use_colnames=True)

    # Generate association rules from the frequent itemsets
    rules = association_rules(frequent_itemsets, metric="lift").sort_values(
        ["support", "confidence", "lift"], axis=0, ascending=False
    )[
        ["antecedents", "consequents", "support", "confidence", "lift"]
    ]

    return rules

@st.cache_data
def phrase_rules(rules, conf_threshold=0):
    """
    Filters and formats the association rules into a human-readable format, highlighting confident rules.

    Args:
        rules: A pandas DataFrame containing the association rules.
        conf_threshold: The minimum confidence threshold for displaying rules (default: 0).

    Returns:
        A pandas DataFrame containing the filtered and formatted association rules.
    """

    # Filter rules based on confidence threshold
    rules = rules[rules['confidence'] >= conf_threshold]

    # Format the antecedents and consequents for better readability
    cols = ["antecedents", "consequents"]
    rules[cols] = rules[cols].applymap(lambda x: str(x).replace("frozenset({'", "").replace("'})", ""))

    return rules

