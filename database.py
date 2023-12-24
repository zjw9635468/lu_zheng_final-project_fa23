from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://hx8hza0129ew5qo6qcx9:pscale_pw_shPNhH52KRX4io6iJaG79nIt7KIDbv9n2Erb9MEVnz@aws.connect.psdb.cloud/lu_zheng_database_project?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
with engine.connect() as conn:
    result = conn.execute(text("select * from ACCOUNT"))
    print(result.all())