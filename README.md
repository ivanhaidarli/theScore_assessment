Introduction  

I decided to go with Python as a language of choice, as mentioned in a requirements doc. This project utilizes Python 3.11 as the interpreter and PyCharm IDE to automate mobile application testing using the Appium framework. If you need more context, please see Coverage description file.  

Project Structure:  
-README.md: Project overview file, what you currently reading, that include setup instructions and other relevant information.  
-Coverage description: document where I described my approach for the testing and assessment coverage.  
-Test.py: Python test scripts file containing the automated test steps using the Appium framework.  
-Apk file that was used to build the tests.  

Prerequisites:  
Before running the tests in this project, ensure you have the following installed:  
Appium-Python-Client==2.5.1  
Selenium == 4.1.0  
Python 3.11: Download and install Python from python.org.  
PyCharm: Install PyCharm, the Python IDE, from jetbrains.com/pycharm.  
Appium Desktop Client: Download and install the latest version of the Appium Desktop Client from the Appium GitHub repository.  
Android Studio for emulator: Used Google Pixel Emulator with Android 14.  

Setup Instructions:  
Clone or download this repository to your local machine.  
Open the project directory in PyCharm.  
Set up a virtual environment for the project:  
In PyCharm, open the terminal and run python3.11 -m venv venv to create a virtual environment named venv.  
Activate the virtual environment by running source venv/bin/activate on macOS/Linux or venv\Scripts\activate on Windows.  
Install the required Python packages by running pip install -r requirements.txt.  
Start the Appium server using the Appium Desktop Client.  
Modify the desired capabilities in the test scripts (test.py) to match your mobile device's configuration.  
Run the test scripts in PyCharm to execute the automated tests.  

Additional Resources:  
Python Documentation: Official documentation for Python 3.11.  
PyCharm Documentation: Official documentation for PyCharm.  
Appium Documentation: Official documentation for the Appium framework.


Contributing:  
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

