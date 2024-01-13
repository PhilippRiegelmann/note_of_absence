# GERMAN AND ENGLISH NOTE OF ABSENCE

This Python script is used to create note of absence in German and English.
To use this script you first need to update the following files:

## data.json

```
{
    "company_basic_number_de": "0351 123456",
    "company_basic_number_en": "0049 (0)351 123456",
    "employees": {
        "pr": {
            "first_name": "Philipp",
            "last_name": "Riegelmann",
            "gender": "male",
            "email": "philipp.riegelmann@mail.com",
            "phone_extension": "042"
        },
        "jd": {
            "first_name": "Jane",
            "last_name": "Doe",
            "gender": "female",
            "email": "jane.doe@mail.com",
            "phone_extension": "001"
        }
    }
}
```

- company_basic_number_de: Fill in the basic number of your company in german format
- company_basic_number_en: Fill in the basic number of your company in english format
- employees (Please choose a own key for each employee):
  - first_name: First name of employee
  - last_name: Last name of employee
  - gender: male / female
  - email: Email adress of employee
  - phone_extension: Phone extension of employee

## input.json

```
{
"sender":"pr",
"representative":"jh",
"date_from":"2022/04/03",
"date_to":"2022/05/03"
}
```

- sender: Key of the employee, which wants to create the note of absence
- representative: Key of the employee representing the sender
- date_from: Start of the absence in english format YYYY/MM/DD
- date_to: End of the absence in english format YYYY/MM/DD

# Usage

To create the file message.txt, which will include your note of absence run the following command in your terminal.

```
python create.py
```
