from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_core.database import Base  

class Metadata(Base):
    __tablename__ = 'image_metadata'
    
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    filename: Mapped[str] = mapped_column(String(200), nullable=False)
    file_extension: Mapped[str] = mapped_column(String(10), nullable=False)
    file_size_kb: Mapped[float] = mapped_column(Float, nullable=False)
    processed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now)
    ocr_engine: Mapped[str] = mapped_column(String(20) , nullable=False)
    texts: Mapped[list["Text"]] = relationship("Text", back_populates="metadata")


class Text(Base):
    __tablename__ = 'image_text'
    
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    analyte: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    range: Mapped[str] = mapped_column(String(50))
    unit: Mapped[str] = mapped_column(String(20))
    assessment: Mapped[str] = mapped_column(String(50))
    metadata_id: Mapped[int] = mapped_column(Integer)  # FK to Metadata
    metadata: Mapped["Metadata"] = relationship("Metadata", back_populates="Texts")
