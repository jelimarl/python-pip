import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)
    #print(header.index("2022 Population"))
    '''
    header[5] = "2022"
    header[6] = "2020"
    header[7] = "2015"
    header[8] = "2010"
    header[9] = "2000"
    header[10] = "1990"
    header[11] = "1980"
    header[12] = "1970"
    '''
    data = []
    data_countries = []
    data_percentage = []

    for row in reader:
      data_countries.append(row[1])
      data_percentage.append(row[-1])
      iterable = zip(header, row)
      #print("***" * 5)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data, data_countries, data_percentage

if __name__ == "__main__":
  data, data_countries, data_percentage = read_csv("./app/data.csv")

  #print(data[0])
  
  data[0].pop("Rank")
  data[0].pop("CCA3")
  data[0].pop("Country/Territory")
  data[0].pop("Capital")
  data[0].pop("Continent")
  data[0].popitem()
  data[0].popitem()
  data[0].popitem()
  data[0].popitem()

  country_keys = list(data[0].keys())
  country_values = list(data[0].values())
  
  new_values = list(map(lambda item : int(item), country_values))
  
  new_iterable = zip(country_keys, new_values)
  new_dict = {key: value for key, value in new_iterable}
  #print(new_dict)