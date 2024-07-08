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

---

¡Gracias por usar nuestra Pokédex Pokémon! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.
