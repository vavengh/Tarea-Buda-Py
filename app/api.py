from __future__ import annotations

from decimal import Decimal

from fastapi import APIRouter, HTTPException

from app.models import PortfolioRequest, PortfolioValueResponse

from app.buda_client import BudaPublicClient, BudaUpstreamError


router = APIRouter()


@router.post("/portfolio/value", response_model=PortfolioValueResponse)
def value_portfolio(payload: PortfolioRequest) -> PortfolioValueResponse:
    """
    Paso 2 (placeholder):
    - Devolvemos 0 en todas las valorizaciones.
    - La integración con precios de Buda viene en el Paso 3/4.
    """
    breakdown = {symbol: Decimal("0") for symbol in payload.portfolio.keys()}
    total = sum(breakdown.values(), start=Decimal("0"))

    return PortfolioValueResponse(
        fiat_currency=payload.fiat_currency,
        total=total,
        breakdown=breakdown,
        unpriced=[],
    )

@router.get("/buda/tickers")
def buda_tickers():
    """
    Endpoint de apoyo: permite verificar rápidamente que estamos consumiendo Buda.
    (No es parte del enunciado final; si quieres lo eliminamos al final.)
    """
    client = BudaPublicClient()
    try:
        tickers = client.get_tickers()
    except BudaUpstreamError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    # Devuelve una muestra pequeña para no mandar miles de líneas
    sample_keys = list(tickers.keys())[:10]
    sample = {k: {"last_price": str(tickers[k].last_price)} for k in sample_keys}
    return {"count": len(tickers), "sample": sample}
