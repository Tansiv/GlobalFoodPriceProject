# 📊 Global Food Price Stability & Inflation Analysis

## 🎯 Project Overview

A comprehensive data analysis of global food prices spanning **26 years (1992-2017)**, covering **74 countries** and **321 food commodities**. This project reveals critical insights about food price inflation, volatility, and affordability worldwide.

## 📁 Project Structure

```
GlobalFoodPriceProject/
├── data/
│   ├── raw/                    # Original dataset
│   └── clean/                  # Cleaned dataset (105MB - not on GitHub)
├── notebooks/
│   ├── 01_data_loading.ipynb   # Phase 1: Data exploration
│   ├── 02_data_cleaning.ipynb  # Phase 2: Data preparation
│   └── 03_eda.ipynb            # Phase 3: Analysis & visualization
├── outputs/
│   ├── charts/                 # 7 interactive HTML visualizations
│   ├── reports/                # Analysis reports
│   └── phase4_reports/         # Final insights & recommendations
└── README.md                   # This file
```

## 🔍 Key Findings

### 1. Extreme Inflation Crisis
- **6,054% price increase** over 25 years
- Average **242% annual inflation** (way above normal!)
- Threatens food affordability globally

### 2. High Price Volatility
- **120 commodities** show extreme price instability (CV > 70%)
- Example: Lamb prices fluctuate **859%**
- Creates budget uncertainty for consumers and farmers

### 3. Geographic Price Disparities
- **185,000x difference** between countries (currency-dependent)
- Colombia: $98,432 avg (COP currency)
- Azerbaijan: $0.53 avg (AZN currency)
- **Note**: Reflects currency units, not real purchasing power

### 4. Seasonal Price Patterns
- **14.5% price variation** between months
- **January**: Lowest prices
- **June**: Highest prices
- **Opportunity**: Time purchases to save 10-15%

### 5. Data Quality Issues
- **16.12%** of records are statistical outliers
- Mixed currency units distort comparisons
- Wholesale/retail pricing inconsistencies

## 📊 Visualizations

This project includes **7 interactive visualizations**:

1. **Global Price Trends** - 25-year inflation analysis
2. **Country Comparison** - Most vs least expensive countries
3. **Commodity Analysis** - Food type price hierarchy
4. **Price Distribution** - Understanding typical price ranges
5. **Seasonal Patterns** - Monthly price variations
6. **Volatility Analysis** - Identifying unstable commodities
7. **Market Comparison** - Retail vs wholesale pricing

**View charts**: Navigate to `outputs/charts/` and open HTML files in browser

## 🚀 How to Run This Project

### Prerequisites
```bash
Python 3.8+
pandas, numpy, matplotlib, seaborn, plotly
```

### Installation
```bash
# Clone repository
git clone https://github.com/Tansiv/GlobalFoodPriceProject.git
cd GlobalFoodPriceProject

# Install dependencies
pip install -r requirements.txt
```

### Run Analysis
```bash
# Phase 1: Load and inspect data
jupyter notebook notebooks/01_data_loading.ipynb

# Phase 2: Clean and prepare data
jupyter notebook notebooks/02_data_cleaning.ipynb

# Phase 3: Exploratory data analysis
jupyter notebook notebooks/03_eda.ipynb
```

## 💡 Key Recommendations

### For Policymakers
- Stabilize prices for 120 volatile commodities
- Establish buffer stocks for critical foods
- Implement farmer price insurance programs

### For Humanitarian Organizations
- **Time procurement in January** (14.5% savings)
- Target high-price, high-volatility countries
- Promote affordable protein alternatives

### For Data Analysts
- **Convert all prices to USD** before analysis
- Filter 16% outliers for cleaner insights
- Validate data entry to prevent future issues

## 📈 Project Phases

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | Data Loading & Inspection | ✅ Complete |
| Phase 2 | Data Cleaning (78.5% memory optimized) | ✅ Complete |
| Phase 3 | EDA with 7 visualizations | ✅ Complete |
| Phase 4 | Insights & Documentation | ✅ Complete |

## 📚 Technologies Used

- **Python 3.11** - Core programming language
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Static visualizations
- **Plotly** - Interactive charts
- **Jupyter Notebook** - Analysis environment

## 🎓 Skills Demonstrated

✅ Data Cleaning (handled 13,949 missing values)  
✅ Memory Optimization (78.5% reduction)  
✅ Statistical Analysis (volatility, distribution, trends)  
✅ Data Visualization (7 professional charts)  
✅ Insight Generation (actionable recommendations)  
✅ Technical Documentation (GitHub-ready)  

## 📊 Dataset Information

**Source**: WFP Global Food Prices Database  
**Records**: 743,895 (after cleaning)  
**Time Period**: January 1992 - June 2017  
**Geography**: 74 countries, 1,449 markets  
**Commodities**: 321 different food types  

**Note**: Cleaned dataset (105MB) not included due to GitHub size limits. Run Phase 2 code to generate it.

## 🤝 Contributing

Suggestions and improvements welcome! Please open an issue or submit a pull request.

## 📧 Contact

**Author**: Tansiv  
**GitHub**: [@Tansiv](https://github.com/Tansiv)  
**Project Link**: [GlobalFoodPriceProject](https://github.com/Tansiv/GlobalFoodPriceProject)

## 📝 License

This project is for educational and portfolio purposes.

---

⭐ **Star this repo** if you found it useful!  
🔗 **Share** to spread awareness about global food price challenges!

