## PROYECTO EJEMPLO - MARKDOWN

1.  Crear el enviroment
- Opción 1: con VsCode
- Opción 2: con consola
2.  Agregar las siguientes dependencias en requirements.txt
- fastapi
- uvicorn
- pydantic
3.  Ejecutar
 - pip install -r requirements.txt

4.  En el archivo main.py
    ´´´bash
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello World"}

    @app.get("/sample/api")
    def read_sample():
        return {"message": "This is the sample API endpoint"}
    ´´´

5. Para ejecutar el servidor: 

uvicorn src.main:app --reload