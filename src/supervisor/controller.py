from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_session
from src.core.repository import Supervisor
from src.core.security import get_current_supervisor
from src.supervisor.schema import (
    SupervisorCreate,
    SupervisorLogin,
    SupervisorResponse,
    SupervisorUpdate,
    TokenResponse,
)
from src.supervisor.service import SupervisorService

router = APIRouter(
    prefix="/supervisores",
    tags=["Supervisores"],
)


@router.post(
    "/",
    response_model=SupervisorResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_supervisor(
    supervisor_create: SupervisorCreate,
    db: AsyncSession = Depends(get_session),
):
    return await SupervisorService.create_supervisor(
        supervisor_create=supervisor_create,
        db=db,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login_supervisor(
    login: SupervisorLogin,
    db: AsyncSession = Depends(get_session),
):
    return await SupervisorService.authenticate_supervisor(
        login=login,
        db=db,
    )


@router.get(
    "/",
    response_model=list[SupervisorResponse],
)
async def list_supervisors(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_session),
    token: Supervisor = Depends(get_current_supervisor),
):
    return await SupervisorService.list_supervisors(
        limit=limit,
        offset=offset,
        db=db,
        token=token,
    )


@router.get(
    "/{id}",
    response_model=SupervisorResponse,
)
async def get_supervisor(
    id: int,
    db: AsyncSession = Depends(get_session),
    token: Supervisor = Depends(get_current_supervisor),
):
    return await SupervisorService.get_supervisor_by_id(
        id=id,
        db=db,
        token=token,
    )


@router.patch(
    "/{id}",
    response_model=SupervisorResponse,
)
async def update_supervisor(
    id: int,
    supervisor_update: SupervisorUpdate,
    db: AsyncSession = Depends(get_session),
    token: Supervisor = Depends(get_current_supervisor),
):
    return await SupervisorService.update_supervisor(
        id=id,
        supervisor_update=supervisor_update,
        db=db,
        token=token,
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_supervisor(
    id: int,
    db: AsyncSession = Depends(get_session),
    token: Supervisor = Depends(get_current_supervisor),
):
    await SupervisorService.delete_supervisor(
        id=id,
        db=db,
        token=token,
    )
