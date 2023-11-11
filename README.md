## :information_desk_person: About project

Project is a End to End Selenium Python Framework, build using Page object design. <br>
The application being tested is located at: https://rahulshettyacademy.com/angularpractice <br>
Automatic tests check two test cases: Login with correct data and the entire product purchase path.

#### :pushpin: List of steps needed to run framework

:one: [Pytest installation](#one)

:two: [Selenium Webdriver installation](#two)

:three: [Pytest-html installation](#three)

:four: [Run the tests](#four)

#### <a name="one">:computer: Pytest installation</a>
- Install [pytest](http://doc.pytest.org/en/latest/getting-started.html) via pip:
```
pip install -U pytest 
```
- After installation, you can check the installed version by running:
```
pytest --version
```

#### <a name="two">:computer: Selenium Webdriver installation</a>
- Install [selenium](http://selenium-python.readthedocs.io/installation.html) via pip:
```
pip install -U selenium
```

#### <a name="three">:computer: Pytest-html installation</a>
- Install [pytest-html](https://pytest-html.readthedocs.io/en/latest/) via pip:
```
pip install pytest-html
```

#### <a name="four">:runner: Run the tests</a>
- To run all tests inside the test directory, simply run this command:
```
pytest --html=raport.html
```

After performing the tests, the report.html file will appear inside the tests directory.
