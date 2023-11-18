import random
from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont
from jproperties import Properties
from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES, COLORS, COUNTRIES


def randomly_select_gender() -> str:
    """
    Generates random gender (male or female)
    :return: str
    """
    genders = ["Male", "Female"]
    selected_gender = random.choice(genders)
    return selected_gender


def randomly_generate_date_of_birth() -> str:
    """
    Generates random date of birth

    :return: str
    """
    # Define the age range (18 to 80 years)
    min_age = 18
    max_age = 80

    # Calculate birthdate based on the age range
    global today
    today = datetime.now()
    random_days = random.randint(min_age * 365, max_age * 365)
    birthdate = today - timedelta(days=random_days)

    return birthdate.strftime("%d-%m-%Y")


def generate_random_id(length=8) -> str:
    """
    Generates random id

    :param length: 8
    :return: str
    """
    # Generate a random ID with the specified length
    return ''.join(random.choices('0123456789', k=length))


def generate_id_cards(configurations):
    """
    Creates an id card and saves it to specified location
    :param configurations: contains configured properties

    """
    # Set the width and height to be configured

    width = 600
    height = 400

    # Create new image with the dimensions above
    id_card = Image.new(mode="RGB", size=(width, height), color=(227, 235, 224))

    # Choose a font and size
    # font = ImageFont.load_default()  # You can replace this with your desired font and size
    font = ImageFont.truetype(configurations.get('ROBOTO_FONT_PATH').data)

    # Define labels
    name_label = 'Name : '
    gender_label = 'Gender : '
    date_of_birth_label = 'Date of Birth : '
    id_number_label = 'ID : '
    country_label = 'Country : '

    # Define the text
    name = get_random_name(combo=[ADJECTIVES, COLORS])
    gender = randomly_select_gender()
    date_of_birth = randomly_generate_date_of_birth()
    id_number = generate_random_id()
    country = get_random_name(combo=[COUNTRIES])
    image_path = ''
    if gender == 'Female':
        image_path = configurations.get('FEMALE_IMG_PATH').data
    elif gender == 'Male':
        image_path = configurations.get('MALE_IMG_PATH').data

    # open the image
    user_image = Image.open(image_path)

    # Resize the image
    resized_image = user_image.resize((200, 200))
    id_card.paste(resized_image, (10, 100))

    # Label positions : Adjust the coordinates based on your preference
    id_label_position = (300, 100)
    name_label_position = (300, 140)
    gender_label_position = (300, 180)
    dob_label_position = (300, 220)
    country_label_position = (300, 260)

    # Text positions : Adjust the coordinates based on your preference
    id_position = (400, 100)
    name_position = (400, 140)
    gender_position = (400, 180)
    dob_position = (400, 220)
    country_position = (400, 260)

    # Create a draw object to add text to the image
    draw = ImageDraw.Draw(id_card)

    # Add id and id label to the image
    draw.text(id_label_position, id_number_label, font=font, fill=(0, 0, 0))
    draw.text(id_position, id_number, font=font, fill=(0, 0, 0))

    # Add name and name label to the image
    draw.text(name_label_position, name_label, font=font, fill=(0, 0, 0))
    draw.text(name_position, name, font=font, fill=(0, 0, 0))

    # Add gender and gender label to the image
    draw.text(gender_label_position, gender_label, font=font, fill=(0, 0, 0))
    draw.text(gender_position, gender, font=font, fill=(0, 0, 0))

    # Add dob and dob label to the image
    draw.text(dob_label_position, date_of_birth_label, font=font, fill=(0, 0, 0))
    draw.text(dob_position, date_of_birth, font=font, fill=(0, 0, 0))

    # Add country and country label to the image
    draw.text(country_label_position, country_label, font=font, fill=(0, 0, 0))
    draw.text(country_position, country, font=font, fill=(0, 0, 0))

    # Save the image with the added text
    id_card.save(configurations.get('OUTPUT_PATH').data + name + ".png")


if __name__ == '__main__':

    # Read the properties file
    configs = Properties()
    with open('../application.properties', 'rb') as config_file:
        configs.load(config_file)

    # Loop 100 times to create 100 ids
    for count in range(1, 101):
        generate_id_cards(configs)

    print("Done")
