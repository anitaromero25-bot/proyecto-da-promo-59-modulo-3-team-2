# 📊 Análisis de Rotación de Empleados (Employee Attrition Analysis)


---

## 🎓 Proyecto del Bootcamp de Análisis de Datos - Adalab

**Módulo 3** - Análisis Exploratorio de Datos

**Equipo de Desarrollo:**
- 👩‍💻 Ana
- 👩‍💻 Ruth  
- 👩‍💻 Tamara
- 👩‍💻 Leire

## 📋 Descripción del Proyecto

Este proyecto analiza la **rotación de personal** en una organización para identificar los factores clave que influyen en que los empleados abandonen la empresa. A través del análisis de datos de recursos humanos, se busca proporcionar insights accionables para mejorar la retención del talento.

Desarrollado como parte del **Módulo 3** del Bootcamp de Análisis de Datos de **Adalab**, este trabajo pone en práctica técnicas de limpieza, transformación y análisis exploratorio de datos usando Python y sus principales librerías.

## 🎯 Objetivos del Proyecto

### Objetivos de Negocio
- Identificar los principales factores asociados con la rotación de empleados
- Analizar patrones demográficos y laborales relacionados con la salida de personal
- Evaluar la relación entre satisfacción laboral y retención de empleados
- Proporcionar métricas clave para la toma de decisiones en RRHH

### Objetivos de Aprendizaje (Módulo 3 - Adalab)
- Aplicar técnicas de limpieza y preparación de datos
- Gestionar valores nulos, duplicados y outliers
- Realizar transformaciones de datos y creación de variables derivadas
- Conducir análisis exploratorio de datos (EDA)
- Generar visualizaciones significativas
- Extraer insights accionables de los datos

## 📁 Estructura del Proyecto

```
employee-attrition-analysis/
│
├── hr.csv                          # Dataset original
├── exploracion_limpieza.ipynb      # Notebook principal de análisis
└── README.md                       # Este archivo
```

## 📊 Dataset

### Características del Dataset
- **Filas**: 1,470 empleados (tras limpieza)
- **Columnas**: 35 variables
- **Fuente**: Datos de recursos humanos

### Variables Principales

#### Variables Demográficas
- `Age`: Edad del empleado
- `Gender`: Género
- `MaritalStatus`: Estado civil
- `Education`: Nivel educativo
- `EducationField`: Campo de estudio

#### Variables Laborales
- `Department`: Departamento
- `JobRole`: Rol/puesto
- `JobLevel`: Nivel del puesto
- `YearsAtCompany`: Años en la empresa
- `TotalWorkingYears`: Años totales de experiencia
- `MonthlyIncome`: Ingreso mensual
- `OverTime`: Realización de horas extra

#### Variables de Satisfacción
- `JobSatisfaction`: Satisfacción laboral (1-4)
- `EnvironmentSatisfaction`: Satisfacción con el entorno (1-4)
- `WorkLifeBalance`: Balance vida-trabajo (1-4)
- `RelationshipSatisfaction`: Satisfacción con relaciones (1-4)

#### Variable Objetivo
- `Attrition`: Indica si el empleado abandonó la empresa (Yes/No)

## 🔧 Proceso de Análisis

### 1. Limpieza de Datos

#### Gestión de Duplicados
- Se identificaron y eliminaron **4 registros duplicados** basándose en `EmployeeNumber`
- Dataset final: 1,470 registros únicos

#### Tratamiento de Valores Nulos
- **Variables numéricas**: Imputación con la mediana
  - `Age`, `MonthlyIncome`, `JobSatisfaction`, `TrainingTimesLastYear`, `YearsWithCurrManager`
- **Variables categóricas**: Reemplazo con "Unknown"
  - `BusinessTravel`, `Department`, `EducationField`, `MaritalStatus`
- **StandardHours**: Imputación con la moda

