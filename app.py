# ==============================================================================
# Dashboard Ejecutivo de Análisis de Ventas y Finanzas
# Autor: Senior Python Developer & Data Visualization Expert
# Versión: 1.0.0 (Producción)
# Tecnologías: Streamlit, Pandas, Plotly Express, Plotly Graph Objects
# ==============================================================================

import io
import datetime
from typing import Tuple, Optional
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ------------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS MODERNOS (DARK THEME)
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Ventas & Finanzas | Executive BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_custom_css():
    """Inyecta estilos CSS personalizados para un diseño moderno en modo oscuro con estética Glassmorphism."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .main .block-container {
            padding-top: 1.6rem;
            padding-bottom: 2.5rem;
            padding-left: 2.2rem;
            padding-right: 2.2rem;
            max-width: 100% !important;
        }

        /* Encabezado Principal */
        .dashboard-header {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 22px 28px;
            margin-bottom: 22px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(12px);
        }

        .dashboard-title {
            font-size: 1.85rem;
            font-weight: 800;
            background: linear-gradient(90deg, #FFFFFF 0%, #CBD5E1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            letter-spacing: -0.5px;
        }

        .dashboard-subtitle {
            color: #94A3B8;
            font-size: 0.92rem;
            font-weight: 400;
            margin-top: 4px;
            margin-bottom: 0;
        }

        .badge-status {
            background: rgba(99, 102, 241, 0.15);
            color: #818CF8;
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 20px;
            padding: 6px 14px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        /* Tarjetas de Métricas KPI */
        .kpi-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 22px;
        }

        @media (max-width: 1024px) {
            .kpi-container {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 640px) {
            .kpi-container {
                grid-template-columns: 1fr;
            }
        }

        .kpi-card {
            background: linear-gradient(145deg, #131B2E 0%, #0F172A 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
            transition: all 0.25s ease-in-out;
        }

        .kpi-card:hover {
            transform: translateY(-3px);
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.15);
        }

        .kpi-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .kpi-label {
            font-size: 0.82rem;
            font-weight: 600;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .kpi-icon-wrapper {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
        }

        .kpi-value {
            font-size: 1.9rem;
            font-weight: 800;
            color: #F8FAFC;
            letter-spacing: -0.5px;
            margin-bottom: 6px;
        }

        .kpi-subtext {
            font-size: 0.82rem;
            color: #64748B;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .kpi-badge-positive {
            color: #10B981;
            background: rgba(16, 185, 129, 0.12);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.75rem;
        }

        .kpi-badge-neutral {
            color: #38BDF8;
            background: rgba(56, 189, 248, 0.12);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.75rem;
        }

        /* Contenedores de Gráficos */
        .chart-box {
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .chart-title {
            color: #F1F5F9;
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .chart-subtitle {
            color: #64748B;
            font-size: 0.82rem;
            margin-bottom: 12px;
        }

        /* Barra Lateral */
        section[data-testid="stSidebar"] {
            background-color: #0B0F19 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        .sidebar-brand {
            padding: 10px 0 16px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 16px;
        }

        .sidebar-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sidebar-subtitle {
            font-size: 0.78rem;
            color: #94A3B8;
            margin-top: 3px;
        }

        /* Pestañas */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: rgba(17, 24, 39, 0.7);
            padding: 6px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }

        .stTabs [data-baseweb="tab"] {
            height: 40px;
            border-radius: 8px;
            color: #94A3B8;
            font-weight: 600;
            font-size: 0.86rem;
            padding: 0 16px;
        }

        .stTabs [aria-selected="true"] {
            background-color: #6366F1 !important;
            color: #FFFFFF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# ------------------------------------------------------------------------------
# 2. GENERADOR DE DATOS DE MUESTRA (SINTÉTICOS Y REALISTAS)
# ------------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_sample_sales_data(n_records: int = 1500) -> pd.DataFrame:
    """
    Genera un conjunto de datos realista de transacciones comerciales y financieras
    con estacionalidad, categorías coherentes, costos y márgenes de ganancia.
    """
    np.random.seed(42)

    catalog = {
        'Tecnología': [
            ('Laptop Workstation Pro 16"', 1850.0, 1150.0),
            ('Monitor UltraWide 34" IPS', 620.0, 390.0),
            ('Smartphone Titanium 5G', 980.0, 610.0),
            ('Auriculares Hi-Fi ANC Pro', 240.0, 130.0),
            ('Teclado Mecánico Ergonómico', 145.0, 75.0),
        ],
        'Mobiliario de Oficina': [
            ('Escritorio Motorizado Elevable', 580.0, 320.0),
            ('Silla Ergonómica Pro Mesh', 420.0, 230.0),
            ('Soporte Neumático Dual Monitor', 110.0, 55.0),
            ('Lámpara LED Antirreflejo Smart', 85.0, 42.0),
        ],
        'Moda & Accesorios': [
            ('Mochila Ejecutiva Antirrobo', 95.0, 42.0),
            ('Smartwatch Deportivo GPS', 210.0, 115.0),
            ('Calzado Business Casual', 140.0, 65.0),
            ('Chaqueta Térmica Impermeable', 175.0, 80.0),
        ],
        'Servicios Cloud & Software': [
            ('Suscripción SaaS Anual Enterprise', 1200.0, 280.0),
            ('Plan Cloud Storage 5TB', 180.0, 45.0),
            ('Suite de Ciberseguridad Pro', 350.0, 85.0),
            ('Consultoría de BI & Datos (Horas)', 750.0, 320.0),
        ],
        'Electrodomésticos Smart': [
            ('Robot Aspirador Láser LiDAR', 490.0, 270.0),
            ('Cafetera Automática Espresso', 680.0, 390.0),
            ('Purificador de Aire Inteligente', 230.0, 125.0),
            ('Freidora de Aire Dual Zone', 160.0, 85.0),
        ]
    }

    regions = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    region_weights = [0.28, 0.22, 0.20, 0.18, 0.12]
    
    payment_methods = ['Tarjeta de Crédito', 'Transferencia Bancaria', 'PayPal', 'Financiamiento 12M']
    payment_weights = [0.55, 0.22, 0.15, 0.08]

    end_date = datetime.date(2026, 9, 24)
    start_date = end_date - datetime.timedelta(days=540)
    total_days = (end_date - start_date).days

    rows = []
    category_names = list(catalog.keys())
    cat_weights = [0.32, 0.20, 0.16, 0.18, 0.14]

    for i in range(1, n_records + 1):
        chosen_cat = np.random.choice(category_names, p=cat_weights)
        prod_tuple = catalog[chosen_cat][np.random.randint(len(catalog[chosen_cat]))]
        prod_name, base_price, base_cost = prod_tuple

        day_offset = int(np.random.beta(a=1.8, b=1.2) * total_days)
        tx_date = start_date + datetime.timedelta(days=day_offset)

        quantity = int(np.random.choice([1, 2, 3, 4, 5], p=[0.60, 0.22, 0.10, 0.05, 0.03]))

        discount_factor = np.random.uniform(0.92, 1.05)
        unit_price = round(base_price * discount_factor, 2)
        unit_cost = round(base_cost, 2)

        total_sales = round(unit_price * quantity, 2)
        total_costs = round(unit_cost * quantity, 2)
        net_profit = round(total_sales - total_costs, 2)
        profit_margin = round((net_profit / total_sales) * 100, 2) if total_sales > 0 else 0.0

        region = np.random.choice(regions, p=region_weights)
        payment = np.random.choice(payment_methods, p=payment_weights)

        rows.append({
            'ID_Pedido': f'ORD-{10000 + i}',
            'Fecha': pd.to_datetime(tx_date),
            'Producto': prod_name,
            'Categoria': chosen_cat,
            'Region': region,
            'Metodo_Pago': payment,
            'Cantidad': quantity,
            'Precio_Unitario': unit_price,
            'Costo_Unitario': unit_cost,
            'Ventas': total_sales,
            'Costos': total_costs,
            'Ganancia': net_profit,
            'Margen_Pct': profit_margin
        })

    df = pd.DataFrame(rows)
    return df.sort_values(by='Fecha').reset_index(drop=True)

# ------------------------------------------------------------------------------
# 3. CARGA Y PROCESAMIENTO ROBUSTO DE ARCHIVOS SUBIDOS
# ------------------------------------------------------------------------------
def load_uploaded_dataset(file) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
    """
    Procesa un archivo CSV o Excel subido por el usuario, valida y estandariza nombres
    de columnas comunes en español e inglés y calcula métricas ausentes si es necesario.
    """
    if file is None:
        return None, None

    try:
        if file.name.endswith('.csv'):
            try:
                df = pd.read_csv(file, encoding='utf-8')
            except UnicodeDecodeError:
                file.seek(0)
                df = pd.read_csv(file, encoding='latin-1')
        elif file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
        else:
            return None, "Formato no compatible. Por favor sube un archivo .CSV o .XLSX."

        if df.empty:
            return None, "El archivo proporcionado está vacío."

        clean_cols = {col: col.strip().lower().replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') for col in df.columns}
        df = df.rename(columns=clean_cols)

        col_mappings = {
            'fecha': ['fecha', 'date', 'order_date', 'transaccion_fecha', 'periodo'],
            'producto': ['producto', 'product', 'item', 'nombre_producto', 'articulo', 'descripcion'],
            'categoria': ['categoria', 'category', 'familia', 'linea_producto', 'departamento'],
            'region': ['region', 'zona', 'territorio', 'area', 'sucursal', 'pais'],
            'cantidad': ['cantidad', 'quantity', 'qty', 'unidades', 'volumen'],
            'ventas': ['ventas', 'sales', 'ingresos', 'revenue', 'monto_total', 'total', 'importe'],
            'ganancia': ['ganancia', 'profit', 'utilidad', 'beneficio', 'margen_bruto', 'ganancia_neta'],
            'costos': ['costos', 'cost', 'costo_total', 'costos_totales', 'gastos']
        }

        std_columns = {}
        for target, aliases in col_mappings.items():
            for alias in aliases:
                if alias in df.columns and target not in std_columns.values():
                    std_columns[alias] = target
                    break

        df = df.rename(columns=std_columns)

        if 'fecha' not in df.columns:
            date_col_candidates = [c for c in df.columns if 'date' in c or 'time' in c or 'año' in c or 'mes' in c]
            if date_col_candidates:
                df['fecha'] = df[date_col_candidates[0]]
            else:
                return None, "No se encontró ninguna columna de fecha ('Fecha', 'Date', etc.)."

        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        df = df.dropna(subset=['fecha'])
        if df.empty:
            return None, "Las fechas en el archivo no pudieron ser interpretadas correctamente."

        if 'producto' not in df.columns:
            df['producto'] = 'Producto General'
        if 'categoria' not in df.columns:
            df['categoria'] = 'General'
        if 'region' not in df.columns:
            df['region'] = 'Nacional'
        if 'cantidad' not in df.columns:
            df['cantidad'] = 1
        else:
            df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(1).astype(int)

        if 'ventas' not in df.columns:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                df['ventas'] = df[numeric_cols[0]]
            else:
                return None, "No se encontró ninguna columna numérica para 'Ventas' / 'Ingresos'."
        else:
            df['ventas'] = pd.to_numeric(df['ventas'], errors='coerce').fillna(0.0)

        if 'ganancia' not in df.columns:
            if 'costos' in df.columns:
                df['costos'] = pd.to_numeric(df['costos'], errors='coerce').fillna(0.0)
                df['ganancia'] = df['ventas'] - df['costos']
            else:
                df['ganancia'] = round(df['ventas'] * 0.35, 2)
                df['costos'] = round(df['ventas'] * 0.65, 2)
        else:
            df['ganancia'] = pd.to_numeric(df['ganancia'], errors='coerce').fillna(0.0)
            if 'costos' not in df.columns:
                df['costos'] = df['ventas'] - df['ganancia']
            else:
                df['costos'] = pd.to_numeric(df['costos'], errors='coerce').fillna(0.0)

        df['margen_pct'] = np.where(df['ventas'] > 0, (df['ganancia'] / df['ventas']) * 100, 0.0)

        if 'id_pedido' not in df.columns:
            df['id_pedido'] = [f'ORD-{1000 + i}' for i in range(len(df))]

        final_df = pd.DataFrame({
            'ID_Pedido': df['id_pedido'].astype(str),
            'Fecha': df['fecha'],
            'Producto': df['producto'].astype(str),
            'Categoria': df['categoria'].astype(str),
            'Region': df['region'].astype(str),
            'Cantidad': df['cantidad'],
            'Ventas': df['ventas'].round(2),
            'Costos': df['costos'].round(2),
            'Ganancia': df['ganancia'].round(2),
            'Margen_Pct': df['margen_pct'].round(2)
        })

        return final_df.sort_values(by='Fecha').reset_index(drop=True), None

    except Exception as e:
        return None, f"Error al procesar el archivo: {str(e)}"
# ------------------------------------------------------------------------------
# 4. COMPONENTES VISUALES: TARJETAS DE MÉTRICAS KPI
# ------------------------------------------------------------------------------
def render_kpis(df: pd.DataFrame):
    """Renderiza 4 tarjetas de métricas ejecutivas clave con diseño moderno y badges de margen."""
    total_sales = df['Ventas'].sum()
    total_profit = df['Ganancia'].sum()
    total_orders = len(df)
    avg_ticket = (total_sales / total_orders) if total_orders > 0 else 0.0
    profit_margin = ((total_profit / total_sales) * 100) if total_sales > 0 else 0.0
    total_units = df['Cantidad'].sum()

    kpi_html = f"""
    <div class="kpi-container">
        <!-- KPI 1: Ventas Totales -->
        <div class="kpi-card">
            <div class="kpi-header">
                <span class="kpi-label">Ventas Totales</span>
                <div class="kpi-icon-wrapper" style="background: rgba(99, 102, 241, 0.15); color: #818CF8;">
                    💵
                </div>
            </div>
            <div class="kpi-value"></div>
            <div class="kpi-subtext">
                <span class="kpi-badge-neutral">{total_units:,} unidades vendidas</span>
            </div>
        </div>

        <!-- KPI 2: Ganancia Neta -->
        <div class="kpi-card">
            <div class="kpi-header">
                <span class="kpi-label">Ganancia Neta</span>
                <div class="kpi-icon-wrapper" style="background: rgba(16, 185, 129, 0.15); color: #34D399;">
                    📈
                </div>
            </div>
            <div class="kpi-value" style="color: #34D399;"></div>
            <div class="kpi-subtext">
                <span class="kpi-badge-positive">Margen: {profit_margin:.1f}%</span> sobre ventas
            </div>
        </div>

        <!-- KPI 3: Total de Pedidos -->
        <div class="kpi-card">
            <div class="kpi-header">
                <span class="kpi-label">Total de Pedidos</span>
                <div class="kpi-icon-wrapper" style="background: rgba(245, 158, 11, 0.15); color: #FBBF24;">
                    📦
                </div>
            </div>
            <div class="kpi-value">{total_orders:,}</div>
            <div class="kpi-subtext">
                <span class="kpi-badge-neutral">{(total_units/total_orders if total_orders else 0):.1f} arts/pedido</span>
            </div>
        </div>

        <!-- KPI 4: Ticket Promedio -->
        <div class="kpi-card">
            <div class="kpi-header">
                <span class="kpi-label">Ticket Promedio (AOV)</span>
                <div class="kpi-icon-wrapper" style="background: rgba(236, 72, 153, 0.15); color: #F472B6;">
                    🎯
                </div>
            </div>
            <div class="kpi-value"></div>
            <div class="kpi-subtext">
                <span class="kpi-badge-positive"></span> ganancia/pedido
            </div>
        </div>
    </div>
    """
    st.markdown(kpi_html, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 5. GRÁFICOS INTERACTIVOS CON PLOTLY
# ------------------------------------------------------------------------------
def plot_sales_trend(df: pd.DataFrame, granularity: str = 'Mensual') -> go.Figure:
    """
    Genera un gráfico de línea interactivo con gradiente y doble métrica:
    Ventas Brutas vs Ganancia Neta a través del tiempo.
    """
    df_temp = df.copy()
    
    if granularity == 'Diario':
        df_temp['Periodo'] = df_temp['Fecha'].dt.date
    elif granularity == 'Semanal':
        df_temp['Periodo'] = df_temp['Fecha'].dt.to_period('W').apply(lambda r: r.start_time.date())
    else:  # Mensual
        df_temp['Periodo'] = df_temp['Fecha'].dt.to_period('M').apply(lambda r: r.start_time.date())

    grouped = df_temp.groupby('Periodo')[['Ventas', 'Ganancia']].sum().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=grouped['Periodo'],
        y=grouped['Ventas'],
        name='Ventas Totales',
        mode='lines+markers',
        line=dict(color='#6366F1', width=3, shape='spline'),
        marker=dict(size=6, color='#818CF8'),
        fill='tozeroy',
        fillcolor='rgba(99, 102, 241, 0.12)',
        hovertemplate='<b>Ventas:</b> $%{y:,.2f}<br><b>Fecha:</b> %{x}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=grouped['Periodo'],
        y=grouped['Ganancia'],
        name='Ganancia Neta',
        mode='lines+markers',
        line=dict(color='#10B981', width=3, shape='spline'),
        marker=dict(size=6, color='#34D399'),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.08)',
        hovertemplate='<b>Ganancia:</b> $%{y:,.2f}<br><b>Fecha:</b> %{x}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        height=380,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#E2E8F0', size=12)
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            tickfont=dict(color='#94A3B8')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(color='#94A3B8')
        ),
        hovermode='x unified'
    )
    return fig

def plot_top_products(df: pd.DataFrame, top_n: int = 8) -> go.Figure:
    """Genera un gráfico de barras horizontales con los productos más vendidos."""
    grouped = df.groupby('Producto')[['Ventas', 'Ganancia', 'Cantidad']].sum().reset_index()
    top_df = grouped.sort_values(by='Ventas', ascending=True).tail(top_n)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=top_df['Ventas'],
        y=top_df['Producto'],
        orientation='h',
        marker=dict(
            color=top_df['Ventas'],
            colorscale=[[0, '#312E81'], [0.5, '#4F46E5'], [1, '#818CF8']],
            line=dict(color='rgba(255, 255, 255, 0.15)', width=1)
        ),
        text=top_df['Ventas'].apply(lambda x: f""),
        textposition='outside',
        textfont=dict(color='#E2E8F0', size=11, family='Plus Jakarta Sans'),
        hovertemplate='<b>%{y}</b><br>Ventas: $%{x:,.2f}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=60, t=20, b=20),
        height=380,
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(color='#94A3B8')
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(color='#F1F5F9', size=12)
        )
    )
    return fig

def plot_category_distribution(df: pd.DataFrame) -> go.Figure:
    """Genera un gráfico circular tipo Donut con la distribución de ventas por categoría."""
    cat_df = df.groupby('Categoria')['Ventas'].sum().reset_index()
    total_sales = cat_df['Ventas'].sum()

    modern_palette = ['#6366F1', '#10B981', '#F59E0B', '#EC4899', '#38BDF8', '#8B5CF6', '#14B8A6']

    fig = go.Figure(data=[go.Pie(
        labels=cat_df['Categoria'],
        values=cat_df['Ventas'],
        hole=0.58,
        marker=dict(colors=modern_palette, line=dict(color='#0F172A', width=2)),
        textinfo='percent',
        hoverinfo='label+value+percent',
        hovertemplate='<b>%{label}</b><br>Ventas: $%{value:,.2f}<br>Participación: %{percent}<extra></extra>',
        textfont=dict(size=12, color='#FFFFFF', family='Plus Jakarta Sans')
    )])

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        height=350,
        annotations=[dict(
            text=f"<b>Total</b><br>",
            x=0.5, y=0.5,
            font_size=13,
            font_color='#F8FAFC',
            font_family='Plus Jakarta Sans',
            showarrow=False
        )],
        legend=dict(
            orientation="v",
            x=1.02,
            y=0.5,
            font=dict(color='#94A3B8', size=11)
        )
    )
    return fig

def plot_sales_heatmap(df: pd.DataFrame) -> go.Figure:
    """
    Genera un Mapa de Calor (Heatmap) que cruza el Día de la Semana
    con el Mes del Año para identificar patrones de compra y estacionalidad.
    """
    df_heat = df.copy()

    day_map = {
        0: 'Lunes', 1: 'Martes', 2: 'Miércoles',
        3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'
    }
    month_map = {
        1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
    }

    df_heat['Dia_Num'] = df_heat['Fecha'].dt.dayofweek
    df_heat['Dia_Semana'] = df_heat['Dia_Num'].map(day_map)
    df_heat['Mes_Num'] = df_heat['Fecha'].dt.month
    df_heat['Mes'] = df_heat['Mes_Num'].map(month_map)

    dias_orden = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    meses_presentes = sorted(df_heat['Mes_Num'].unique())
    meses_orden = [month_map[m] for m in meses_presentes]

    pivot = df_heat.pivot_table(
        index='Dia_Semana',
        columns='Mes',
        values='Ventas',
        aggfunc='sum',
        fill_value=0
    )

    pivot = pivot.reindex(index=dias_orden, columns=meses_orden, fill_value=0)

    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns.tolist(),
        y=pivot.index.tolist(),
        colorscale='Viridis',
        colorbar=dict(
            title=dict(text="Ventas ($)", font=dict(color='#94A3B8', size=11)),
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(color='#94A3B8', size=10)
        ),
        hovertemplate='<b>%{y} en %{x}</b><br>Ventas: $%{z:,.2f}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=10, b=20),
        height=350,
        xaxis=dict(
            tickfont=dict(color='#94A3B8'),
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(color='#F1F5F9'),
            showgrid=False,
            autorange='reversed'
        )
    )
    return fig
# ------------------------------------------------------------------------------
# 6. FUNCIÓN PRINCIPAL DE LA APLICACIÓN
# ------------------------------------------------------------------------------
def main():
    inject_custom_css()

    # ------------------ BARRA LATERAL (SIDEBAR) ------------------
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-title">
                    <span style="font-size: 1.5rem;">📊</span> BI Executive Suite
                </div>
                <div class="sidebar-subtitle">Ventas & Análisis Financiero • v1.0</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("#### 📂 Carga de Datos")
        uploaded_file = st.file_uploader(
            "Sube tu archivo (CSV o Excel):",
            type=["csv", "xlsx", "xls"],
            help="Sube tus registros de ventas. Si no subes ninguno, se usarán datos ficticios por defecto."
        )

        error_msg = None
        if uploaded_file is not None:
            df_raw, error_msg = load_uploaded_dataset(uploaded_file)
            if error_msg:
                st.error(error_msg)
                st.info("Cargando dataset ficticio por defecto como respaldo...")
                df_raw = generate_sample_sales_data()
                data_mode = "Muestra (Respaldo por Error)"
            else:
                st.success("¡Archivo cargado con éxito!")
                data_mode = f"Personalizado: {uploaded_file.name}"
        else:
            df_raw = generate_sample_sales_data()
            data_mode = "Datos de Muestra (Ficticios)"

        st.markdown(
            f"""
            <div style="margin-bottom: 20px;">
                <span class="badge-status">
                    <span style="font-size: 8px; color: #10B981;">●</span> {data_mode}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("--- ")
        st.markdown("#### 🔍 Filtros Dinámicos")

        min_date = df_raw['Fecha'].min().date()
        max_date = df_raw['Fecha'].max().date()

        date_range = st.date_input(
            "Rango de Fechas:",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            help="Selecciona fecha de inicio y fin para acotar el análisis."
        )

        if isinstance(date_range, tuple) and len(date_range) == 2:
            start_date, end_date = date_range
        elif isinstance(date_range, tuple) and len(date_range) == 1:
            start_date = date_range[0]
            end_date = max_date
        else:
            start_date, end_date = min_date, max_date

        all_categories = sorted(df_raw['Categoria'].dropna().unique().tolist())
        selected_categories = st.multiselect(
            "Categoría de Producto:",
            options=all_categories,
            default=all_categories,
            placeholder="Elige una o más categorías..."
        )

        all_regions = sorted(df_raw['Region'].dropna().unique().tolist())
        selected_regions = st.multiselect(
            "Región Geográfica:",
            options=all_regions,
            default=all_regions,
            placeholder="Elige una o más regiones..."
        )

        st.markdown("--- ")
        sample_csv = generate_sample_sales_data(100).to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Descargar Plantilla CSV",
            data=sample_csv,
            file_name="plantilla_ventas_ejemplo.csv",
            mime="text/csv",
            help="Descarga un archivo con el formato esperado para verificar tus columnas."
        )

    # ------------------ FILTRADO DE DATOS ------------------
    mask = (
        (df_raw['Fecha'].dt.date >= start_date) &
        (df_raw['Fecha'].dt.date <= end_date) &
        (df_raw['Categoria'].isin(selected_categories if selected_categories else all_categories)) &
        (df_raw['Region'].isin(selected_regions if selected_regions else all_regions))
    )
    df_filtered = df_raw[mask].copy()

    if df_filtered.empty:
        st.warning("⚠️ No se encontraron registros con los filtros seleccionados. Por favor ajusta los filtros en la barra lateral.")
        return

    # ------------------ ENCABEZADO PRINCIPAL ------------------
    st.markdown(
        f"""
        <div class="dashboard-header">
            <div>
                <h1 class="dashboard-title">Dashboard de Análisis de Ventas y Finanzas</h1>
                <p class="dashboard-subtitle">
                    Control ejecutivo de rendimiento comercial, rentabilidad y estacionalidad de ingresos
                </p>
            </div>
            <div>
                <span class="badge-status">
                    Filtrado: {len(df_filtered):,} pedidos de {len(df_raw):,}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------ SECCIÓN DE TARJETAS KPI ------------------
    render_kpis(df_filtered)

    # ------------------ PESTAÑAS DE CONTENIDO ------------------
    tab1, tab2, tab3 = st.tabs([
        "📊 Gráficos & Análisis Visual",
        "💼 Resumen Financiero por Segmento",
        "📑 Explorador de Datos & Exportación"
    ])

    # PESTAÑA 1: VISUALIZACIONES PRINCIPALES
    with tab1:
        col1, col2 = st.columns([1.5, 1])

        with col1:
            st.markdown(
                """
                <div class="chart-box">
                    <div class="chart-title">📉 Tendencia Temporal de Ventas y Ganancias</div>
                    <div class="chart-subtitle">Evolución de ingresos brutos y rentabilidad neta acumulada</div>
                """,
                unsafe_allow_html=True
            )
            granularity = st.radio(
                "Agrupación temporal:",
                options=['Diario', 'Semanal', 'Mensual'],
                index=2,
                horizontal=True,
                label_visibility="collapsed"
            )
            st.plotly_chart(plot_sales_trend(df_filtered, granularity), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(
                """
                <div class="chart-box">
                    <div class="chart-title">🏆 Top Productos Más Vendidos</div>
                    <div class="chart-subtitle">Ranking de desempeño por facturación total</div>
                """,
                unsafe_allow_html=True
            )
            top_n = st.slider("Cantidad de productos a mostrar:", min_value=5, max_value=12, value=7, label_visibility="collapsed")
            st.plotly_chart(plot_top_products(df_filtered, top_n=top_n), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        col3, col4 = st.columns([1, 1.3])

        with col3:
            st.markdown(
                """
                <div class="chart-box">
                    <div class="chart-title">🥧 Distribución de Ventas por Categoría</div>
                    <div class="chart-subtitle">Participación porcentual en los ingresos totales</div>
                """,
                unsafe_allow_html=True
            )
            st.plotly_chart(plot_category_distribution(df_filtered), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col4:
            st.markdown(
                """
                <div class="chart-box">
                    <div class="chart-title">🗓️ Mapa de Calor: Ventas por Día y Mes</div>
                    <div class="chart-subtitle">Densidad de facturación por día de la semana y estacionalidad mensual</div>
                """,
                unsafe_allow_html=True
            )
            st.plotly_chart(plot_sales_heatmap(df_filtered), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # PESTAÑA 2: TABLAS RESUMEN FINANCIERO
    with tab2:
        st.markdown("### 📊 Desempeño Consolidado por Categoría de Producto")
        cat_summary = df_filtered.groupby('Categoria').agg(
            Ventas_Totales=('Ventas', 'sum'),
            Costos_Totales=('Costos', 'sum'),
            Ganancia_Neta=('Ganancia', 'sum'),
            Pedidos=('ID_Pedido', 'count'),
            Unidades=('Cantidad', 'sum')
        ).reset_index()

        cat_summary['Margen_Neto_%'] = (cat_summary['Ganancia_Neta'] / cat_summary['Ventas_Totales']) * 100
        cat_summary['Ticket_Promedio'] = cat_summary['Ventas_Totales'] / cat_summary['Pedidos']

        st.dataframe(
            cat_summary.sort_values(by='Ventas_Totales', ascending=False),
            column_config={
                "Categoria": st.column_config.TextColumn("Categoría"),
                "Ventas_Totales": st.column_config.NumberColumn("Ventas Totales", format="$%.2f"),
                "Costos_Totales": st.column_config.NumberColumn("Costos Totales", format="$%.2f"),
                "Ganancia_Neta": st.column_config.NumberColumn("Ganancia Neta", format="$%.2f"),
                "Margen_Neto_%": st.column_config.ProgressColumn("Margen Neto", format="%.1f%%", min_value=0, max_value=100),
                "Ticket_Promedio": st.column_config.NumberColumn("Ticket Promedio", format="$%.2f"),
                "Pedidos": st.column_config.NumberColumn("Pedidos", format="%d"),
                "Unidades": st.column_config.NumberColumn("Unidades", format="%d"),
            },
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### 🗺️ Desempeño por Región Geográfica")
        reg_summary = df_filtered.groupby('Region').agg(
            Ventas_Totales=('Ventas', 'sum'),
            Ganancia_Neta=('Ganancia', 'sum'),
            Pedidos=('ID_Pedido', 'count'),
            Unidades=('Cantidad', 'sum')
        ).reset_index()
        reg_summary['Margen_Neto_%'] = (reg_summary['Ganancia_Neta'] / reg_summary['Ventas_Totales']) * 100

        st.dataframe(
            reg_summary.sort_values(by='Ventas_Totales', ascending=False),
            column_config={
                "Region": st.column_config.TextColumn("Región"),
                "Ventas_Totales": st.column_config.NumberColumn("Ventas Totales", format="$%.2f"),
                "Ganancia_Neta": st.column_config.NumberColumn("Ganancia Neta", format="$%.2f"),
                "Margen_Neto_%": st.column_config.ProgressColumn("Margen Neto", format="%.1f%%", min_value=0, max_value=100),
                "Pedidos": st.column_config.NumberColumn("Pedidos", format="%d"),
                "Unidades": st.column_config.NumberColumn("Unidades", format="%d"),
            },
            use_container_width=True,
            hide_index=True
        )

    # PESTAÑA 3: EXPLORADOR DE DATOS Y DESCARGA
    with tab3:
        st.markdown("### 📑 Registros Detallados Filtrados")
        st.markdown("Visualiza y audita las transacciones comerciales que cumplen con los filtros vigentes.")

        csv_buffer = io.StringIO()
        df_filtered.to_csv(csv_buffer, index=False, encoding='utf-8')
        csv_bytes = csv_buffer.getvalue().encode('utf-8-sig')

        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            label="⬇️ Descargar Datos Filtrados (CSV)",
            data=csv_bytes,
            file_name=f"ventas_finanzas_filtradas_{timestamp_str}.csv",
            mime="text/csv",
            help="Descarga el conjunto de datos filtrado en formato CSV con codificación UTF-8 compatible con Microsoft Excel."
        )

        st.dataframe(
            df_filtered,
            column_config={
                "ID_Pedido": st.column_config.TextColumn("ID Pedido"),
                "Fecha": st.column_config.DateColumn("Fecha", format="YYYY-MM-DD"),
                "Producto": st.column_config.TextColumn("Producto"),
                "Categoria": st.column_config.TextColumn("Categoría"),
                "Region": st.column_config.TextColumn("Región"),
                "Cantidad": st.column_config.NumberColumn("Cantidad", format="%d"),
                "Ventas": st.column_config.NumberColumn("Ventas", format="$%.2f"),
                "Costos": st.column_config.NumberColumn("Costos", format="$%.2f"),
                "Ganancia": st.column_config.NumberColumn("Ganancia", format="$%.2f"),
                "Margen_Pct": st.column_config.NumberColumn("Margen (%)", format="%.2f%%"),
            },
            use_container_width=True,
            hide_index=True
        )

if __name__ == '__main__':
    main()
