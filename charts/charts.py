import matplotlib.pyplot as plot

def generate_pie_chart():
  labels = ["A", "B", "C"]
  values = [200, 34, 120]

  fig, ax = plot.subplots()
  ax.pie(values, labels = labels)
  plot.savefig("pie.png")
  plot.close()