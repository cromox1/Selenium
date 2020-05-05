# Selenium

## MengKome (Rosli_Talib Django)

### https://mengkome.pythonanywhere.com/ 

Assignment 1 (Test1) :

- Launch Google Website
- Search for "github cromox1"
- Select the main cromox1 github link
- Go to main page github cromox1
- Check all the repositories that cromox1 has

Assignment 2 (Test2) :

- Go to main page https://mengkome.pythonanywhere.com/
- Login (with admin username / passwd = bacaone / qawsed123456 )
- Check some infos inside 
  - go & click Users button
  - click at your own user
  - check email address & date joined
  - go back to home page
- Logout

## 1) Basic UnitTest :

To run :

### python3 testOne_basictest.py

## 2) pytest Automation Framework

MengKome Automation Framework consise these directories:

1) apps
2) base
3) configfiles
4) features
5) pages
6) tests
7) utilities
8) screenshots (screenshot's pictures - create automatically if ERROR occured)

To run tests (example) :

### py.test -v -s tests/p01google/p01searchgithubcromox1_test1.py --browser "$browser"

"$browser" = [ ie / chrome / firefox / opera ]

