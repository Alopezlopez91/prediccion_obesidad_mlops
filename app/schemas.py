from pydantic import BaseModel, Field

# ======================================================
# 1. Esquema de entrada para predicción
# ======================================================

class PredictionRequest(BaseModel):
    Gender: str = Field(...)
    Age: float = Field(...)
    Height: float = Field(...)
    Weight: float = Field(...)
    family_history: str = Field(...)
    FAVC: str = Field(...)
    FCVC: float = Field(...)
    NCP: float = Field(...)
    CAEC: str = Field(...)
    SMOKE: str = Field(...)
    CH2O: float = Field(...)
    SCC: str = Field(...)
    FAF: float = Field(...)
    TUE: float = Field(...)
    CALC: str = Field(...)
    MTRANS: str = Field(...)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Gender": "Male",
                    "Age": 25,
                    "Height": 1.75,
                    "Weight": 82,
                    "family_history": "yes",
                    "FAVC": "yes",
                    "FCVC": 2,
                    "NCP": 3,
                    "CAEC": "Sometimes",
                    "SMOKE": "no",
                    "CH2O": 2,
                    "SCC": "no",
                    "FAF": 1,
                    "TUE": 1,
                    "CALC": "Sometimes",
                    "MTRANS": "Public_Transportation",
                }
            ]
        }
    }


# ======================================================
# 2. Esquema de salida
# ======================================================

class PredictionResponse(BaseModel):
    prediction: str


# ======================================================
# 3. Estado de salud de la API
# ======================================================

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool