import pandas
import logging


def readcsv(*colonnes):
    """
    Cette fonction permet de lire le fichier csv avec pandas.read_csv(),
    sans prendre ne compte les 2 premières lignes avec header=2,
    renommant chaques colonnes avec names=[],
    et permet d'utiliser les colonnes voulues avec usecols=(colonnes).

    This function reads the csv file with pandas.read_csv(),
    without taking into account the first 2 lines with header=2,
    renaming each column with names=[],
    and allows to use the desired columns with usecols=(columns).
    """
    logging.debug(f"Utilisation de la fonction readcsv({colonnes})")
    logging.info("Lecture du fichier csv")
    return pandas.read_csv(
        'data.csv',
        header=2,
        names=[
            'id',
            'Region',
            'Year',
            'Emission',
            'Value',
            'Footnote',
            'Source'],
        usecols=colonnes)
