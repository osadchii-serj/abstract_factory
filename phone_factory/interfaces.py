from abc import ABC, abstractmethod


class PhoneComponentsFactory(ABC):

    @abstractmethod
    def create_a_battery(self):
        pass

    @abstractmethod
    def create_processor(self):
        pass

    @abstractmethod
    def create_a_camera(self):
        pass

    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_model(self):
        pass


class Display(ABC):

    @abstractmethod
    def display_type(self):
        pass


class Processor(ABC):

    @abstractmethod
    def power(self):
        pass


class Camera(ABC):

    @abstractmethod
    def permission(self):
        pass


class Battery(ABC):

    @abstractmethod
    def capacity(self):
        pass
