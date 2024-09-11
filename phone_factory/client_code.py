from interfaces import PhoneComponentsFactory
from phones import XiaomiRedmiNote13
from phones import SamsungGalaxyS24
from phones import AppleIPhone15Pro
from phones import AppleIPhone13Pro
from phones import HuaweiMate60Pro
from phones import GooglePixel8Pro
from phones import HuaweiNova12
from phones import SiemensME45
from phones import NokiaXR21

from random import choice


def client_code(factory: PhoneComponentsFactory):
    print()
    print(factory.create_model())
    print(factory.create_a_camera().permission())
    print(factory.create_display().display_type())
    print(factory.create_a_battery().capacity())
    print(factory.create_processor().power())
    print("=" * 50)


if __name__ == "__main__":

    list_phones = [
        XiaomiRedmiNote13(),
        SamsungGalaxyS24(),
        AppleIPhone15Pro(),
        HuaweiMate60Pro(),
        AppleIPhone13Pro(),
        GooglePixel8Pro(),
        HuaweiNova12(),
        SiemensME45(),
        NokiaXR21(),
    ]

    for _ in range(20):
        client_code(choice(list_phones))
