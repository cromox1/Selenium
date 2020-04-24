# Selenium

## Pixit Media

### https://www.pixitmedia.com/ 

Assignment :

- Launch Google Website
- Search for pixitmedia
- Select the PRODUCTS menu link
- Select the PixStor Search link
- Validate that the VIEW DATASHEET button returns a PDF/download
- Select the CONTACT US menu link
- Fill in the form with your contact details.  
    For the Message text area insert the characters: This is a test for Jez
- Send the form

## 1) Basic UnitTest :

To run :

### python3 testOne_basictest.py

## 2) pytest Automation Framework

PixitMedia Automation Framework consise these directories:

1) apps
2) base
3) configfiles
4) features
5) pages
6) tests
7) utilities
8) screenshots (screenshot's pictures - create automatically if ERROR occured)

To run tests (example) :

### py.test -v -s tests/p01google/p01searchpixitmedia_tests.py --browser "$browser"

"$browser" = [ ie / chrome / firefox / opera ]

(has been simplify by bash script - xruntest.sh )