#### Eliminación de Variables
Se eliminaron columnas sin variabilidad o información redundante:
- `EmployeeCount`: Valor constante (1)
- `Over18`: Todos los empleados son mayores de 18
- `StandardHours`: Sin variabilidad (todos trabajan 80 horas)

### 2. Transformación de Datos

#### Estandarización de Categorías
- Aplicación de formato **Title Case** en variables categóricas
- Eliminación de espacios y caracteres inconsistentes
- Normalización de valores en: `Department`, `EducationField`, `JobRole`, `BusinessTravel`

#### Creación de Variables Derivadas
- **`Attrition_flag`**: Variable binaria (1 = se fue, 0 = se quedó)
- **`AgeGroup`**: Grupos etarios
  - `<30`: Menores de 30 años
  - `30-40`: Entre 30 y 40 años
  - `40-50`: Entre 40 y 50 años
  - `>=50`: 50 años o más

#### Ajuste de Tipos de Datos
- Variables de satisfacción convertidas a enteros
- Variables categóricas convertidas al tipo `category` (optimización de memoria)

### 3. Análisis Exploratorio

## 📈 Resultados Principales

### Tasa Global de Rotación
- **16.1%** de los empleados abandonan la empresa

### Rotación por Grupo de Edad
| Grupo de Edad | Tasa de Rotación |
|---------------|------------------|
| <30           | 28.0%            |
| 30-40         | 14.5%            |
| 40-50         | 9.6%             |
| >=50          | 13.6%            |

**Insight**: Los empleados más jóvenes (<30 años) tienen casi el doble de probabilidad de irse.

### Rotación por Departamento
| Departamento              | Tasa de Rotación |
|---------------------------|------------------|
| Unknown                   | 34.5%            |
| Sales                     | 20.3%            |
| Human Resources           | 19.0%            |
| Research & Development    | 13.4%            |

**Insight**: Los departamentos de ventas y RRHH presentan mayor rotación.

### Rotación según Horas Extra
| OverTime | Tasa de Rotación |
|----------|------------------|
| No       | 10.2%            |
| Unknown  | 18.2%            |
| Yes      | 30.9%            |

**Insight**: Las horas extra están fuertemente asociadas con mayor rotación.

### Análisis de Satisfacción

#### Satisfacción Laboral (JobSatisfaction)
- **Empleados que permanecen**: 2.79 (promedio)
- **Empleados que se van**: 2.48 (promedio)
- **Diferencia**: -0.31 puntos

#### Satisfacción con el Entorno (EnvironmentSatisfaction)
- **Empleados que permanecen**: 2.77
- **Empleados que se van**: 2.46
- **Diferencia**: -0.31 puntos

#### Balance Vida-Trabajo (WorkLifeBalance)
- **Empleados que permanecen**: 2.78
- **Empleados que se van**: 2.66
- **Diferencia**: -0.12 puntos

**Insight**: Los empleados que abandonan la empresa tienen niveles de satisfacción consistentemente más bajos en todas las dimensiones evaluadas.

## 💡 Hipótesis Validada

✅ **La satisfacción laboral es un factor relevante en la retención de personal**

Los datos demuestran que existe una correlación entre los niveles de satisfacción (laboral, entorno, balance vida-trabajo) y la permanencia en la empresa.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **Matplotlib**: Visualización de datos
- **Seaborn**: Visualización estadística
- **Jupyter Notebook**: Entorno de desarrollo interactivo

## 📦 Instalación y Uso

### Requisitos Previos
```bash
python >= 3.8
```

### Instalación de Dependencias
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Ejecución del Proyecto
```bash
# Clonar el repositorio (si aplica)
git clone <url-repositorio>
cd employee-attrition-analysis

# Iniciar Jupyter Notebook
jupyter notebook

# Abrir exploracion_limpieza.ipynb
```

## 🔍 Funciones Principales

### `leer_y_explorar_df(ruta_fichero)`
Carga y realiza una exploración inicial del dataset mostrando:
- Primeras filas
- Dimensiones
- Información general
- Valores nulos
- Duplicados
- Estadísticas descriptivas

