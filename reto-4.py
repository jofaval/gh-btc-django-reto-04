from dataclasses import dataclass

@dataclass
class Entregable():
    """Interfaz para entidades que se entregan"""

    def entregar(self) -> None:
        self.entregado = True

    def devolver(self) -> None:
        self.entregado = False

    def isEntregado(self) -> bool:
        return self.entregado

    pass

@dataclass
class Serie(Entregable):
    """Clase para las Series del sistema"""
    titulo: str
    genero: str
    creador: str
    numero_de_temporadas: int = 3
    entregado: bool = False

    def __str__(self) -> str:
        return f"""
        Serie "{self.titulo}" con {self.numero_de_temporadas} temporada(s),
        Creada por {self.creador}, en el género {self.genero}.

        Está {"entregado" if self.isEntregado() else "por entregar"}.
        """

    pass

@dataclass
class Videojuego(Entregable):
    """Clase para los Videojuegos del sistema"""
    titulo: str
    genero: str
    comanyia: str
    horas_estimadas: int = 10
    entregado: bool = False

    def __str__(self) -> str:
        return f"""
        Videojuego "{self.titulo}" con {self.horas_estimadas} hora(s) estimada(s) de duración,
        Del género {self.genero} y desarrollado por la compañía {self.comanyia}.

        Está {"entregado" if self.isEntregado() else "por entregar"}.
        """

    pass

def display_list(elements: list) -> None:
    [ print(element) for element in elements ]

def main() -> None:
    """
    El hilo principal de ejecución

    returns None
    """
    series = [
        Serie('How I Met Your Mother', 'Sitcom', 'Carter Bays', 9),
        Serie('El juego del calamar', 'Drama', 'Hwang Dong-hyuk', 1),
    ]
    videojuegos = [
        Videojuego('Darksiders', 'Hack n\' Slash', 'THQ Nordic', 20),
        Videojuego('Skyrim', 'RPG', 'Bethesda', 34),
        Videojuego('Dark Souls', 'RPG Acción', 'FromSoftware', 40),
        Videojuego('Gris', 'Plataformas', 'Nomada Studio', 4),
        Videojuego('Fez', 'Puzzles', 'Polytron', 6),
    ]
    
    series[1].entregar()
    videojuegos[2].entregar()
    videojuegos[4].entregar()

    series_entregadas = [ serie for serie in series if serie.isEntregado() ]
    print('series_entregados')
    display_list(series_entregadas)

    videojuegos_entregadas = [ videojuego for videojuego in videojuegos if videojuego.isEntregado() ]
    print('videojuegos_entregados')
    display_list(videojuegos_entregadas)

    videojuego_mas_largo = None

    for videojuego in videojuegos:
        if (videojuego_mas_largo) and (videojuego.horas_estimadas < videojuego_mas_largo.horas_estimadas):
            continue

        videojuego_mas_largo = videojuego
    
    print('El videojuego más largo es:', videojuego_mas_largo)

if __name__ == "__main__":
    main()