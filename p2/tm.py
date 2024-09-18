import json
import pprint
import sys
import re
import xmltodict


class TuringMachine:

    def __init__(self, dict_tm=None, word=None) -> None:
        pass

    def run(self):
        """
        Implementar la lógica de la máquina de Turing, que debe seguir las reglas de las transiciones y simular el
        movimiento del cabezal de lectura/escritura a través de la cinta.
        :return: Un booleano para indicar si se llegó a un estado final o no.
        """
        return False


def turing_machine(turing_machine: dict, tape: str) -> (bool, str):
    """
    Crea y ejecuta una instancia de Máquina de Turing (TuringMachine).
    :param turing_machine:
    :param tape:
    :return: Tupla (aceptación True|False y cinta)
    """
    return None, None


def load_jff(filename):
    """
    Parsea un archivo JFLAP (.jff) en formato XML y lo convierte a formato JSON.
    :param filename:
    :return:
    """
    return data


if __name__ == '__main__':
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename, 'r') as data:
        pass
