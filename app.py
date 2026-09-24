# ==============================================================================
# Consola Ejecutiva de Analisis de Ventas y Finanzas
# Autor: Senior Python Developer & Data Visualization Expert
# Version: 2.0.0 (Executive Redesign - Professional FinTech Edition)
# Tecnologias: Streamlit, Pandas, Plotly Express, Plotly Graph Objects
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
# 1. CONFIGURACION DE PAGINA Y ESTILOS
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Consola de Analisis de Ventas y Finanzas",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #E2E8F0;
        }

        h1, h2, h3, h4, .brand-title, .dashboard-title {
            font-family: 'Space Grotesk', sans-serif !important;
            letter-spacing: -0.02em;
        }

        .metric-num, .kpi-num, [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-feature-settings: "tnum" 1, "zero" 1;
        }

        .main .block-container {
            padding-top: 1.4rem;
            padding-bottom: 2.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 100% !important;
        }

        .dashboard-header {
            background: #0E131F;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-left: 3px solid #3B82F6;
            border-radius: 8px;
            padding: 18px 24px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .dashboard-title {
            font-size: 1.55rem;
            font-weight: 700;
            color: #F8FAFC;
            margin: 0;
            line-height: 1.2;
        }

        .dashboard-subtitle {
            color: #7E8B9B;
            font-size: 0.86rem;
            font-weight: 400;
            margin-top: 4px;
            margin-bottom: 0;
        }

        .badge-terminal {
            background: rgba(59, 130, 246, 0.1);
            color: #60A5FA;
            border: 1px solid rgba(59, 130, 246, 0.25);
            border-radius: 4px;
            padding: 4px 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            font-weight: 600;
        }

        .badge-status {
            background: rgba(16, 185, 129, 0.1);
            color: #34D399;
            border: 1px solid rgba(16, 185, 129, 0.25);
            border-radius: 4px;
            padding: 4px 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.76rem;
            font-weight: 600;
        }

        .kpi-title {
            font-size: 0.74rem;
            font-weight: 600;
            color: #7E8B9B;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 6px;
        }

        .kpi-num {
            font-size: 1.75rem;
            font-weight: 700;
            color: #F8FAFC;
            line-height: 1.1;
            margin-bottom: 6px;
        }

        .kpi-num-positive {
            font-size: 1.75rem;
            font-weight: 700;
            color: #10B981;
            line-height: 1.1;
            margin-bottom: 6px;
        }

        .kpi-subtext {
            font-size: 0.78rem;
            color: #64748B;
            font-family: 'DM Sans', sans-serif;
        }

        .kpi-tag-pos {
            color: #10B981;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            font-size: 0.74rem;
            background: rgba(16, 185, 129, 0.1);
            padding: 2px 6px;
            border-radius: 3px;
        }

        .kpi-tag-neu {
            color: #60A5FA;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            font-size: 0.74rem;
            background: rgba(59, 130, 246, 0.1);
            padding: 2px 6px;
            border-radius: 3px;
        }

        .section-header {
            font-size: 0.92rem;
            font-weight: 600;
            color: #F1F5F9;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 2px;
        }

        .section-caption {
            font-size: 0.78rem;
            color: #7E8B9B;
            margin-bottom: 10px;
        }

        section[data-testid="stSidebar"] {
            background-color: #0A0D14 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06);
        }

        .sidebar-brand {
            padding: 6px 0 14px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 14px;
        }

        .sidebar-brand-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.02rem;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: -0.01em;
        }

        .sidebar-brand-sub {
            font-size: 0.73rem;
            color: #64748B;
            font-family: 'JetBrains Mono', monospace;
            margin-top: 2px;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
            background-color: #0E131F;
            padding: 4px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }

        .stTabs [data-baseweb="tab"] {
            height: 36px;
            border-radius: 4px;
            color: #7E8B9B;
            font-weight: 500;
            font-size: 0.84rem;
            padding: 0 14px;
        }

        .stTabs [aria-selected="true"] {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }

        .stDownloadButton button {
            background: #1E293B !important;
            color: #F8FAFC !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.80rem !important;
            font-weight: 600 !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 6px !important;
            padding: 7px 14px !important;
            transition: all 0.15s ease !important;
        }

        .stDownloadButton button:hover {
            background: #2563EB !important;
            border-color: #3B82F6 !important;
            color: #FFFFFF !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 8px !important;
            background-color: #0E131F !important;
            border-color: rgba(255, 255, 255, 0.07) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------------------------
# 2. GENERADOR DE DATOS DE MUESTRA (SINTETICOS Y REALISTAS)
# ------------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_sample_sales_data(n_records: int = 1500) -> pd.DataFrame:
    np.random.seed(42)

    catalog = {
        'Tecnologia': [
            ('Laptop Workstation Pro 16', 1850.0, 1150.0),
            ('Monitor UltraWide 34 IPS', 620.0, 390.0),
            ('Smartphone Titanium 5G', 980.0, 610.0),
            ('Auriculares Hi-Fi ANC Pro', 240.0, 130.0),
            ('Teclado Mecanico Ergonomico', 145.0, 75.0),
        ],
        'Mobiliario': [
            ('Escritorio Motorizado Elevable', 580.0, 320.0),
            ('Silla Ergonomica Pro Mesh', 420.0, 230.0),
            ('Soporte Neumatico Dual Monitor', 110.0, 55.0),
            ('Lampara LED Antirreflejo Smart', 85.0, 42.0),
        ],
        'Moda y Accesorios': [
            ('Mochila Ejecutiva Antirrobo', 95.0, 42.0),
            ('Reloj Deportivo GPS Smart', 210.0, 115.0),
            ('Calzado Business Casual', 140.0, 65.0),
            ('Chaqueta Termica Impermeable', 175.0, 80.0),
        ],
        'Servicios Cloud': [
            ('Suscripcion SaaS Anual Enterprise', 1200.0, 280.0),
            ('Plan Cloud Storage 5TB', 180.0, 45.0),
            ('Suite de Ciberseguridad Pro', 350.0, 85.0),
            ('Consultoria de BI y Datos (Pack)', 750.0, 320.0),
        ],
        'Electrodomesticos': [
            ('Robot Aspirador Laser LiDAR', 490.0, 270.0),
            ('Cafetera Automatica Espresso', 680.0, 390.0),
            ('Purificador de Aire Inteligente', 230.0, 125.0),
            ('Freidora de Aire Dual Zone', 160.0, 85.0),
        ]
    }

    regions = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    region_weights = [0.28, 0.22, 0.20, 0.18, 0.12]

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

        rows.append({
            'ID_Pedido': f'ORD-{10000 + i}',
            'Fecha': pd.to_datetime(tx_date),
            'Producto': prod_name,
            'Categoria': chosen_cat,
            'Region': region,
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
# 3. CARGA Y PROCESAMIENTO DE ARCHIVOS
# ------------------------------------------------------------------------------
def load_uploaded_dataset(file) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
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
            return None, "El archivo proporcionado esta vacio."

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
            date_candidates = [c for c in df.columns if 'date' in c or 'time' in c or 'año' in c or 'mes' in c]
            if date_candidates:
                df['fecha'] = df[date_candidates[0]]
            else:
                return None, "No se encontro ninguna columna de fecha ('Fecha', 'Date', etc.)."

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
                return None, "No se encontro ninguna columna numerica para 'Ventas' / 'Ingresos'."
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
# 4. TARJETAS DE METRICAS KPI NATIVAS
# ------------------------------------------------------------------------------
def render_kpis(df: pd.DataFrame):
    total_sales = float(df['Ventas'].sum())
    total_profit = float(df['Ganancia'].sum())
    total_orders = int(len(df))
    avg_ticket = float(total_sales / total_orders) if total_orders > 0 else 0.0
    profit_margin = float((total_profit / total_sales) * 100) if total_sales > 0 else 0.0
    total_units = int(df['Cantidad'].sum())
    avg_profit_order = float(total_profit / total_orders) if total_orders > 0 else 0.0
    units_per_order = float(total_units / total_orders) if total_orders > 0 else 0.0

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.markdown('<div class="kpi-title">Ventas Totales [Bruto]</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-num">${total_sales:,.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-subtext"><span class="kpi-tag-neu">{total_units:,} unidades</span> comercializadas</div>', unsafe_allow_html=True)

    with c2:
        with st.container(border=True):
            st.markdown('<div class="kpi-title">Ganancia Neta [Utilidad]</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-num-positive">${total_profit:,.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-subtext"><span class="kpi-tag-pos">Margen: {profit_margin:.1f}%</span> sobre facturacion</div>', unsafe_allow_html=True)

    with c3:
        with st.container(border=True):
            st.markdown('<div class="kpi-title">Total de Ordenes [Transacciones]</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-num">{total_orders:,}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-subtext"><span class="kpi-tag-neu">{units_per_order:.1f} arts/orden</span> promedio</div>', unsafe_allow_html=True)

    with c4:
        with st.container(border=True):
            st.markdown('<div class="kpi-title">Ticket Promedio [AOV]</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-num">${avg_ticket:,.2f}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kpi-subtext"><span class="kpi-tag-pos">${avg_profit_order:,.2f}</span> ganancia/orden</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 5. GRAFICOS INTERACTIVOS PLOTLY
# ------------------------------------------------------------------------------
def plot_sales_trend(df: pd.DataFrame, granularity: str = 'Mensual') -> go.Figure:
    df_temp = df.copy()

    if granularity == 'Diario':
        df_temp['Periodo'] = df_temp['Fecha'].dt.date
    elif granularity == 'Semanal':
        df_temp['Periodo'] = df_temp['Fecha'].dt.to_period('W').apply(lambda r: r.start_time.date())
    else:
        df_temp['Periodo'] = df_temp['Fecha'].dt.to_period('M').apply(lambda r: r.start_time.date())

    grouped = df_temp.groupby('Periodo')[['Ventas', 'Ganancia']].sum().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=grouped['Periodo'],
        y=grouped['Ventas'],
        name='Ventas Brutas',
        mode='lines',
        line=dict(color='#3B82F6', width=2.5),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.08)',
        hovertemplate='Ventas: $%{y:,.2f}<br>Fecha: %{x}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=grouped['Periodo'],
        y=grouped['Ganancia'],
        name='Ganancia Neta',
        mode='lines',
        line=dict(color='#10B981', width=2.5),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.05)',
        hovertemplate='Ganancia: $%{y:,.2f}<br>Fecha: %{x}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        height=340,
        font=dict(family='DM Sans, sans-serif', color='#94A3B8'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#E2E8F0', size=11, family='JetBrains Mono, monospace')
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.05)',
            tickfont=dict(family='JetBrains Mono, monospace', size=10, color='#64748B')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.05)',
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(family='JetBrains Mono, monospace', size=10, color='#64748B')
        ),
        hovermode='x unified'
    )
    return fig

