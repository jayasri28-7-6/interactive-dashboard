# Sales Performance Dashboard

**Internship Details:**
* **Company:** CODTECH IT SOLUTIONS
* **Name:** Jayasri N
* **Intern ID:** CT04DG1603
* **Domain:** Data Analytics
* **Duration:** 4 Weeks
* **Mentor:** Neela Santosh Kumar

This project demonstrates an interactive web dashboard using **Plotly Dash** to visualize synthetic sales performance data. It allows users to filter data by product category and region, providing dynamic and actionable insights.

## Features

* **Synthetic Data Generation**: Creates a sample dataset of sales records.
* **Interactive Dashboard**: A web-based dashboard built with Plotly Dash.
* **Multiple Visualizations**: Displays key metrics and trends (e.g., sales over time, sales by category, profit by region).
* **Filtering Capabilities**: Allows interactive filtering by `Region` and `Product Category`.
* **Actionable Insights**: Designed to help identify top-performing areas and products.

## Dashboard Preview

Here's a static preview of the interactive dashboard:

![Interactive Sales Dashboard Screenshot](dashboard_screenshot.png)

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
   https://github.com/YOUR_USERNAME/sales-performance-dashboard.git   
    ```
    *(Note: Replace `YOUR_USERNAME` with your actual GitHub username and adjust the repo name if it's different)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### How to Run

1.  **Generate the dataset:**
    This script creates `sales_data.csv`.
    ```bash
    python data_generator.py
    ```

2.  **Run the Dash Dashboard:**
    This will start a local web server (usually at `http://127.0.0.1:8050/`) where your interactive dashboard will be accessible.
    ```bash
    python app.py
    ```
    Open the URL provided in your terminal in a web browser.

## Project Structure
```
sales-performance-dashboard
├── README.md
├── requirements.txt
├── data_generator.py       
├── app.py
```
## Dependencies

All dependencies are listed in `requirements.txt`.

## Future Enhancements

* **Real Dataset**: Integrate with a real-world sales dataset.
* **Advanced Analytics**: Integrate statistical models or ML predictions.
* **User Authentication**: Add user login capabilities.
* **Deployment**: Deploy the Dash app to a cloud platform.
* **Additional Interactivity**: Add more filter options, cross-filtering, or drill-down.
* **Theming and Styling**: Enhance visual appeal with custom CSS.


