# WebScraping-2019

Web Scripting is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format. There are many different ways to perform web scraping to obtain data from websites. these include using online services, particular API’s or even creating your code for web scraping from scratch.
<br/>
Here, we will be exploring web scraping with Python using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](https://www.selenium.dev/).

## Table of Contents

* [Prerequisites](#prerequisites)
* [Beautiful Soup](#beautiful-soup)
* [Selenium](#selenium)
* [Credits](#credits)

<p align="center">
<img src="https://www.webharvy.com/images/web%20scraping.png">
</p>

### Prerequisites
* [Python](https://www.python.org/)
* [Google Chrome](https://www.google.co.in/chrome/)
* [Google Chrome Web-Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Beautiful Soup

We'll be extracting all the sections of a [Wikipedia page](https://en.wikipedia.org/wiki/Artificial_intelligence) using the file [BeautifulSoup.py](https://github.com/ISTE-VESIT-ORG/WebScraping-2019/blob/master/BeautifulSoup.py).
* Install the [Beautiful Soup](https://pypi.org/project/bs4/) module for Python.
```
pip install bs4
```
* Run the file [BeautifulSoup.py](https://github.com/ISTE-VESIT-ORG/WebScraping-2019/blob/master/BeautifulSoup.py) for extracting all the sections of the <b>Wikipedia page.</b>
```
python Beautifulsoup.py
```
* **Output**:
```
1 History
2 Basics
3 Challenges
3.1 Reasoning, problem solving
3.2 Knowledge representation  
3.3 Planning
3.4 Learning
3.5 Natural language processing
3.6 Perception
3.7 Motion and manipulation
3.8 Social intelligence
3.9 General intelligence
4 Approaches
4.1 Cybernetics and brain simulation
4.2 Symbolic
4.2.1 Cognitive simulation
4.2.2 Logic-based
4.2.3 Anti-logic or scruffy
4.2.4 Knowledge-based
4.3 Sub-symbolic
4.3.1 Embodied intelligence
4.3.2 Computational intelligence and soft computing
4.4 Statistical
4.5 Integrating the approaches
5 Tools
6 Applications
7 Philosophy and ethics
7.1 The limits of artificial general intelligence
7.2 Ethical machines
7.2.1 Artificial moral agents
7.2.2 Machine ethics
7.2.3 Malevolent and friendly AI
7.3 Machine consciousness, sentience and mind
7.3.1 Consciousness
7.3.2 Computationalism and functionalism
7.3.3 Strong AI hypothesis
7.3.4 Robot rights
7.4 Superintelligence
7.4.1 Technological singularity
7.4.2 Transhumanism
8 Impact
8.1 Risks of narrow AI
8.2 Risks of general AI
9 Regulation
10 In fiction
11 See also
12 Explanatory notes
13 References
13.1 AI textbooks
13.2 History of AI
13.3 Other sources
14 Further reading
15 External links
```

## Selenium

[Selenium](https://www.selenium.dev/) is one of the most widely used open source Web UI (User Interface) automation testing suite. Along with automation, it also has the capability of scraping data.
<br/>
We'll be automating the process of entering credentials and logging into [Facebook](https://www.facebook.com/) account and extracting the data from the posts done by a selenium bot.
<br/>
* Install the [Selenium](https://selenium-python.readthedocs.io/installation.html) module for Python.
```
pip install selenium
```
* Open your **[Google Chrome](https://www.google.co.in/chrome/)** browser, go to Settings and note your Chrome's version. example: **Version 84.0.4147.89 (Official Build) (64-bit)**.
* Now we need the Chrome Web-Driver. Download the web-driver matching the confguration of your system and version of your browser. Refer this [video]( https://youtu.be/Xjv1sY630Uc).
* Open file Selenium.py and mention your Facebook account credentials. example -
```
username.send_keys("ISTE-VESIT")  # Facebook - Username
password.send_keys("1234567890")  # Facebook - Password
```
* Run the file.
```
python Selenium.py
```

## Credits
* **Gaurav Sahu**
* **Chinmay Patil**



