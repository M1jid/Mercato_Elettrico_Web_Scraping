# Web Scraping Project: Mercato Elettrico Automation ⚡📊

## Project Overview 📑
This project automates the process of scraping electricity prices and volumes from the **Mercato Elettrico** website using **Selenium**. The script interacts with various elements on the webpage such as checkboxes and dropdowns to download data in `.XLSX` format.

## Features ✨
- **Headless Browser Mode**: The script runs in headless mode (without opening a browser window), making it efficient and suitable for automation.
- **Automated Data Interaction**: Selects checkboxes, opens dropdowns, and triggers downloads automatically.
- **Multiple Downloads**: Downloads electricity data for both **Zonal Prices** and **Volumes**.
- **Fast and Reliable**: The script is optimized for scraping speed and reliability using Python and Selenium.

## How It Works 🛠️
1. The script uses **Selenium WebDriver** to launch a headless Chrome browser.
2. It navigates to the **Mercato Elettrico** website for Zonal Prices.
3. The script automatically interacts with checkboxes, buttons, and dropdown menus to select the desired data.
4. It downloads the **Zonal Prices** data as an `.XLSX` file.
5. The process repeats for **Volumes** data from the same website.
6. Finally, the browser is closed once the data is downloaded.

## Prerequisites 🛑
Make sure you have the following installed on your system:
- Python 3.x
- Google Chrome
- **Chromedriver** (Make sure to download the appropriate version of Chromedriver based on your installed Chrome version. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)).

## Installation 🧑‍💻

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Mercato_Elettrico_Web_Scraping.git
   ```
2.Navigate to the project directory:
   ```bash
   cd Mercato_Elettrico_Web_Scraping
   ```
3.Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
Running the Script ▶️
To run the web scraper, use the following command:

   ```bash
   python scraper.py
   ```
Ensure that the path to Chromedriver in the script (Z:/web_scraping/chromedriver.exe) is correct. If you have Chromedriver in another location, make sure to update the executable_path variable accordingly.

Important Notes 📋
The script uses Selenium to automate web interaction. Make sure that Chromedriver is compatible with your version of Chrome.
Since the script is running in headless mode, you won’t see any browser window pop up.
Data is automatically downloaded as .XLSX files, so make sure you have enough storage in the download path.
License 📄
This project is open source and available under the MIT License.

Contact 📧
For any issues or contributions, please reach out via the GitHub Issues page.

Happy Scraping! 🚀


   
