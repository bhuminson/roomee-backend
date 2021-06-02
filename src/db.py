from flask import jsonify
from constants import host, db, user, pw
import psycopg2
from psycopg2.extras import RealDictCursor


def executeQuery(query, args, fetchall=False, commit=False):
    res = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query, args)
        if commit:
            conn.commit()
        else:
            res = cur.fetchall() if fetchall else cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        if commit:
            res = jsonify(success=True)
            res.status_code = 201
        return res if res is not None else {}
