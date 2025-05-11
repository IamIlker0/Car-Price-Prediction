import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
import time
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Car Price Prediction & Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .dashboard-main-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: white;
        background-color: #084272;
        padding: 8px 15px;
        border-radius: 5px;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #003366;
    }
    .dashboard-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.3s;
        cursor: pointer;
        background-color: #1E2A38;
        color: white;
    }
    .dashboard-card:hover {
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

# Load the dataset (at the beginning)
@st.cache_data
def load_car_data():
    try:
        return pd.read_csv('streamlit/cleaned_car_price_data.csv')
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

car_data = load_car_data()

# Define dashboard embed codes (as it was missing)
dashboard_embed_codes = {
    "Price by Fuel & Brand": """
    <div style='border-radius: 10px; overflow: hidden; padding: 10px; background-color: #f0f0f0; margin: 0 auto; width: 95%; max-width: 2000px;'>
        <div style='background-color: #4b3f72; color: #ffd166; padding: 8px; margin-bottom: 10px; border-radius: 8px; text-align: center; font-weight: bold; max-width: 600px; margin-left: auto; margin-right: auto;'>
            For better viewing please use the full screen button in the bottom right corner.
        </div>
        <div class='tableauPlaceholder' id='viz1740883581426' style='position: relative; width: 100%; height: 75vh;'>
            <noscript>
                <a href='#'>
                <img alt='Price - Brand and Fuel_Type ' 
                    src='https://public.tableau.com/static/images/Pr/Price-brandfuel_type/Price-BrandandFuel_Type/1_rss.png' 
                    style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Price-brandfuel_type/Price-BrandandFuel_Type' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/Pr/Price-brandfuel_type/Price-BrandandFuel_Type/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1740883581426');
            var vizElement = divElement.getElementsByTagName('object')[0];
            
            // Setting dimensions for better viewing
            vizElement.style.width = '100%';
            vizElement.style.height = '75vh'; // 75% of screen height
            
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    </div>
    """,
    "Model Price Analysis": """
    <div style='border-radius: 10px; overflow: hidden; padding: 10px; background-color: #f0f0f0; margin: 0 auto; width: 95%; max-width: 1200px;'>
        <div style='background-color: #4b3f72; color: #ffd166; padding: 8px; margin-bottom: 10px; border-radius: 8px; text-align: center; font-weight: bold; max-width: 600px; margin-left: auto; margin-right: auto;'>
            For better viewing please use the full screen button in the bottom right corner.
        </div>
        <div class='tableauPlaceholder' id='viz1740884092931' style='position: relative'>
        <noscript>
            <a href='#'>
            <img alt='brand&amp;model&amp;Transmission-fuel_type&amp;transmission '
                src='https://public.tableau.com/static/images/br/brandmodelTransmission-fuel_typetransmission/brandmodelTransmission-fuel_typetransmission/1_rss.png'
                style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='brandmodelTransmission-fuel_typetransmission/brandmodelTransmission-fuel_typetransmission' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/br/brandmodelTransmission-fuel_typetransmission/brandmodelTransmission-fuel_typetransmission/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
            <param name='filter' value='publish=yes' />
        </object>
        </div>
        <script type='text/javascript'>
        var divElement = document.getElementById('viz1740884092931');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
        } else {
            vizElement.style.width = '100%';
            vizElement.style.height = '1027px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>    </div>
    """,
    "Engine Specs Heatmap": """
    <div style='border-radius: 10px; overflow: hidden; padding: 10px; background-color: #f0f0f0; margin: 0 auto; width: 95%; max-width: 1200px;'>
        <div style='background-color: #4b3f72; color: #ffd166; padding: 8px; margin-bottom: 10px; border-radius: 8px; text-align: center; font-weight: bold; max-width: 600px; margin-left: auto; margin-right: auto;'>
            For better viewing please use the full screen button in the bottom right corner.
        </div>
        <div class='tableauPlaceholder' id='viz1740888006297' style='position: relative'>
        <noscript>
            <a href='#'>
            <img alt='Engine_Size%BrandModal-Fuel_typeTransmission '
                src='https://public.tableau.com/static/images/En/Engine_Size-BrandModalFuel_typeTransmission/Engine_SizeBrandModal-Fuel_typeTransmission/1_rss.png'
                style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='Engine_Size-BrandModalFuel_typeTransmission/Engine_SizeBrandModal-Fuel_typeTransmission' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/En/Engine_Size-BrandModalFuel_typeTransmission/Engine_SizeBrandModal-Fuel_typeTransmission/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
        </div>
        <script type='text/javascript'>
        var divElement = document.getElementById('viz1740888006297');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.width = '100%';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
        } else {
            vizElement.style.width = '100%';
            vizElement.style.height = '727px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>    </div>
    """,
    "Best Features Plot": """
    <div style='border-radius: 10px; overflow: hidden; padding: 10px; background-color: #f0f0f0; margin: 0 auto; width: 95%; max-width: 1200px;'>
        <div style='background-color: #4b3f72; color: #ffd166; padding: 8px; margin-bottom: 10px; border-radius: 8px; text-align: center; font-weight: bold; max-width: 600px; margin-left: auto; margin-right: auto;'>
            For better viewing please use the full screen button in the bottom right corner.
        </div>
        <div class='tableauPlaceholder' id='viz1740888120969' style='position: relative'>
            <noscript>
                <a href='#'>
                <img alt='Best_Feature_plot '
                    src='https://public.tableau.com/static/images/Be/Best_Feature_Plot/Best_Feature_plot/1_rss.png'
                    style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Best_Feature_Plot/Best_Feature_plot' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/Be/Best_Feature_Plot/Best_Feature_plot/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
            </div>
            <script type='text/javascript'>
            var divElement = document.getElementById('viz1740888120969');
            var vizElement = divElement.getElementsByTagName('object')[0];
            if (divElement.offsetWidth > 800) {
                vizElement.style.width = '100%';
                vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
            } else if (divElement.offsetWidth > 500) {
                vizElement.style.width = '100%';
                vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
            } else {
                vizElement.style.width = '100%';
                vizElement.style.height = '727px';
            }
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
            </script>
    </div>
    """
}

# Load ML model
@st.cache_resource
def load_model():
    try:
        with open('streamlit/car_price_model.pkl', 'rb') as f:
            model_info = pickle.load(f)
        return model_info
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_info = load_model()
model_loaded = model_info is not None

if model_loaded:
    model = model_info['model']
    selected_features = model_info['features']
    r2_score_val = model_info.get('r2_score', 0.94)

# Main title and description
st.markdown('<h1 class="main-header">🚗 Car Price Prediction & Analysis</h1>', unsafe_allow_html=True)

# Show model diagnostic information (optional - can be helpful during development)
with st.expander("Model Diagnostic Information", expanded=False):
    try:
        st.success("Model loaded successfully!")
        
        st.write("Model information:")
        st.write("- Model type:", type(model_info['model']))
        st.write("- Features used:", model_info['features'])
        st.write("- R² score:", model_info.get('r2_score', "Not specified"))
        
        test_data = {
            'Year': 2015,
            'Engine_Size': 2.0,
            'Mileage': 50000,
            'Fuel_Type_Electric': 0,
            'Transmission_Manual': 0
        }
        test_df = pd.DataFrame([test_data])
        
        st.write("Test data:", test_data)
        
        try:
            test_prediction = model_info['model'].predict(test_df)[0]
            abs_prediction = abs(test_prediction)
            st.write("Original test prediction:", test_prediction)
            st.write("Adjusted test prediction (absolute value):", abs_prediction)
        except Exception as predict_error:
            st.error(f"Could not make test prediction: {predict_error}")
        
    except Exception as e:
        st.error(f"Error loading model: {e}")

# Navigation with tabs
tab1 = st.tabs(["📊 Analysis Dashboards"])[0]

# Tab 1: Analysis Dashboards
with tab1:
    st.markdown('<div class="dashboard-main-title">Car Data Analysis Dashboards</div>', unsafe_allow_html=True)
    loading_message = st.empty()
    
    # Dashboard selection with cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.subheader("Price by Fuel & Brand")
        st.image("streamlit/images/Price - Brand and Fuel_Type.png", output_format="PNG", width=None)
        dashboard_choice1 = st.button("View Dashboard", key="db1", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.subheader("Engine Specs Heatmap")
        st.image("streamlit/images/Engine_Size%BrandModal-Fuel_typeTransmission.png", output_format="PNG", width=None)
        dashboard_choice3 = st.button("View Dashboard", key="db3", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.subheader("Model Price Analysis")
        st.image("streamlit/images/brand&model-fuel_type&transmission-brand&transmission.png", output_format="PNG", width=None)
        dashboard_choice2 = st.button("View Dashboard", key="db2", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.subheader("Best Features Plot")
        st.image("streamlit/images/Best_Feature_Plot.png", output_format="PNG", width=None)
        dashboard_choice4 = st.button("View Dashboard", key="db4", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Dashboard display section
    dashboard_displayed = False
    
    if dashboard_choice1 or dashboard_choice2 or dashboard_choice3 or dashboard_choice4:
        loading_message.success("Dashboard is loading. You can view it by scrolling down.")
        dashboard_displayed = True
        st.markdown('<div id="dashboard-view" class="dashboard-view"></div>', unsafe_allow_html=True)
        st.info("💡 **Please make it full screen for better viewing.**")
        
        if dashboard_choice1:
            st.markdown("### Price by Fuel & Brand Dashboard")
            components.html(dashboard_embed_codes["Price by Fuel & Brand"], height=800, scrolling=True)
        elif dashboard_choice2:
            st.markdown("### Model Price Analysis Dashboard")
            components.html(dashboard_embed_codes["Model Price Analysis"], height=800, scrolling=True)
        elif dashboard_choice3:
            st.markdown("### Engine Specs Heatmap Dashboard")
            components.html(dashboard_embed_codes["Engine Specs Heatmap"], height=800, scrolling=True)
        elif dashboard_choice4:
            st.markdown("### Best Features Plot Dashboard")
            components.html(dashboard_embed_codes["Best Features Plot"], height=800, scrolling=True)
    
    if not dashboard_displayed:
        st.info("👆 Select a dashboard above or click on the 'Price Prediction' tab to use our ML model.")


st.sidebar.title("About This Project")
st.sidebar.info("""
This application provides car price prediction using machine learning and data analysis tools.

**Features:**
- 4 interactive dashboards
- AI-powered price prediction
- What-if scenario analysis
- Market trend visualization

**Model Information:**
- Algorithm: Ridge Regression
- Training data: 10,000+ vehicle records
- Accuracy (R²): 0.94
""")

st.sidebar.title("Creator")
st.sidebar.markdown("Developer: Ilker Aydin Yilmaz")
st.sidebar.markdown("[GitHub Repository](https://github.com/IamIlker0/car-price-prediction)")




