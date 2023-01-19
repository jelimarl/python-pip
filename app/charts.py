import matplotlib.pyplot as plot

def generate_bar_chart(name, labels, values):
  # figura y coordenadas
  fig, ax = plot.subplots()
  ax.bar(labels, values)
  plot.savefig(f"./imgs/{name}.png")
  plot.close()

def generate_pie_chart(labels, values):
  fig, ax = plot.subplots()
  ax.pie(values, labels = labels)
  # en el centro y en forma de círculo (con ese axis equal)
  ax.axis("equal")
  plot.savefig("pie.png")
  plot.close()

if __name__ == "__main__":
  labels = ["a", "b", "c"]
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)