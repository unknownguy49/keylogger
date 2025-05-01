# KeyLogger

**KeyLogger** is a simple Python-based keylogger tool with a graphical user interface built using Tkinter. It captures and logs keystrokes in both JSON and text formats and provides an interface to start and stop the keylogger.

## Features

- Logs all key presses, holds, and releases.
- Saves logs to `logs.txt` (plain text) and `logs.json` (structured JSON).
- Real-time GUI status updates.
- Simple Start/Stop button interface.
- Multithreaded logging using `pynput` for non-blocking behavior.

## How It Works

- **Start Keylogger**: Begins monitoring keyboard inputs. Updates the UI to show that logging is active.
- **On Key Press/Hold**: Logs pressed or held keys in a JSON file.
- **On Key Release**: Appends released keys to both JSON and plain text files.
- **Stop Keylogger**: Halts key capturing and updates the UI status.

## Dependencies

- `tkinter`
- `pynput`
- `json` (standard library)
- `threading` (standard library)

## Usage

1. Run the script: `python keylogger.py`
2. Click on "Start Keylogger" to begin logging.
3. Click on "Stop Keylogger" to end the session.

## Disclaimer

This tool is for **educational purposes only**. Unauthorized use of keyloggers can be illegal and unethical. Always obtain proper permission before using this software.

## Screenshot

![Keylogger GUI Example](/demo/screenshot.png)
