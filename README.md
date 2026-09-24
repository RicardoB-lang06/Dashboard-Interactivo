# 📊 Dashboard Ejecutivo de Análisis de Ventas y Finanzas

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una aplicación web analítica moderna, intuitiva y de alto impacto visual desarrollada en **Streamlit** y **Plotly** para el monitoreo en tiempo real de transacciones comerciales, ingresos, rentabilidad y estacionalidad.

Diseñada con una estética moderna en **Modo Oscuro (Dark Theme)** inspirada en interfaces ejecutivas de Business Intelligence, ofrece tarjetas de métricas KPI, gráficos dinámicos interactivos, carga de archivos propios y exportación de datos.

---

## 🚀 Características Principales

### 1. 🎨 Interfaz y Experiencia de Usuario (UI/UX)
* **Diseño Ejecutivo Moderno**: Paleta de colores en modo oscuro (*Midnight Navy / Glassmorphism*) con contrastes optimizados para largas sesiones de análisis.
* **4 Tarjetas KPI Principales**:
  * 💵 **Ventas Totales**: Facturación bruta acumulada con total de unidades vendidas.
  * 📈 **Ganancia Neta**: Utilidad neta calculada con badge dinámico del **Margen Porcentual Neto**.
  * 📦 **Total de Pedidos**: Volumen de transacciones y promedio de artículos por orden.
  * 🎯 **Ticket Promedio (AOV)**: Gasto medio por cliente y utilidad generada por transacción.
* **Barra Lateral Estilizada**: Panel de control con selector de archivos, filtros dinámicos y descarga de plantilla de prueba.

### 2. ⚡ Capacidades Analíticas y Funcionales
* **Carga de Archivos Flexible**: Soporte directo para archivos **CSV** y **Excel (`.xlsx`, `.xls`)**.
* **Manejo Robusto de Errores**:
  * Detección automática y tolerancia a diferentes encodings (`utf-8`, `latin-1`).
  * Mapeo inteligente de alias de columnas en español e inglés (ej. *ventas*, *sales*, *ingresos*, *date*, *fecha*, *profit*, etc.).
  * Si el usuario no sube ningún archivo (o si sube un archivo con formato erróneo), el sistema activa automáticamente un **dataset sintético ultrarrealista de más de 1,500 transacciones** para una experiencia *ready-to-use*.
* **Filtros Dinámicos**:
  * 📅 **Rango de Fechas** interactivo con selector de calendario.
  * 🏷️ **Categoría de Producto** con selección múltiple.
  * 🗺️ **Región Geográfica** con selección múltiple.
* **Visualizaciones Interactivas (Plotly Dark)**:
  * 📉 **Tendencia de Ventas y Ganancias**: Gráfico de líneas con áreas de gradiente suave, selector de granularidad (*Diario*, *Semanal*, *Mensual*) y hover unificado.
  * 🏆 **Top Productos Más Vendidos**: Gráfico de barras horizontales con ranking por facturación y control deslizante de cantidad.
  * 🥧 **Distribución por Categoría**: Gráfico Donut con desglose porcentual, paleta cromática vibrante y total central.
  * 🗓️ **Mapa de Calor (Heatmap)**: Matriz de ventas cruzando *Día de la Semana* vs. *Mes del Año* para detectar estacionalidad y días de mayor tráfico comercial.
* **Exportación y Descarga**:
  * Botón para descargar el conjunto de datos filtrado en formato **CSV compatible con Excel** (codificación `utf-8-sig`).
  * Botón para descargar la plantilla de ejemplo desde la barra lateral.
  * Tablas interactivas con resumen agrupado por Categoría y Región.

---

## 📁 Estructura del Repositorio

```text
sales_finance_dashboard/
├── .streamlit/
│   └── config.toml          # Configuración del tema visual y servidor de Streamlit
├── app.py                   # Código principal de la aplicación (modular y documentado)
├── requirements.txt         # Lista de dependencias del entorno Python
└── README.md                # Documentación del proyecto
```

---

## 🛠️ Instalación y Ejecución Local

