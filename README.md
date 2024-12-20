<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/9626/9626716.png" width="150" height="150" alt="icon">
</div>

<h1 align="center">Body Sign Language To Morse Code</h1>

* [Purpose](#purpose)
* [Features](#features)
    * [Prerequisites](#prerequisites)
    * [Notes](#notes)
* [Project Structure](#project-structure)
* [How To Run?](#how-to-run)
* [Test](#test)
* [Licence](#licence)

## Purpose
<div align="justify">

Machine Learning Project based on the Python image processing and 


## Features
### Prerequisites
* Raspberry Pi 3B or 4B Model
* 

### Notes
1. Run the project with the following command `python3 test_classifier.py` after installing the 4th step from [How To Run?](#how-to-run) section below for directly trying to run.

</div>


## Project Structure

The project follows this directory structure:

```
body_sign_language_to_morse_code/
│
├── client/
│   ├── collect_imgs.py
│   ├── create_dataset.py
│   ├── socket_client.py
│   ├── train_classifier.py
│   └── test_classifier.py
│
├── data/
│
├── images/
│   ├── mors_alphabet_for_numbers.jpg
│   ├── real-time-test.jpeg
│   └── the-26-letters-and-10-digits-of-American-Sign-Language-ASL.png
│
├── models/
│   ├── data.pickle
│   └── model.p
│
├── env/
│
├── server/
│   └── socket_server.py
│
├── gitignore
├── README.md
└── requirements.txt
```

- client/: Contains config files for yolov3 and yolov4-tiny.
    - 
- data/: Contains datas created by collect_img.py file.
- images/: Contains visual informations as images for the project.
- models/:
- requirements.txt: Lists project dependencies.


## How To Run?
1. Clone the repository:
```
https://github.com/abdulkerimakten/body_sign_language_to_morse_code.git
cd body_sign_language_to_morse_code
```

2. Virtual environment setup (Optional but recommended):

- For Windows:
```
python3 -m venv env
env/Scripts/activate
```

- For Linux & MacOS:
```
python3 -m venv env
source env/bin/activate
```

4. Install dependencies:

- If you are running repository on hardware platforms such as Raspberry Pi or Jetson, you should install `RPi.GPIO` library sepereatly; because this library is designed specifically for devices equipped with GPIO pins and may not be compatible with other platforms.

```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run the project in order:
```
python3 collect_imgs.py
```

```
python3 create_dataset.py
```

```
python3 train_classifier.py
```

```
python3 test_classifier.py
```


## Test
### Preview from the real-time test:

<img src="/images/real-time-test.jpeg" weight="auto" height="500" alt="preview">


## Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PRU-Robotic/body_sign_language_to_morse_code?tab=MIT-1-ov-file#readme) file for details.