def plot_top_products(df: pd.DataFrame, top_n: int = 8) -> go.Figure:
    grouped = df.groupby('Producto')[['Ventas', 'Ganancia', 'Cantidad']].sum().reset_index()
    top_df = grouped.sort_values(by='Ventas', ascending=True).tail(top_n)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=top_df['Ventas'],
        y=top_df['Producto'],
        orientation='h',
        marker=dict(
            color='#3B82F6',
            line=dict(color='rgba(255, 255, 255, 0.1)', width=1)
        ),
        text=top_df['Ventas'].apply(lambda val: f"${val:,.0f}"),
        textposition='outside',
        textfont=dict(color='#CBD5E1', size=10, family='JetBrains Mono, monospace'),
        hovertemplate='%{y}<br>Ventas: $%{x:,.2f}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=50, t=10, b=10),
        height=340,
        font=dict(family='DM Sans, sans-serif', color='#94A3B8'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.05)',
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(family='JetBrains Mono, monospace', size=10, color='#64748B')
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(color='#E2E8F0', size=11, family='DM Sans, sans-serif')
        )
    )
    return fig

def plot_category_distribution(df: pd.DataFrame) -> go.Figure:
    cat_df = df.groupby('Categoria')['Ventas'].sum().reset_index()
    total_sales = cat_df['Ventas'].sum()

    palette = ['#3B82F6', '#10B981', '#F59E0B', '#6366F1', '#EC4899', '#06B6D4']

    fig = go.Figure(data=[go.Pie(
        labels=cat_df['Categoria'],
        values=cat_df['Ventas'],
        hole=0.62,
        marker=dict(colors=palette, line=dict(color='#0E131F', width=2)),
        textinfo='percent',
        hoverinfo='label+value+percent',
        hovertemplate='<b>%{label}</b><br>Facturacion: $%{value:,.2f}<br>Participacion: %{percent}<extra></extra>',
        textfont=dict(size=11, color='#FFFFFF', family='JetBrains Mono, monospace')
    )])

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        height=320,
        annotations=[dict(
            text=f"TOTAL<br>${total_sales:,.0f}",
            x=0.5, y=0.5,
            font_size=12,
            font_color='#F8FAFC',
            font_family='JetBrains Mono, monospace',
            showarrow=False
        )],
        legend=dict(
            orientation="v",
            x=1.02,
            y=0.5,
            font=dict(color='#94A3B8', size=11, family='DM Sans, sans-serif')
        )
    )
    return fig

