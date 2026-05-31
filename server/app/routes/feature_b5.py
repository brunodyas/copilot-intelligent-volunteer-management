from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/b5', tags=['feature'])

@router.get('/status')
def feature_b5_status():
    return {'ok': True, 'feature': 'Desenvolver métricas ESG', 'task': 'B5'}
