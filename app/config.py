import os
from pathlib import Path


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Obesity Prediction API")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Rutas relativas del proyecto
    ROOT_DIR: Path = Path(__file__).resolve().parent.parent
    MODEL_PATH: Path = ROOT_DIR / "models" / "model.pkl"
    ENCODER_PATH: Path = ROOT_DIR / "models" / "encoders.pkl"
    METADATA_PATH: Path = ROOT_DIR / "models" / "metadata.json"


settings = Settings()
