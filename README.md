# 🏥 Medical Center API

> **Una API REST robusta y optimizada para la gestión eficiente de turnos médicos y agendas clínicas.**

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.12+-blue)
![Framework](https://img.shields.io/badge/django--rest--framework-3.15+-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Descripción

**Medical Center API** es un backend diseñado para resolver las complejas reglas de negocio que demanda un sistema de salud real. La aplicación automatiza el agendamiento de citas, previene conflictos de horarios en la agenda de los profesionales y optimiza las consultas a la base de datos pensando en un alto rendimiento para el cliente frontend.

### 🚀 Funcionalidades y Reglas de Negocio Críticas

* 🛡️ **Validación de Colisiones:** El sistema impide de forma estricta que un médico reciba dos turnos en el mismo bloque horario.
* ⏳ **Control de Fechas:** Validación nativa en la capa de serialización para bloquear solicitudes de turnos en fechas u horas pasadas.
* 🔍 **Filtros Dinámicos (Query Params):** Endpoints adaptables que permiten al frontend filtrar consultas en tiempo real por estado del turno (`pendiente`, `cancelado`, etc.) o por médico específico.
* 💾 **Borrado Lógico:** Gestión profesional del ciclo de vida del turno a través de transiciones de estado, garantizando la persistencia del historial clínico.
* ⚙️ **Panel de Administración:** Panel administrativo interno integrado para el control absoluto del personal médico, especialidades y usuarios.

---

## 🛠️ Tecnologías Utilizadas

Este proyecto está construido con el ecosistema moderno de desarrollo web en Python:

* **Lenguaje:** Python 3.12+
* **Framework Backend:** Django 6.0 & Django REST Framework (DRF)
* **Base de Datos:** SQLite (Relacional, optimizada con indexación en campos clave)
* **ORM:** Django ORM (con técnicas de optimización `select_related` para evitar problemas de consultas $N+1$)

---

## 🔌 Arquitectura de Endpoints y DX (Developer Experience)

La API cuenta con un diseño de contratos de datos asimétrico: el frontend **envía IDs numéricos simples** para agendar, pero el backend **responde con objetos JSON profundamente anidados** para facilitar el renderizado de la UI en un solo paso.

### Endpoints Disponibles (`/api/`)

| Método | Endpoint | Descripción | Parámetros de Filtro (Opcionales) |
|:---:|:---|:---|:---|
| **GET** | `/api/especialidades/` | Lista todas las especialidades médicas. | Ninguno |
| **GET** | `/api/medicos/` | Lista los médicos con sus datos personales y especialidad. | Ninguno |
| **GET** | `/api/turnos/` | Lista el historial de turnos con datos anidados del paciente y médico. | `?estado=...` , `?medico_id=...` |
| **POST** | `/api/turnos/` | Agenda un nuevo turno (Aplica validaciones de negocio). | Cuerpo JSON (IDs nativos) |
| **GET** | `/api/turnos/<id>/` | Obtiene el detalle exhaustivo de una sola cita médica. | URL Path Parám |
| **PATCH** | `/api/turnos/<id>/` | Actualiza de forma parcial un turno (Cancelar o reprogramar). | Cuerpo JSON parcial |

---

## 🔧 Instalación y Configuración

Sigue estos pasos para clonar y ejecutar el servidor de desarrollo localmente:

### Prerrequisitos
* Git
* Python 3.12 instalado en tu sistema

### Pasos

1. **Clonar el repositorio:**
  ```bash
  git clone [https://github.com/RedBoth/medical-center-api.git](https://github.com/RedBoth/medical-center-api.git)
  cd medical-center-api
  ```

2. **Crear e inicializar entorno virtual**
  ```bash
  # Crear entorno
  python -m venv venv --without-pip

  # Activar en Windows (PowerShell)
  .\venv\Scripts\Activate.ps1

  # Activar en Mac/Linux
  source venv/bin/activate
  ```

3. **Instalar dependencias y gestor de paquetes**
  ```bash
  python -m ensurepip --default-pip
  pip install -r requirements.txt
  ```

4. **Ejecutar las migraciones**
  ```bash
  python manage.py migrate
  ```

5. **Crear cuenta administrador**
  ```bash
  python manage.py createsuperuser
  ```

6. **Ejecutar el servidor**
  ```bash
  python manage.py runserver
  ```

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar Campo-app:

1.  Haz un Fork del proyecto.
2.  Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3.  Haz Commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`).
4.  Haz Push a la rama (`git push origin feature/nueva-funcionalidad`).
5.  Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE) para más detalles.

---

⌨️ con ❤️ por [RedBoth](https://github.com/RedBoth)