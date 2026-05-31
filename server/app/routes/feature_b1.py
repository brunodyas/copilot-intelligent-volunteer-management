from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/b1', tags=['feature'])

@router.get('/status')
def feature_b1_status():
    return {'ok': True, 'feature': 'Clonar e configurar o projeto no GitHub', 'task': 'B1'}
