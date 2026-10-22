# Exception Handling en Python — `safe_print_list`

Guía del proyecto de **manejo de excepciones** en Python 3.8.x sobre Ubuntu 20.04 LTS.
Cubre la implementación de `safe_print_list`, las restricciones del enunciado,
las soluciones válidas y cómo verificar PEP8 con `pycodestyle 2.7.x`.

---

## 📋 Tabla de contenidos

1. [Contexto](#-contexto)
2. [Objetivos de aprendizaje](#-objetivos-de-aprendizaje)
3. [Requisitos generales](#-requisitos-generales)
4. [Tarea 0 — Impresión segura de listas](#-tarea-0--impresión-segura-de-listas)
5. [Análisis del problema](#-análisis-del-problema)
6. [Solución recomendada (Opción B)](#-solución-recomendada-opción-b)
7. [Enfoques alternativos](#-enfoques-alternativos)
8. [`pass` vs `break`: por qué importa dónde esté el `try`](#-pass-vs-break-por-qué-importa-dónde-esté-el-try)
9. [La nueva línea final: alternativas al `print("")`](#-la-nueva-línea-final-alternativas-al-print)
10. [Verificación de PEP8 con `pycodestyle`](#-verificación-de-pep8-con-pycodestyle)
11. [Checklist de entrega](#-checklist-de-entrega)
12. [Casos de prueba](#-casos-de-prueba)
13. [Errores comunes](#-errores-comunes)
14. [Recursos](#-recursos)

---

## 🎯 Contexto

Los programas del mundo real deben ser **resistentes**. Las entradas pueden ser
inválidas, los datos pueden faltar y las operaciones pueden fallar
inesperadamente. El **manejo de excepciones** permite que un programa detecte
errores, responda de forma apropiada y continúe ejecutándose con seguridad
cuando sea posible.

En este proyecto aprenderás cómo maneja Python los errores en tiempo de
ejecución y cómo gestionarlos usando:

- `try` / `except`
- Tipos de excepción específicos
- Bloques `else` y `finally`
- Lanzar excepciones explícitamente

El foco está en escribir **código defensivo y predecible**.

---

## 🎓 Objetivos de aprendizaje

Al final del proyecto deberías poder:

- Identificar excepciones comunes en tiempo de ejecución
  (`TypeError`, `IndexError`, `ZeroDivisionError`, `KeyError`).
- Usar correctamente los bloques `try` y `except`.
- Capturar **tipos de excepción específicos** en lugar de excepciones amplias.
- Usar `else` y `finally` de forma apropiada.
- Lanzar excepciones explícitamente cuando sea necesario.
- Escribir funciones que fallen de forma **segura y predecible**.

---

## ⚙️ Requisitos generales

| Requisito | Detalle |
|-----------|---------|
| Sistema de corrección | Ubuntu 20.04 LTS |
| Versión de Python | Python 3.8.x |
| Shebang obligatorio | `#!/usr/bin/env python3` (exacto, primera línea) |
| Permisos | El archivo debe ser **ejecutable** (`chmod +x`) |
| Fin de archivo | Debe terminar con **una** nueva línea (`\n`) |
| Estilo | PEP8 con `pycodestyle 2.7.x` |
| Bibliotecas externas | ❌ **No permitidas** |
| `except` amplio | ❌ **No permitido** (salvo indicación explícita) |

---

## 📝 Tarea 0 — Impresión segura de listas

Escribe una función que imprima `x` elementos de una lista.

**Prototipo:**

```python
def safe_print_list(my_list=[], x=0):
    ...
