# ============================================================
# PHASE 5: PROFESSIONAL STREAMLIT DASHBOARD
# Clean, Modern UI with Excellent Usability
# ============================================================
# File: app/dashboard.py
# Run: streamlit run app/dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Global Food Prices Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CLEAN, PROFESSIONAL CSS
# ============================================================
st.markdown("""
<style>
    /* Clean white background */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Container styling */
    .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Headers */
    h1 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 600;
        padding-bottom: 1rem;
        border-bottom: 3px solid #3b82f6;
    }
    
    h2 {
        color: #1e40af;
        font-weight: 500;
        margin-top: 2rem;
    }
    
    h3 {
        color: #475569;
        font-weight: 500;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #e2e8f0;
    }
    
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #1e40af;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1e3a8a;
    }
    
    [data-testid="stMetricLabel"] {
        color: #64748b;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .stButton>button:hover {
        background-color: #2563eb;
    }
    
    /* Download button */
    .stDownloadButton>button {
        background-color: #10b981;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        width: 100%;
    }
    
    .stDownloadButton>button:hover {
        background-color: #059669;
    }
    
    /* Select boxes */
    .stSelectbox label {
        color: #475569;
        font-weight: 500;
    }
    
    /* Info box */
    .info-card {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .info-card h3 {
        color: #1e40af;
        margin: 0 0 0.5rem 0;
    }
    
    .info-card p {
        color: #475569;
        margin: 0;
        line-height: 1.6;
    }
    
    /* Success box */
    .success-card {
        background-color: #f0fdf4;
        border-left: 4px solid #10b981;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .success-card h3 {
        color: #065f46;
        margin: 0 0 0.5rem 0;
    }
    
    /* Warning box */
    .warning-card {
        background-color: #fffbeb;
        border-left: 4px solid #f59e0b;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .warning-card h3 {
        color: #92400e;
        margin: 0 0 0.5rem 0;
    }
    
    /* Stats box */
    .stats-box {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Radio buttons */
    .stRadio label {
        color: #475569;
        font-weight: 500;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1.5rem;
        background-color: #f1f5f9;
        border-radius: 6px;
        color: #64748b;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
    
    /* Dataframe styling */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Divider */
    hr {
        border: none;
        border-top: 2px solid #e2e8f0;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data(show_spinner=False)
def load_data():
    """Load cleaned dataset with caching"""
    try:
        df = pd.read_csv('data/clean/cleaned_food_prices.csv', parse_dates=['date'])
        return df
    except:
        st.info("📂 Cleaned dataset not found. Using sample data for demonstration.")
        return generate_sample_data()

def generate_sample_data():
    """Generate sample data if actual data not available"""
    np.random.seed(42)
    n = 10000
    
    countries = ['USA', 'India', 'China', 'Brazil', 'Kenya', 'Nigeria', 'Bangladesh', 'Ethiopia']
    commodities = ['Rice', 'Wheat', 'Maize', 'Beans', 'Meat (beef)', 'Milk', 'Eggs', 'Cooking oil']
    
    df = pd.DataFrame({
        'adm0_name': np.random.choice(countries, n),
        'cm_name': np.random.choice(commodities, n),
        'mp_price': np.abs(np.random.normal(100, 50, n)),
        'mp_year': np.random.randint(1992, 2018, n),
        'mp_month': np.random.randint(1, 13, n),
    })
    
    df['date'] = pd.to_datetime(df[['mp_year', 'mp_month']].assign(day=1))
    
    return df

# ============================================================
# MAIN APPLICATION
# ============================================================
def main():
    # Load data
    with st.spinner('📊 Loading data...'):
        df = load_data()
    
    # ============================================================
    # HEADER
    # ============================================================
    st.title("📊 Global Food Prices Analytics Dashboard")
    
    st.markdown("""
    <div class='info-card'>
        <h3>🌾 About This Dashboard</h3>
        <p>Explore comprehensive food price data spanning 26 years across 74 countries and 321 commodities. 
        Analyze trends, compare prices, and gain insights into global food security patterns.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================
    # SIDEBAR FILTERS
    # ============================================================
    with st.sidebar:
        st.header("⚙️ Filter Options")
        
        st.markdown("---")
        
        # Year range
        st.subheader("📅 Time Period")
        year_min, year_max = int(df['mp_year'].min()), int(df['mp_year'].max())
        year_range = st.slider(
            "Select year range:",
            min_value=year_min,
            max_value=year_max,
            value=(year_min, year_max)
        )
        
        # Country filter
        st.subheader("🌍 Geography")
        countries = ['All Countries'] + sorted(df['adm0_name'].unique().tolist())
        selected_country = st.selectbox("Select country:", countries)
        
        # Commodity filter
        st.subheader("🌾 Commodity")
        commodities = ['All Commodities'] + sorted(df['cm_name'].unique().tolist())
        selected_commodity = st.selectbox("Select commodity:", commodities)
        
        st.markdown("---")
        
        # Quick stats
        st.subheader("📈 Dataset Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Records", f"{len(df):,}")
            st.metric("Countries", df['adm0_name'].nunique())
        with col2:
            st.metric("Commodities", df['cm_name'].nunique())
            st.metric("Years", f"{year_max - year_min + 1}")
        
        st.markdown("---")
        
        # Export
        st.subheader("💾 Export")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f'food_prices_{datetime.now().strftime("%Y%m%d")}.csv',
            mime='text/csv'
        )
    
    # ============================================================
    # FILTER DATA
    # ============================================================
    filtered_df = df[
        (df['mp_year'] >= year_range[0]) & 
        (df['mp_year'] <= year_range[1])
    ].copy()
    
    if selected_country != 'All Countries':
        filtered_df = filtered_df[filtered_df['adm0_name'] == selected_country]
    
    if selected_commodity != 'All Commodities':
        filtered_df = filtered_df[filtered_df['cm_name'] == selected_commodity]
    
    # Check if data exists
    if len(filtered_df) == 0:
        st.warning("⚠️ No data available for selected filters. Please adjust your selection.")
        return
    
    # ============================================================
    # KEY METRICS
    # ============================================================
    st.markdown("## 📊 Key Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_price = filtered_df['mp_price'].mean()
        global_avg = df['mp_price'].mean()
        delta = ((avg_price - global_avg) / global_avg * 100)
        st.metric(
            "Average Price",
            f"${avg_price:.2f}",
            f"{delta:+.1f}% vs global"
        )
    
    with col2:
        volatility = filtered_df['mp_price'].std()
        st.metric(
            "Price Volatility",
            f"±${volatility:.2f}",
            "Standard deviation"
        )
    
    with col3:
        records = len(filtered_df)
        st.metric(
            "Data Points",
            f"{records:,}",
            f"{(records/len(df)*100):.1f}% of total"
        )
    
    with col4:
        if len(filtered_df[filtered_df['mp_year']==year_range[0]]) > 0 and len(filtered_df[filtered_df['mp_year']==year_range[1]]) > 0:
            start_price = filtered_df[filtered_df['mp_year']==year_range[0]]['mp_price'].mean()
            end_price = filtered_df[filtered_df['mp_year']==year_range[1]]['mp_price'].mean()
            price_change = ((end_price - start_price) / start_price * 100)
            st.metric(
                "Period Change",
                f"{price_change:+.1f}%",
                f"{year_range[0]} to {year_range[1]}"
            )
        else:
            st.metric("Period Change", "N/A", "Insufficient data")
    
    st.markdown("---")
    
    # ============================================================
    # ANALYSIS TABS
    # ============================================================
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "🔬 Deep Dive", "🔄 Compare", "🔮 Forecast"])
    
    with tab1:
        show_overview(filtered_df)
    
    with tab2:
        show_deep_dive(filtered_df)
    
    with tab3:
        show_comparison(df, year_range)
    
    with tab4:
        show_forecast(filtered_df)

