from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://ngqsl4t2ffefl3eqcrnp:pscale_pw_emBs2mwhXBwrIdQQWg3zDL2l5OJRQrGMBgg9hqybwCg@aws.connect.psdb.cloud/lu_zheng_database_project?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
with engine.connect() as conn:
    result = conn.execute(text("select * from ACCOUNT"))
    print(result.all())