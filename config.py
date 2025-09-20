import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))
    
    # ✅ FIX: use postgresql:// instead of postgres://
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "Database_URL",
        "postgresql://postgres.nxuustbvlkdbkzeyvgix:nPaIp4RweTXbOQFc@aws-1-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
