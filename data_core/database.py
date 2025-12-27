from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys, os
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from general_utils.utils import CustomException
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{os.getenv('MYSQL_PASSWORD')}@localhost:3306/LabIQ_DB"

try:
    Engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True )
    SessionLocal = sessionmaker(bind=Engine, autocommit=False, autoflush=False)
    Base = declarative_base()()
except Exception as e:
    raise CustomException(e, sys)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()