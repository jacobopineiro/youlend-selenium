# youlend-selenium

Example project with python and selenium.

## Project Structure

```bash
├── README.md
├── credentials.py (Needs to be created)
├── locators.py
├── pages
│   ├── __init__.py
│   ├── base.py
│   ├── checkout.py
│   ├── home.py
│   └── login.py
└── tests.py
```
## Prerequisites

Before running the tests, you need to install the following modules with pip:
- selenium
- html-testRunner

Also, you need to download ChromeDriver(https://chromedriver.chromium.org/)
and add it to PATH.

## Usage

Before running the tests, you need to create a credentials.py file in the project root to insert your credentials, eg:
```python
email = 'youremail@youremail.com'
password = 'yourpassword'
```

To run the tests from a terminal window:
```bash
python3 tests.py
```

This will generate an html report in the output folder(will be created if it doesn't exists)

## Future Improvements

* Implement ExpectedConditions usage in get_size_quick_view() and change_item_size() to avoid using time.sleep()
before being able to access the elements
* Generate screenshot on test failed and save in directory
* Implement cross browser support with selenium-grid


