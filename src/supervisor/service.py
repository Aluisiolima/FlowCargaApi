from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.repository import Supervisor
from src.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from src.core.types import TipoUsuario
from src.supervisor.schema import (
    SupervisorCreate,
    SupervisorLogin,
    SupervisorUpdate,
)


class SupervisorService:
    @staticmethod
    async def create_supervisor(
        *,
        supervisor_create: SupervisorCreate,
        db: AsyncSession,
    ) -> Supervisor:

        stmt = select(Supervisor).where(Supervisor.email == supervisor_create.email)

        if await db.scalar(stmt):
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Email already registered",
            )

        supervisor_data = supervisor_create.model_dump(exclude={"senha"})

        supervisor = Supervisor(
            **supervisor_data,
            senha_hash=hash_password(supervisor_create.senha),
            tipo=TipoUsuario.SUPERVISOR,
            ativo=True,
        )

        db.add(supervisor)
        await db.commit()
        await db.refresh(supervisor)

        return supervisor

    @staticmethod
    async def list_supervisors(
        *,
        limit: int,
        offset: int,
        db: AsyncSession,
        token: Supervisor,
    ) -> list[Supervisor]:

        if token.tipo != TipoUsuario.ADMINISTRADOR:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Not enough permissions",
            )

        stmt = (
            select(Supervisor)
            .where(Supervisor.ativo.is_(True))
            .offset(offset)
            .limit(limit)
        )

        result = await db.scalars(stmt)

        return list(result.all())

    @staticmethod
    async def get_supervisor_by_id(
        *,
        id: int,
        db: AsyncSession,
        token: Supervisor,
    ) -> Supervisor:

        if token.id != id and token.tipo != TipoUsuario.ADMINISTRADOR:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Not enough permissions",
            )

        supervisor = await db.get(Supervisor, id)

        if not supervisor or not supervisor.ativo:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="Supervisor not found",
            )

        return supervisor

    @staticmethod
    async def update_supervisor(
        *,
        id: int,
        supervisor_update: SupervisorUpdate,
        db: AsyncSession,
        token: Supervisor,
    ) -> Supervisor:

        if token.id != id and token.tipo != TipoUsuario.ADMINISTRADOR:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Not enough permissions",
            )

        supervisor = await db.get(Supervisor, id)

        if not supervisor or not supervisor.ativo:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="Supervisor not found",
            )

        update_data = supervisor_update.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        if "tipo" in update_data or "ativo" in update_data:
            if token.tipo != TipoUsuario.ADMINISTRADOR:
                raise HTTPException(
                    status_code=HTTPStatus.FORBIDDEN,
                    detail="Not enough permissions",
                )

        if "email" in update_data:
            stmt = select(Supervisor).where(
                Supervisor.email == update_data["email"],
                Supervisor.id != id,
            )

            if await db.scalar(stmt):
                raise HTTPException(
                    status_code=HTTPStatus.CONFLICT,
                    detail="Email already registered",
                )

        if "senha" in update_data:
            update_data["senha_hash"] = hash_password(update_data.pop("senha"))

        for key, value in update_data.items():
            setattr(supervisor, key, value)

        await db.commit()
        await db.refresh(supervisor)

        return supervisor

    @staticmethod
    async def delete_supervisor(
        *,
        id: int,
        db: AsyncSession,
        token: Supervisor,
    ) -> None:

        if token.tipo != TipoUsuario.ADMINISTRADOR:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Not enough permissions",
            )

        supervisor = await db.get(Supervisor, id)

        if not supervisor or not supervisor.ativo:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="Supervisor not found",
            )

        if supervisor.id == token.id:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Cannot deactivate your own account",
            )

        supervisor.ativo = False

        await db.commit()

    @staticmethod
    async def authenticate_supervisor(
        *,
        login: SupervisorLogin,
        db: AsyncSession,
    ) -> dict:

        stmt = select(Supervisor).where(Supervisor.email == login.email)

        supervisor = await db.scalar(stmt)

        if not supervisor or not verify_password(
            login.senha,
            supervisor.senha_hash,
        ):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not supervisor.ativo:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Inactive account",
            )

        return {
            "access_token": create_access_token(supervisor),
            "token_type": "bearer",
            "supervisor": supervisor,
        }
