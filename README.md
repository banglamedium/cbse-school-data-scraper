# cbse-school-data-scraper
**README.txt: Scraping CBSE School Data**

# CBSE School Data Scraper

This Python script uses Selenium and BeautifulSoup to scrape CBSE school data from the CBSE School Directory website (https://saras.cbse.gov.in/cbse_aff/schdir_Report/userview.aspx). The script allows you to collect school names for each state and save the data in CSV format.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (https://www.python.org/)
- Chrome browser
- ChromeDriver (automatically installed by the script using WebDriver Manager)

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/cbse-school-data-scraper.git
```

2. Navigate to the project directory.

```bash
cd cbse-school-data-scraper
```

3. Install the required Python packages.

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script.

```bash
python cbse_school_scraper.py
```

2. The script will open the CBSE School Directory website, select the 'State-wise' radio button, and start scraping school data for each state.

3. School data for each state will be saved in separate CSV files.

## Configuration

You can customize the script by modifying the code according to your specific requirements. For example, you can change the target URL or adjust the data extraction logic.

## Troubleshooting

If you encounter any issues, please make sure your Chrome browser is up to date, and the WebDriver Manager will automatically download the compatible ChromeDriver version.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


Happy scraping!
