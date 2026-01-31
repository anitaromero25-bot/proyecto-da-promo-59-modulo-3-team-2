# =============================================================================
# VISUALIZACIONES COMPLETAS + GENERACIÓN DE PDF
# Proyecto Módulo 3 - Adalab
# Equipo: Ana, Ruth, Tamara, Leire
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import warnings
import os
import datetime

warnings.filterwarnings("ignore")

# Configuración global de visualizaciones
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 10

# =============================================================================
# 1. INTRODUCCIÓN - DASHBOARD GENERAL DE LA EMPRESA
# =============================================================================

def dashboard_general(df):
    """Dashboard ejecutivo con KPIs principales y resumen visual"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # KPIs principales
    ax1 = fig.add_subplot(gs[0, :])
    ax1.axis('off')
    
    total_emp = len(df)
    salario_prom = df['MonthlyIncome'].mean()
    satisfaccion = df['JobSatisfaction'].mean()
    overtime_count = (df['OverTime']=='Yes').sum()
    
    ax1.text(0.1, 0.7, f"👥 Total Empleados: {total_emp}", fontsize=22, fontweight='bold')
    ax1.text(0.1, 0.3, f"💰 Salario Promedio: ${salario_prom:.0f}", fontsize=22)
    ax1.text(0.5, 0.7, f"😊 Satisfacción Laboral: {satisfaccion:.2f}/4", fontsize=22)
    ax1.text(0.5, 0.3, f"⏰ Empleados con Overtime: {overtime_count}", fontsize=22)
    
    # Distribución por departamento
    ax2 = fig.add_subplot(gs[1, 0])
    dept_counts = df['Department'].value_counts()
    ax2.barh(dept_counts.index, dept_counts.values, color='steelblue')
    ax2.set_title('Empleados por Departamento', fontweight='bold', fontsize=12)
    ax2.set_xlabel('Número de Empleados')
    
    # Distribución salarial
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.hist(df['MonthlyIncome'], bins=20, color='green', alpha=0.7, edgecolor='black')
    ax3.set_title('Distribución Salarial', fontweight='bold', fontsize=12)
    ax3.set_xlabel('Salario ($)')
    ax3.set_ylabel('Frecuencia')
    
    # Grupos de edad
    ax4 = fig.add_subplot(gs[1, 2])
    age_counts = df['AgeGroup'].value_counts()
    colors_age = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    ax4.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', colors=colors_age, startangle=90)
    ax4.set_title('Grupos de Edad', fontweight='bold', fontsize=12)
    
    # Satisfacción promedio
    ax5 = fig.add_subplot(gs[2, :])
    sat_means = df[['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction']].mean()
    sat_means.index = ['Satisfacción\nLaboral', 'Satisfacción\ncon Entorno', 'Balance\nVida-Trabajo', 'Satisfacción\ncon Relaciones']
    colors_sat = ['#66c2a5' if x >= 2.5 else '#fc8d62' for x in sat_means]
    ax5.barh(sat_means.index, sat_means.values, color=colors_sat)
    ax5.set_xlim(0, 4)
    ax5.set_title('Niveles Promedio de Satisfacción (1-4)', fontweight='bold', fontsize=12)
    ax5.set_xlabel('Puntuación')
    ax5.axvline(x=2.5, color='red', linestyle='--', linewidth=1, alpha=0.5)
    
    plt.suptitle('🏢 DASHBOARD GENERAL DE LA EMPRESA', fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    return fig


def analisis_edad(df):
    """Distribución de edad con histograma y pie chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].hist(df['Age'].dropna(), bins=20, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(df['Age'].mean(), color='red', linestyle='--', linewidth=2, label=f"Media: {df['Age'].mean():.1f} años")
    axes[0].axvline(df['Age'].median(), color='orange', linestyle='--', linewidth=2, label=f"Mediana: {df['Age'].median():.1f} años")
    axes[0].set_title('Distribución de Edad en la Empresa', fontweight='bold', fontsize=14)
    axes[0].set_xlabel('Edad (años)')
    axes[0].set_ylabel('Número de Empleados')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    age_counts = df['AgeGroup'].value_counts()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    axes[1].pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'fontsize': 11})
    axes[1].set_title('Composición por Grupos de Edad', fontweight='bold', fontsize=14)
    
    plt.tight_layout()
    return fig


