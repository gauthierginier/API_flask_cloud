import pandas
import logging


def readcsv(*colonnes):
    """
    Cette fonction permet de lire le fichier csv avec pandas.read_csv(),
    sans prendre ne compte les 2 premières lignes avec header=2,
    renommant chaques colonnes avec names=[],
    et permet d'utiliser les colonnes voulues avec usecols=(colonnes),
    d'encoder le fichier en 'utf-8' et uniformise la langue et le format
    de certain pays.

    This function reads the csv file with pandas.read_csv(),
    without taking into account the first 2 lines with header=2,
    renaming each column with names=[],
    and allows to use the desired columns with usecols=(columns),
    to encode the file in 'utf-8' and standardize the language and format.
    of certain countries.
    """
    logging.debug(f"Utilisation de la fonction readcsv({colonnes})")
    logging.info("Lecture du fichier csv")
    df = pandas.read_csv(
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
        usecols=colonnes,
        encoding='utf-8')
    df['Region'] = df['Region'].replace(
        ['Bolivia (Plurin. State of)'], 'Bolivia')
    df['Region'] = df['Region'].replace(
        ['China, Hong Kong SAR'], 'China')
    df['Region'] = df['Region'].replace(
        ['Côte d’Ivoire'], 'Ivory Coast')
    df['Region'] = df['Region'].replace(
        ["Dem. People's Rep. Korea"], 'North Korea')
    df['Region'] = df['Region'].replace(
        ['Dem. Rep. of the Congo'], 'Congo')
    df['Region'] = df['Region'].replace(
        ['Iran (Islamic Republic of)'], 'Iran')
    df['Region'] = df['Region'].replace(
        ['Republic of Korea'], 'South Korea')
    df['Region'] = df['Region'].replace(
        ['United Rep. of Tanzania'], 'Tanzania')
    df['Region'] = df['Region'].replace(
        ['Venezuela (Boliv. Rep. of)'], 'Venezuela')
    df['Region'] = df['Region'].str.lower()
    return df
