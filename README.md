# Visual-Snow-Syndrome

This repository contains a diagnostic tool for Visual Snow Syndrome. The application simulates the conditions of Visual Snow Syndrome so that the progression of the disease can be quantified.

## What is Visual Snow Syndrome? <br/>
To Be Added.

## For Users:<br/>
Please have a look at the user manual available at https://github.com/sh-r/Visual-Snow-Syndrome/tree/master/documentation.

### For Windows (Tested and Packaged on Windows 10):<br/>
You do not need Python or any of the libraries installed. Please download the executable (you can download just the .exe file) available in the releases section https://github.com/sh-r/Visual-Snow-Syndrome/releases/tag/v1.0.0. A Setup Wizard has also been added which will walk you through the whole installation process. <br/>
If you are not using Windows 10, https://pyinstaller.readthedocs.io/en/stable/usage.html#windows this issue may cause problems. Support for this is coming soon!

### For Linux (Tested and Packaged on Ubuntu 20.04):<br/>
You do not need Python or any of the libraries installed. Please download the executable available in the releases section https://github.com/sh-r/Visual-Snow-Syndrome/releases/tag/v1.1.0. <br/>
Double clicking the application file will not work. You have to run it from the terminal.<br/>

Commands:<pre><code>$ cd (name of directory you have downloaded the file)
$ chmod +x Visual_Snow_Diagnostic
$ ./Visual_Snow_Diagnostic
</code></pre>

The 'chmod +x' command makes it executable. You may have to make the file executable if it is not working from the terminal. Refer to the steps below.
1. Right click the file 
2. Click Properties 
3. Change permissions to executable

Note:
Also, since PyInstaller applications are not backward compatible (https://pyinstaller.readthedocs.io/en/stable/usage.html#gnu-linux) and the development was done on Ubuntu   20.04, it may not work on Ubuntu 18.04 and earlier versions. Still, you are welcome to test it out! <br/>
The application is bundled on a 64 bit system. If you are using a 32 bit system, the bundled application may not work. However, you can always have a look at the documentation for developers and follow the instructions to run the code directly from your system.


### For MAC OS:<br/>
Mostly not coming soon :( Don't have a MAC and PyInstaller doesn't support cross-compilation. <br/>

## For developers:<br/>
You can clone this repository and download the contents.<br/> 
Have a look at the instructions for installation here- https://github.com/sh-r/Visual-Snow-Syndrome/blob/master/documentation/Developer_Installation.md. The instructions for contribution and ideas are also mentioned. <br/>
For the Code Documentation like the file structure, packages used, etc, please refer to - https://github.com/sh-r/Visual-Snow-Syndrome/tree/master/documentation.

Note: We are NOT distributing it using Pypi i.e pip install as it's a GUI application and not just a module. <br/>

## Contributions<br/>
Project Members:
1. Shika Rao
2. Tyler Dulin
3. Aryan Zutshi

Original Contributors to the code:
1. Shika Rao
2. Aryan Zutshi

We also welocme open source contributions. Have a look at https://github.com/sh-r/Visual-Snow-Syndrome/blob/master/documentation/Contributions.md for guidenlines.
