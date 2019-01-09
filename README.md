
## Table of contents

- [Project](#instructions)
    - [Instructions](#instructions)
    - [Prerequisite](#prerequisite)
    - [Scenario breakdown](#scenario-breakdown)
- [Code Examples](#code-examples)
- [Cheat Sheet](#cheat-sheet)
    - [Browser Instantiation](#browser-instantiation)
    - [Browser Actions](#browser-actions)
    - [Finding Elements](#finding-elements)
        - [Id](#id)
        - [XPath](#xpath)
        - [Link Text](#link-text)
        - [Partial Link Text](#partial-link-text)
        - [Name](#name)
        - [Tag Name](#tag-name)
        - [Class Name](#class-name)
        - [CSS Selector](#css-selector)
    - [Back, Forward & Refresh](#back-forward--refresh)
    - [Maximize and Minimize](#maximize-and-minimize)
    - [Switch to Frame & Window](#switch-to-frame--window)
    - [Cookies](#cookies)
- [Page Object](#page-object)
- [Page Factory](#page-factory)
- [Useful Links](#useful-links)

&nbsp;


## Instructions:

In this tutorial we will go through some typical customer interactions on saucedemo.com. 
We will break down this rough workflow into usable PageObject and automate them. 


### Scenario breakdown

|Feature|Scenario|Smoke Test|Regression Test|End to End|
|---|---|---|---|---|
|login|Verify valid users can sign in|Yes|Yes|No|
|login|Verify locked out user gets locked out message|No|Yes|No|
|login|Verify invalid users cannot sign in|No|Yes|No|
|orders|Place a single item in the shopping cart|Yes|Yes|No|
|orders|Place multiple items in the shopping cart|No|Yes|No|
|orders|Validate Order Totals|No|Yes|No|


&nbsp;


## Prerequisite

Follow the steps below to install ChromeDriver and GeckoDriver driver on your macOS.

- ```GeckoDriver``` is the library you need to download to be able to use WebDriver with Firefox.
- ```ChromeDriver``` is the library you need to download to be able to use WebDriver with Chrome.

The easiest way to install ChromeDriver and GeckoDriver on macOS is to use homebrew package manager:
```
brew install geckodriver
brew cask install chromedriver
```

&nbsp;

## Code Examples


&nbsp;


## Cheat Sheet


### Browser Instantiation
```python
from selenium import webdriver

firefox = webdriver.Firefox(executable_path='drivers\geckodriver.exe')
chrome = webdriver.Chrome(executable_path='drivers\chromedriver.exe')
edge = webdriver.Edge(executable_path='drivers\MicrosoftWebDriver.exe')
ie = webdriver.Ie(executable_path='drivers\IEDriverServer.exe')
```
### Browser Actions
```python
#Get Browser Name
self.driver.name

#Get Title
print(browser.title)

#Get Current URL
self.driver.current_url

#Get Current Window Handle
self.driver.current_window_handle

#Get All Window Handles
handles_list=self.driver.window_handles

#Get Page Source
self.driver.page_source
````

### Finding Elements

##### ID
```python
#Find Element By ID
element = by(id_="locator")

#Find a list of Elements By ID
elements = by(id_="locator", multiple=True)
```
##### Xpath
```python
#Find Element By XPATH
element = by(xpath="locator")

#Find a list of Elements By XPATH
elements = by(xpath="locator", multiple=True)
```

##### Link Text
```python
#Find Element By Link Text
element = by(link_text="locator")

#Find a list of Elements By Link Text
elements = by(link_text="locator", multiple=True)
```

##### Partial Link Text
```python
#Find Element By Partial Link Text
element = by(partial_link_text="locator")

#Find a list of Elements By Partial Link Text
elements = by(partial_link_text="locator", multiple=True)
```

##### Name
```python
#Find Element By Name
element = by(name="locator")

#Find a list of Elements By Name
elements = by(name="locator", multiple=True)
```

##### Tag Name
```python
#Find Element By Tag Name
element = by(tag_name="locator")

#Find a list of Elements By Tag Name
elements = by(tag_name="locator", multiple=True)
```

##### Class Name
```python
#Find Element By Class Name
element = by(class_name="locator")

#Find a list of Elements By Class Name
elements = by(class_name="locator", multiple=True)
```

##### CSS Selector
```python
#Find Element By CSS Selector
element = by(css_selector="locator")

#Find a list of Elements By CSS Selector
elements = by(css_selector="locator", multiple=True)
```

### Back, Forward & Refresh
```python
self.driver.back()
self.driver.forward()
self.driver.refresh()
```

### Maximize and Minimize
```python
self.driver.maximize_window()
self.driver.minimize_window()
````

### Switch to Frame & Window
```python
self.driver.switch_to.active_element

self.driver.switch_to.alert

self.driver.switch_to.default_content()

# You can pass Window Name or Handle to switch between windows
self.driver.switch_to.window("window_name")

#You can switch to frame using Name, ID, Index & WebElement
self.driver.switch_to.frame(1)

self.driver.switch_to.parent_frame()
```
### Cookies
```python
#Get all cookies in a list
cookies_list = self.driver.get_cookies

#Get a Cookie value
cookie_value = self.driver.get_cookie("my_cookie")

#Delete a Cookie
self.driver.delete_cookie("my_cookie")

#Delete all Cookies
self.driver.delete_all_cookies()

#Add Cookie
self.driver.add_cookie({"name:value"})
```


&nbsp;


## Page Object



&nbsp;

## Page Factory



&nbsp;


## Useful Links
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Implementing Page Factory (or PageFactory) Pattern in Python](https://jeremykao.wordpress.com/2015/06/10/pagefactory-pattern-in-python/) 
