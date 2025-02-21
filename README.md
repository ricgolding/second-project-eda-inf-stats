# Vanguard Digital Experiment Analysis

## Overview
This project analyzes a digital experiment conducted by Vanguard to evaluate whether a new user interface (UI) improved process completion rates. The project involves data cleaning, exploratory data analysis (EDA), performance metric evaluation, hypothesis testing, and visualization using Tableau.

## Team Members
- Esteban, Muskan, Carles & Ricardo
- Group 2

## Project Structure
```
├── data
│   ├── df_final_demo.txt
│   ├── df_final_experiment_clients.txt
│   ├── df_final_web_data_pt_1.txt
│   ├── df_final_web_data_pt_2.txt
├── notebooks
│   ├── notebooks/cleaning_join_all.ipynb
│   ├── kpi_error_rate_eb.ipynb
│   ├── step_time_analysis_carles.ipynb
│   ├── kpi_conversion_funnel_eb.ipynb
├── visualizations
│   ├── tableau_dashboard
├── README.md
```

## Datasets Used
- **Client Profiles**: Contains demographic information of clients.
- **Digital Footprints**: Tracks online interactions and engagement levels.
- **Experiment Roster**: Assigns users to the Control or Test group.

## Methodology
1. **Data Cleaning & Merging**:
   - Removed duplicates and handled missing values.
   - Standardized data formats and merged datasets.

2. **Exploratory Data Analysis (EDA)**:
   - Identified key demographic insights and engagement patterns.
   - Assessed initial differences between Control and Test groups.

3. **Performance Metrics Evaluation**:
   - Defined KPIs (Completion Rate, Time to Completion, Drop-off Rates).
   - Compared Control vs. Test groups using visual and statistical methods.

4. **Hypothesis Testing**:
   - Conducted statistical tests (T-tests, Chi-square) to determine significance.
   - Evaluated cost-effectiveness of UI changes.

5. **Tableau Visualizations**:
   - Created interactive dashboards to visualize trends and insights.

## Key Findings
- The new UI led to a **statistically significant** increase in completion rates.
- Users in the Test group showed **lower drop-off rates** at key steps.
- The improved UI resulted in **faster completion times**.
- Cost-benefit analysis suggests **rolling out the new UI** across all users.

## Tableau Dashboard
Check out our **interactive Tableau dashboard** for a deep dive into the experiment data.

## Technologies Used
- **Python**: pandas, numpy, matplotlib, seaborn, scipy
- **Jupyter Notebooks**: Data exploration & analysis
- **Tableau**: Interactive data visualization
- **GitHub**: Version control & collaboration

## How to Run the Analysis
1. Clone the repository:
   ```bash
   git clone https://github.com/estebanba/second-project-eda-inf-stats
   cd vanguard-digital-experiment
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebooks for data analysis:
   ```bash
   jupyter notebook
   ```
4. Open the Tableau dashboard to explore visualizations.

## Contributions
Feel free to contribute by submitting issues, feature requests, or pull requests.

## License
This project is for educational purposes and is not affiliated with Vanguard.
