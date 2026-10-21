# -*- coding: utf-8 -*-
"""
Script de resumen de análisis y modelado UML/DFD - Empresa Koki Muebles
Para exportación ligera a otros modelos de IA.
"""

RESUMEN_PROMPT = """
SITUACIÓN DE ANÁLISIS: EMPRESA KOKI MUEBLES
ESTÁNDARES: ISO/IEC/IEEE 29148, ISO/IEC 25010:2023, BABOK v3, OMG UML 2.5.1, RUP+Scrum

1. DIAGNÓSTICO DE FUENTES EXISTENTES:
- Documento "PREGUNTAS DE ESTRATEGIA KOKI MUEBLES": Contiene guion de 13 preguntas. Falta registrar respuestas de stakeholders y etiquetar evidencias con códigos trazables (E-01).
- Documento "Analisis de Sistemas . INICIO-FIN": Contiene diagnóstico de problema, matriz de stakeholders (ST-001 a ST-007), matriz JAD, necesidades crudas (N-001 a N-005) y requisitos (RF-001 a RF-007, RNF-007).
- FALTANTES A MEJORAR:
  a) Completar campos en blanco (Alcance, Proceso Principal, N-006 a N-008, filas RTM).
  b) Redactar RFs bajo ISO 29148 (ID + El sistema deberá + Verbo Infinitivo + Objeto + Regla).
  c) Cuantificar RNFs bajo ISO 25010 (ej. <= 1.5s a 300 usuarios concurrentes).
  d) Separar Reglas de Negocio (RN-XXX) de los RFs.
  e) Elaborar DFD (Contexto 0.0, Nivel 0, Nivel 1) y UML (Casos de Uso, Secuencia, Clases, Componentes, Despliegue).
  f) Completar Matriz RTM de 18 eslabones.

2. TRATAMIENTO DE RF Y RNF EN DIAGRAMAS:
- RF: Se grafican en DFD (Procesos), UML (Casos de Uso CU-XXX, Diagramas de Secuencia y Actividades).
- RNF: NO se dibujan como óvalos de Casos de Uso. Se reflejan con Notas/Constraints {constraint}, Diagrama de Despliegue (Servidores, HTTPS, TLS 1.3), Componentes y Sección 3.2 de SRS ISO 29148.

3. CANTIDAD Y TIPO DE DIAGRAMAS OBLIGATORIOS:
- DFD Contexto (Nivel 0.0): 1 por sistema (Proceso 0.0, Entidades Externas. Sin almacenes).
- DFD Nivel 0: 1 por arquitectura core (Procesos 1.0, 2.0..., Almacenes D1, D2...).
- DFD Nivel 1: 1 por Proceso Core (Subprocesos 3.1, 3.2..., Regla de Balanceo).
- Casos de Uso (UCD): 1 General + 1 por RF (System Boundary, Actores, CU-XXX, <<include>>, <<extend>>).
- Diagrama de Secuencia: 1 por cada RF/CU principal (Lifelines: Boundary, Control, Entity; mensajes síncronos/retorno; alt/loop).
- Diagrama de Actividades: 1 por RF complejo (Swimlanes, Inicio/Fin, Rombos [Si/No]).
- Máquina de Estados: 1 por entidad principal (Estados, transiciones evento [guarda] / acción).
- Diagrama de Clases: 1 General del Dominio (Clases, atributos -, métodos +, multiplicidad, composición, agregación).
- Diagrama de Paquetes: 1 de arquitectura (Paquetes por capas y dependencias).
- Diagrama de Componentes: 1 de servicios/módulos (Componentes, interfaces Provided/Required).
- Diagrama de Despliegue: 1 de infraestructura (Nodos, entornos, artefactos, HTTPS/TCP).
"""

if __name__ == "__main__":
    print(RESUMEN_PROMPT)
