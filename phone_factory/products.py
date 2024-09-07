from interfaces import Processor
from interfaces import Camera
from interfaces import Battery
from interfaces import Display


# Display ==============================================================================================================
class DisplayOLED(Display):

    def display_type(self):
        return "Дисплей - OLED (Organic Light Emitting Diode)"


class DisplayAMOLED(Display):

    def display_type(self):
        return "Дисплей - AMOLED (Active Matrix OLED)"


class DisplayLCD(Display):

    def display_type(self):
        return "Дисплей - LCD (Liquid Crystal Display)"


class DisplayRetina(Display):

    def display_type(self):
        return "Дисплей - Retina"


# Camera ==============================================================================================================
class Camera12MP(Camera):

    def permission(self):
        return "Камера 12 MP"


class Camera16MP(Camera):

    def permission(self):
        return "Камера 16 MP"


class Camera24MP(Camera):

    def permission(self):
        return "Камера 24 MP"


class Camera32MP(Camera):

    def permission(self):
        return "Камера 32 MP"


class Camera48MP(Camera):

    def permission(self):
        return "Камера 48 MP"


class Camera64MP(Camera):

    def permission(self):
        return "Камера 64 MP"


class Camera108MP(Camera):

    def permission(self):
        return "Камера 108 MP"


class Camera4K(Camera):

    def permission(self):
        return "Камера 4K"


class Camera8K(Camera):

    def permission(self):
        return "Камера 8K"


# Processor =============================================================================================================
class ProcessorQualcommSnapdragon(Processor):

    def power(self):
        return "Процессор - Qualcomm Snapdragon"


class ProcessorSamsungExynos(Processor):

    def power(self):
        return "Процессор - Samsung Exynos"


class ProcessorAppleASeries(Processor):

    def power(self):
        return "Процессор - Apple A-Series"


class ProcessorGoogleTensor(Processor):

    def power(self):
        return "Процессор - Google Tensor"


class ProcessorHuaweiKirin(Processor):

    def power(self):
        return "Процессор - Huawei Kirin"


class ProcessorMediaTek(Processor):

    def power(self):
        return "Процессор - MediaTek"


class ProcessorUnisoc(Processor):

    def power(self):
        return "Процессор - Unisoc"


# Battery ===============================================================================================================
class BatteryNickelMetalHydride(Battery):

    def capacity(self):
        return "Батарея - Никель-металлгидридные (NiMH) 4000 мАч"


class BatteryLithiumPolymer(Battery):

    def capacity(self):
        return "Батарея - Литий-полимерный (Li-Po) 5000 мАч"


class BatteryNickelCadmium(Battery):

    def capacity(self):
        return "Батарея - Никель-кадмиевые (NiCd) 5000 мАч"


class BatteryNickelMagnesium(Battery):

    def capacity(self):
        return "Батарея - Никель-магниевые (NiMH) 2000 мАч"


class BatteryLithiumIon(Battery):

    def capacity(self):
        return "Батарея - Литий-ионный (Li-Ion) 7000 мАч"
