from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

# Initialize Chrome driver
options = webdriver.ChromeOptions()
# Uncomment the line below to run in headless mode
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Navigate to the URL
    url = "https://saras.cbse.gov.in/cbse_aff/schdir_Report/userview.aspx"
    driver.get(url)

    # Click the 'State-wise' radio button
    state_wise_radio = driver.find_element(By.XPATH, '//*[@id="optlist_2"]')
    state_wise_radio.click()

    # Find the state dropdown
    state_dropdown = driver.find_element(By.ID, 'ddlitem')

    # Get all options from the dropdown
    state_options = Select(state_dropdown).options

    # Loop through each state and perform the search
    for i in range(1, len(state_options)):  # Skip the first option ('---Select A State---')
        try:
            # Find the state dropdown each time to avoid stale element reference
            state_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'ddlitem'))
            )

            # Select a state from the dropdown
            state_options = Select(state_dropdown).options
            selected_state = state_options[i].text
            state_options[i].click()

            print(f"\nSelected state: {selected_state}")

            # Click the 'Search' button using relative XPath
            search_button = driver.find_element(By.XPATH, '//*[@id="search"]')
            search_button.click()
            print(f"Clicked on search")

            # Wait for the dynamic loading of school list
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="T1"]'))
            )

            # Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # Extract school names
            school_names = soup.select("#T1 .repItem a")

            # Save data to CSV
            csv_filename = f"{selected_state}_schools.csv"
            with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["School Name"])
                # Write data
                writer.writerows([[school_name.text] for school_name in school_names])

            print(f"Data for {selected_state} saved to {csv_filename}")

        except Exception as e:
            print(f"An error occurred for {selected_state}: {e}")

finally:
    # Close the browser
    driver.quit()
