# Image-Generator

## Overview
This project is an ID card generator that creates random ID cards with personalized information such as name, gender, date of birth, and more. It uses the PIL library for image manipulation and the unique_names_generator library for generating random names.

## Features
- Generates random gender (male or female).
- Generates random date of birth within a specified age range.
- Generates random ID numbers.
- Creates ID cards with personalized information.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)
- jproperties
- unique_names_generator

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/id-card-generator.git
    cd id-card-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the application by updating the `application.properties` file with the required paths and settings.

## Usage
Run the script to generate ID cards:

```bash
python id_card_generator.py
```
This will create 100 ID cards with random information and save them to the specified output path.

## Configuration
Update the `application.properties` file with the paths and settings for fonts, image paths, and output location.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/)
- [jproperties](https://pypi.org/project/jproperties/)
- [unique_names_generator](https://pypi.org/project/unique-names-generator/)
