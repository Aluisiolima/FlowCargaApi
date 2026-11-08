from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.exc import DataError, IntegrityError, OperationalError
from sqlalchemy.ext.asyncio import AsyncSession


class ExceptionMessages:
    @staticmethod
    async def handle_exception(exc, db_session: AsyncSession):
        await db_session.rollback()

        if isinstance(exc, IntegrityError):
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Violação de integridade, dados duplicados",
            )
        elif isinstance(exc, DataError):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=("Erro nos dados enviados, verifique os tipos e formatos"),
            )
        elif isinstance(exc, OperationalError):
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=("Erro de operação no banco de dados, verifique a consulta"),
            )
        elif isinstance(exc, HTTPException):
            raise exc
        else:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"{exc}",
            )


def exceptions(func):
    async def wrapper(*args, **kwargs):
        db = kwargs.get("db") or args[1]
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            await ExceptionMessages.handle_exception(e, db)

    return wrapper
