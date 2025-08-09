<p align="center">
  <img src="visuals/logo.jpeg" alt="Vendor Performance Analysis" width="800"/>
</p>

# Vendor Performance Analysis: Optimizing Vendor & Inventory Strategies

<details open>
<summary><strong><span style="font-size: 1.25em;">Executive Summary and Overview</span></strong></summary>

This project focuses on **optimizing vendor performance and inventory management** to reduce costs, improve supply chain resilience, and enhance profitability.  

Using a combination of **Power BI**, **Python**, and **SQL**, raw CSV data was transformed into a unified vendor performance dataset, enriched with **statistical analysis** and **business intelligence dashboards**. The final output is a set of **actionable strategies** that address vendor dependency, pricing inefficiencies, bulk purchase benefits, and inventory turnover.  

Stakeholders gain access to a **live, interactive Power BI dashboard** enabling them to explore vendor metrics, brand performance, and purchasing trends in real time.

</details>

---

## Table of Contents

- [Business Context & Objectives](#business-context--objectives)
- [Project Workflow Overview](#project-workflow-overview)
- [Tools & Technologies](#tools--technologies)
- [Data Preparation & Processing](#data-preparation--processing)
- [Statistical Analysis & Visualizations](#statistical-analysis--visualizations)
- [General Findings](#general-findings)
- [Strategic Findings](#strategic-findings)
- [Recommendations](#recommendations)
- [Technical Execution Details](#technical-execution-details)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

---

<details>
<summary id="business-context--objectives"><strong>Business Context & Objectives</strong></summary>

Vendor and inventory performance directly influence **profitability**, **cash flow**, and **supply chain stability**.  

The **core business challenge**:  
> How to **optimize vendor relationships** and **streamline inventory management** for cost reduction and operational efficiency.

**Key Objectives:**
- Identify top- and low-performing vendors.
- Detect pricing inefficiencies and vendor dependency risks.
- Improve inventory turnover and reduce slow-moving stock.
- Validate findings using statistical hypothesis testing.

</details>

---

<details>
<summary id="project-workflow-overview"><strong>Project Workflow Overview</strong></summary>

**Workflow Pipeline:**
CSV Files → SQLite Database → Aggregated Vendor Table → Analysis & Dashboard → Insights & Recommendations

**Phases:**
- **Phase 1 – Exploratory_Data_Analysis.ipynb**  
  Data ingestion, database setup, aggregated table creation, logging.
- **Phase 2 – Vendor_Performance_Analysis.ipynb**  
  Statistical analysis, answering business questions, creating visualizations, and generating actionable insights.

![Workflow Diagram](assets/workflow_diagram.png)

</details>

---

<details>
<summary id="tools--technologies"><strong>Tools & Technologies</strong></summary>

| Category | Tools / Languages |
|----------|-------------------|
| **Business Intelligence** | Power BI, DAX, M Language |
| **Python Libraries** | pandas, numpy, matplotlib, seaborn, sqlite3, SQLAlchemy ORM |
| **Database** | SQLite |
| **SQL Features Used** | JOIN, WHERE, GROUP BY, ORDER BY, subqueries, CTEs, table creation |
| **Statistics** | Descriptive statistics, IQR, percentiles, quantile discretization, cumulative sum, confidence intervals, hypothesis testing, significance testing, t-test |
| **IDE / Environment** | Jupyter Notebook |

</details>

---

<details>
<summary id="data-preparation--processing"><strong>Data Preparation & Processing</strong></summary>

**Manager Summary:**  
Data was cleaned, standardized, and merged into a single vendor performance dataset for accurate analysis. This dataset powered a **live interactive Power BI dashboard** for real-time vendor and inventory insights.

**Technical Details:**
- **Scripts:**
  1. `ingestion_db.py` – Uploads CSV files into SQLite, supports large files, logs ingestion progress/errors.
  2. `get_vendor_summary.py` – Runs SQL aggregations, cleans/enriches data, calculates KPIs, uploads summary table to database, logs process.

- **Logging:**
  - `log/logging.log` → Tracks CSV ingestion.
  - `log/get_vendor_summary.log` → Tracks vendor summary creation & upload.

- **SQL Used:** JOIN, GROUP BY, CTEs, subqueries, filtering.

- **Python (pandas):** New columns, type conversions, lambda/custom functions, missing value handling.

- **Power BI:**
  - Loaded **`vendor_sales_summary`** table from SQLite.
  - Created **calculated tables** for analysis:
    1. **BrandPerformance** – AvgProfitMargin, TargetBrands, TotalSales  
    2. **LowTurnoverVendors** – AvgStockTurnover, VendorName  
    3. **PurchaseContribution** – PurchaseContribution%, TotalPurchaseDollars, VendorName  
  - Added **calculated columns** in DAX for improved filtering and metrics.
  - Built **live dashboard** with filters, slicers, and drill-down capabilities.  
  - Example View:  
    ![Dashboard Screenshot](assets/dashboard_sample.png)

</details>

---

<details>
<summary id="statistical-analysis--visualizations"><strong>Statistical Analysis & Visualizations</strong></summary>

**Statistics Applied:**
- Descriptive stats (max, min, mean, std, quartiles)
- Outlier detection (IQR)
- Correlation analysis
- Hypothesis testing (t-test, confidence intervals)
- Quantile-based discretization

**Visualizations:**
- Histograms (KDE)
- Boxplots
- Pie & donut charts
- Horizontal bar charts
- Scatterplots
- Heatmaps (correlation)
- KDE plots

</details>

---

<details>
<summary id="general-findings"><strong>General Findings</strong></summary>

- Loss-making transactions due to high costs or zero revenue.
- Outliers:  
  - Purchase Price max = 5,681.81 vs mean = 24.39  
  - Freight Cost range = 0.09 to 257,032.07  
- Strong correlation between purchase quantity and sales quantity (0.999).
- Weak correlation between purchase price and gross profit (–0.016).

![General Findings Chart](assets/general_findings_chart.png)

</details>

---

<details>
<summary id="strategic-findings"><strong>Strategic Findings</strong></summary>

- **High-Margin, Low-Sales Brands:** 198 brands show high profitability but low sales volume.  
- **Vendor Dependency:** Top 10 vendors = 65.69% of purchases.  
- **Bulk Purchase Benefits:** 72% lower unit cost for large orders.  
- **Slow-Moving Inventory:** $2.71M tied up in low-turnover stock.  
- **Profit Margin Models:** Low-performing vendors have higher margins but lower sales.  
- **Statistical Validation:** Significant profit margin difference between top & low vendors.

![Strategic Findings Chart](assets/strategic_findings_chart.png)

</details>

---

<details>
<summary id="recommendations"><strong>Recommendations</strong></summary>

1. Re-evaluate pricing for high-margin, low-sales brands.
2. Optimize slow-moving stock with refined purchasing and clearance promotions.
3. Support low-performing vendors with targeted marketing and expanded distribution.
4. Align bulk purchasing with demand to reduce costs without overstocking.
5. Diversify vendor base to reduce dependency risk.

![Recommendations Chart](assets/recommendations_chart.png)

</details>

---

<details>
<summary id="technical-execution-details"><strong>Technical Execution Details</strong></summary>

- **SQL:** JOINs, aggregations, subqueries, CTE-based summaries.
- **Python:** Data cleaning, metric calculations, outlier detection, binning.
- **Logging:** Centralized logs for ingestion & summary creation.

</details>

---

<details>
<summary id="folder-structure"><strong>Folder Structure</strong></summary>

```bash
vendor-performance-analysis/
│
├── assets/             # Images & banners for README
├── data/               # Raw & cleaned datasets
├── notebooks/          # Jupyter notebooks
├── dashboards/         # Power BI files
├── scripts/            # ingestion_db.py, get_vendor_summary.py
├── visuals/            # Exported charts
├── log/                # Logging files
└── README.md
```

</details>

---

<details> <summary id="future-enhancements"><strong>Future Enhancements</strong></summary>
  
- Real-time vendor tracking

- Automated KPI alerts

- Predictive vendor risk modeling

- Multi-year trend analysis

</details>

---

<details> <summary id="contact"><strong>Contact</strong></summary>
Author: Rajdeep Ray
📧 Email: rajdeepray.c48.it@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/rajdeep-ray-3616501b6/
🐙 GitHub: https://github.com/deadlineZeus/vendor-inventory-performance-analysis-sqlite-python-powerbi

</details> 

---
