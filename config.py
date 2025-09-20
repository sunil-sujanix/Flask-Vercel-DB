import os


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY',os.urandom(24))
    SQLALCHEMY_DATABASE_URI=os.getenv('Database_URL',"postgresql://neondb_owner:npg_F5GWma9cEBIK@ep-small-forest-ad1245c3-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require")
    SQLALCHEMY_TRACK_MODIFICATIONS=False