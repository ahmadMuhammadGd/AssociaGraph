import streamlit as st


st.image("logo2.svg", width=350)

st.sidebar.markdown("""
                    # AssociaGraph Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Uploading Data](#uploading-data)
3. [Association Rules](#association-rules)
    - [Column Selection](#column-selection)
    - [Executing the Algorithm](#executing-the-algorithm)
    - [Viewing Results](#viewing-results)
    - [Downloading CSV](#downloading-csv)
4. [Network Graph](#network-graph)
    - [Choosing Metrics](#choosing-metrics)
    - [Generating the Graph](#generating-the-graph)
    - [Downloading Graph](#downloading-graph)
5. [Troubleshooting](#troubleshooting)
6. [Feedback and Support](#feedback-and-support)            
""")
st.markdown(
"""
## Introduction

AssociaGraph is a Streamlit web application designed to help users analyze association rules and visualize network graphs based on their dataset. This documentation provides a comprehensive guide on using the features and functionalities offered by the app.

## Getting Started

### Uploading Data

- Use the sidebar to upload your dataset (CSV, Excel, etc.) using the file uploader.
"""
)

st.image("./user_doc_imgs/step 1 uploading data.png")
st.image("./user_doc_imgs/step 1-2 uploading data.png")
st.markdown("- Make sure that you can see the success message and the apperance of your data set ")
st.image("./user_doc_imgs/step 1-3 uploading data.png")
st.markdown(

"""
# Association Rules

Association rules are a crucial concept in data mining and analytics, particularly in understanding the relationships and patterns within datasets. These rules highlight associations or correlations between items in a dataset. The most common application is in market basket analysis, where associations between products purchased together are identified.

## Column Selection

When using AssociaGraph, the first step is to select the appropriate columns for **order ID** and **sold products**. The **order ID** is a unique identifier for each individual order, while the **sold products** column contains items that customers have purchased.

## Executing the Algorithm

Click the "Continue" button to initiate the association rules algorithm. AssociaGraph employs the Apriori algorithm to generate frequent itemsets, which are then used to derive association rules.
"""
)

st.image("./user_doc_imgs/step 2 choose columns.png")

st.markdown("""## Viewing Results

Once the algorithm has been executed, the generated association rules will be displayed in the "Association Rules" section. These rules consist of antecedents, consequents, support, confidence, and lift values.

- **Antecedents:** The items that are present before a purchase.
- **Consequents:** The items that are likely to be purchased together with the antecedents.
- **Support:** The proportion of transactions that include both antecedents and consequents.
- **Confidence:** The likelihood that the purchase of antecedents will lead to the purchase of consequents.
- **Lift:** The ratio of the observed support to the expected support, indicating how much more likely the consequents are to be purchased when considering antecedents.

## Downloading CSV

To further analyze or share the association rules, you can download them in CSV format using the "Download Association Rules CSV" button.

This information can be invaluable for businesses to understand customer behavior, optimize inventory management, and implement targeted marketing strategies.
""")

st.image("./user_doc_imgs/step 2-2 choose columns.png")

st.markdown(
"""
## Network Graph

### Choosing Metrics

- In the "Network Graph" section, choose the weight metric (confidence, support, lift) from the dropdown menu.
"""
)

st.image("./user_doc_imgs/step 3 graph.png")

st.markdown(
"""
### Downloading Graph

- Use the "Download Graph as HTML" button to download the generated network graph in HTML format.
"""
)

st.image("./user_doc_imgs/step 3-2 graph.png")

st.markdown(
"""
## Troubleshooting

If you encounter any issues or have questions, please refer to the troubleshooting section in the [official documentation](#).

## Feedback and Support

For feedback, bug reports, or additional support, please contact us at [ahmadmuhammad@gmail.com](mailto:ahmadmuhammad@gmail.com) or visit my [Linkedin](https://www.linkedin.com/in/ahmadmuhammadgd/).

"""
)