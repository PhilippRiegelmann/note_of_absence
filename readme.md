# GERMAN AND ENGLISH ABSENCE NOTE

This Python script is used to create absence notes in German and English.
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
- company_basic_number_en: Fill in the basic number of your company in enlish format
- employees:
  - first_name: First name of employee
  - last_name: Last name of employee
  - gender: male / female
  - email: Email adress of employee
  - phone_extension: Phone extension of employee
    Please choose a own key for each employee

## input.json

```
{
"sender":"pr",
"representative":"jh",
"date_from":"2022/04/03",
"date_to":"2022/05/03"
}
```

- sender: Key of the employee, which wants to create the absence note
- representative: Key of the employee representing the sender
- date_from: Start of the absence in english format YYYY/MM/DD
- date_to: End of the absence in english format YYYY/MM/DD

# Usage

To create the file message.txt, which will include your absence note run the following command in your terminal.
''' python create.py '''
