# API_flask_cloud
 On vous permet d'obtenir en JSON les taux d'émission de CO2 en fonction de différents pays

    Pour avoir la valeur d'émission totale la plus récente pour un pays demandé :

    Taper votre localhost suivi de : '/latest_by_country/' et 'le pays demandé'.
    Exemple :
    Taper: http://localhost:5000/latest_by_country/Bulgaria
    et vous optiendrez:
    {"Country": "Bulgaria", "Year": 2017, "Emissions": 42819.932}
    Pour avoir la valeur moyenne des émissions totales pour une année demandée :

    Taper votre localhost suivi de : '/average_by_year/' et 'l'année désirée'.
    Exemple :
    Taper: http://localhost:5000/average_by_year/2017
    et vous optiendrez:
    {"Year": "2017", "Total": 219666.446}
    Pour avoir les émissions par habitant d'un pays donné :

    Taper votre localhost suivi de : '/per_capita/' et 'le nom du pays voulu'.
    Exemple :
    Taper: http://localhost:5000//per_capita/Morocco
    et vous optiendrez:
    {"1975": 0.543, "1985": 0.722, "1995": 0.963, "2005": 1.285, "2010": 1.432, "2015": 1.591, "2016": 1.568, "2017": 1.627}
