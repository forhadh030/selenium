## Table of contents

- [Installation and Getting Started](#installation-and-getting-started) 
    - [Setup PyCharm to run pytest](https://www.jetbrains.com/help/pycharm/pytest.html)
- [Running tests](#running-tests) 
- [Skipping tests](#skipping-tests) 
- [Failing tests](#failing-tests) 
- [Assertion](#assertion) 
- [Fixtures](#fixtures) 
- [Grouping tests](#grouping-tests) 
    - [Marking a single function](#marking-a-single-function)
    - [Marking whole classes or modules](#marking-whole-classes-or-modules)
- [Parametrizing tests](#parametrizing-tests)  
- [Parallel tests](#parallel-tests) 
- [Test reports](#test-reports)
- [Environment Variables](#environment-variables) 
- [Command Line Option](#command-line-option)
- [Configuration Options](#configuration-options)  
- [Plugins](#plugins)



&nbsp;&nbsp;&nbsp;&nbsp;


### Installation and Getting Started
---

Run the following command in your command line:

```$ pip install -U pytest```

Check that you installed the correct version:

```$ pytest --version```

--- 

#### Setup PyCharm to run pytest

- Open up the **Preferences…** dialog and choose **Python Integrated Tools** under Project Settings.
- Choose **py.test** as the Default test runner.
- Click **OK**.

&nbsp;
### Running tests
---

Pytest supports several ways to run and select tests from the command-line.

#### Run tests in a module
```pytest test_mod.py```

#### Run tests in a directory
```pytest testing/```

#### Run tests by keyword expressions

```pytest -k "MyClass and not method"```

#### Run tests by marker expressions
```pytest -m smoke```


&nbsp;

Let's create a directory called ```selenium``` with a file ```/selenium/test_example.py```:

**Note:** Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py.

```python
# content of /selenium/test_example.py

def test_passing():
    assert True
```

Run the following command from terminal:

```$ pytest```

Result:

````
============================= test session starts ==============================
platform darwin -- Python 3.7.2, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /Users/sayem/IdeaProjects/coding.practice/python/selenium, inifile:collected 1 item

test_one.py .                                                            [100%]

=========================== 1 passed in 0.01 seconds ===========================
````


&nbsp;
### Skipping tests
---



&nbsp;
### Failing tests
---


&nbsp;
### Assertion
---



&nbsp;
### Fixtures
---

Fixtures are a powerful feature of PyTest. Fixtures help us to setup some pre-conditions like setup a database connection / get test data from files etc that should run before any tests are executed.

PyTest suggests you define all your fixtures within one single ```conftest.py``` file so that tests from multiple test classes/modules in the directory can access the fixture function.

When fixture function is called, it will run the code in the function from the beginning until it hits yield statement which serves as the ```setUp``` code and the code after the ```yield``` statement serves as the ```tearDown``` code. The code after the ```yield``` is guaranteed to run regardless of what happens during the tests.

It is usually a good idea to keep your ```conftest.py``` file in the top level test or project root directory.

We will create ```conftest.py``` file and add below code to a ```conftest.py``` file at the root of your tests' directory : -

```python
# content of conftest.py

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("chrome driver path") #if not added in PATH
    driver.get("http://www.google.com")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
````

Then to use this fixture on the test function we can just pass it in as function argument:

```python
# content of test_sample.py

def test_one(setup):
    ...

def test_two(setup):
    ...

def test_three(setup):
    ...

def test_four(setup):
    ...
```

Or to use this fixture on the class we can just decorated with ```@pytest.mark.usefixtures("setup")```:

```python
# content of test_example.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        ....
     
    def test_search(self):
        ....
        
````

The above two classes ```test_example.py``` is decorated with ```@pytest.mark.usefixtures("setup")```.

Applying ```@pytest.mark.usefixtures``` to the class is same as applying a fixture to every test methods in the class. Since the fixture **setup** has a scope defined as **class**, webdriver will be initialized only once per each class.

If you observe, In fixture, we have set the driver attribute via ```request.cls.driver = driver```, So that test classes can access the webdriver instance with self.driver.

Run your program using ```pytest -s``` and if everything goes well, the output looks like below :-

---

#### Scope

Scope controls how often a fixture gets called. The default is **function**.
Here are the options for scope:

- **function** - Run once per test
- **class**	    - Run once per class of tests
- **module**	 - Run once per module
- **session**	 - Run once per session

&nbsp;
### Grouping tests
---


Pytest allows to group tests using markers. **pytest.mark** decorator is used to mark a test function with custom metadata like **@pytest.mark.smoke**

This is very handy when we want to run only a subset of tests like "smoke tests" to quickly verify if the changes made by the developer not breaking any major functionalities.

#### Marking a single function

You can mark a test function with custom metadata like below:

```python
@pytest.mark.smoke
def test_case_one():
    assert True
```
A test can have more than one marker, and also a marker can be on multiple tests. Please look at the below example:-

```python
@pytest.mark.smoke
@pytest.mark.regression
def test_case_two():
    assert True
```

#### Marking whole classes or modules

You can use ```@pytest.mark.regression``` on top of the class to apply markers to all of its test methods:

```python

@pyest.mark.regression
class SeleniumTest

def test_addition(self):
    pass

def test_subtraction(self):
    pass

def test_multiplication(self):
    pass

```

Now, let’s just run above tests that are marked with marker name using -m command line option like below :-

```pytest -v -m regression```
 
 If we want to run all the selenium automation tests except regression, we can do like below using 'not' :-
 
```pytest -v -m "not regression"```

Now there may be a case where we want to execute selenium webdriver tests which are both 'regression' and 'smoke'. To do that, we should use command like below :-

```pytest -v -m "smoke and regression"```

&nbsp;
### Parametrizing tests
---


&nbsp;
### Parallel tests
---


&nbsp;
### Test reports
---
#### Creating JUnitXML format files
To create result files which can be read by Jenkins or other Continuous integration servers, use this invocation:
- ```pytest --junitxml=path```


&nbsp;
### Environment Variables
---


&nbsp;
### Command Line Option
---


&nbsp;
### Configuration Options
---


&nbsp;
### Plugins
---


&nbsp;
