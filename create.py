import os
import json
import datetime


def read_text(txt):
    with open(os.path.join(os.path.dirname(__file__), txt), "r") as f:
        text = f.read()
    return text


def create_text(str):
    with open(os.path.join(os.path.dirname(__file__), "message.txt"), "w") as f:
        f.write(str)


def read_database(data):
    with open(os.path.join(os.path.dirname(__file__), data), "r") as f:
        database = json.load(f)
    return database


def read_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "r") as f:
        input = json.load(f)
    return input


def convert_date(date):
    date_fields = []
    date_fields = date.rstrip("\n").split("/")
    raw_date = datetime.datetime(
        int(date_fields[0]), int(date_fields[1]), int(date_fields[2])
    )
    date_de = raw_date.strftime("%d.%m.%y")
    if date_fields[2] == "1" or date_fields[2] == "01":
        date_en = raw_date.strftime("%-dst %B %Y")
    elif date_fields[2] == "2" or date_fields[2] == "02":
        date_en = raw_date.strftime("%-dnd %B %Y")
    elif date_fields[2] == "3" or date_fields[2] == "03":
        date_en = raw_date.strftime("%-drd %B %Y")
    else:
        date_en = raw_date.strftime("%-dth %B %Y")
    return date_de, date_en


def main():
    # read employee-database
    database = read_database("data.json")
    # read input-file
    input = read_input("input.json")
    # set sender and representative
    sender = database[input["sender"]]
    representative = database[input["representative"]]
    # set dates
    date_from_de, date_from_en = convert_date(input["date_from"])
    date_to_de, date_to_en = convert_date(input["date_to"])
    # set variables
    representative_fullname = (
        representative["first_name"] + " " + representative["last_name"]
    )
    if representative["gender"] == "male":
        foa_de = "Herrn"
        foa_en = "Mr."
    else:
        foa_de = "Frau"
        foa_en = "Mrs."
    representative_lastname = representative["last_name"]
    representative_email = representative["email"]
    representative_phone_de = "0351 48205 " + representative["phone_extension"]
    representative_phone_en = "0049 (0)351 48205 " + representative["phone_extension"]
    sender_fullname = sender["first_name"] + " " + sender["last_name"]
    # create text
    text = read_text("text.txt").format(
        date_from_de=date_from_de,
        date_to_de=date_to_de,
        date_from_en=date_from_en,
        date_to_en=date_to_en,
        representative_fullname=representative_fullname,
        foa_de=foa_de,
        foa_en=foa_en,
        representative_lastname=representative_lastname,
        representative_email=representative_email,
        representative_phone_de=representative_phone_de,
        representative_phone_en=representative_phone_en,
        sender_fullname=sender_fullname,
    )
    create_text(text)


if __name__ == "__main__":
    main()