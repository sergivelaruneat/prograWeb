from app import create_app;
# Creamos la aplicacion
app = create_app()

# Ejecucion del archivo y activa el debug
if __name__ == '__main__':
    app.run(debug=True)