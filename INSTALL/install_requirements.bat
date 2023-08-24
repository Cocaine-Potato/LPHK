@ECHO OFF

ECHO Starting Install...

pip install MouseInfo==0.1.3
pip install Pillow==9.3.0
pip install py-getch==1.0.1
pip install PyAutoGUI==0.9.50
pip install pygame==2.1.2
pip install PyGetWindow==0.0.8
pip install PyMsgBox==1.0.7
pip install pynput==1.6.8
pip install pyperclip==1.8.0
pip install PyRect==0.1.4
pip install PyScreeze==0.1.26
pip install python-xlib==0.27
pip install python3-xlib==0.15
pip install PyTweening==1.0.3
pip install six==1.14.0
pip install tkcolorpicker==2.1.3
pip install -e git+https://github.com/FMMT666/launchpad.py.git@master#egg=launchpad-py

ECHO Installed all needed packages successfully!
pause