# ============================================================
# OVERVIEW TAB
# ============================================================
def show_overview(df):
    st.markdown("### Price Trends Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Yearly trend
        yearly_avg = df.groupby('mp_year')['mp_price'].mean().reset_index()
        
        fig = px.line(
            yearly_avg,
            x='mp_year',
            y='mp_price',
            title="Average Price Over Time",
            labels={'mp_year': 'Year', 'mp_price': 'Average Price ($)'}
        )
        
        fig.update_traces(line_color='#3b82f6', line_width=3)
        fig.update_layout(
            template="simple_white",
            height=400,
            title_font_size=16,
            title_font_color='#1e40af'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Distribution
        fig = px.histogram(
            df,
            x='mp_price',
            nbins=40,
            title="Price Distribution",
            labels={'mp_price': 'Price ($)', 'count': 'Frequency'}
        )
        
        fig.update_traces(marker_color='#3b82f6')
        fig.update_layout(
            template="simple_white",
            height=400,
            title_font_size=16,
            title_font_color='#1e40af'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Seasonality
    st.markdown("### Seasonal Patterns")
    
    monthly_avg = df.groupby('mp_month')['mp_price'].mean().reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_avg['month_name'] = [month_names[m-1] for m in monthly_avg['mp_month']]
    
    fig = px.bar(
        monthly_avg,
        x='month_name',
        y='mp_price',
        title="Average Prices by Month",
        labels={'month_name': 'Month', 'mp_price': 'Average Price ($)'}
    )
    
    fig.update_traces(marker_color='#3b82f6')
    fig.update_layout(
        template="simple_white",
        height=400,
        title_font_size=16,
        title_font_color='#1e40af'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Insights
    max_month = monthly_avg.loc[monthly_avg['mp_price'].idxmax(), 'month_name']
    min_month = monthly_avg.loc[monthly_avg['mp_price'].idxmin(), 'month_name']
    variation = ((monthly_avg['mp_price'].max() - monthly_avg['mp_price'].min()) / 
                 monthly_avg['mp_price'].min() * 100)
    
    st.markdown(f"""
    <div class='success-card'>
        <h3>💡 Key Insights</h3>
        <ul>
            <li><strong>Highest prices:</strong> {max_month} - Consider avoiding procurement during this period</li>
            <li><strong>Lowest prices:</strong> {min_month} - Optimal time for bulk purchasing</li>
            <li><strong>Seasonal variation:</strong> {variation:.1f}% - {"Significant" if variation > 15 else "Moderate"} price fluctuation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# DEEP DIVE TAB
# ============================================================
def show_deep_dive(df):
    st.markdown("### Statistical Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='stats-box'>", unsafe_allow_html=True)
        st.markdown("**Central Tendency**")
        st.write(f"Mean: ${df['mp_price'].mean():.2f}")
        st.write(f"Median: ${df['mp_price'].median():.2f}")
        if len(df['mp_price'].mode()) > 0:
            st.write(f"Mode: ${df['mp_price'].mode().iloc[0]:.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='stats-box'>", unsafe_allow_html=True)
        st.markdown("**Dispersion**")
        st.write(f"Std Dev: ${df['mp_price'].std():.2f}")
        st.write(f"Variance: ${df['mp_price'].var():.2f}")
        st.write(f"IQR: ${df['mp_price'].quantile(0.75) - df['mp_price'].quantile(0.25):.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='stats-box'>", unsafe_allow_html=True)
        st.markdown("**Range**")
        st.write(f"Min: ${df['mp_price'].min():.2f}")
        st.write(f"Max: ${df['mp_price'].max():.2f}")
        st.write(f"Range: ${df['mp_price'].max() - df['mp_price'].min():.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Box plot
    st.markdown("### Distribution with Outliers")
    
    fig = px.box(
        df,
        y='mp_price',
        title="Price Distribution Box Plot",
        labels={'mp_price': 'Price ($)'}
    )
    
    fig.update_traces(marker_color='#3b82f6', line_color='#1e40af')
    fig.update_layout(
        template="simple_white",
        height=400,
        title_font_size=16,
        title_font_color='#1e40af'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Volatility
    st.markdown("### Volatility Assessment")
    
    cv = (df['mp_price'].std() / df['mp_price'].mean()) * 100
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Coefficient of Variation", f"{cv:.2f}%")
    
    with col2:
        if cv < 30:
            st.success("✅ **Low Volatility** - Prices are stable and predictable")
        elif cv < 70:
            st.info("ℹ️ **Moderate Volatility** - Some price fluctuation observed")
        else:
            st.warning("⚠️ **High Volatility** - Significant price instability")

# ============================================================
# COMPARISON TAB
# ============================================================
def show_comparison(df, year_range):
    st.markdown("### Comparative Analysis")
    
    compare_type = st.radio(
        "Compare by:",
        ["Countries", "Commodities"],
        horizontal=True
    )
    
    df_filtered = df[(df['mp_year'] >= year_range[0]) & (df['mp_year'] <= year_range[1])]
    
    if compare_type == "Countries":
        all_items = sorted(df_filtered['adm0_name'].unique().tolist())
        column_name = 'adm0_name'
        label = 'Country'
    else:
        all_items = sorted(df_filtered['cm_name'].unique().tolist())
        column_name = 'cm_name'
        label = 'Commodity'
    
    selected_items = st.multiselect(
        f"Select {label.lower()}s to compare (up to 5):",
        all_items,
        default=all_items[:min(3, len(all_items))],
        max_selections=5
    )
    
    if selected_items:
        comparison_df = df_filtered[df_filtered[column_name].isin(selected_items)]
        yearly_comparison = comparison_df.groupby(['mp_year', column_name])['mp_price'].mean().reset_index()
        
        fig = px.line(
            yearly_comparison,
            x='mp_year',
            y='mp_price',
            color=column_name,
            title=f"{label} Price Comparison Over Time",
            labels={'mp_year': 'Year', 'mp_price': 'Average Price ($)', column_name: label}
        )
        
        fig.update_layout(
            template="simple_white",
            height=500,
            title_font_size=16,
            title_font_color='#1e40af',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Comparison table
        st.markdown("### Comparison Statistics")
        
        comparison_stats = comparison_df.groupby(column_name).agg({
            'mp_price': ['mean', 'median', 'std', 'min', 'max']
        }).round(2)
        
        comparison_stats.columns = ['Average', 'Median', 'Std Dev', 'Min', 'Max']
        comparison_stats = comparison_stats.reset_index()
        
        st.dataframe(comparison_stats, use_container_width=True, hide_index=True)

# ============================================================
# FORECAST TAB
# ============================================================
def show_forecast(df):
    st.markdown("### Price Forecasting")
    
    st.markdown("""
    <div class='warning-card'>
        <h3>⚠️ Important Note</h3>
        <p>This forecast uses simple linear regression for demonstration. 
        For production use, consider advanced time series models (ARIMA, Prophet, LSTM).</p>
    </div>
    """, unsafe_allow_html=True)
    
    yearly_avg = df.groupby('mp_year')['mp_price'].mean().reset_index()
    
    if len(yearly_avg) < 3:
        st.warning("Insufficient data for forecasting. Need at least 3 years of data.")
        return
    
    # Simple linear regression
    from sklearn.linear_model import LinearRegression
    
    X = yearly_avg['mp_year'].values.reshape(-1, 1)
    y = yearly_avg['mp_price'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Forecast next 3 years
    last_year = yearly_avg['mp_year'].max()
    future_years = np.array([last_year + i for i in range(1, 4)]).reshape(-1, 1)
    forecast = model.predict(future_years)
    
    # Visualization
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=yearly_avg['mp_year'],
        y=yearly_avg['mp_price'],
        mode='lines+markers',
        name='Historical Data',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=future_years.flatten(),
        y=forecast,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#10b981', width=3, dash='dash'),
        marker=dict(size=10, symbol='star')
    ))
    
    fig.update_layout(
        title="3-Year Price Forecast",
        xaxis_title="Year",
        yaxis_title="Price ($)",
        template="simple_white",
        height=500,
        title_font_size=16,
        title_font_color='#1e40af',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Forecast values
    st.markdown("### Projected Prices")
    
    cols = st.columns(3)
    for i, (year, price) in enumerate(zip(future_years.flatten(), forecast)):
        with cols[i]:
            delta = ((price - yearly_avg['mp_price'].iloc[-1]) / yearly_avg['mp_price'].iloc[-1] * 100)
            st.metric(
                f"Year {int(year)}",
                f"${price:.2f}",
                f"{delta:+.1f}%"
            )

# ============================================================
# FOOTER
# ============================================================
def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #64748b; padding: 2rem 0;'>
        <p><strong>Global Food Prices Analytics Dashboard</strong></p>
        <p>Data Source: WFP Global Food Prices Database | Built with Streamlit</p>
        <p>
            <a href='https://github.com/Tansiv/GlobalFoodPriceProject' target='_blank' style='color: #3b82f6; text-decoration: none;'>
                View on GitHub
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RUN APPLICATION
# ============================================================
if __name__ == "__main__":
    main()
    show_footer()