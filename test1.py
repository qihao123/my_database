
from syldb import Engine
from syldb.core.field import Field, FieldType, FieldKey

e = Engine()                    # 实例化数据库引擎对象
e.create_database('test_db')    # 创建数据库 test_db
e.select_db('test_db')          # 选择数据库 test_db

e.create_table(
    name='t_test',
    f_id=Field(data_type=FieldType.INT, keys=[FieldKey.PRIMARY, FieldKey.INCREMENT]),
    f_name=Field(data_type=FieldType.VARCHAR, keys=FieldKey.NOT_NULL),
    f_age=Field(data_type=FieldType.INT, keys=FieldKey.NOT_NULL)
)

# 向数据表 t_test 中插入数据
e.insert(table_name='t_test', f_name='shiyanlou_001', f_age=20)
e.insert(table_name='t_test', f_name='shiyanlou_002', f_age=10)

ret = e.search('t_test')
for row in ret:
    print(row)

# 保存数据库内容到本地默认的 db.data 文件中
e.commit()