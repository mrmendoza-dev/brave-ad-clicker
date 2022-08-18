# Brave Ad Clicker
- Currently only compatible with Windows 10/11
- [Brave](https://brave.com/) is a web browser that rewards users with cryptocurrency BAT tokens for viewing ads
- This Python program uses the pyautogui library to detect a Brave ad popup (Only on Windows 10), which will then open and close the ad, returning the cursor to the previous location uninterrupted
- Meant to be used during active computer use, Brave Browser is able to detect human vs machine interactions to prevent ad farming

### Improvements (TODO)
- User Interface for controlling settings
- Add detection for MacOS, Linux

### User Interface (TODO)
- Tkinter UI launches when executable runs
- Displays elapsed time, number of ads clicked
- Button to turn bot On/Off
- Spinbox input to change time variables
![User Interface v1]("https://github.com/mrmendoza171/brave-ad-clicker/blob/main/images/other/ui-example-1.png")


### Performance Tweaks
#### No significant performance issues so far, possible upgrades to consider
- Reduce screenshot size to where popup appears
- Adjust wait time intervals

#### Resources
- https://www.geeksforgeeks.org/taking-screenshots-using-pyscreenshot-in-python/
