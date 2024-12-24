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
* [References](#references)
* [License](#license)

## Purpose
<div align="justify">

This Machine Learning (ML) project converts body sign language gestures into Morse code using Python and image processing techniques. It is designed to process visual input on a client device (laptop) and send results to a server device (Raspberry Pi) to control LEDs that blink Morse code. The division of processing ensures efficient execution, as the Raspberry Pi cannot run certain libraries like `mediapipe` effectively.

The project provides a creative and practical tool for learning about Python, ML and hardware integration.


## Features
- Real-time body gesture recognition using Python and image processing.
- Conversion of recognized gestures into Morse code.
- Transmission of Morse code data from a client to a server via sockets.
- LED control on a Raspberry Pi to display Morse code.
- Modular project structure for ease of testing and future extension.

### Prerequisites
* Raspberry Pi 3B or 4B Model
* Python 3.8+
* Camera (for client device)
* Python libraries specified in `requirements.txt`
* Optional: GPIO setup for controlling LEDs on the Raspberry Pi

### Notes
1. Directly test the project by running: `python3 test_classifier.py`<br>
Ensure you've completed Step 3 in the [How To Run?](#how-to-run) section before testing.

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

- client/: Contains client and ML codes.
    - collect_imgs.py: Collect images for training
    - create_dataset.py: Create datasets from collected images
    - socket_client.py: Handles communication with the server
    - train_classifier.py: Train the gesture classifier
    - test_classifier.py: Test the trained classifier
- data/: Contains datas created by collect_img.py file.
- images/: Contains visual informations as images for the project.
- models/: Stores trained models and data files.
- env/: Virtual environment.
- server/socket_server.py: Receives data and controls the LEDs.
- requirements.txt: Lists project dependencies.


## How To Run?
1. Clone the repository:
```
git clone https://github.com/abdulkerimakten/body_sign_language_to_morse_code.git
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

3. Install dependencies:

- If you are running repository on hardware platforms such as Raspberry Pi or Jetson, you should install `RPi.GPIO` library sepereatly; because this library is designed specifically for devices equipped with GPIO pins and may not be compatible with other platforms.

```
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

4. Run the project in order:
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

<div align="center">
    <img src="/images/real-time-test.jpeg" weight="auto" height="500" alt="preview">
</div>


## References
- [Sign language detection with Python and Scikit Learn...](https://www.youtube.com/watch?v=MJCSjXepaAM)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/abdulkerimakten/body_sign_language_to_morse_code?tab=MIT-1-ov-file#readme) file for details.