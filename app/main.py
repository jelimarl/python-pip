import utils
import read_csv
import charts
import pandas as pd

def run():
  #dataframe
  df = pd.read_csv("data.csv")
  # equivale a filtrar
  df = df[df["Continent"] == "Africa"]
  # valores de una columna
  countries = df["Country/Territory"].values
  percentages = df["World Population Percentage"].values

  data, data_countries, data_percentage = read_csv.read_csv("data.csv")
  #data = list(filter(lambda item : item["Continent"] == "South America", data))
  country = input("Type Country: ")
  
  result = utils.population_by_country(data, country.title())
  print(result)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)
  
  ''' 
  countries = list(map(lambda item : item["Country/Territory"], data))
  data_percentage = list(map(lambda item : item["World Population Percentage"], data))
  percentages = utils.get_population_percentage(data_percentage)
  '''
  charts.generate_pie_chart(countries, percentages)
 
if __name__ == "__main__":
  run()