def plot_sales_heatmap(df: pd.DataFrame) -> go.Figure:
    df_heat = df.copy()

    day_map = {
        0: 'Lunes', 1: 'Martes', 2: 'Miercoles',
        3: 'Jueves', 4: 'Viernes', 5: 'Sabado', 6: 'Domingo'
    }
    month_map = {
        1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
    }

    df_heat['Dia_Num'] = df_heat['Fecha'].dt.dayofweek
    df_heat['Dia_Semana'] = df_heat['Dia_Num'].map(day_map)
    df_heat['Mes_Num'] = df_heat['Fecha'].dt.month
    df_heat['Mes'] = df_heat['Mes_Num'].map(month_map)

    dias_orden = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
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
        colorscale='Blues',
        colorbar=dict(
            title=dict(text="Ventas ($)", font=dict(color='#94A3B8', size=10, family='DM Sans')),
            tickprefix='$',
            tickformat=',.0f',
            tickfont=dict(color='#64748B', size=9, family='JetBrains Mono')
        ),
        hovertemplate='%{y} en %{x}<br>Total: $%{z:,.2f}<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        height=320,
        font=dict(family='DM Sans, sans-serif', color='#94A3B8'),
        xaxis=dict(
            tickfont=dict(color='#64748B', family='JetBrains Mono', size=10),
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(color='#E2E8F0', family='DM Sans', size=11),
            showgrid=False,
            autorange='reversed'
        )
    )
    return fig

