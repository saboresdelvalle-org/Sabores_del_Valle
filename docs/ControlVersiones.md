# Procedimientos de Control de Versiones

Este documento describe cómo el equipo del proyecto **Sabores del Valle** gestionó el control de versiones utilizando Git y GitHub, incluyendo prácticas de commits, fusión de ramas y resolución de conflictos.

---

## 1. Realización de Commits

Cada integrante del equipo trabaja en una rama específica y realiza *commits* locales de manera frecuente y organizada, siguiendo un formato estándar de mensajes:

- `feat:` para nuevas funcionalidades o contenido.
- `fix:` para correcciones.
- `docs:` para cambios en documentación.
- `style:` para mejoras visuales o de formato sin lógica.

### Ejemplos:

- `feat: agrega receta de arroz chaufa` (chef-jose)
- `fix: corrige precio del ceviche mixto` (editor-precios)
- `docs: mejora descripción del lomo saltado` (editor-descripciones)

Los commits se realizan después de completar una unidad funcional clara (por ejemplo, una receta completa, corrección de todos los precios de una categoría, o la redacción de una descripción).

---

## 2. Fusión de Ramas (Merge)

Una vez que un colaborador finaliza su tarea en su rama (por ejemplo, `chef-jose`), realiza `push` de su rama al repositorio remoto. Luego:

1. Se accede a GitHub y se crea un **Pull Request** (PR) desde su rama hacia `develop`.
2. El desarrollador revisa los cambios y aprueba el merge.
3. Una vez aprobado, se fusionan los cambios a `develop`.

### Ejemplo en terminal (fusión manual):

```bash
git checkout develop
git pull origin develop
git merge chef-jose
git push origin develop
