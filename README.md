# Visual-Snow-Syndrome

## For Users:<br/>
Please have a look at the user manual available at https://github.com/sh-r/Visual-Snow-Syndrome/tree/master/documentation.

### For Windows (Tested on Windows 10):<br/>
You do not need Python or any of the libraries installed. Please download the executable (you can download just the .exe file) available in the releases section https://github.com/sh-r/Visual-Snow-Syndrome/releases/tag/v1.0.0. A Setup Wizard has also been added which will walk you through the whole installation process. <br/>
If you are not using Windows 10, https://pyinstaller.readthedocs.io/en/stable/usage.html#windows this issue may cause problems. Support for this is coming soon!

### For Linux (Tested on Ubuntu 20.04):<br/>
You do not need Python or any of the libraries installed. Please download the executable available in the releases section https://github.com/sh-r/Visual-Snow-Syndrome/releases/tag/v1.1.0. <br/>
Double clicking the application file will not work. You have to run it from the terminal.<br/>

Commands:<pre><code>$ cd <name of driectory you have downloaded the file><br/>
$ ./Visual_Snow_Diagnostic
</code></pre>

You may have to make the file executable if it is not working from the terminal. 
> Right click the file <br/>
> Click Properties <br/>
> Change permissions to executable

Note:
Also, since PyInstaller applications are not backward compatible (https://pyinstaller.readthedocs.io/en/stable/usage.html#gnu-linux) and the development was done on Ubuntu   20.04, it may not work on Ubuntu 18.04 and earlier versions. Still, you are welcome to test it out!
The application is bundled on a 64 bit system. If you are using a 32 bit system, the bundled application may not work. However, you can always have a look at the documentation for developers and follow the instructions to run the code directly from your system.


### For MAC OS:<br/>
Mostly not coming soon :( Don't have a MAC and PyInstaller doesn't support cross-compilation. <br/>
PyInstaller executable (To Be Added).

## For developers:<br/>
You can clone this repository and download the contents.<br/> 
Have a look at the instructions for this- https://github.com/sh-r/Visual-Snow-Syndrome/blob/master/documentation/For_Developers.md.

Note 1: We are NOT distributing it using Pypi i.e pip install as it's a GUI application and not just a module. <br/>
Note 2: Versioning System used is:
- v1.0.0- for Windows
- v1.1.0- for Linux
- v1.2.0- for MAC OS <br/>

Then v1.0.1 would indicate updates to the first version of Windows and similarly for Linux and MAC.

## Contributions<br/>
Project Members:
1. Shika Rao
2. Tyler Dulin
3. Aryan Zutshi

Original Contributors to the code:
1. Shika Rao
2. Aryan Zutshi
