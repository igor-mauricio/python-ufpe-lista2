from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Client:
    name: str
    cpf: str

    @staticmethod
    def create(name: str, cpf: str) -> Client:
        return Client(name, cpf)
    
    @staticmethod
    def restore(name: str, cpf: str) -> Client:
        return Client(name, cpf)
    