# Socialización - Talleres de POO en Python

> Tiempo estimado: 2 a 3 minutos

---

## Implementación de los talleres en proyectos prácticos

En el **Taller 1** trabajé con la clase `Libro`. Lo que hice fue crear una plantilla que representara cualquier libro de una biblioteca. Cada libro que creo a partir de esa clase tiene su propio título, autor, páginas y un estado que dice si está disponible o prestado. Los métodos `prestar()` y `devolver()` se encargan de cambiar ese estado, pero siempre preguntando primero: si ya está prestado no se puede prestar otra vez, y si ya está disponible no se puede devolver. Esto evita errores lógicos.

En el **Taller 2** trabajé con encapsulación usando la clase `CuentaBancaria`. Aquí el titular y el saldo están protegidos, no se pueden tocar directamente desde fuera. Usé propiedades para controlar el acceso: el titular solo se puede leer, no modificar; y el saldo tiene una regla importante — nunca puede ser negativo. Si alguien intenta poner un saldo negativo, el programa lanza un error. También implementé métodos para depositar y retirar dinero, que verifican que las cantidades sean válidas antes de hacer el cambio.

Ambos talleres los probé directamente ejecutando el archivo con `python libro.py` o `python cuenta_bancaria.py`, sin necesidad de imports ni configuraciones adicionales.

## Integración de POO en el reto final

El reto final fue un **Sistema de Préstamos de Equipos**, que simula el control de inventario de una institución. Aunque este reto no usa clases propiamente dichas, aplica los principios de la programación orientada a objetos de las siguientes maneras:

- **Organización modular**: Cada funcionalidad está en su propia función (`mostrar_equipos`, `registrar_prestamo`, `devolver_equipo`, `ver_historial`, `agregar_equipo`). Esto sigue el principio de responsabilidad única: cada función hace una sola cosa y la hace bien.

- **Encapsulación de datos**: El inventario es un diccionario que centraliza toda la información. Los datos solo se modifican a través de las funciones diseñadas para eso, nadie puede cambiar un estado por accidente.

- **Estructuras de datos inmutables**: Usé tuplas `(usuario, fecha)` para los préstamos. Una vez que se registra un préstamo, ese dato no se puede modificar, manteniendo la integridad del historial. Esto es similar al concepto de datos privados en POO.

- **Menú interactivo**: El menú funciona como la interfaz pública del sistema. El usuario solo ve las opciones disponibles, pero no sabe cómo funciona internamente cada operación. Eso es abstracción: mostrar solo lo necesario y esconder la complejidad.

- **Validaciones**: Cada función revisa condiciones antes de ejecutarse, como si fueran setters con validación. Por ejemplo, no se puede prestar un equipo que no existe o que ya está prestado.

En conclusión, estos talleres me permitieron entender cómo pasar de escribir código lineal a organizarlo en clases y objetos, protegiendo los datos y haciendo el código más reutilizable y fácil de mantener.
