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
La API quedará disponible en:

Health check: http://127.0.0.1:8000/health

Documentación Swagger (OpenAPI): http://127.0.0.1:8000/docs

## Endpoints:

POST /portfolio/value (endpoint principal)

Calcula el valor de un portafolio de criptomonedas en una moneda fiat de referencia.

Request body (JSON)

{
  "portfolio": {
    "BTC": 0.5,
    "ETH": 2.0
  },
  "fiat_currency": "CLP"
}

portfolio: mapa de símbolo de criptomoneda a cantidad (no negativa)
fiat_currency: moneda fiat de referencia (CLP, PEN o COP)

Respuesta exitosa (200)
{
  "fiat_currency": "CLP",
  "total": "45400000",
  "breakdown": {
    "BTC": "40000000",
    "ETH": "5400000"
  },
  "unpriced": []
}


total: valor total del portafolio en la moneda fiat
breakdown: valorización individual por cripto
unpriced: criptos que no pudieron valorizarse

## Ejemplos de uso manual (curl)

Ejemplo válido – conversión directa:
```bash
curl -X POST "http://127.0.0.1:8000/portfolio/value" \
  -H "Content-Type: application/json" \
  -d '{
    "portfolio": {"BTC": 0.5},
    "fiat_currency": "CLP"
  }'
```

Ejemplo inválido – cantidad negativa:
```bash
curl -X POST "http://127.0.0.1:8000/portfolio/value" \
  -H "Content-Type: application/json" \
  -d '{
    "portfolio": {"BTC": -1},
    "fiat_currency": "CLP"
  }'
```
Respuesta esperada: 422 Unprocessable Entity

Ejemplo inválido – moneda fiat no permitida
```bash
curl -X POST "http://127.0.0.1:8000/portfolio/value" \
  -H "Content-Type: application/json" \
  -d '{
    "portfolio": {"BTC": 1},
    "fiat_currency": "USD"
  }'
```
Respuesta esperada: 422 Unprocessable Entity

## Tests automatizados
Para ejecutar los tests automatizados, asegúrate de tener instalado `pytest` y luego corre:

```bash
source .venv/bin/activate
pytest -q
```