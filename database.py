from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()
db_connection_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(db_connection_string, connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
with engine.connect() as conn:
    result = conn.execute(text("select * from ACCOUNT"))
    print(result.all())