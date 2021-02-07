# Android Manifest Analysis

AMA (Android Manifest Analysis) is a tool to automate analysis of AndroidManifest.xml files.

## Features

AMA extracts information from an APK file and generates a report in excel.

- App version information:
  - Package Name
  - Version Code
  - Version Name
- Device compatibility:
  - < uses-feature >
  - < uses-sdk >
- Permissions:
  - < permissions >
  - < uses-permission >
  - < uses-permission-sdk-23 >	
- App Components:
  - < service >
  - < receiver >
  - < provider >

## Getting Started:

Clone the project repository: 

```
git clone https://github.com/fredpedroso/android-manifest-analysis
```

### Requirements:

Install the requirements:

```
pip install -r requirements.txt
```

### How to use:

Running:

```
python ama.py --path <file or directory>
```

The report will be generated in the _report_ folder.