import pymysql

class MyDB:
    def getConnection(self):
        try:
            conn = pymysql.connect(
                host= "127.0.0.1",
                port = 3306,
                user = "root",
                passwd= "lol187134",
                db = "Music",
                charset="utf8"
            )
            print("数据库连接成功",conn.host,conn.user,conn.db,conn.charset)
            return conn
        except pymysql.Error as e:
            print("数据库连接失败 Error 是 %s"%(e))

        # 查询playlist 表的所有信息
    def select_playlist(self):
        self.conn = self.getConnection()
        try:
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM playlist;")
            fc = cur.fetchall()
            return fc

        except Exception as e:
            print(f"查询出现异常 {e}")
            self.conn.rollback()
        finally:
            cur.close()
            self.conn.close()

    # 查询music_message 表的所有信息
    def select_music_message(self):
        self.conn = self.getConnection()
        try:
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM music_message;")
            fc = cur.fetchall()
            return fc

        except Exception as e:
            print(f"查询出现异常 {e}")
            self.conn.rollback()
        finally:
            cur.close()
            self.conn.close()

    # 查询arealist 表的所有信息
    def select_arealist(self):
        self.conn = self.getConnection()
        try:
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM arealist;")
            fc = cur.fetchall()
            return fc

        except Exception as e:
            print(f"查询出现异常 {e}")
            self.conn.rollback()
        finally:
            cur.close()
            self.conn.close()

    def select_music_hotsonglist(self):
        self.conn = self.getConnection()
        try:
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute("SELECT * FROM hotsonglist;")
            fc = cur.fetchall()
            return fc

        except Exception as e:
            print("查询出现异常 {e}")
            self.conn.rollback()
        finally:
            cur.close()
            self.conn.close()

