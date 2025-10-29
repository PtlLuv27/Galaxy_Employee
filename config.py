import os
from datetime import timedelta

class Config:
    # All credentials come from environment variables only
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'employee_management')
    
    # Aiven SSL support
    MYSQL_SSL_MODE = os.getenv('MYSQL_SSL_MODE', 'REQUIRED')
    
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    
    UPLOAD_FOLDER = 'static/images/uploads'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '')

    PERMANENT_SESSION_LIFETIME = timedelta(days=30)