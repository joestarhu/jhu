from datetime import datetime
from dataclasses import dataclass
from math import ceil
from typing import List, Callable
from urllib.parse import quote_plus

from sqlalchemy import func, Select, MappingResult
from sqlalchemy.orm.session import Session


@dataclass
class ORMFormatRule:
    filed: str
    format: Callable


def format_datetime(dt: datetime) -> str:
    """格式化日期
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def format_filed(data: dict, rules: list[ORMFormatRule] = []) -> dict:
    """格式化读取的字段
    """
    basic_rules = [
        ORMFormatRule("create_dt", format_datetime),
        ORMFormatRule("update_dt", format_datetime),
    ]

    basic_rules.extend(rules)

    for obj in basic_rules:
        filed = data.get(obj.filed, None)
        if filed is not None:
            data[obj.filed] = ORMFormatRule.format(filed)

    return data


class ORM:
    @staticmethod
    def build_engine_url(dialect_dbapi: str, host: str, port: str, username: str = "", passwd: str = "", database: str = "", **kw) -> str:
        """创建sqlalchemy的engine url

        Args:
            dialect_dbapi:数据库方言和数据库API,比如'pymsql+mysql','postgresql'
            host:主机地址
            port:端口号
            username:用户名
            passwd:密码
            database:数据库名
            **kw:数据库的参数

        Return:
            str: 返回格式为:dialect+dbapi://username:passwd@host:port/database?key=value&key=value
        """
        # 拼接用户名以及密码
        username, passwd = map(quote_plus, [username, passwd])
        auth_info = f"{username}:{passwd}" if passwd else username

        # 设置数据库信息
        database = f"/{database}" if database else ""

        # 设置参数信息
        if kw:
            args = '&'.join([f"{k}={kw[k]}" for k in kw])
            param = f"?{args}"
        else:
            param = ""

        # 拼接url
        url = f"{dialect_dbapi}://{auth_info}@{host}:{port}{database}{param}"
        return url

    @staticmethod
    def mapping(db: Session, stmt) -> MappingResult:
        """ORM执行结果mapping
        """
        return db.execute(stmt).mappings()

    @staticmethod
    def all(db: Session, stmt: Select, format_rules: list[ORMFormatRule] = []) -> List[dict]:
        """获取所有数据
        """
        ds = db.execute(stmt).mappings()
        return [dict(**data) for data in ds]

    @staticmethod
    def one(db: Session, stmt: Select, format_rules: list[ORMFormatRule] = []) -> dict | None:
        """获取第一行数据
        """
        ds = ORM.all(db, stmt)
        return ds[0] if ds else None

    @staticmethod
    def counts(db: Session, stmt: Select) -> int:
        """获取数据量
        """
        return db.scalar(stmt.with_only_columns(func.count("1")))

    @staticmethod
    def pagination(db: Session, stmt: Select, page_idx: int = 1, page_size: int = 10, order: list = None) -> dict:
        """分页查询数据
        """
        if page_size < 1:
            page_size = 1

        match(page_idx):
            case page_idx if page_idx > 0:
                offset = (page_idx - 1) * page_size
            case _:
                offset = 0
                page_idx = 1

        total = ORM.counts(db, stmt)
        page_total = ceil(total / page_size)

        pagination = dict(page_idx=page_idx, page_size=page_size,
                          page_total=page_total, total=total)

        # 配置排序条件
        if order is not None:
            stmt = stmt.order_by(*order)

        # 配置分页条件
        stmt = stmt.offset(offset).limit(page_size)
        records = ORM.all(db, stmt)
        data = dict(records=records, pagination=pagination)

        return data
