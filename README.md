# Reto IV: Herencia Python #

Crearemos una clase Serie con las siguientes características:

- Sus atributos son titulo, numero de temporadas, entregado, genero y creador.

- Por defecto, el numero de temporadas es de 3 temporadas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
Los métodos que se implementara serán:

- Métodos get de todos los atributos, excepto de entregado.
- Métodos set de todos los atributos, excepto de entregado.
- Sobrescribe los métodos __str__.

Crearemos una clase Videojuego con las siguientes características:

- Sus atributos son titulo, horas estimadas, entregado, genero y compañía.

- Por defecto, las horas estimadas serán de 10 horas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.

Los métodos que se implementara serán:

- Métodos get de todos los atributos, excepto de entregado.
- Métodos set de todos los atributos, excepto de entregado.
- Sobrescribe los métodos __str__.

Como vemos, en principio, las clases anteriores no son padre-hija, pero si tienen en común, por eso vamos a hacer una interfaz Entregable con los siguientes métodos:

- entregar(): cambia el atributo prestado a true.

- devolver(): cambia el atributo prestado a false.

- isEntregado(): devuelve el estado del atributo prestado.
- Método compareTo (Object a), compara las horas estimadas en los videojuegos y en las series el numero de temporadas. Como parámetro que tenga un objeto.

Ahora crea una aplicación ejecutable y realiza lo siguiente:

1. Crea dos arrays, uno de Series y otro de Videojuegos, de 5 posiciones cada uno.
2. Crea un objeto en cada posición del array, con los valores que desees, puedes usar distintos constructores.

3. Entrega algunos Videojuegos y Series con el método entregar().

4. Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos, devuélvelos.

5. Por último, indica el Videojuego tiene más horas estimadas y la serie con mas temporadas. Muéstralos en pantalla con toda su información (usa el método __str__).