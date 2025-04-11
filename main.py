from openai import OpenAI
import os
import csv
import pandas as pd




# attention ! "This project requires a paid OpenAI API key to function properly, because after the recent update, API usage is no longer free.
client = OpenAI(api_key="your_api_key")

def get_experiences(city):
    prompt = f"Create a list of 5 experiences in {city} that a tourist can do. Include title, description (at least 100 words), price in USD, and time."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


print(get_experiences("Tokyo"))

experiences = [
    {
        "title": "Tokyo Skytree Observation Deck",
        "description": "Enjoy a panoramic view of Tokyo from the tallest tower in Japan. Includes access to the observation decks and a complimentary drink at the top.",
        "price_usd": 25.0,
        "duration_hours": 2.0,
        "start_time": "10:00"
    },
    {
        "title": "Tsukiji Outer Market Food Tour",
        "description": "Taste the flavors of Japan on a guided walking tour through the historic Tsukiji Outer Market. Includes samples of sushi, tamagoyaki, and more.",
        "price_usd": 50.0,
        "duration_hours": 3.0,
        "start_time": "09:30"
    },
    {
        "title": "Asakusa Rickshaw Ride",
        "description": "Ride through the historic Asakusa district in a traditional rickshaw. A fun and unique way to explore the area with insights from your guide.",
        "price_usd": 40.0,
        "duration_hours": 1.0,
        "start_time": "14:00"
    },
    {
        "title": "Senso-ji Temple Guided Tour",
        "description": "Learn about Tokyo's oldest temple, Senso-ji, with a local guide. Tour includes a stroll down Nakamise Street and cultural background of the site.",
        "price_usd": 15.0,
        "duration_hours": 1.5,
        "start_time": "11:00"
    },
    {
        "title": "Evening Tokyo Cruise",
        "description": "Take a scenic evening cruise along Tokyo Bay. Enjoy city lights, a gentle breeze, and a relaxing atmosphere on board.",
        "price_usd": 60.0,
        "duration_hours": 2.5,
        "start_time": "18:30"
    }
]

# 1. create CSV doc
csv_filename = "tokyo_experiences.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "description", "price_usd", "duration_hours", "start_time"])
    writer.writeheader()
    writer.writerows(experiences)

# 2.  create SQL doc
sql_filename = "tokyo_experiences.sql"
with open(sql_filename, mode="w", encoding="utf-8") as sqlfile:
    sqlfile.write("CREATE TABLE experiences (\n")
    sqlfile.write("    id INTEGER PRIMARY KEY AUTOINCREMENT,\n")
    sqlfile.write("    title TEXT,\n")
    sqlfile.write("    description TEXT,\n")
    sqlfile.write("    price_usd REAL,\n")
    sqlfile.write("    duration_hours REAL,\n")
    sqlfile.write("    start_time TEXT\n")
    sqlfile.write(");\n\n")

    for exp in experiences:
        insert = f"""INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES (
    '{exp["title"].replace("'", "''")}',
    '{exp["description"].replace("'", "''")}',
    {exp["price_usd"]},
    {exp["duration_hours"]},
    '{exp["start_time"]}'
);\n\n"""
        sqlfile.write(insert)


# 4. SQL write doc
sql_filename = "tokyo_experiences.sql"
with open(sql_filename, mode="w", encoding="utf-8") as sqlfile:
    
    sqlfile.write("CREATE TABLE experiences (\n")
    sqlfile.write("    id INTEGER PRIMARY KEY AUTOINCREMENT,\n")
    sqlfile.write("    title TEXT,\n")
    sqlfile.write("    description TEXT,\n")
    sqlfile.write("    price_usd REAL,\n")
    sqlfile.write("    duration_hours REAL,\n")
    sqlfile.write("    start_time TEXT\n")
    sqlfile.write(");\n\n")

    # add 
    for exp in experiences:
        insert = f"""INSERT INTO experiences (title, description, price_usd, duration_hours, start_time)
VALUES (
    '{exp["title"].replace("'", "''")}',
    '{exp["description"].replace("'", "''")}',
    {exp["price_usd"]},
    {exp["duration_hours"]},
    '{exp["start_time"]}'
);\n\n"""
        sqlfile.write(insert)

print(" SQL dosyası oluşturuldu:", sql_filename)






