# near-production-examples
These code snippets demonstrate some of the capabilities required for using Colaboratory

The codes and files in this folder demonstrate some of the capabilities of Python/Colaboratory that may be required for near production work.  For much of this work, the code samples are generally run locally in "crostini", but they are designed to be used within a Colaboratory notebook.

# Rationale

As a rule, Google Drive associates applications with files, but the applications must be run as micro-services.  This means they have to be production or near production to be accepted by Google.  Most of the applications I use are for learning and are custom; therefore, this is not particularly good model.

However, there is a fairly decent solution, use crostini on a Chromebox to run custom applications during testing then integrate the snippets into a Colaboratory file as necessary.  Once the code is good enough, I may develop a library and put it into a github repository but this method lets me get through the first pieces of "demo".

I will keep a running log of issues so we will see if some of this works out.

# Configuration File Management

For any larger code (even within colaboratory), there is a need for a configuration file (.ini file) that supports setting various processing parameters.  The current standard is probably the .ini file which is supported by configparser.  There are a couple of important items:

*  If you try to have a .ini file and upload it to Google drive through the web interface, then it becomes a gdoc file.  You have to put in into Google Drive via the files app so that the import function doesn't mess with it too much.
