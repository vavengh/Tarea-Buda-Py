# Crypto Portfolio API – Buda.com

REST API desarrollada en **Python + FastAPI** que permite valorizar un portafolio de criptomonedas usando precios en tiempo real obtenidos desde la API pública de **Buda.com**.

> Este repositorio se está construyendo de manera incremental, priorizando buenas prácticas, código limpio y tests automatizados.

---

## Requisitos del sistema

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.10 o superior**
- **pip**
- **git**

En sistemas basados en Debian/Ubuntu (incluido WSL):

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

## Instalación y ejecución local

1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Tarea-Buda-Py.git
cd Tarea-Buda-Py
```

## Crear y activar entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Levantar el servidor

```bash
uvicorn app.main:app --reload
```