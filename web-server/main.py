import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/") # decorador donde indicamos la ruta desde la web para poder ingresar
def get_list():
  return [1, 2, 3]

@app.get("/contact", response_class = HTMLResponse) # version HTML
def get_list():
  return """
   <h1>Hola soy una página</h1>
   <p>Soy un párrafo</p>
  """

def run():
  store.get_categories()

if __name__ == "__main__":
  run()