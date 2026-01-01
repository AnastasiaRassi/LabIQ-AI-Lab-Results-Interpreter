from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pathlib import Path
import shutil, sys
from datetime import datetime
from data_core.database import get_db
from data_core.table_models import Metadata, Text
from general_utils.utils import setup_logger, load_config, CustomException
config = load_config()
router = APIRouter()

img_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        ext = Path(file.filename).suffix.lower()
        if ext not in img_extensions:
            return {"error": f"File extension {ext} not allowed."}

        if config.get('Settings', {}).get('Testing', True):
            # when testing, my data is already local.
            pass
        else:
            # In a true production setting, images might be stored (for instance) within an S3 bucket.
            # I will simulate this effect, as this project is for demonstration purposes.
            return f"s3://labiq-images/{file.filename}"

        meta = Metadata(
            filename=file.filename, 
            filetype=file.content_type,
            file_size_kb=file.size
        )
        db.add(meta)
        db.commit()
        db.refresh(meta)

        text = ocr(file)
        db.add(text)
    except Exception as e:
        raise CustomException(e, sys)

    return {"message": "Image uploaded and processed.", "image_id": meta.id}
    