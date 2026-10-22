# Cómo contribuir a ut2-git-python

Este repositorio recoge los ejercicios de estructuras de control en Python
de la UT2 (Despliegue de Aplicaciones Web, 2º DAW). Cada ejercicio es un
script independiente que se ejecuta por consola.

## Requisitos

- Git y una cuenta de GitHub con clave SSH configurada.
- Python 3.10 o superior (`ej05_menu.py` usa `match-case`, que no existe
  en versiones anteriores). Se ha probado con Python 3.14.
- No hace falta instalar librerías externas: solo se usa la librería
  estándar (`random` en `ej04_adivina.py`).

## Estructura del repositorio

| Fichero | Contenido |
|---|---|
| `ejercicio1.py`, `ejercicio2.py` | Ejercicios 1 y 2 (if / else, if / elif / else) |
| `ej03_...py` a `ej08_...py` | Ejercicios 3 a 8, uno por estructura de control |
| `README.md` | Descripción del proyecto y tabla de ejercicios |
| `.gitignore` | Excluye `__pycache__/`, `*.pyc` y `notas.txt` |

Los ejercicios nuevos siguen el formato `ejNN_descripcion.py` (dos cifras y
el nombre en minúsculas con guiones bajos). Al añadir uno, actualiza también
la tabla del README.

## Flujo de ramas

- `main` contiene siempre una versión que funciona. Nunca se hacen commits
  directamente sobre ella.
- Cada cambio va en su propia rama, creada desde un `main` actualizado:

  ```bash
  git switch main
  git pull
  git switch -c nombre-descriptivo
  ```

- El nombre de la rama describe el cambio: `mejora-readme`,
  `validar-nota`, `ej09-bucle-anidado`...
- Las versiones estables se marcan con etiquetas (`v1.0`, `v2.0`).

## Mensajes de commit

Formato: `tipo: descripción breve`, en minúsculas y en presente.

| Tipo | Cuándo usarlo | Ejemplo del repositorio |
|---|---|---|
| `feat` | Ejercicio o funcionalidad nueva | `feat: ej08 cinco intentos` |
| `fix` | Corrección de un error | `fix: Ej02 valida que la nota esté entre 0 y 10` |
| `docs` | Cambios en README u otra documentación | `docs: añade ej07 y ej08 al README` |
| `style` | Formato, sin cambiar el comportamiento | `style: ej03 alinea la tabla` |
| `refactor` | Reorganizar código sin cambiar lo que hace | |
| `test` | Pruebas | |
| `chore` | Mantenimiento (`.gitignore`, configuración...) | |

## Cómo proponer un cambio

1. Actualiza `main` y crea una rama nueva (ver "Flujo de ramas").
2. Haz el cambio y comprueba que el script se ejecuta sin errores.
3. Haz uno o varios commits con el formato anterior.
4. Sube la rama: `git push -u origin nombre-de-la-rama`.
5. En GitHub, abre una Pull Request hacia `main` y explica qué cambia y por qué.
6. Espera la revisión. Si te piden cambios, haz más commits en la misma
   rama: la Pull Request se actualiza sola.
7. Una vez fusionada, borra la rama y actualiza tu copia local con `git pull`.

## Cómo clonar y ejecutar el proyecto

```bash
git clone git@github.com:frannp18/ut2-git-python.git
cd ut2-git-python
python ejercicio1.py        # en Windows
python3 ejercicio1.py       # en Linux / macOS
```

Sustituye `ejercicio1.py` por el ejercicio que quieras probar.