# Brave Ad Clicker

- Currently only compatible with Windows 10
- [Brave](https://brave.com/) is a web browser that rewards users with cryptocurrency BAT tokens for viewing ads
- This Python program uses the pyautogui library to detect a Brave ad popup (Only on Windows 10), which will then open and close the ad, returning the cursor to the previous location uninterrupted
- Meant to be used during active computer use, Brave Browser is able to detect human vs machine interactions to prevent ad farming 


### Improvements (TODO)
- Reduce screenshot size to target bottom-right corner where popup is
- Add detection for MacOS, Linux
- Create executable (.exe) file

### User Interface (TODO)
- Tkinter UI launches when executable runs
- Displays elapsed time, number of ads clicked
- Button to turn bot On/Off
- Spinbox input to change time variables
