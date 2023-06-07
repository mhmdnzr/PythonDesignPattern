from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class WebApp(Implementation):
    def operation_implementation(self) -> str:
        return "Web app: Here's the result on the platform A."


class Desktop(Implementation):
    def operation_implementation(self) -> str:
        return "Desktop device: Here's the result on the platform."


class Mobile(Implementation):
    def operation_implementation(self) -> str:
        return "Mobile device: Here's the result on the platform."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = WebApp()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = Desktop()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print("\n")
    mobile_implementation = Mobile()
    mobile_abs = ExtendedAbstraction(mobile_implementation)
    client_code(mobile_abs)
