# Proyecto Pokédex Pokémon

## Descripción

Este proyecto es una Pokédex en línea que muestra información detallada sobre los primeros 150 Pokémon. Utiliza Python 3.11.5 junto con Flask 3.0.0 para el backend y HTML, CSS y JavaScript para el frontend. La información de los Pokémon se obtiene de dos APIs:

- [PokeApi](https://pokeapi.co/): Para obtener información detallada de cada Pokémon, como sus estadísticas, tipos, descripción, número, género, etc.
- [Pokemon Database](https://pokemondb.net/): Para obtener imágenes de los Pokémon, tanto en su forma normal como shiny.

## Características

- **Página Principal:** Lista de los primeros 150 Pokémon.
- **Buscador:** Permite buscar un Pokémon por su nombre y acceder a su ficha técnica.
- **Ficha Técnica:** Muestra información detallada de un Pokémon específico y permite navegar al siguiente o anterior Pokémon usando botones tipo flecha.
- **Navegación Directa:** Desde la lista principal, se puede hacer clic en cualquier Pokémon para ver su ficha técnica.
- **Página de Pokémon No Encontrado:** Se muestra cuando se busca un Pokémon con un nombre incorrecto.

## Tecnologías Utilizadas

- **Backend:**
  - Python 3.11.5
  - Flask 3.0.0
- **Frontend:**
  - HTML
  - CSS
  - JavaScript

## Instalación y Uso

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/pokedex-pokemon.git
    cd pokedex-pokemon
    ```

2. **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar la aplicación:**

    ```bash
    flask run
    ```

5. **Abrir el navegador:**

    Navegar a `http://127.0.0.1:5000` para ver la aplicación en acción.

## Estructura del Proyecto

pokedex-pokemon/
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── templates/
│ ├── index.html
│ ├── pokemon.html
│ └── not_found.html
├── app.py
├── requirements.txt
└── README.md


- **static/**: Contiene los archivos estáticos (CSS, JavaScript, imágenes).
- **templates/**: Contiene las plantillas HTML.
- **app.py**: Archivo principal de la aplicación Flask.
- **requirements.txt**: Archivo de dependencias del proyecto.
- **README.md**: Este archivo.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza los cambios necesarios y commitea (`git commit -am 'Agrega nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

¡Gracias por usar nuestra Pokédex Pokémon! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.
