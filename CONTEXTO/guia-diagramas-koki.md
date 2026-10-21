# DIAGNÓSTICO Y GUÍA DE MODELADO: EMPRESA KOKI MUEBLES
**Estándares:** ISO/IEC/IEEE 29148, ISO/IEC 25010:2023, BABOK v3, OMG UML 2.5.1, RUP + Scrum

---

## 1. DIAGNÓSTICO DE FUENTES EXISTENTES

### A. Documento: "PREGUNTAS DE ESTRATEGIA KOKI MUEBLES"
* **Existe:** Guion de 13 preguntas en 4 ejes (Ventas, Inventario, Producción, Tecnología).
* **Falta/Mejorar:** Registrar respuestas de stakeholders; asignar códigos de evidencia (`E-01`, `O-01`) trazables a necesidades crudas (`N-001`).

### B. Documento: "Analisis de Sistemas . INICIO-FIN"
* **Existe:** Problema de Koki Muebles, Matriz de Stakeholders (`ST-001` a `ST-007`), entrevista transcripta, matriz JAD, necesidades crudas (`N-001` a `N-005`), requisitos preliminares (`RF-001` a `RF-007` y `RNF-007`).
* **Falta/Mejorar:**
  1. Completar campos vacíos: `Proceso principal`, `Alcance inicial`, `Fuera de alcance`, necesidades `N-006` a `N-008` y filas de la Matriz RTM.
  2. Redactar RFs bajo ISO 29148: `ID` + *El sistema deberá* + *Verbo Infinitivo* + *Objeto Directo* + *Regla/Condición*.
  3. Cuantificar RNFs bajo ISO 25010 (Ej. `RNF-007`: tiempo `<= 1.5s` a `300` usuarios concurrentes).
  4. Extraer Reglas de Negocio (`RN-XXX`) independientes (Ej. `RN-KOK-02`: adelanto del 50%).
  5. Construir DFD (Contexto 0.0, Nivel 0, Nivel 1) y UML (Casos de Uso, Secuencia, Clases, Componentes, Despliegue).
  6. Completar Matriz de Trazabilidad RTM (18 eslabones).

---

## 2. TRATAMIENTO DE RF Y RNF EN DIAGRAMAS

* **Requisitos Funcionales (RF):**
  * **DFD:** Procesos/Subprocesos.
  * **UML:** Casos de Uso (`CU-XXX`), Diagramas de Secuencia y Actividades.
* **Requisitos No Funcionales (RNF):**
  * **UML:** Notas/Constraints `{constraint}` adosadas a Casos de Uso/Clases.
  * **Despliegue:** Servidores, redes, TLS 1.3, HTTPS, balanceadores.
  * **Componentes:** Capas desacopladas (Clean/MVC).
  * **SRS (ISO 29148):** Sección 3.2.

---

## 3. INVENTARIO Y CANTIDAD DE DIAGRAMAS OBLIGATORIOS

| Tipo de Diagrama | Cantidad Recomendada | Elementos Obligatorios |
| :--- | :--- | :--- |
| **DFD Contexto (Nivel 0.0)** | 1 por sistema | Proceso `0.0`, Entidades Externas, Flujos globales. *Sin almacenes*. |
| **DFD Nivel 0** | 1 por arquitectura core | Procesos Core (`1.0, 2.0`), Entidades Externas, Almacenes (`D1, D2`). |
| **DFD Nivel 1** | 1 por Proceso Core | Subprocesos (`3.1, 3.2`), Almacenes, Regla de Balanceo. |
| **Casos de Uso (UCD)** | 1 General + 1 por RF | System Boundary, Actores, Casos de Uso (`CU-XXX`), `<<include>>`, `<<extend>>`. |
| **Diagrama de Secuencia** | 1 por cada RF/CU principal | Lifelines (`:Boundary`, `:Control`, `:Entity`), Mensajes síncronos/retorno, `alt`/`loop`. |
| **Diagrama de Actividades** | 1 por RF complejo | Swimlanes por rol, Inicio/Fin, Acciones, Rombos de decisión `[Si/No]`. |
| **Máquina de Estados** | 1 por entidad principal | Estados (`Pendiente`, `Aprobado`), Transiciones `evento [guarda] / acción`. |
| **Diagrama de Clases** | 1 General del Dominio | Clases, Atributos privados `-`, Métodos públicos `+`, Multiplicidad, Composición `◆`, Agregación `◇`. |
| **Diagrama de Paquetes** | 1 de arquitectura | Paquetes por capas (`<<subsystem>>`, `<<layer>>`) y dependencias. |
| **Diagrama de Componentes**| 1 de servicios/módulos | Componentes (`<<component>>`), Interfaces Provided (*Lollipop*)/Required (*Socket*). |
| **Diagrama de Despliegue** | 1 de infraestructura | Nodos (`<<device>>`), Entornos (`<<executionEnvironment>>`), Artefactos (`<<artifact>>`), HTTPS/TCP. |