def distribucion_genero_departamento(df):
    """Distribución por género y departamento"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    gender_counts = df['Gender'].value_counts()
    colors_gender = ['#87ceeb', '#ffb6c1']
    wedges, texts, autotexts = axes[0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', 
                                            colors=colors_gender, startangle=90, textprops={'fontsize': 12})
    axes[0].set_title('Distribución por Género', fontweight='bold', fontsize=14)
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    
    dept_counts = df['Department'].value_counts()
    axes[1].barh(dept_counts.index, dept_counts.values, color='coral', alpha=0.7)
    axes[1].set_title('Empleados por Departamento', fontweight='bold', fontsize=14)
    axes[1].set_xlabel('Número de Empleados')
    axes[1].grid(axis='x', alpha=0.3)
    for i, v in enumerate(dept_counts.values):
        axes[1].text(v + 10, i, str(v), va='center', fontweight='bold')
    
    plt.tight_layout()
    return fig


def top_roles(df):
    """Top 8 roles más comunes"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    top_roles = df['JobRole'].value_counts().head(8)
    bars = ax.barh(top_roles.index, top_roles.values, color='skyblue', edgecolor='navy', alpha=0.7)
    
    for i, (bar, val) in enumerate(zip(bars, top_roles.values)):
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, str(val), va='center', fontweight='bold')
    
    ax.set_title('Top 8 Roles más Comunes en la Empresa', fontweight='bold', fontsize=14)
    ax.set_xlabel('Número de Empleados')
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    return fig


def distribucion_salarios(df):
    """Distribución de salarios con media y mediana"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(df['MonthlyIncome'], bins=30, color='green', alpha=0.7, edgecolor='black')
    media = df['MonthlyIncome'].mean()
    mediana = df['MonthlyIncome'].median()
    
    ax.axvline(media, color='red', linestyle='--', linewidth=2.5, label=f'Media: ${media:.0f}')
    ax.axvline(mediana, color='blue', linestyle='--', linewidth=2.5, label=f'Mediana: ${mediana:.0f}')
    
    ax.set_title('Distribución de Salarios en la Empresa', fontweight='bold', fontsize=14)
    ax.set_xlabel('Salario Mensual ($)', fontsize=12)
    ax.set_ylabel('Frecuencia', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


def salario_por_nivel(df):
    """Salario promedio por nivel de puesto"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    salario_nivel = df.groupby('JobLevel')['MonthlyIncome'].mean().sort_index()
    bars = ax.bar(salario_nivel.index, salario_nivel.values, color='purple', alpha=0.7, edgecolor='black')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, f'${height:.0f}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax.set_title('Salario Promedio por Nivel de Puesto', fontweight='bold', fontsize=14)
    ax.set_xlabel('Nivel del Puesto', fontsize=12)
    ax.set_ylabel('Salario Mensual Promedio ($)', fontsize=12)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


