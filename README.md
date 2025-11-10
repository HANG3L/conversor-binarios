# Proyecto Django: Conversor de Binario

Este proyecto es una aplicación web simple hecha con Django que permite convertir números binarios a **decimal**, **octal** y **hexadecimal**. Utiliza **Bootstrap 5** para un diseño moderno y responsivo.

---

## Características

- Validación de números binarios (solo 0 y 1).
- Conversión a:
  - Decimal
  - Octal
  - Hexadecimal
- Mensajes de error amigables si el número no es válido.
- Plantilla flexible y fácil de personalizar.

---

## Estructura del proyecto

```js
conversor-binarios/       ==> Proyecto Django
│
├── conversiones/         ==> Configuración del proyecto
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── conversor/            ==> Aplicación principal
│ ├── templates/
│ │ └── index.html
│ ├── templatetags/
│ │ ├── init.py
│ │ └── form_tags.py
│ ├── forms.py
│ ├── views.py
│ └── urls.py
│
└── manage.py
```

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repo>
```

```bash
cd <repo-clonado>
```

2. Crear un entorno virtual:

```bash
python -m venv venv
```

```bash
source venv/bin/activate  # Linux/Mac
```

```bash
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Iniciar el servidor:

```bash
python manage.py runserver
```

5. Abrir el navegador en:

```bash
http://127.0.0.1:8000/
```

---

## Uso

- Ingresa un número binario en el formulario.
- Presiona Convertir.
- Se mostrarán los resultados en decimal, octal y hexadecimal.
- Si ingresas un valor inválido, aparecerá un mensaje de error.