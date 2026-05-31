from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/b15', tags=['feature'])

@router.get('/status')
def feature_b15_status():
    return {'ok': True, 'feature': 'Implementar funcionalidades de métricas ESG', 'task': 'B15'}
