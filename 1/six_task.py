import requests
import json


def fetch_country_data():
    url = 'https://restcountries.com/v3.1/all'
    try:
        response = requests.get(url)
        response.raise_for_status()
        countries = response.json()

        html_content = "<html><head><title>Country Data</title></head><body>"
        html_content += "<h1>List of Countries</h1><ul>"

        for country in countries:
            country_name = country.get('name', {}).get('common', 'Unknown')
            capital = country.get('capital', ['Unknown'])[0]
            region = country.get('region', 'Unknown')
            population = country.get('population', 'Unknown')

            html_content += f"""
                <li>
                    <h2>{country_name}</h2>
                    <p><strong>Capital:</strong> {capital}</p>
                    <p><strong>Region:</strong> {region}</p>
                    <p><strong>Population:</strong> {population}</p>
                </li>
            """

        html_content += "</ul></body></html>"

        with open('data/countries.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")

fetch_country_data()