### Prerrequisitos
* Tener instalado **Python 3.9** o superior.
* Gestor de paquetes `pip` o `uv`.

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/RicardoB-lang06/Dashboard-Interactivo.git
cd Dashboard-Interactivo
```

### Paso 2: Crear y activar un entorno virtual
* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Iniciar la aplicación
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador web en `http://localhost:8501`.

---

## ☁️ Despliegue en Streamlit Community Cloud (Paso a Paso)

Streamlit Community Cloud permite alojar y compartir la aplicación de forma 100% gratuita directamente desde GitHub:

1. **Subir el código a GitHub**:
   * Tu repositorio en GitHub: [RicardoB-lang06/Dashboard-Interactivo](https://github.com/RicardoB-lang06/Dashboard-Interactivo).
   * Inicializa git y realiza el push de los archivos:
     ```bash
     git init
     git add .
     git commit -m "feat: release inicial del dashboard de ventas y finanzas"
     git branch -M main
     git remote add origin https://github.com/RicardoB-lang06/Dashboard-Interactivo.git
     git push -u origin main
     ```

2. **Acceder a Streamlit Community Cloud**:
   * Ingresa a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con tu cuenta de GitHub.

3. **Crear una nueva App**:
   * Haz clic en el botón **"New app"**.
   * Selecciona el repositorio: `RicardoB-lang06/Dashboard-Interactivo`.
   * Rama (*Branch*): `main`.
   * Archivo principal (*Main file path*): `app.py`.

4. **Desplegar**:
   * Haz clic en **"Deploy!"**.
   * Streamlit detectará automáticamente el archivo `requirements.txt` e instalará las librerías necesarias. En menos de 2 minutos tu dashboard estará en vivo con un enlace público compartible.

---

## 📋 Estructura de Datos para Archivos Propios

Si deseas subir tus propios archivos CSV o Excel, la aplicación reconoce de forma inteligente los siguientes nombres de columna (en mayúsculas, minúsculas o con tildes):

| Columna Estándar | Alias Reconocidos | Tipo de Dato | Descripción |
| :--- | :--- | :--- | :--- |
| **Fecha** | `fecha`, `date`, `order_date`, `periodo` | Fecha / Datetime | Fecha en que se realizó la venta (`AAAA-MM-DD` o similar) |
| **Ventas** | `ventas`, `sales`, `ingresos`, `revenue`, `total` | Numérico | Monto monetario bruto de la venta |
| **Ganancia** *(opcional)* | `ganancia`, `profit`, `utilidad`, `margen` | Numérico | Utilidad neta (si no existe, se infiere con el 35%) |
| **Costos** *(opcional)* | `costos`, `cost`, `costo_total` | Numérico | Costo total asociado (si no existe, se calcula `Ventas - Ganancia`) |
| **Producto** | `producto`, `product`, `item`, `articulo` | Texto | Nombre o descripción del artículo |
| **Categoria** | `categoria`, `category`, `familia`, `linea` | Texto | Clasificación o departamento del producto |
| **Region** | `region`, `zona`, `territorio`, `area`, `sucursal` | Texto | Ubicación o área geográfica de la venta |
| **Cantidad** | `cantidad`, `quantity`, `qty`, `unidades` | Entero | Número de unidades vendidas en la transacción |

> 💡 **Nota**: Puedes hacer clic en el botón **"📥 Descargar Plantilla CSV"** en la barra lateral de la aplicación para obtener un archivo de ejemplo con datos válidos.

---

## 📦 Dependencias Principales

* [Streamlit](https://streamlit.io/) (>=1.35.0) - Framework web ágil para aplicaciones de datos
* [Pandas](https://pandas.pydata.org/) (>=2.0.0) - Manipulación, limpieza y agregación de datos
* [Plotly](https://plotly.com/python/) (>=5.20.0) - Gráficos interactivos de alto rendimiento
* [OpenPyXL](https://openpyxl.readthedocs.io/) (>=3.1.2) - Soporte para lectura y escritura de hojas de cálculo Excel (`.xlsx`)
* [NumPy](https://numpy.org/) (>=1.24.0) - Cálculos numéricos y generación de datos probabilísticos

---

## 👨‍💻 Autor

Desarrollado con altos estándares de ingeniería de software, arquitectura de datos y principios de diseño visual por un **Senior Python Developer & Data Visualization Expert**.
