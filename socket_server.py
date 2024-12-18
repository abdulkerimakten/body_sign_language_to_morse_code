import RPi.GPIO as GPIO
import socket

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setwarnings(False)  # Disable warnings for GPIO re-usage

# Pin numbers for LEDs
led_pins = [4, 17, 18, 27, 22, 23, 24, 25, 5, 6]
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)  # Set all pins as output
    GPIO.output(pin, GPIO.LOW)  # Initially turn off all LEDs

# Morse code definitions for digits 0-9
morse_code = {
    0: ['-', '-', '-', '-', '-'],  # 0 represented as five dashes
    1: ['.', '-', '-', '-', '-'],  # 1: dot followed by four dashes
    2: ['.', '.', '-', '-', '-'],  # 2: two dots, three dashes
    3: ['.', '.', '.', '-', '-'],  # 3: three dots, two dashes
    4: ['.', '.', '.', '.', '-'],  # 4: four dots, one dash
    5: ['.', '.', '.', '.', '.'],  # 5: five dots
    6: ['-', '.', '.', '.', '.'],  # 6: one dash, four dots
    7: ['-', '-', '.', '.', '.'],  # 7: two dashes, three dots
    8: ['-', '-', '-', '.', '.'],  # 8: three dashes, two dots
    9: ['-', '-', '-', '-', '.']   # 9: four dashes, one dot
}

# Label-to-digit mapping received from the client
labels_dic = {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5,
              'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'ZERO': 0}

def signal_morse_code(digit):
    """
    Lights up LEDs according to the Morse code pattern for the given digit.
    - '.' turns on the first LED in a pair, the second remains OFF.
    - '-' turns on both LEDs in a pair.
    """
    code = morse_code[digit]
    for i, symbol in enumerate(code):
        pin1, pin2 = led_pins[i * 2], led_pins[i * 2 + 1]  # Get the pair of pins for this symbol
        if symbol == '.':
            GPIO.output(pin1, GPIO.HIGH)  # Turn on the first LED
            GPIO.output(pin2, GPIO.LOW)   # Keep the second LED off
        elif symbol == '-':
            GPIO.output(pin1, GPIO.HIGH)  # Turn on both LEDs
            GPIO.output(pin2, GPIO.HIGH)
        else:
            GPIO.output(pin1, GPIO.LOW)  # Turn off both LEDs
            GPIO.output(pin2, GPIO.LOW)

# Socket setup
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 65432      # Port to listen for connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print("Waiting for connection...")
conn, addr = sock.accept()  # Accept a connection from a client
print(f"Connection established with: {addr}")

try:
    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        if not data:  # If no data is received, exit the loop
            break

        # Convert the received label to its corresponding digit
        if data in labels_dic:
            digit = labels_dic[data]
            print(f"Received Label: {data}, Digit: {digit}")

            # Reset all LEDs before updating
            for pin in led_pins:
                GPIO.output(pin, GPIO.LOW)

            # Update LEDs to represent the Morse code of the digit
            if 0 <= digit <= 9:
                signal_morse_code(digit)

finally:
    # Cleanup GPIO pins and close the connection
    conn.close()
    GPIO.cleanup()
