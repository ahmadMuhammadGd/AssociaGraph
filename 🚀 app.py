from modules import streamlit_functions, read_module, apropri, graph
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration and title
st.set_page_config(
    #layout='wide',
    initial_sidebar_state='expanded',
    page_title='AssociaGraph 📊',
    page_icon='📊'
)

st.image("logo2.svg", width=350)
#st.markdown("# **AssociaGraph** (Free)")

# Display logo and app title in the sidebar

# Display warnings and information in the sidebar
st.sidebar.success("Comming Soon: Time series basket analysis 🔲")
st.sidebar.warning("⚠️ This analysis may not be accurate due to other external factors.")
st.sidebar.info("But it's a good start to recognize your customers' behaviors and buying habits. 🛍️")

# Upload the file
uploaded_file = streamlit_functions.upload_file()

# Initialize session state
if 'apropri_state' not in st.session_state:
    st.session_state.apropri_state = False

if 'graph_state' not in st.session_state:
    st.session_state.graph_state = False

# Check if a file was uploaded
if not uploaded_file:
    st.info("Please upload a file.")
else:
    file_name = uploaded_file.name

    # Read the uploaded file
    df = read_module.read_any_table(file_name, uploaded_file)

    # Display success message and uploaded data
    st.success("File uploaded successfully!")
    st.markdown("## Your dataset:")
    st.write(df)
    st.divider()

    # Column selection for order ID and sold products
    st.markdown("## Choose the column containing order ID and sold products")

    col1, col2 = st.columns(2)
    col1.info("Choose the ID and product columns, then press 'Continue' to start executing the algorithm.")

    orderId_col = col2.selectbox(
        'Order ID Column',
        options=df.columns,
    )
    col2.markdown("""
        An order ID is a unique identifier assigned to each individual order placed within a specific system.
        It serves several key functions, such as identifying and tracking individual orders, and facilitates efficient management and organization of order information.
    """)

    product_col = col2.selectbox(
        'Sold Products Column',
        options=df.columns,
    )
    col2.markdown("""
        Sold products refer to items successfully purchased and paid for by customers within a specific order.
    """)

    # Continue button
    if col1.button('Continue'):
        st.session_state.apropri_state = True

    # Execute algorithm if Continue button is clicked
    if st.session_state.apropri_state:
        progress_bar = col1.progress(0)

        # Execute association rules algorithm
        rules = apropri.phrase_rules(
            apropri.asso_rules(df, orderId_col, product_col)
        )
        progress_bar.progress(100)

        # Display success message and association rules
        col1.success("🚀 The algorithm has been executed successfully!")
        st.divider()
        st.markdown('## Association Rules')
        st.table(rules)

        # Download button for association rules CSV
        st.success("Association rules have been successfully calculated.")
        st.download_button(
            "Download Association Rules CSV",
            rules.to_csv(index=False).encode('utf-8'),
            "association_rules.csv",
            "text/csv",
            key='download-csv'
        )

        # Network Graph Section
        st.divider()
        st.markdown('## Network Graph')
        st.info("Please select the weight metric for the network graph.")
        col11, _ = st.columns(2)
        algorithm_elements_list = ['confidence', 'support', 'lift']
        weights = col11.selectbox('', options=algorithm_elements_list)

        # Progress bar for network graph
        progress_bar2 = st.progress(0)

        # Plot network graph
        plot = graph.plot_network(rules, weights=weights)

        # Display network graph and update progress bar
        st.components.v1.html(plot, height=820, scrolling=False)
        progress_bar2.progress(100)

        # Download button for network graph as HTML
        st.download_button(
            label="Download Graph as HTML",
            data=plot,
            file_name="Network.html",
            mime="html"
        )
