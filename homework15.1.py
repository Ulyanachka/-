import logging
import argparse
import sys

# РќР°СЃС‚СЂРѕР№РєР° Р»РѕРіРёСЂРѕРІР°РЅРёСЏ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls.archive_text.append(text)
            cls.archive_number.append(number)
            logging.info(f"РРЅРёС†РёР°Р»РёР·Р°С†РёСЏ Р°СЂС…РёРІР° СЃ Р·Р°РїРёСЃСЊСЋ: {text}, {number}")
        else:
            cls.archive_text.append(text)
            cls.archive_number.append(number)
            logging.info(f"Р”РѕР±Р°РІР»РµРЅРёРµ РІ Р°СЂС…РёРІ Р·Р°РїРёСЃРё: {text}, {number}")
        return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. " \
               f"Also {Archive.archive_text} and {Archive.archive_number}"

    def __repr__(self):
        return f"Archive({self.text!r}, {self.number!r})"

def main(text, number):
    try:
        archive = Archive(text, number)
        print(archive)
    except Exception as e:
        logging.error(f"РћС€РёР±РєР° РїСЂРё СЂР°Р±РѕС‚Рµ СЃ Р°СЂС…РёРІРѕРј: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Р Р°Р±РѕС‚Р° СЃ Р°СЂС…РёРІРѕРј Р·Р°РїРёСЃРµР№")
    parser.add_argument("text", type=str, help="РўРµРєСЃС‚ РґР»СЏ РґРѕР±Р°РІР»РµРЅРёСЏ РІ Р°СЂС…РёРІ")
    parser.add_argument("number", type=float, help="Р§РёСЃР»Рѕ РґР»СЏ РґРѕР±Р°РІР»РµРЅРёСЏ РІ Р°СЂС…РёРІ")

    args = parser.parse_args()

    main(args.text, args.number)

#python homework15.1.py "Тестовая запись" 123.45