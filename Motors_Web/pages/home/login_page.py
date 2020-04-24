__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
# import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Base
    _common_loc_type = 'xpath'
    _search_main_page = "//span[@class='sp__btn-title']"
    _location_postcode = "//input[@type='text']" ## <input type="text" maxlength="10" autocomplete="off" placeholder="Postcode" name="PostCode" value="OX30LF" style="" xpath="1">
    _make_model = "//select[@name='Make']"
    ## <select name="Make" xpath="1"><option value="*">Make (Any)</option>
    # <option value="Abarth">Abarth</option><option value="AC">AC</option><option value="Aixam">Aixam</option><option value="Alfa Romeo">Alfa Romeo</option>
    # <option value="Aprilia">Aprilia</option><option value="Ariel">Ariel</option><option value="Aston Martin">Aston Martin</option>
    # <option value="Audi">Audi</option><option value="Austin">Austin</option><option value="Bentley">Bentley</option><option value="BMW">BMW</option>
    # <option value="Buick">Buick</option><option value="Cadillac">Cadillac</option><option value="Caterham">Caterham</option>
    # <option value="Chevrolet">Chevrolet</option><option value="Chrysler">Chrysler</option><option value="Citroen">Citroen</option>
    # <option value="Corvette">Corvette</option><option value="Dacia">Dacia</option><option value="Daewoo">Daewoo</option><option value="DAF">DAF</option>
    # <option value="Daihatsu">Daihatsu</option><option value="Daimler">Daimler</option><option value="DAX">DAX</option><option value="Dodge">Dodge</option>
    # <option value="DS">DS</option><option value="Ducati">Ducati</option><option value="Ferrari">Ferrari</option><option value="Fiat">Fiat</option>
    # <option value="Ford">Ford</option><option value="Ginetta">Ginetta</option><option value="Great Wall">Great Wall</option>
    # <option value="Harley-Davidson">Harley-Davidson</option><option value="Hillman">Hillman</option><option value="Honda">Honda</option>
    # <option value="Hummer">Hummer</option><option value="Hyundai">Hyundai</option><option value="Infiniti">Infiniti</option><option value="Isuzu">Isuzu</option>
    # <option value="Isuzu Trucks">Isuzu Trucks</option><option value="Iveco">Iveco</option><option value="Jaguar">Jaguar</option><option value="Jeep">Jeep</option>
    # <option value="Jensen">Jensen</option><option value="Kawasaki">Kawasaki</option><option value="Kia">Kia</option><option value="KTM">KTM</option>
    # <option value="Lada">Lada</option><option value="Lamborghini">Lamborghini</option><option value="Lancia">Lancia</option><option value="Land Rover">Land Rover</option>
    # <option value="LDV">LDV</option><option value="Lexus">Lexus</option><option value="Lincoln">Lincoln</option><option value="Lotus">Lotus</option>
    # <option value="LTC">LTC</option><option value="Malaguti">Malaguti</option><option value="Maserati">Maserati</option><option value="Maybach">Maybach</option>
    # <option value="Mazda">Mazda</option><option value="McLaren">McLaren</option><option value="Mercedes-Benz">Mercedes-Benz</option><option value="MG">MG</option>
    # <option value="Microcar">Microcar</option><option value="MINI">MINI</option><option value="Mitsubishi">Mitsubishi</option><option value="Mitsubishi Fuso">Mitsubishi Fuso</option>
    # <option value="Mitsuoka">Mitsuoka</option><option value="Morgan">Morgan</option><option value="Morris">Morris</option><option value="Nissan">Nissan</option>
    # <option value="Opel">Opel</option><option value="Perodua">Perodua</option><option value="Peugeot">Peugeot</option><option value="Piaggio">Piaggio</option>
    # <option value="Pontiac">Pontiac</option><option value="Porsche">Porsche</option><option value="Proton">Proton</option><option value="Renault">Renault</option>
    # <option value="Rolls-Royce">Rolls-Royce</option><option value="Rover">Rover</option><option value="Saab">Saab</option><option value="SEAT">SEAT</option>
    # <option value="Skoda">Skoda</option><option value="smart">smart</option><option value="Ssangyong">Ssangyong</option><option value="Subaru">Subaru</option>
    # <option value="Suzuki">Suzuki</option><option value="Talbot">Talbot</option><option value="Tesla">Tesla</option><option value="Toyota">Toyota</option>
    # <option value="Triumph">Triumph</option><option value="TVR">TVR</option><option value="Vauxhall">Vauxhall</option><option value="Volkswagen">Volkswagen</option>
    # <option value="Volvo">Volvo</option><option value="Westfield">Westfield</option><option value="Yamaha">Yamaha</option></select>
    _min_price = "//select[@name='MinPrice']"
    _max_price = "//select[@name='MaxPrice']"
    _reset_button = "//button[@class='btn btn--alt btn--ghost reset']"

    def clickButtonAfterWait(self, locator, locatorType):
        elementone = self.waitForElement(locator, locatorType, timeout=5, pollFrequency=1)
        self.elementClick(element=elementone)

    def continueButtonClick(self, locator, locatorType):
        if self.isElementPresent(locator, locatorType) == True:
            self.elementClick(locator, locatorType)

    def motorsSite(self):
        iMotorsURL = 'https://www.motors.co.uk'
        print("\nMotors URL : " + iMotorsURL)
        self.log.info("Motors URL : " + iMotorsURL)
        self.driver.get(iMotorsURL)

    def gotoMotorsMainSite(self, poctcode):
        self.motorsSite()
        print('VALUE = ' + str(self.getValue(self._location_postcode, self._common_loc_type)))
        self.sendKeys(poctcode, self._location_postcode, self._common_loc_type)
        self.clickButtonAfterWait(self._search_main_page, self._common_loc_type)


