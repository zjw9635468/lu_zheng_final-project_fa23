from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://w58g1hh6z47z1y9cdo7g:pscale_pw_KqWGRx5MJNauDGskh5ojUVuAWc6TZuJ2Zd7WqOwHmEv@aws.connect.psdb.cloud/lu_zheng_database_project?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args = {
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})
with engine.connect() as conn:
    result = conn.execute(text("select * from ACCOUNT"))
    print(result.all())