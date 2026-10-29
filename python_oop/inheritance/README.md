# BaseGeometry

Clase base para figuras geométricas que define comportamiento compartido y una interfaz común para las subclases.

## Archivo

`base_geometry.py`

## Descripción

`BaseGeometry` representa un concepto fundamental para figuras geométricas. Su propósito es proporcionar funcionalidad reutilizable (como la validación de enteros positivos) y establecer una interfaz que las subclases concretas deberán implementar.

## Métodos

### `area(self)`

Representa el área de una figura geométrica.

En la clase base **no se define el cálculo**, ya que cada figura lo implementa de forma distinta. Por ello, este método lanza una excepción:
