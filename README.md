<img src="https://raw.githubusercontent.com/Xiddoc/JadPlusPlus/master/static/JadPP.PNG" width="64" align="left" />

# JadPlusPlus

Extensions and helpful add-on tools for Jadx projects.

*(AKA Jad++ or JadPP)*

## Features

### Merging JadX projects
If you and your friend are working on the same APK, but have saved your JadX projects locally, 
then you can use the merging feature to group together all your comments, variable renames, and class renames.
The output is one `.jadx` project file which includes all the changes in one place.

More info can be found at:
```cmd
python jadpp.py merge -h
```  

### Updating JadX projects
It's frustrating and demanding work to deobfuscate an entire APK file, especially for the apps of large corporations.
When the app is updated, usually the obfuscation is re-run, and therefore all your deobfuscation work is wiped.
This feature takes a JadX project and the newly obfuscated/updated APK, and tries to match up all your renames and 
comments to the new APK file. The output is a new JadX project which has your work lined up with the new APK file.
For best results, try to use the update feature with the closest minor update, so that minimal changes are made in the
actual code logic between APK versions.

More info can be found at:
```cmd
python jadpp.py update -h
```

## Usage

Run the following command for a full list of actions and features to use:
```cmd
python jadpp.py -h
```
