import logging
from func_annexe_o import allcountries, allyears, allcontinent
from func_annexe_o import bycountry, byyear, bypercapita, bycontinent
from flask import Flask, abort, jsonify, render_template
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    """
    Cette fonction permet de vérifier que la route pour l'API
    fonctionne en arrivant sur le manuel du fonctionnement de l'API .

    This function checks that the route for the PLC
    works by arriving on the manuel of the operation of the API .
    ---
    example request for API
    ---
    get: http://localhost:5000/
    result : Manuel API en page HTML
      description: Manuel de l'API en HTML
    """
    logging.debug("Utilisation de la fonction index()")
    logging.debug("L'app fonctionne correctement")
    # utilisé pour tester si l'app fonctionne bien
    return render_template('index.html')


@app.route('/latest_by_country/<country>')
def by_country(country):
    """
    Cette fonction est utilisé si la route '/latest_by_country/<country>'
    est utilisée.
    Si le pays choisi est dans la liste des pays de la fonction allcountries()
    alors on appel la fonction bycountry()
    Sinon un message d'erreur nous préviens que le pays choisi n'est pas dans
    la liste.

    This function is used if the route '/latest_by_country/<country>' is used.
    is used.
    If the selected country is in the list of countries in the allcountries()
    function then we call the function bycountry()
    Otherwise an error message will warn us that the selected country is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000/latest_by_country/bulgaria
    result : {"Country": "Bulgaria", "Year": 2017, "Emissions": 42819.932}
      description: print the latest entry for total CO2 emissions
    in Thousands of tons.
    """
    # on veut la valeur la plus récente
    # des emissions totales pour le pays demandé
    logging.debug(f"Utilisation de la fonction by_country({country})")
    if country.lower() in allcountries():
        logging.debug(f"Pays demandé : {country}")
        return jsonify(bycountry(country.lower()))

    else:
        logging.warning(f"Le pays {country} n'est pas dans la liste")
        abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    """
    Cette fonction est utilisé si la route '/average_by_year/<year>'
    est utilisée.
    Si l'année choisie est dans la liste des années de la fonction allyears()
    alors on appel la fonction byyear()
    Sinon un message d'erreur nous préviens que l'année choisie n'est pas dans
    la liste.

    This function is used if the route '/average_by_year/<year>'.
    is used.
    If the chosen year is in the list of years in the allyears() function
    then we call the byyear() function
    Otherwise an error message will warn us that the chosen year is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000/average_by_year/2017
    result : {"Year": "2017", "Total": 219666.446}
      description: print average total CO2 emissions (in Thousands of tons)
    worldwide.
    """
    # on cherche la moyenne des émissions
    # totales au niveau mondial pour une année demandée
    logging.debug(f"Utilisation de la fonction average_for_year({year})")
    try:
        if int(year) in allyears() and len(year) == 4:
            logging.debug(f"Année demandée : {year}")
            return jsonify(byyear(year))
        else:
            logging.warning(f"L'année {year} n'est pas dans la liste")
            abort(404)
    except ValueError as e:
        logging.warning(f"Erreur : {e}")
        logging.warning(f"{year} n'est pas une année")
        abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    """
    Cette fonction est utilisé si la route '/per_capita/<country>'
    est utilisée.
    Si le pays choisi est dans la liste des pays de la fonction allcountries()
    alors on appel la fonction bypercapita()
    Sinon un message d'erreur nous préviens que le pays choisi n'est pas dans
    la liste.

    This function is used if the route '/per_capita/<country>' is used.
    is used.
    If the selected country is in the list of countries in the allcountries()
    function then we call the function bypercapita()
    Otherwise an error message will warn us that the selected country is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000//per_capita/Morocco
    result : {
        "1975": 0.543,
        "1985": 0.722,
        "1995": 0.963,
        "2005": 1.285,
        "2010": 1.432,
        "2015": 1.591,
        "2016": 1.568,
        "2017": 1.627
        }
      description: print CO2 emissions (in tons per capita)
    in relation to the different survey years.
    """
    logging.debug(f"Utilisation de la fonction per_capita({country})")
    if country.lower() in allcountries():
        logging.debug(f"Pays demandé : {country}")
        return jsonify(bypercapita(country.lower()))

    else:
        logging.warning(f"Le pays {country} n'est pas dans la liste")
        abort(404)


@app.route('/latest_by_continent/<continents>')
def by_continent(continents):
    """
    Cette fonction est utilisé si la route '/latest_by_continent/<country>'
    est utilisée.
    Si le continent choisi est dans la liste des continents de la
    fonction allcontinent() alors on appel la fonction bycontinent()
    Sinon un message d'erreur nous préviens que le continent choisi n'est pas
    dans la liste.

    This function is used if the route '/latest_by_continent/<continents>'
    is used.
    If the selected continent is in the list of continents in the
    allcontinent() function then we call the function bycontinent()
    Otherwise an error message will warn us that the selected country is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000/latest_by_continent/europe
    result : {
        "Continent": "Europe",
        "Year": 2017,
        "Emissions": 125318.85465853658
        }
      description: print the latest entry for total CO2 emissions
    in Thousands of tons.
    """
    # on veut la valeur la plus récente
    # des emissions totales pour le pays demandé
    logging.debug(
        f"Utilisation de la fonction by_continent({continents})")
    if continents.title() in allcontinent():
        logging.debug(f"Continent demandé : {continents}")
        return jsonify(bycontinent(continents.title()))
    else:
        logging.warning(
            f"Le continent {continents} n'est pas dans la liste")
        abort(404)


if __name__ == "__main__":
    app.config.update(
        ENV="development",
        JSON_SORT_KEYS=False
        )
    app.run(debug=True)
