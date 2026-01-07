# 📊 Global Food Price Stability & Inflation Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

> A comprehensive data analytics project analyzing 26 years of global food prices (1992-2017) across 74 countries and 321 commodities, featuring an interactive web dashboard for real-time insights.

## 🌟 Live Demo

**🚀 [Try the Dashboard](https://your-streamlit-app-url.streamlit.app)** *(Deploy to get URL)*

## 📸 Dashboard Preview

*Interactive dashboard featuring price trends, statistical analysis, and forecasting capabilities*

## 🎯 Project Overview

This project delivers end-to-end data analysis of global food prices, revealing:

- **6,054% inflation** over 25 years
- **120 commodities** with extreme volatility
- **14.5% seasonal variation** (January cheapest, June most expensive)
- Geographic price disparities across 74 countries
- Actionable insights for procurement and policy decisions

## 📁 Project Structure

```
GlobalFoodPriceProject/
├── app/
│   └── dashboard.py              # Streamlit web application
├── data/
│   ├── raw/                      # Original dataset
│   └── clean/                    # Cleaned dataset (not on GitHub - 105MB)
├── notebooks/
│   ├── 01_data_loading.ipynb     # Phase 1: Data exploration
│   ├── 02_data_cleaning.ipynb    # Phase 2: Data preparation
│   ├── 03_eda.ipynb              # Phase 3: Exploratory analysis
│   └── 04_insights.ipynb         # Phase 4: Insights generation
├── outputs/
│   ├── charts/                   # 7 interactive HTML visualizations
│   ├── reports/                  # Analysis reports
│   └── phase4_reports/           # Executive summaries
├── requirements.txt              # Project dependencies
└── README.md                     # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Tansiv/GlobalFoodPriceProject.git
cd GlobalFoodPriceProject

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app/dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Dependencies

```
pandas>=2.1.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
streamlit>=1.28.0
scikit-learn>=1.3.0
```

## 📊 Features

### Interactive Dashboard

- **🎛️ Dynamic Filters**: Year range, country, commodity selection
- **📈 4 Analysis Modes**:
  - **Overview**: Price trends, distribution, seasonality
  - **Deep Dive**: Statistical analysis, volatility metrics
  - **Compare**: Multi-country/commodity comparison
  - **Forecast**: 3-year price predictions
- **💾 Data Export**: Download filtered data as CSV
- **📱 Responsive Design**: Works on desktop, tablet, and mobile

### Analysis Capabilities

| Feature | Description |
|---------|-------------|
| **Trend Analysis** | 25-year price evolution tracking |
| **Statistical Insights** | Mean, median, standard deviation, CV |
| **Seasonal Patterns** | Monthly price variation analysis |
| **Volatility Assessment** | Risk evaluation via coefficient of variation |
| **Comparative Analysis** | Side-by-side country/commodity comparison |
| **Forecasting** | Linear regression-based predictions |

## 🔍 Key Findings

### 1. 🚨 Severe Inflation Crisis
- Food prices increased **6,054%** over 25 years
- Average annual inflation: **242%** (far exceeding normal 2-3%)
- Threatens global food affordability

### 2. 📊 High Price Volatility
- **120 commodities** show extreme instability (CV > 70%)
- Example: Lamb prices fluctuate **859%**
- Creates budget uncertainty for consumers and farmers

### 3. 🌍 Geographic Disparities
- **185,000x price difference** between countries
- Note: Reflects currency units, not purchasing power
- Colombia: $98,432 avg | Azerbaijan: $0.53 avg

### 4. 📅 Seasonal Opportunities
- **14.5% price variation** between months
- **January**: Lowest prices (optimal for procurement)
- **June**: Highest prices (avoid bulk purchases)
- Potential savings: **10-15%** through timing

### 5. 📉 Data Quality Issues
- **16.12%** of records are outliers
- Mixed currency units distort comparisons
- Recommendation: Standardize to USD

## 💡 Recommendations

### For Policymakers
- ✅ Stabilize prices for 120 volatile commodities
- ✅ Establish buffer stocks for critical foods
- ✅ Implement farmer price insurance programs
- ✅ Create early warning systems for price spikes

### For Humanitarian Organizations
- ✅ Time procurement in January (14.5% savings)
- ✅ Target high-price, high-volatility countries
- ✅ Promote affordable protein alternatives
- ✅ Monitor seasonal patterns for cost optimization

### For Data Analysts
- ✅ Convert all prices to USD before analysis
- ✅ Filter 16% outliers for cleaner insights
- ✅ Analyze countries separately (currency issues)
- ✅ Implement robust data validation rules

## 📈 Project Phases

| Phase | Description | Status | Key Deliverables |
|-------|-------------|--------|------------------|
| **Phase 1** | Data Loading & Inspection | ✅ Complete | Dataset overview, quality assessment |
| **Phase 2** | Data Cleaning & Preprocessing | ✅ Complete | 743,895 clean records, 78.5% memory optimized |
| **Phase 3** | Exploratory Data Analysis | ✅ Complete | 7 interactive visualizations, insights reports |
| **Phase 4** | Insights & Documentation | ✅ Complete | Executive summary, recommendations |
| **Phase 5** | Interactive Dashboard | ✅ Complete | Streamlit web app with 4 analysis modes |

## 📚 Technologies Used

### Data Analysis
- **Python 3.11** - Core programming
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **scikit-learn** - Machine learning (forecasting)

### Visualization
- **Matplotlib** - Static charts
- **Seaborn** - Statistical visualizations
- **Plotly** - Interactive charts
- **Streamlit** - Web dashboard

### Development
- **Jupyter Notebook** - Analysis environment
- **Git/GitHub** - Version control
- **VS Code** - Code editor

## 🎓 Skills Demonstrated

### Technical Skills
✅ Data Cleaning (13,949 missing values handled)  
✅ Memory Optimization (78.5% reduction)  
✅ Statistical Analysis (volatility, trends, distributions)  
✅ Data Visualization (12+ professional charts)  
✅ Web Development (Interactive dashboard)  
✅ Machine Learning (Forecasting models)  

### Business Skills
✅ Insight Generation (Top 10 strategic insights)  
✅ Stakeholder Communication (Executive summaries)  
✅ Problem Solving (Data quality issues)  
✅ Project Management (5-phase structured approach)  
✅ Documentation (Technical & business reports)  

## 📊 Dataset Information

**Source**: [WFP Global Food Prices Database](https://www.kaggle.com/datasets/jboysen/global-food-prices)

| Metric | Value |
|--------|-------|
| **Records** | 743,895 (after cleaning) |
| **Time Period** | January 1992 - June 2017 (26 years) |
| **Countries** | 74 |
| **Regions** | 589 |
| **Markets** | 1,449 |
| **Commodities** | 321 different food types |
| **Currencies** | 61 |

**Note**: Cleaned dataset (105MB) excluded from repository due to GitHub size limits. Run Phase 2 notebook to generate.

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free!)

1. **Fork this repository** on GitHub

2. **Go to** [share.streamlit.io](https://share.streamlit.io)

3. **Sign in** with GitHub

4. **New app** → Select your repository

5. **Configure**:
   - Main file: `app/dashboard.py`
   - Python version: 3.11

6. **Deploy** → Get your public URL!

Your dashboard will be live at: `https://[your-app-name].streamlit.app`

### Local Deployment

```bash
# Install Streamlit
pip install streamlit

# Run dashboard
streamlit run app/dashboard.py

# Access at http://localhost:8501
```

## 📖 Documentation

- **[Executive Summary](outputs/reports/executive_summary.txt)** - 1-page overview
- **[Comprehensive Report](outputs/reports/02_comprehensive_analysis_report.txt)** - Detailed findings
- **[Phase 3 Charts](outputs/charts/)** - 7 interactive visualizations
- **[Notebooks](notebooks/)** - Complete analysis code

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Author**: Tansiv  
**GitHub**: [@Tansiv](https://github.com/Tansiv)  
**Project Link**: [GlobalFoodPriceProject](https://github.com/Tansiv/GlobalFoodPriceProject)

## 📝 License

This project is for educational and portfolio purposes.

## 🙏 Acknowledgments

- **Data Source**: [World Food Programme](https://www.wfp.org/)
- **Dataset**: [Kaggle - Global Food Prices](https://www.kaggle.com/datasets/jboysen/global-food-prices)
- **Libraries**: Pandas, Plotly, Streamlit, scikit-learn

## 📈 Project Stats

![GitHub last commit](https://img.shields.io/github/last-commit/Tansiv/GlobalFoodPriceProject)
![GitHub repo size](https://img.shields.io/github/repo-size/Tansiv/GlobalFoodPriceProject)
![GitHub language count](https://img.shields.io/github/languages/count/Tansiv/GlobalFoodPriceProject)

---

⭐ **Star this repository** if you found it useful!  
🔗 **Share** to raise awareness about global food price challenges!  
💼 **Connect** for collaboration opportunities!

**Made with ❤️ for data science and social impact**