# ------------------------------------------------------------------------------
# 6. ORQUESTACION PRINCIPAL
# ------------------------------------------------------------------------------
def main():
    inject_custom_css()

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-brand-name">ANALYTICS ENGINE</div>
                <div class="sidebar-brand-sub">FINANCIAL INTELLIGENCE // v2.0</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption("FUENTE DE DATOS")
        uploaded_file = st.file_uploader(
            "Cargar archivo de transacciones:",
            type=["csv", "xlsx", "xls"],
            help="Sube un archivo de ventas en CSV o Excel. Si no subes ninguno, se utilizaran datos sinteticos por defecto."
        )

        error_msg = None
        if uploaded_file is not None:
            df_raw, error_msg = load_uploaded_dataset(uploaded_file)
            if error_msg:
                st.error(error_msg)
                df_raw = generate_sample_sales_data()
                data_mode = "MUESTRA (RESPALDO)"
            else:
                st.success("Archivo procesado correctamente")
                data_mode = f"ACTIVO: {uploaded_file.name[:18]}"
        else:
            df_raw = generate_sample_sales_data()
            data_mode = "DATOS SINTETICOS"

        st.markdown(
            f'<div style="margin-bottom: 18px;"><span class="badge-status">{data_mode}</span></div>',
            unsafe_allow_html=True
        )

        st.caption("PARAMETROS DE FILTRADO")

        min_date = df_raw['Fecha'].min().date()
        max_date = df_raw['Fecha'].max().date()

        date_range = st.date_input(
            "Ventana de Observacion:",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            help="Selecciona rango temporal de analisis."
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
            "Categorias:",
            options=all_categories,
            default=all_categories,
            placeholder="Seleccionar categorias..."
        )

        all_regions = sorted(df_raw['Region'].dropna().unique().tolist())
        selected_regions = st.multiselect(
            "Regiones:",
            options=all_regions,
            default=all_regions,
            placeholder="Seleccionar regiones..."
        )

        st.markdown("<hr style='border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)
        sample_csv = generate_sample_sales_data(100).to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="Descargar Plantilla CSV",
            data=sample_csv,
            file_name="plantilla_ventas_formato.csv",
            mime="text/csv",
            help="Descarga un archivo con la estructura de columnas requerida."
        )

    # ------------------ FILTRADO VECTORIAL ------------------
    mask = (
        (df_raw['Fecha'].dt.date >= start_date) &
        (df_raw['Fecha'].dt.date <= end_date) &
        (df_raw['Categoria'].isin(selected_categories if selected_categories else all_categories)) &
        (df_raw['Region'].isin(selected_regions if selected_regions else all_regions))
    )
    df_filtered = df_raw[mask].copy()

    if df_filtered.empty:
        st.warning("No se encontraron registros bajo los criterios de filtrado seleccionados.")
        return

    # ------------------ ENCABEZADO EJECUTIVO ------------------
    st.markdown(
        f"""
        <div class="dashboard-header">
            <div>
                <h1 class="dashboard-title">Consola de Analisis de Ventas y Finanzas</h1>
                <p class="dashboard-subtitle">
                    Control cuantitativo de facturacion, margen de contribucion y estacionalidad transaccional
                </p>
            </div>
            <div>
                <span class="badge-terminal">REGISTROS: {len(df_filtered):,} / {len(df_raw):,}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------ SECCION DE TARJETAS KPI ------------------
    render_kpis(df_filtered)

    # ------------------ PESTAÑAS ANALITICAS ------------------
    tab1, tab2, tab3 = st.tabs([
        "Graficos y Analisis",
        "Resumen por Segmento",
        "Registro Detallado y Exportacion"
    ])

    # PESTAÑA 1: VISUALIZACIONES PRINCIPALES
    with tab1:
        c1, c2 = st.columns([1.5, 1])

        with c1:
            with st.container(border=True):
                st.markdown('<div class="section-header">Tendencia Temporal de Ventas y Utilidad</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-caption">Evolucion de facturacion bruta y ganancia neta acumulada</div>', unsafe_allow_html=True)
                granularity = st.radio(
                    "Granularidad:",
                    options=['Diario', 'Semanal', 'Mensual'],
                    index=2,
                    horizontal=True,
                    label_visibility="collapsed"
                )
                st.plotly_chart(plot_sales_trend(df_filtered, granularity), use_container_width=True)

        with c2:
            with st.container(border=True):
                st.markdown('<div class="section-header">Top Productos por Facturacion</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-caption">Ranking de articulos por volumen monetario vendido</div>', unsafe_allow_html=True)
                top_n = st.slider("Cantidad de productos:", min_value=5, max_value=12, value=7, label_visibility="collapsed")
                st.plotly_chart(plot_top_products(df_filtered, top_n=top_n), use_container_width=True)

        c3, c4 = st.columns([1, 1.3])

        with c3:
            with st.container(border=True):
                st.markdown('<div class="section-header">Distribucion de Ingresos por Categoria</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-caption">Participacion relativa en la facturacion total</div>', unsafe_allow_html=True)
                st.plotly_chart(plot_category_distribution(df_filtered), use_container_width=True)

        with c4:
            with st.container(border=True):
                st.markdown('<div class="section-header">Matriz de Estacionalidad: Dia vs Mes</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-caption">Densidad de ventas por dia de semana y periodo mensual</div>', unsafe_allow_html=True)
                st.plotly_chart(plot_sales_heatmap(df_filtered), use_container_width=True)

    # PESTAÑA 2: RESUMEN FINANCIERO CONSOLIDADO
    with tab2:
        st.markdown('<div class="section-header" style="margin-top: 10px;">Desempeño Consolidado por Categoria</div>', unsafe_allow_html=True)
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
                "Categoria": st.column_config.TextColumn("Categoria"),
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

        st.markdown('<div class="section-header" style="margin-top: 24px;">Desempeño Consolidado por Region</div>', unsafe_allow_html=True)
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
                "Region": st.column_config.TextColumn("Region"),
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
        st.markdown('<div class="section-header" style="margin-top: 10px;">Registro Individual de Transacciones</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Auditoria detallada de cada orden procesada bajo el filtro activo</div>', unsafe_allow_html=True)

        csv_buffer = io.StringIO()
        df_filtered.to_csv(csv_buffer, index=False, encoding='utf-8')
        csv_bytes = csv_buffer.getvalue().encode('utf-8-sig')

        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            label="Descargar Datos Filtrados (CSV)",
            data=csv_bytes,
            file_name=f"transacciones_filtradas_{timestamp_str}.csv",
            mime="text/csv",
            help="Descarga el dataset activo en formato CSV delimitado por comas con codificacion UTF-8."
        )

        st.dataframe(
            df_filtered,
            column_config={
                "ID_Pedido": st.column_config.TextColumn("ID Pedido"),
                "Fecha": st.column_config.DateColumn("Fecha", format="YYYY-MM-DD"),
                "Producto": st.column_config.TextColumn("Producto"),
                "Categoria": st.column_config.TextColumn("Categoria"),
                "Region": st.column_config.TextColumn("Region"),
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
