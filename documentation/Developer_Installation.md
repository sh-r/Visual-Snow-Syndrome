# Installation Guidelines
Currently application was developed and tested on Windows 10 and Ubuntu 20.04. But the application should work with other OS too since PyQT5 is used for the application development and it has cross-platform development support. The application works with WSL2 as well when an X-server application, like Vcxsrv is used for GUI forwarding. <br/>

I would highly recommend using a virtual environment so that there is no interference from global site packages. The instructions for the same are given below.
 
## For Windows:
 
If you have PyCharm, I would recommend using it.

### With Pycharm:
1. Create a new project with virtual environment, and DO NOT INHERIT GLOBAL SITE PACKAGES.
2. In that project directory, download this repo.
3. Install pip- Most of the time pip comes installed with python builds.
<pre><code>pip help
</code></pre>
Type the above in the command prompt to check if you have pip already installed. If you don't, then please refer to below for instructions: https://www.liquidweb.com/kb/install-pip-windows/ 
4. Install the requirements file and then run the file.
<pre><code>pip3 install requirements.txt
python VisualSnowSyndrome_Diagnostic.py 
</code></pre>
 
### Without PyCharm:
 
1. Install a virtual environment. For installing 'pip' refer above section.

2. Create a virtual environment and activate it
<pre><code>pip install virtualenv
cd (the directory you wish to create the folder in)
virtualenv (the name of your environment) 
(the name of your environment)\Scripts\activate 
</code></pre>
 
3. Download this repository and copy this repo into the virtual environment folder.
 
4. Install the requirements file in the same directory of the virtual environment where you have downloaded the repo.

5. Run the application
<pre><code>pip3 install requirements.txt
python VisualSnowSyndrome_Diagnostic.py  
</code></pre>
 
## Using Linux:

1. First install pip and virtual environment
2. Create a virtual environment and activate it
<pre><code>$ sudo apt install python3-pip
$ sudo apt-get install python3-venv
$ cd (the directory you wish to create the folder in)
$ python3 -m venv <the name of your environment>
$ source (the name of your environment)/bin/activate
</code></pre>

3. Download this repository into the virtual environment.
4. Install the requirements file - All of the dependencies of this application will then be installed.
5. Run the application
<pre><code>$ cd (the name of your environment)
$ pip install -r requirements.txt
$ python VisualSnowSyndrome_Diagnostic.py
</code></pre>
If you face an error, it could probably be that Windows uses CLRF line endings and Linux uses LF line endings. Mostly when you download the code from GitHub, the line endings are according to the OS you are using. But if you are facing an issue, open all of the files in Visual Studio Code or any other IDE and change the line endings to LF. Otherwise, you can also:
<pre><code>$ pip install dos2unix
$ dos2unix (filename)
</code></pre>

# Open Source Contributions
We welcome any open source contributions you would like to make! Just fork and clone the repo and send a pull request. Some of the improvements we thought of till now:
1. Adding more types of noise like gaussian, poisson, localvar, etc 
2. In the Linux executable file, the icon is not shown when opened in File Explorer though the --icon flag was set in PyInstaller.
3. An executable file compatible with MAC OS X
4. Making the noise continuously moving, sort of like an animation
5. Simulating nyctalopia, floaters, afterimages, etc
6. Taking in a saved image and using the saved text file to continue editing the same image 
7. Implementing stacks, i.e. Undo and Redo operations
8. Bug fixes

