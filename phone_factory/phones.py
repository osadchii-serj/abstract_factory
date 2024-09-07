from interfaces import PhoneComponentsFactory

from products import ProcessorQualcommSnapdragon
from products import ProcessorSamsungExynos
from products import ProcessorGoogleTensor
from products import ProcessorAppleASeries
from products import ProcessorHuaweiKirin
from products import ProcessorMediaTek
from products import ProcessorUnisoc

from products import BatteryNickelMetalHydride
from products import BatteryNickelMagnesium
from products import BatteryLithiumPolymer
from products import BatteryNickelCadmium
from products import BatteryLithiumIon

from products import DisplayAMOLED
from products import DisplayRetina
from products import DisplayOLED
from products import DisplayLCD

from products import Camera108MP
from products import Camera12MP
from products import Camera16MP
from products import Camera24MP
from products import Camera32MP
from products import Camera48MP
from products import Camera64MP
from products import Camera4K
from products import Camera8K


class AppleIPhone15Pro(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Apple IPhone 15 Pro"

    def create_processor(self):
        return ProcessorAppleASeries()

    def create_a_battery(self):
        return BatteryLithiumPolymer()

    def create_display(self):
        return DisplayAMOLED()

    def create_a_camera(self):
        return Camera48MP()

    def create_model(self):
        return self.__model


class AppleIPhone13Pro(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Apple IPhone 13 Pro Max"

    def create_processor(self):
        return ProcessorAppleASeries()

    def create_a_battery(self):
        return BatteryNickelMetalHydride()

    def create_display(self):
        return DisplayOLED()

    def create_a_camera(self):
        return Camera32MP()

    def create_model(self):
        return self.__model


class XiaomiRedmiNote13(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Xiaomi Redmi Note 13"

    def create_processor(self):
        return ProcessorQualcommSnapdragon()

    def create_a_battery(self):
        return BatteryNickelMagnesium()

    def create_display(self):
        return DisplayRetina()

    def create_a_camera(self):
        return Camera64MP()

    def create_model(self):
        return self.__model


class SamsungGalaxyS24(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Samsung Galaxy S24"

    def create_processor(self):
        return ProcessorSamsungExynos()

    def create_a_battery(self):
        return BatteryNickelCadmium()

    def create_display(self):
        return DisplayAMOLED()

    def create_a_camera(self):
        return Camera4K()

    def create_model(self):
        return self.__model


class GooglePixel8Pro(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Google Pixel 8 Pro"

    def create_processor(self):
        return ProcessorGoogleTensor()

    def create_a_battery(self):
        return BatteryNickelMetalHydride()

    def create_display(self):
        return DisplayLCD()

    def create_a_camera(self):
        return Camera8K()

    def create_model(self):
        return self.__model


class HuaweiMate60Pro(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Huawei Mate 60 Pro"

    def create_processor(self):
        return ProcessorHuaweiKirin()

    def create_a_battery(self):
        return BatteryLithiumIon()

    def create_display(self):
        return DisplayLCD()

    def create_a_camera(self):
        return Camera108MP()

    def create_model(self):
        return self.__model


class HuaweiNova12(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Huawei Nova 12"

    def create_processor(self):
        return ProcessorMediaTek()

    def create_a_battery(self):
        return BatteryLithiumIon()

    def create_display(self):
        return DisplayOLED()

    def create_a_camera(self):
        return Camera12MP()

    def create_model(self):
        return self.__model


class NokiaXR21(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Nokia XR21"

    def create_processor(self):
        return ProcessorUnisoc()

    def create_a_battery(self):
        return BatteryNickelCadmium()

    def create_display(self):
        return DisplayAMOLED()

    def create_a_camera(self):
        return Camera24MP()

    def create_model(self):
        return self.__model


class SiemensME45(PhoneComponentsFactory):

    def __init__(self) -> None:
        self.__model = "Siemens ME45"

    def create_processor(self):
        return ProcessorUnisoc()

    def create_a_battery(self):
        return BatteryNickelCadmium()

    def create_display(self):
        return DisplayLCD()

    def create_a_camera(self):
        return Camera16MP()

    def create_model(self):
        return self.__model