def salario_por_departamento(df):
    """Salario promedio por departamento"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    salario_dept = df.groupby('Department')['MonthlyIncome'].mean().sort_values()
    bars = ax.barh(salario_dept.index, salario_dept.values, color='orange', alpha=0.7, edgecolor='black')
    
    for i, (bar, val) in enumerate(zip(bars, salario_dept.values)):
        ax.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2, f'${val:.0f}', va='center', fontweight='bold')
    
    ax.set_title('Salario Promedio por Departamento', fontweight='bold', fontsize=14)
    ax.set_xlabel('Salario Mensual Promedio ($)', fontsize=12)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    return fig


def niveles_satisfaccion(df):
    """4 dimensiones de satisfacción en la empresa"""
    satisfaccion_cols = ['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction']
    titulos = ['Satisfacción Laboral', 'Satisfacción con el Entorno', 'Balance Vida-Trabajo', 'Satisfacción con Relaciones']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    for i, (col, titulo) in enumerate(zip(satisfaccion_cols, titulos)):
        counts = df[col].value_counts().sort_index()
        media = df[col].mean()
        
        bars = axes[i].bar(counts.index, counts.values, color='teal', alpha=0.7, edgecolor='black')
        
        for j, bar in enumerate(bars):
            if counts.index[j] <= 2:
                bar.set_color('#e74c3c')
            elif counts.index[j] == 3:
                bar.set_color('#f39c12')
            else:
                bar.set_color('#27ae60')
        
        axes[i].axhline(y=media * len(df) / 4, color='blue', linestyle='--', linewidth=2, alpha=0.6, label=f'Nivel medio: {media:.2f}')
        axes[i].set_title(titulo, fontweight='bold', fontsize=12)
        axes[i].set_xlabel('Nivel (1=Bajo, 4=Alto)')
        axes[i].set_ylabel('Número de Empleados')
        axes[i].set_xticks([1, 2, 3, 4])
        axes[i].legend()
        axes[i].grid(axis='y', alpha=0.3)
    
    plt.suptitle('📊 Niveles de Satisfacción en la Empresa', fontsize=16, fontweight='bold')
    plt.tight_layout()
    return fig


def relacion_edad_salario_nivel(df):
    """Scatter plot: Edad vs Salario coloreado por JobLevel"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    scatter = ax.scatter(df['Age'], df['MonthlyIncome'], c=df['JobLevel'], s=df['YearsAtCompany']*10,
                        cmap='viridis', alpha=0.6, edgecolors='black', linewidth=0.5)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Nivel del Puesto', fontsize=12, fontweight='bold')
    
    ax.set_title('Relación entre Edad, Salario, Nivel de Puesto y Antigüedad', fontweight='bold', fontsize=14)
    ax.set_xlabel('Edad (años)', fontsize=12)
    ax.set_ylabel('Salario Mensual ($)', fontsize=12)
    ax.grid(alpha=0.3)
    
    legend_sizes = [5, 15, 30]
    legend_labels = ['5 años', '15 años', '30 años']
    legend_handles = [plt.scatter([], [], s=size*10, c='gray', alpha=0.6, edgecolors='black') for size in legend_sizes]
    ax.legend(legend_handles, legend_labels, title='Años en la Empresa', loc='upper left', fontsize=10)
    
    plt.tight_layout()
    return fig


