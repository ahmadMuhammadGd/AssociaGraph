import streamlit as st
from pyvis.network import Network


def plot_network(df, weights = 'confidence'):
    net = Network(  
        height='800px',
        width='100%',
        bgcolor='#222222',
        font_color='white',
        directed=True
        )

    
    net.barnes_hut(
            gravity=-80000,
            central_gravity=1.5,
            spring_length=250,
            spring_strength=0.001,
            damping=0.5,
            overlap=0
            )
    
    # Add nodes and edges to the network
    for _, row in df.iterrows():
        net.add_node(row['antecedents'], label=row['antecedents'], title=row['antecedents'])
        net.add_node(row['consequents'], label=row['consequents'], title=row['consequents'])
        net.add_edge(row['antecedents'], row['consequents'], title=f"Support: {row['support']}, Confidence: {row['confidence']}, Lift: {row['lift']}", value=row[weights])


    html = net.generate_html("node.html")
    return html