### `imputar_nulos(df)`
Gestiona valores nulos mediante:
- Mediana para variables numéricas clave
- Moda para StandardHours
- "Unknown" para variables categóricas

### `limpiar_categoricas(df)`
Estandariza variables categóricas:
- Formato Title Case
- Eliminación de espacios
- Homogeneización de valores

### `crear_variables_derivadas(df)`
Genera nuevas variables:
- `Attrition_flag`: Variable binaria de rotación
- `AgeGroup`: Grupos de edad categorizados

### `ajustar_tipos_y_columnas(df)`
Optimiza tipos de datos:
- Conversión a enteros de escalas discretas
- Conversión a category de variables categóricas
- Eliminación de columnas sin información

## 📊 Visualizaciones

El proyecto incluye visualizaciones para:
- Tasa de rotación por departamento (gráfico de barras)
- (Potencial para más visualizaciones)

## 🎓 Aprendizajes Clave

### Conceptos Aplicados del Módulo 3
1. **Limpieza de Datos**
   - Detección y eliminación de duplicados
   - Gestión de valores nulos con diferentes estrategias
   - Estandarización de variables categóricas

2. **Transformación de Datos**
   - Creación de variables derivadas
   - Codificación de variables categóricas
   - Binning y agrupación de datos numéricos

3. **Análisis Exploratorio de Datos (EDA)**
   - Análisis univariado y bivariado
   - Cálculo de métricas descriptivas
   - Identificación de patrones y tendencias

4. **Visualización de Datos**
   - Gráficos con Matplotlib y Seaborn
   - Comunicación efectiva de insights

### Insights de Negocio
1. **Edad y Rotación**: Los empleados jóvenes son un grupo de riesgo
2. **Horas Extra**: Factor crítico asociado con la rotación
3. **Satisfacción**: Predictor consistente de retención
4. **Departamentos**: Diferencias significativas entre áreas
5. **Limpieza de Datos**: Importancia de un tratamiento riguroso de valores nulos y duplicados

## 🚀 Próximos Pasos

- [ ] Análisis predictivo (Machine Learning)
- [ ] Modelo de clasificación para predecir rotación
- [ ] Análisis de importancia de variables
- [ ] Dashboard interactivo
- [ ] Segmentación de empleados en grupos de riesgo
- [ ] Análisis de tendencias temporales

## 🤝 Sobre el Equipo

Este proyecto ha sido desarrollado por el equipo compuesto por **Ana, Ruth, Tamara y Leire** como parte del Bootcamp de Análisis de Datos de Adalab.

### Distribución de Tareas
- **Limpieza de datos**: Trabajo colaborativo del equipo
- **Análisis exploratorio**: Trabajo colaborativo del equipo
- **Visualizaciones**: Trabajo colaborativo del equipo
- **Documentación**: Trabajo colaborativo del equipo

### Metodología de Trabajo
- Programación en pair/mob programming
- Revisiones de código en equipo
- Documentación colaborativa
- Uso de Jupyter Notebooks para análisis reproducible

## 📝 Sobre Adalab

[Adalab](https://adalab.es/) es una escuela especializada en formación digital para mujeres que ofrece bootcamps intensivos de programación web y análisis de datos, con el objetivo de aumentar la empleabilidad y diversidad en el sector tecnológico.

## 👥 Autoras

**Equipo Módulo 3 - Análisis de Datos**
- Ana
- Ruth
- Tamara
- Leire

**Promoción**: [Indicar promoción]  
**Fecha**: Enero 2025

## 📧 Contacto

Para más información sobre este proyecto, contactar a través de:
- **Adalab**: [https://adalab.es/](https://adalab.es/)
- **LinkedIn**: [Perfil del equipo o individual]

---

**Nota**: Este proyecto ha sido desarrollado con fines educativos como parte del Bootcamp de Análisis de Datos de Adalab. Los datos utilizados son de carácter público o han sido anonimizados.