def analisis_overtime(df):
    """Análisis de horas extra"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    overtime_counts = df['OverTime'].value_counts()
    colors_ot = ['#2ecc71', '#e74c3c', '#95a5a6']
    explode = (0.05, 0.05, 0)
    
    axes[0].pie(overtime_counts, labels=overtime_counts.index, autopct='%1.1f%%',
                colors=colors_ot, startangle=90, explode=explode, textprops={'fontsize': 12, 'fontweight': 'bold'})
    axes[0].set_title('Proporción de Empleados con Horas Extra', fontweight='bold', fontsize=14)
    
    overtime_by_dept = pd.crosstab(df['Department'], df['OverTime'], normalize='index') * 100
    
    if 'Yes' in overtime_by_dept.columns:
        overtime_sorted = overtime_by_dept['Yes'].sort_values(ascending=True)
        bars = axes[1].barh(overtime_sorted.index, overtime_sorted.values, color='salmon', alpha=0.7, edgecolor='black')
        
        for bar in bars:
            width = bar.get_width()
            axes[1].text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', va='center', fontweight='bold')
        
        axes[1].set_title('% de Empleados con Overtime por Departamento', fontweight='bold', fontsize=14)
        axes[1].set_xlabel('Porcentaje (%)', fontsize=12)
        axes[1].grid(axis='x', alpha=0.3)
        axes[1].set_xlim(0, max(overtime_sorted.values) + 10)
    
    plt.tight_layout()
    return fig


def distancia_hogar(df):
    """Distribución de distancia del hogar"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(df['DistanceFromHome'], bins=25, color='steelblue', edgecolor='black', alpha=0.7)
    media = df['DistanceFromHome'].mean()
    ax.axvline(media, color='red', linestyle='--', linewidth=2.5, label=f'Media: {media:.1f} km')
    
    ax.set_title('Distribución de Distancia del Hogar al Trabajo', fontweight='bold', fontsize=14)
    ax.set_xlabel('Distancia (km)', fontsize=12)
    ax.set_ylabel('Número de Empleados', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


# =============================================================================
# GENERACIÓN DE PDF COMPLETO
# =============================================================================

def generar_pdf_completo(df, nombre_archivo='Visualizaciones/Informe_Visualizaciones_Completo.pdf'):
    """
    Genera un PDF con todas las visualizaciones
    Incluye portada, índice y 11 visualizaciones
    """
    
    print("="*70)
    print(f"📄 GENERANDO PDF: {nombre_archivo}")
    print("="*70)
    
    visualizaciones = [
        ("Dashboard General de la Empresa", dashboard_general),
        ("Análisis de Edad", analisis_edad),
        ("Distribución por Género y Departamento", distribucion_genero_departamento),
        ("Top 8 Roles más Comunes", top_roles),
        ("Distribución de Salarios", distribucion_salarios),
        ("Salario Promedio por Nivel de Puesto", salario_por_nivel),
        ("Salario Promedio por Departamento", salario_por_departamento),
        ("Niveles de Satisfacción en la Empresa", niveles_satisfaccion),
        ("Relación Edad-Salario-Nivel-Antigüedad", relacion_edad_salario_nivel),
        ("Análisis de Horas Extra", analisis_overtime),
        ("Distribución de Distancia del Hogar", distancia_hogar)
    ]
    
    with PdfPages(nombre_archivo) as pdf:
        
        # PORTADA
        print("\n[1/13] Generando portada...")
        fig_portada = plt.figure(figsize=(11, 8.5))
        fig_portada.patch.set_facecolor('#f8f9fa')
        
        fig_portada.text(0.5, 0.75, 'ANÁLISIS DE ROTACIÓN', ha='center', fontsize=32, fontweight='bold', color='#2c3e50')
        fig_portada.text(0.5, 0.68, 'DE EMPLEADOS', ha='center', fontsize=32, fontweight='bold', color='#2c3e50')
        fig_portada.text(0.5, 0.58, 'Informe de Visualizaciones', ha='center', fontsize=18, color='#34495e')
        
        plt.plot([0.2, 0.8], [0.52, 0.52], color='#3498db', linewidth=3)
        
        fig_portada.text(0.5, 0.42, 'Proyecto Módulo 3', ha='center', fontsize=14, color='#7f8c8d')
        fig_portada.text(0.5, 0.38, 'Bootcamp Análisis de Datos - Adalab', ha='center', fontsize=14, color='#7f8c8d')
        fig_portada.text(0.5, 0.28, '👥 Equipo', ha='center', fontsize=12, fontweight='bold')
        fig_portada.text(0.5, 0.24, 'Ana • Ruth • Tamara • Leire', ha='center', fontsize=11)
        
        fecha_actual = datetime.date.today().strftime("%B %Y")
        fig_portada.text(0.5, 0.14, f'📅 {fecha_actual}', ha='center', fontsize=10, style='italic')
        fig_portada.text(0.5, 0.05, f'Total empleados analizados: {len(df):,}', ha='center', fontsize=9, color='#95a5a6')
        
        plt.axis('off')
        pdf.savefig(fig_portada, bbox_inches='tight', facecolor=fig_portada.get_facecolor())
        plt.close()
        
        # ÍNDICE
        print("[2/13] Generando índice...")
        fig_indice = plt.figure(figsize=(11, 8.5))
        fig_indice.text(0.5, 0.9, '📋 ÍNDICE DE CONTENIDOS', ha='center', fontsize=20, fontweight='bold')
        
        contenidos = [
            "1.  Dashboard General de la Empresa",
            "2.  Análisis Demográfico - Edad",
            "3.  Distribución por Género y Departamento",
            "4.  Top 8 Roles más Comunes",
            "5.  Análisis de Compensación - Distribución Salarial",
            "6.  Salario Promedio por Nivel de Puesto",
            "7.  Salario Promedio por Departamento",
            "8.  Niveles de Satisfacción (4 Dimensiones)",
            "9.  Relación Edad-Salario-Nivel-Antigüedad",
            "10. Análisis de Horas Extra",
            "11. Distribución de Distancia del Hogar"
        ]
        
        y_pos = 0.75
        for contenido in contenidos:
            fig_indice.text(0.15, y_pos, contenido, fontsize=12, va='top')
            y_pos -= 0.06
        
        plt.axis('off')
        pdf.savefig(fig_indice, bbox_inches='tight')
        plt.close()
        
        # VISUALIZACIONES
        for i, (titulo, funcion) in enumerate(visualizaciones, 3):
            print(f"[{i}/13] Generando: {titulo}...")
            try:
                fig = funcion(df)
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()
            except Exception as e:
                print(f"    ✗ Error en {titulo}: {e}")
        
        # METADATA
        d = pdf.infodict()
        d['Title'] = 'Análisis de Rotación de Empleados'
        d['Author'] = 'Ana, Ruth, Tamara, Leire - Adalab Team 2'
        d['Subject'] = 'Employee Attrition Analysis - Módulo 3'
        d['Keywords'] = 'HR Analytics, Data Analysis, Adalab'
    
    print("\n" + "="*70)
    print(f"✅ PDF GENERADO EXITOSAMENTE")
    print("="*70)
    print(f"📁 Archivo: {nombre_archivo}")
    print(f"📍 Ubicación: {os.path.abspath(nombre_archivo)}")
    print(f"📄 Páginas: 13 (portada + índice + 11 visualizaciones)")
    print("="*70)
    
    return nombre_archivo


def generar_todas_visualizaciones(df, guardar=False):
    """Genera todas las visualizaciones como PNGs individuales"""
    
    visualizaciones = [
        ("01_dashboard_general", dashboard_general),
        ("02_analisis_edad", analisis_edad),
        ("03_genero_departamento", distribucion_genero_departamento),
        ("04_top_roles", top_roles),
        ("05_distribucion_salarios", distribucion_salarios),
        ("06_salario_por_nivel", salario_por_nivel),
        ("07_salario_por_departamento", salario_por_departamento),
        ("08_niveles_satisfaccion", niveles_satisfaccion),
        ("09_edad_salario_nivel", relacion_edad_salario_nivel),
        ("10_analisis_overtime", analisis_overtime),
        ("11_distancia_hogar", distancia_hogar)
    ]
    
    figuras = {}
    
    print("="*70)
    print("GENERANDO VISUALIZACIONES INDIVIDUALES")
    print("="*70)
    
    for i, (nombre, funcion) in enumerate(visualizaciones, 1):
        print(f"\n[{i}/11] Generando: {nombre}...")
        try:
            fig = funcion(df)
            figuras[nombre] = fig
            
            if guardar:
                fig.savefig(f'{nombre}.png', dpi=300, bbox_inches='tight')
                print(f"    ✓ Guardado como {nombre}.png")
            
        except Exception as e:
            print(f"    ✗ Error: {e}")
    
    print("\n" + "="*70)
    print(f"✅ COMPLETADO: {len(figuras)}/11 visualizaciones generadas")
    print("="*70)
    
    return figuras


# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    
    print(f"Directorio actual: {os.getcwd()}")
    
    ruta_csv = "hr.csv"
    if not os.path.exists(ruta_csv):
        ruta_csv = "../hr.csv"
    
    try:
        print(f"\n📂 Cargando datos: {ruta_csv}")
        df_emp = pd.read_csv(ruta_csv)
        print(f"✅ Cargados: {len(df_emp)} filas")
        
        # Limpieza básica
        df_emp = df_emp.drop_duplicates(subset='EmployeeNumber', keep='first')
        df_emp['Age'] = df_emp['Age'].fillna(df_emp['Age'].median())
        df_emp['MonthlyIncome'] = df_emp['MonthlyIncome'].fillna(df_emp['MonthlyIncome'].median())
        df_emp['JobSatisfaction'] = df_emp['JobSatisfaction'].fillna(df_emp['JobSatisfaction'].median())
        
        for col in ['Department', 'JobRole', 'Attrition', 'OverTime']:
            if col in df_emp.columns:
                df_emp[col] = df_emp[col].astype(str).str.strip().str.title()
        
        # Variables derivadas
        if 'AgeGroup' not in df_emp.columns:
            df_emp['AgeGroup'] = pd.cut(df_emp['Age'], bins=[0, 30, 40, 50, 100], labels=['<30', '30-40', '40-50', '>=50'], right=False)
        
        if 'Attrition_flag' not in df_emp.columns:
            df_emp['Attrition_flag'] = df_emp['Attrition'].map({'Yes': 1, 'No': 0})
        
        # GENERAR PDF
        generar_pdf_completo(df_emp, 'Visualizaciones/Informe_Team2_Visualizaciones.pdf')
        
        print("\n✅ Proceso completado!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
