<p align="center">
  <img src="visuals/logo.jpeg" alt="Vendor Performance Analysis" width="800"/>
</p>

# Vendor Performance Analysis: Optimizing Vendor & Inventory Strategies

<details open>
<summary><strong><span style="font-size: 1.25em;">Executive Summary and Overview</span></strong></summary>
<br>

This project focuses on **optimizing vendor performance and inventory management** to reduce costs, improve supply chain resilience, and enhance profitability.  

Using a combination of **Power BI**, **Python**, and **SQL**, raw CSV data was transformed into a unified vendor performance dataset, enriched with **statistical analysis** and **business intelligence dashboards**. The final output is a set of **actionable strategies** that address vendor dependency, pricing inefficiencies, bulk purchase benefits, and inventory turnover.  

Stakeholders gain access to a **live, interactive Power BI dashboard** enabling them to explore vendor metrics, brand performance, and purchasing trends in real time.

</details>

---

<details open>
<summary id="table-of-content"><strong>Table of Content</strong></summary>

- [Business Context & Objectives](#business-context--objectives)
- [Project Workflow Overview](#project-workflow-overview)
- [Tools & Technologies](#tools--technologies)
- [Data Preparation & Processing](#data-preparation--processing)
- [Power BI Section Demo](#power-bi-section-demo)
- [Statistical Analysis & Visualizations](#statistical-analysis--visualizations)
- [General Insights](#general-insights)
- [Strategic Insights](#strategic-insights)
- [Recommendations](#recommendations)
- [Technical Execution Details](#technical-execution-details)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

  </details>

---

<details>
<summary id="business-context--objectives"><strong>Business Context & Objectives</strong></summary>
<br>

Vendor and inventory performance directly influence **profitability**, **cash flow**, and **supply chain stability**. The **core business challenge** is to determine how to **optimize vendor relationships** and **streamline inventory management** in order to reduce costs and enhance operational efficiency.

**Key Objectives:**  
- Identify top- and low-performing vendors.  
- Detect pricing inefficiencies and vendor dependency risks.  
- Improve inventory turnover and reduce slow-moving stock.  
- Validate findings using statistical hypothesis testing.

</details>

---

<details>
<summary id="project-workflow-overview"><strong>Project Workflow Overview</strong></summary>
<br>

### Data Flow Summary:
CSV Files → SQLite Database → Aggregated Vendor Table → SQLite Database → Analysis & Dashboard on Jupyter Notebook → Insights & Recommendations → Final Report

---

### Project Phases:

- **Phase 1 – Exploratory_Data_Analysis.ipynb**  
  - Data ingestion from CSV files  
  - Database setup (SQLite)  
  - Creation of aggregated vendor table  
  - Logging for process tracking  

- **Phase 2 – Vendor_Performance_Analysis.ipynb**  
  - Statistical analysis of aggregated data  
  - Answering business questions  
  - Creating visualizations  
  - Generating actionable insights  

---

### Visual Overview:

![Workflow Diagram](assets/project_flowchart.png)

</details>

---

<details>
<summary id="tools--technologies"><strong>Tools & Technologies</strong></summary>
<br>

| **Category**             | **Tools / Languages**                                                      |
|--------------------------|---------------------------------------------------------------------------|
| **Business Intelligence** | Power BI, DAX, M Language                                                 |
| **Python Libraries**      | pandas, numpy, matplotlib, seaborn, sqlite3, SQLAlchemy                   |
| **Database**              | SQLite                                                                    |
| **SQL Features Used**     | JOIN, WHERE, GROUP BY, ORDER BY, Subqueries, CTEs, Table creation        |
| **Statistics**            | Descriptive stats, IQR, Percentiles, Quantile discretization, Cumulative sum, Confidence intervals, Hypothesis testing (T-test, significance testing) |
| **IDE / Environment**     | Jupyter Notebook                                                          |

</details>

---

<details>
<summary id="data-preparation--processing"><strong>Data Preparation & Processing</strong></summary>
<br>

### Manager Summary:  
Data from multiple CSV files was cleaned, standardized, and merged into a unified aggregated vendor performance dataset, which powers a **real-time Power BI dashboard** for vendor and inventory insights.

---

### Implementation Details:

- **Scripts & Logging:**

  - `ingestion_db.py`  
    - Loads raw CSV files into SQLite database  
    - Handles large file ingestion efficiently  
    - Maintains ingestion logs at `log/logging.log`

  - `get_vendor_summary.py`  
    - Performs SQL aggregations to generate summary data  
    - Cleans and calculates key performance indicators (KPIs)  
    - Uploads summary table back to the database  
    - Maintains detailed logs at `log/get_vendor_summary.log`

---

### Technology Usage:

- **SQL:**  
  - Complex queries using JOINs, GROUP BY, CTEs, subqueries, and filtering to aggregate data efficiently.

- **Python (pandas):**  
  - Data transformation tasks such as column creation, type conversions, custom function applications, and missing-value handling.

- **Power BI:**  
  - Loaded aggregated vendor sales summary table  
  - Built calculated tables including `BrandPerformance`, `LowTurnoverVendors`, and `PurchaseContribution`  
  - Added calculated DAX columns for business metrics  
  - Designed interactive filters and slicers to enable dynamic dashboard exploration

</details>


---

<details>
<summary id="power-bi-section-demo"><strong>Power BI section demo</strong></summary>
<br>
  
**DAX and table snapshot:**
  ![Dashboard Screenshot](assets/dax.png) 
<br>

**Dashboard snapshot Views:**
  ![Dashboard Screenshot](assets/dashboard_screenshot.png)
  
<p><a href="https://youtu.be/6Yqrk_L77L8" target="_blank" rel="noopener noreferrer">
<strong>▶️ Check Dashbaord live demo on YouTube, click down below</strong>
</a></p>

<a href="https://youtu.be/6Yqrk_L77L8" target="_blank" rel="noopener noreferrer">
  <img src="https://img.youtube.com/vi/6Yqrk_L77L8/hqdefault.jpg"
       alt="Vendor Performance Analysis — Live demo"
       style="width:100%; max-width:400px; border-radius:6px;">
</a>
  
</details>

---

<details>
<summary id="statistical-analysis--visualizations"><strong>Statistical Concepts & Visualizations</strong></summary>
<br>
  
**Statistical concepts Applied:**
- Descriptive stats (max, min, mean, std, quartiles)
- Outlier detection (IQR)
- Correlation analysis
- Hypothesis testing (t-test, confidence intervals)
- Quantile-based discretization

**Visualizations:**
- Histograms
- Boxplots
- Pie & donut charts
- Horizontal bar charts
- Scatterplots
- Heatmaps (correlation)
- KDE plots

</details>

---

<details>
<summary id="general-insights"><strong>General Insights</strong></summary>

**_(Click each insight to see the supporting chart)_**

<details>
<summary>• Some products incur significant losses, with gross profit minimum reaching -52,000+, indicating pricing or cost issues.</summary>
<img src="visuals/P9.png" alt="Gross Profit Losses Overview" width="600" />
</details>

<details>
<summary>• Strong correlation (0.999) between purchase quantity and sales quantity confirms effective inventory turnover.</summary>
<img src="visuals/P6.png" alt="Purchase vs Sales Quantity Correlation" width="600" />
</details>

<details>
<summary>• Freight costs vary hugely, from less than 1 to over 250,000, highlighting potential logistics inefficiencies or bulk shipments.</summary>
<img src="visuals/P7.png" alt="Freight Cost Variation" width="600" />
</details>

<details>
<summary>• Stock turnover ranges widely; some products sell fast, others remain in stock indefinitely, impacting working capital.</summary>
<img src="visuals/P8.png" alt="Stock Turnover Range" width="600" />
</details>

<details>
<summary>• Price variations have little impact on sales revenue or gross profit, indicating other factors drive profitability.</summary>
<img src="visuals/P5.png" alt="Purchase Price Correlations" width="600" />
</details>

<details>
<summary>• Higher sales prices tend to correlate with lower profit margins, possibly due to competitive pricing pressures.</summary>
<img src="visuals/P12.png" alt="Profit Margin vs Sales Price" width="600" />
</details>

</details>

---

<details>
<summary id="strategic-insights"><strong>Strategic Insights</strong></summary>

**_(Click each insight to see the evidence)_**

<details>
<summary>• High-Margin, Low-Sales Brands: 198 brands show high profitability but low sales volume.</summary>
<img src="visuals/P19.png" alt="High-Margin Low-Sales Brands Chart" width="600" />
</details>

<details>
<summary>• Vendor Dependency: Top 10 vendors = 65.7% of purchases.</summary>
<img src="visuals/P15.png" alt="Vendor Dependency Chart" width="600" />
</details>

<details>
<summary>• Bulk Purchase Benefits: 72% lower unit cost for large orders.</summary>
<img src="visuals/P16.png" alt="Bulk Purchase Benefits Chart" width="600" />
</details>

<details>
<summary>• Slow-Moving Inventory: $2.71M tied up in low-turnover stock.</summary>
<img src="visuals/P18.png" alt="Slow-Moving Inventory Chart" width="600" />
</details>

<details>
<summary>• Profit Margin Models: Low-performing vendors have higher margins but lower sales.</summary>
<img src="visuals/P20.png" alt="Profit Margin Models Chart" width="600" />
</details>

<details>
<summary>• Statistical Validation: Significant profit margin difference between top & low vendors.</summary>
<img src="visuals/P12.png" alt="Statistical Validation Chart" width="600" />
</details>

</details>

---

<details>
<summary id="recommendations"><strong>Recommendations</strong></summary>
<br>

1. **Re-evaluate Pricing for Low-Sales, High-Margin Brands**  
   Review pricing for brands with high margins but low sales to balance profitability and competitiveness. Strategic price adjustments can help capture additional demand without significantly eroding margins.

2. **Optimize Slow-Moving Inventory**  
   Refine purchase quantities, introduce clearance promotions, and assess storage costs to reduce holding expenses and free up capital for faster-moving, more profitable products.

3. **Enhance Marketing & Distribution for Low-Performing Vendors**  
   Support underperforming vendors with targeted marketing, expanded distribution channels, and focused sales initiatives to increase sales volumes while preserving profitability.

4. **Leverage Bulk Purchasing Advantages**  
   Use bulk purchasing strategically to secure competitive pricing and improve inventory turnover. Align orders with demand patterns to cut procurement costs without overstocking.

5. **Diversify Vendor Base**  
   Reduce reliance on the top 10 suppliers to strengthen supply chain resilience. Expanding the vendor network ensures continuity, mitigates disruption risks, and improves negotiation leverage.

</details>


---

<details>
<summary id="technical-execution-details"><strong>Technical Execution Details</strong></summary>
<br>

- **SQL:** JOINs, aggregations, subqueries, CTE-based summaries.
- **Python:** Data cleaning, metric calculations, outlier detection, binning.
- **Logging:** Centralized logs for ingestion & summary creation.

</details>

---

<details>
<summary id="folder-structure"><strong>Folder Structure</strong></summary>
<br>

bash
vendor-performance-analysis/
│
├── assets/
|    └── Project_Flowchart.png                         # Images & banners for README
|
├── data/
|    └── processed/                                    # Agreegated table after initial analysis
|    |    └── vendor_sales_summary_sample.csv
|    |
|    └── raw/                                          # Raw & cleaned datasets with limited records
|         └── begin_inventory_sample.csv
|         └── end_inventory_sample.csv
|         └── purchase_prices_sample.csv
|         └── purchases_sample.csv
|         └── sales_sample.csv
|         └── vendor_invoice_sample.csv           
|
├── deliverables/
|    └── final_report.pdf
|    └── vendor_performance_analysis_dashboard.pbix
|
├── log/
|     └── ingestion_db.py         # Logging files
|     └── get_vendor_summary.log
|
├── notebooks/
|    └── Exploratory_Data_Anaysis.ipynb
|    └── Vendor_Performance_Analysis.ipynb              # Jupyter notebooks
| 
├── scripts/
|    └── get_vendor_summary.py                                # Jupyter notebooks
|    └── ingestion_db.py
|                               
├── visuals/
|    └── P1.png
|    └── P2.png
|    └── P3.png
|    └── P4.png
|    └── P5.png
|    └── P6.png
|    └── P7.png
|    └── P8.png
|    └── P9.png
|    └── P10.png
|    └── P11.png
|    └── P12.png                           
|    └── P13.png
|    └── P14.png
|    └── P15.png
|    └── P16.png
|    └── P18.png
|    └── P19.png
|    └── logo.jpeg
|    └── power_bi_dashboard_live_demo.mp4 
|               
├── README.md
|
└── requirements.txt                                 # Important libraries from python that were used


</details>

---

<details> <summary id="future-enhancements"><strong>Future Enhancements</strong></summary>
<br>
  
- Real-time vendor tracking

- Automated KPI alerts

- Predictive vendor risk modeling

- Multi-year trend analysis

</details>

---

<details> <summary id="contact"><strong>Contact</strong></summary>
<br>
  
Author: Rajdeep Ray
📧 Email: rajdeepray.c48.it@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/rajdeep-ray-3616501b6/
🐙 GitHub: https://github.com/deadlineZeus/vendor-inventory-performance-analysis-sqlite-python-powerbi

</details> 

---
